#!/usr/bin/env node
/**
 * dom_geometry_audit.mjs
 * Rendered DOM & computed-style geometry auditor using Playwright.
 *
 * Resolves Playwright from the current project first, then from the global npm
 * root, so the script works when the skill pack lives outside the target repo.
 *
 * Usage:
 *   node dom_geometry_audit.mjs --url http://localhost:3000 --out ./audit-out
 *   node dom_geometry_audit.mjs --url http://localhost:3000 --routes /,/pricing --viewports mobile,desktop
 *   node dom_geometry_audit.mjs --url http://localhost:3000 --channel msedge --fail-on P1
 */

import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';

const SEVERITY_RANK = { P0: 0, P1: 1, P2: 2, P3: 3 };

function parseArgs(argv) {
  const args = {
    url: '',
    out: './audit-out',
    viewports: 'mobile,tablet,desktop',
    routes: '/',
    waitMs: 800,
    timeout: 30000,
    channel: '',
    storageState: '',
    headers: '',
    colorScheme: 'light',
    failOn: '',
  };
  for (let i = 2; i < argv.length; i++) {
    const key = argv[i];
    const val = argv[i + 1];
    if (!val && key.startsWith('--')) {
      console.error(`Missing value for ${key}`);
      process.exit(2);
    }
    if (key === '--url') { args.url = val; i++; }
    else if (key === '--out') { args.out = val; i++; }
    else if (key === '--viewports') { args.viewports = val; i++; }
    else if (key === '--routes') { args.routes = val; i++; }
    else if (key === '--wait') { args.waitMs = Number(val) || 800; i++; }
    else if (key === '--timeout') { args.timeout = Number(val) || 30000; i++; }
    else if (key === '--channel') { args.channel = val; i++; }
    else if (key === '--storage-state') { args.storageState = val; i++; }
    else if (key === '--headers') { args.headers = val; i++; }
    else if (key === '--color-scheme') { args.colorScheme = val; i++; }
    else if (key === '--fail-on') { args.failOn = val.toUpperCase(); i++; }
  }
  if (!args.url) {
    console.error('Error: --url is required. Example: node dom_geometry_audit.mjs --url http://localhost:3000 --out ./audit-out');
    process.exit(2);
  }
  if (args.failOn && !(args.failOn in SEVERITY_RANK)) {
    console.error(`Invalid --fail-on: ${args.failOn}. Use P0, P1, P2, or P3.`);
    process.exit(2);
  }
  return args;
}

function loadPlaywright() {
  const require = createRequire(path.join(process.cwd(), 'package.json'));
  const attempts = [];

  try {
    return require('playwright');
  } catch (err) {
    attempts.push(`cwd: ${err.message}`);
  }

  try {
    const globalRoot = execSync('npm root -g', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
    const globalEntry = path.join(globalRoot, 'playwright');
    return require(globalEntry);
  } catch (err) {
    attempts.push(`global: ${err.message}`);
  }

  console.error('Playwright not found. Install it in the target project:');
  console.error('  npm install -D playwright && npx playwright install chromium');
  console.error('Or use a system browser channel: --channel msedge / --channel chrome');
  console.error(attempts.join('\n'));
  process.exit(2);
}

const VIEWPORT_PRESETS = {
  'mobile-320': { width: 320, height: 568, deviceScaleFactor: 2 },
  mobile: { width: 375, height: 812, deviceScaleFactor: 2 },
  'mobile-large': { width: 430, height: 932, deviceScaleFactor: 3 },
  tablet: { width: 768, height: 1024, deviceScaleFactor: 2 },
  laptop: { width: 1280, height: 800, deviceScaleFactor: 1 },
  desktop: { width: 1440, height: 900, deviceScaleFactor: 1 },
  wide: { width: 1920, height: 1080, deviceScaleFactor: 1 },
};

function routeSlug(route) {
  const cleaned = route.replace(/^https?:\/\/[^/]+/i, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-+|-+$/g, '');
  return cleaned || 'root';
}

async function auditPage(page, vpName, vpConfig) {
  return page.evaluate(({ vpName, vpWidth }) => {
    const findings = [];
    let counter = 1;
    const nextId = (prefix) => `${prefix}-${String(counter++).padStart(3, '0')}`;

    const isVisible = (el) => {
      const style = window.getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden' || parseFloat(style.opacity) === 0) return false;
      const rect = el.getBoundingClientRect();
      return rect.width > 0.5 && rect.height > 0.5;
    };

    const getSelector = (el) => {
      if (!el || !el.tagName) return 'unknown';
      if (el.id) return `#${el.id}`;
      const tag = el.tagName.toLowerCase();
      const cls = typeof el.className === 'string'
        ? el.className.trim().split(/\s+/).filter(Boolean).slice(0, 3).join('.')
        : '';
      return cls ? `${tag}.${cls}` : tag;
    };

    // 1. Horizontal page overflow
    const docScrollW = document.documentElement.scrollWidth;
    if (docScrollW > vpWidth + 1) {
      const offenders = [];
      for (const el of document.querySelectorAll('*')) {
        if (!isVisible(el)) continue;
        const r = el.getBoundingClientRect();
        if (r.right > vpWidth + 1 || r.left < -1) {
          offenders.push({
            selector: getSelector(el),
            left: Number(r.left.toFixed(1)),
            right: Number(r.right.toFixed(1)),
            overflowRightPx: Number((r.right - vpWidth).toFixed(1)),
          });
        }
      }
      findings.push({
        id: nextId('OVR'),
        severity: 'P0',
        category: 'horizontal-overflow',
        viewport: vpName,
        selector: 'document.documentElement',
        evidence: {
          scrollWidth: docScrollW,
          viewportWidth: vpWidth,
          overflowPx: docScrollW - vpWidth,
          topOffenders: offenders.slice(0, 5),
        },
        rootCause: `Page overflows horizontally by ${docScrollW - vpWidth}px at ${vpWidth}px viewport.`,
      });
    }

    // 2. Centering drift
    const centerCandidates = document.querySelectorAll(
      'header img, header svg, nav img, nav svg, [class*="logo" i], [id*="logo" i], h1, h2, [class*="center" i]'
    );
    for (const el of centerCandidates) {
      if (!isVisible(el)) continue;
      const parent = el.parentElement;
      if (!parent) continue;
      const elStyle = window.getComputedStyle(el);
      const pStyle = window.getComputedStyle(parent);
      const r = el.getBoundingClientRect();
      const pr = parent.getBoundingClientRect();

      const intendedCentered =
        elStyle.textAlign === 'center' ||
        pStyle.textAlign === 'center' ||
        pStyle.justifyContent === 'center' ||
        (elStyle.marginLeft === elStyle.marginRight && parseFloat(elStyle.marginLeft) > 8) ||
        (pStyle.display.includes('flex') && pStyle.justifyContent === 'space-between' && parent.children.length === 3 && parent.children[1].contains(el));

      if (!intendedCentered) continue;

      const refRect = (parent.tagName === 'NAV' || parent.tagName === 'HEADER' || pr.width > r.width + 20)
        ? pr
        : document.documentElement.getBoundingClientRect();
      const elCenterX = r.left + r.width / 2;
      const refCenterX = refRect.left + refRect.width / 2;
      const deltaX = Number((elCenterX - refCenterX).toFixed(2));

      if (Math.abs(deltaX) > 1.5 && Math.abs(deltaX) < refRect.width * 0.25) {
        findings.push({
          id: nextId('CTR'),
          severity: Math.abs(deltaX) > 4 ? 'P1' : 'P2',
          category: 'centering-drift',
          viewport: vpName,
          selector: getSelector(el),
          evidence: {
            elementCenterX: Number(elCenterX.toFixed(2)),
            containerCenterX: Number(refCenterX.toFixed(2)),
            deltaX_px: deltaX,
            parentSelector: getSelector(parent),
            parentDisplay: pStyle.display,
            parentJustifyContent: pStyle.justifyContent,
          },
          rootCause: `Element center is shifted ${deltaX > 0 ? 'right' : 'left'} by ${Math.abs(deltaX)}px relative to container center (${pStyle.display} / ${pStyle.justifyContent}).`,
        });
      }
    }

    // 3. Divider completeness and symmetry
    for (const el of document.querySelectorAll('*')) {
      if (!isVisible(el)) continue;
      const r = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      const isHr = el.tagName === 'HR' || el.getAttribute('role') === 'separator';
      const hasDividerShape =
        !isHr &&
        el.children.length === 0 &&
        (el.textContent || '').trim() === '' &&
        r.height <= 4 &&
        r.width >= 40 &&
        (style.backgroundColor !== 'rgba(0, 0, 0, 0)' || parseFloat(style.borderTopWidth) > 0 || parseFloat(style.borderBottomWidth) > 0);

      if (!isHr && !hasDividerShape) continue;
      const parent = el.parentElement;
      if (!parent) continue;
      const pr = parent.getBoundingClientRect();
      const pStyle = window.getComputedStyle(parent);
      const padL = parseFloat(pStyle.paddingLeft) || 0;
      const padR = parseFloat(pStyle.paddingRight) || 0;
      const contentLeft = pr.left + padL;
      const contentRight = pr.right - padR;
      const contentWidth = contentRight - contentLeft;

      const leftGapFromContent = Number((r.left - contentLeft).toFixed(2));
      const rightGapFromContent = Number((contentRight - r.right).toFixed(2));
      const fillRatio = contentWidth > 0 ? Number((r.width / contentWidth).toFixed(3)) : 1;

      const asymmetricInset = Math.abs(leftGapFromContent - rightGapFromContent) > 2;
      const almostFullButShort = fillRatio > 0.72 && fillRatio < 0.992 && (Math.abs(leftGapFromContent) > 1 || Math.abs(rightGapFromContent) > 1);

      if (asymmetricInset || almostFullButShort) {
        findings.push({
          id: nextId('DIV'),
          severity: 'P1',
          category: 'divider-incomplete',
          viewport: vpName,
          selector: getSelector(el),
          evidence: {
            dividerWidth: Number(r.width.toFixed(1)),
            parentContentWidth: Number(contentWidth.toFixed(1)),
            fillRatio,
            leftGapPx: leftGapFromContent,
            rightGapPx: rightGapFromContent,
            parentSelector: getSelector(parent),
          },
          rootCause: asymmetricInset
            ? `Divider has asymmetric horizontal insets (left gap ${leftGapFromContent}px vs right gap ${rightGapFromContent}px).`
            : `Divider spans ${(fillRatio * 100).toFixed(1)}% of parent content width (${r.width.toFixed(1)}px / ${contentWidth.toFixed(1)}px), stopping short of container edges.`,
        });
      }
    }

    // 4. Text clipping / accidental truncation
    for (const el of document.querySelectorAll('h1,h2,h3,h4,p,span,a,button,label,li')) {
      if (!isVisible(el)) continue;
      if (el.children.length > 0) continue;
      const style = window.getComputedStyle(el);
      const isEllipsis = style.textOverflow === 'ellipsis' && style.whiteSpace === 'nowrap';
      if (isEllipsis) continue;

      const clippedX = el.scrollWidth > el.clientWidth + 2 && (style.overflowX === 'hidden' || style.overflow === 'hidden');
      const clippedY = el.scrollHeight > el.clientHeight + 2 && (style.overflowY === 'hidden' || style.overflow === 'hidden');
      if (clippedX || clippedY) {
        findings.push({
          id: nextId('CLP'),
          severity: 'P0',
          category: 'text-clipping',
          viewport: vpName,
          selector: getSelector(el),
          evidence: {
            textPreview: (el.textContent || '').trim().slice(0, 60),
            clientSize: `${el.clientWidth}x${el.clientHeight}`,
            scrollSize: `${el.scrollWidth}x${el.scrollHeight}`,
            overflow: `${style.overflowX}/${style.overflowY}`,
          },
          rootCause: 'Text content exceeds its overflow-hidden box and is visibly clipped.',
        });
      }
    }

    // 5. Sibling card symmetry
    for (const c of document.querySelectorAll('section, main, div, ul')) {
      if (!isVisible(c)) continue;
      const cStyle = window.getComputedStyle(c);
      if (cStyle.display !== 'grid' && cStyle.display !== 'flex') continue;
      const children = Array.from(c.children).filter(isVisible);
      if (children.length < 2 || children.length > 8) continue;

      const rows = [];
      for (const ch of children) {
        const r = ch.getBoundingClientRect();
        if (r.width < 120 || r.height < 60) continue;
        let placed = false;
        for (const row of rows) {
          if (Math.abs(row[0].rect.top - r.top) <= 6) {
            row.push({ el: ch, rect: r });
            placed = true;
            break;
          }
        }
        if (!placed) rows.push([{ el: ch, rect: r }]);
      }

      for (const row of rows) {
        if (row.length < 2) continue;
        const heights = row.map((item) => item.rect.height);
        const minH = Math.min(...heights);
        const maxH = Math.max(...heights);
        if (maxH - minH > 8 && minH > 80) {
          findings.push({
            id: nextId('SYM'),
            severity: 'P2',
            category: 'sibling-asymmetry',
            viewport: vpName,
            selector: getSelector(c),
            evidence: {
              rowCardCount: row.length,
              minHeightPx: Number(minH.toFixed(1)),
              maxHeightPx: Number(maxH.toFixed(1)),
              heightDeltaPx: Number((maxH - minH).toFixed(1)),
              containerAlignItems: cStyle.alignItems,
            },
            rootCause: `Sibling cards in the same ${cStyle.display} row have uneven heights (delta ${(maxH - minH).toFixed(1)}px).`,
          });
        }
      }
    }

    // 6. Interactive element overlap
    const interactives = Array.from(document.querySelectorAll('a, button, input, select, textarea')).filter(isVisible);
    const rects = interactives.map((el) => ({ el, r: el.getBoundingClientRect() }));
    for (let i = 0; i < rects.length; i++) {
      for (let j = i + 1; j < rects.length; j++) {
        const a = rects[i];
        const b = rects[j];
        if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
        const overlapX = Math.max(0, Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left));
        const overlapY = Math.max(0, Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top));
        if (overlapX > 3 && overlapY > 3) {
          findings.push({
            id: nextId('OVL'),
            severity: 'P0',
            category: 'element-overlap',
            viewport: vpName,
            selector: `${getSelector(a.el)} <> ${getSelector(b.el)}`,
            evidence: { overlapPx: `${overlapX.toFixed(1)}x${overlapY.toFixed(1)}` },
            rootCause: 'Two distinct interactive controls overlap in rendered screen space.',
          });
        }
      }
    }

    return {
      viewport: vpName,
      dimensions: `${vpWidth}x${window.innerHeight}`,
      totalFindings: findings.length,
      findings,
    };
  }, { vpName, vpWidth: vpConfig.width });
}

async function main() {
  const args = parseArgs(process.argv);
  fs.mkdirSync(args.out, { recursive: true });

  const playwright = loadPlaywright();
  const vpKeys = args.viewports.split(',').map((s) => s.trim()).filter((k) => VIEWPORT_PRESETS[k]);
  if (vpKeys.length === 0) {
    console.error(`No valid viewports. Choose from: ${Object.keys(VIEWPORT_PRESETS).join(', ')}`);
    process.exit(2);
  }

  const routes = args.routes.split(',').map((s) => s.trim()).filter(Boolean);
  if (routes.length === 0) routes.push('/');

  let headers = {};
  if (args.headers) {
    try {
      headers = JSON.parse(args.headers);
    } catch {
      console.error('Invalid --headers JSON.');
      process.exit(2);
    }
  }

  let storageState;
  if (args.storageState) {
    if (!fs.existsSync(args.storageState)) {
      console.error(`Storage state not found: ${args.storageState}`);
      process.exit(2);
    }
    storageState = args.storageState;
  }

  const browser = await playwright.chromium.launch({
    headless: true,
    ...(args.channel ? { channel: args.channel } : {}),
  });

  const report = {
    url: args.url,
    routes,
    timestamp: new Date().toISOString(),
    viewports: vpKeys,
    channel: args.channel || 'bundled-chromium',
    summary: { P0: 0, P1: 0, P2: 0, P3: 0, total: 0 },
    results: {},
  };

  try {
    for (const route of routes) {
      const target = new URL(route, args.url).toString();
      report.results[route] = {};
      for (const vpName of vpKeys) {
        const vpConfig = VIEWPORT_PRESETS[vpName];
        const context = await browser.newContext({
          viewport: { width: vpConfig.width, height: vpConfig.height },
          deviceScaleFactor: vpConfig.deviceScaleFactor,
          colorScheme: args.colorScheme,
          reducedMotion: 'reduce',
          ...(storageState ? { storageState } : {}),
          ...(Object.keys(headers).length ? { extraHTTPHeaders: headers } : {}),
        });
        const page = await context.newPage();
        try {
          await page.goto(target, { waitUntil: 'networkidle', timeout: args.timeout }).catch(async () => {
            await page.goto(target, { waitUntil: 'load', timeout: args.timeout });
          });
          await page.evaluate(() => document.fonts.ready).catch(() => {});
          await page.addStyleTag({ content: '*{caret-color:transparent !important}' }).catch(() => {});
          await page.waitForTimeout(args.waitMs);

          const slug = routeSlug(route);
          const screenshotPath = path.join(args.out, `${slug}-${vpName}-${vpConfig.width}.png`);
          await page.screenshot({ path: screenshotPath, fullPage: true });

          const result = await auditPage(page, vpName, vpConfig);
          result.route = route;
          result.target = target;
          result.screenshot = screenshotPath;
          report.results[route][vpName] = result;

          for (const f of result.findings) {
            if (report.summary[f.severity] !== undefined) report.summary[f.severity]++;
            report.summary.total++;
          }
        } catch (err) {
          report.results[route][vpName] = {
            route,
            viewport: vpName,
            error: err.message,
            totalFindings: 0,
            findings: [],
          };
        } finally {
          await context.close();
        }
      }
    }
  } finally {
    await browser.close();
  }

  const reportPath = path.join(args.out, 'geometry-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
  console.log(`DOM Geometry Audit complete -> ${reportPath}`);
  console.log(`Summary: Total=${report.summary.total} (P0=${report.summary.P0}, P1=${report.summary.P1}, P2=${report.summary.P2}, P3=${report.summary.P3})`);

  if (args.failOn) {
    const threshold = SEVERITY_RANK[args.failOn];
    const failed = report.summary.P0 + report.summary.P1 + report.summary.P2 + report.summary.P3 > 0
      && Object.entries(SEVERITY_RANK).some(([sev, rank]) => rank <= threshold && report.summary[sev] > 0);
    if (failed) {
      console.error(`Failing because findings at or above ${args.failOn} were detected.`);
      process.exit(1);
    }
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
