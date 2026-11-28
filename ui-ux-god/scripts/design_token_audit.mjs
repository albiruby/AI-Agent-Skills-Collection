#!/usr/bin/env node
/**
 * design_token_audit.mjs
 * Extracts rendered typography, WCAG contrast, 4px spacing-grid compliance,
 * and concentric border-radius nesting using Playwright.
 *
 * Resolves Playwright from the current project first, then from the global npm root.
 *
 * Usage:
 *   node design_token_audit.mjs --url http://localhost:3000 --out ./audit-out
 *   node design_token_audit.mjs --url http://localhost:3000 --routes /,/pricing --channel msedge
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
    routes: '/',
    width: 1440,
    height: 900,
    channel: '',
    colorScheme: 'light',
    storageState: '',
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
    else if (key === '--routes') { args.routes = val; i++; }
    else if (key === '--width') { args.width = Number(val) || 1440; i++; }
    else if (key === '--height') { args.height = Number(val) || 900; i++; }
    else if (key === '--channel') { args.channel = val; i++; }
    else if (key === '--color-scheme') { args.colorScheme = val; i++; }
    else if (key === '--storage-state') { args.storageState = val; i++; }
    else if (key === '--fail-on') { args.failOn = val.toUpperCase(); i++; }
  }
  if (!args.url) {
    console.error('Error: --url is required.');
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
  try {
    return require('playwright');
  } catch {}
  try {
    const globalRoot = execSync('npm root -g', { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
    return require(path.join(globalRoot, 'playwright'));
  } catch {}
  console.error('Playwright not found. Install it in the target project:');
  console.error('  npm install -D playwright && npx playwright install chromium');
  console.error('Or use a system browser channel: --channel msedge / --channel chrome');
  process.exit(2);
}

async function auditPage(page, url) {
  return page.evaluate(() => {
    const parseRgba = (str) => {
      const m = str && str.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
      if (!m) return null;
      return { r: Number(m[1]), g: Number(m[2]), b: Number(m[3]), a: m[4] !== undefined ? Number(m[4]) : 1 };
    };

    const relLuminance = ({ r, g, b }) => {
      const ch = [r, g, b].map((v) => {
        const s = v / 255;
        return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2];
    };

    const contrastRatio = (c1, c2) => {
      const l1 = relLuminance(c1);
      const l2 = relLuminance(c2);
      return Number(((Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05)).toFixed(2));
    };

    const getEffectiveBg = (el) => {
      let cur = el;
      while (cur && cur !== document.documentElement) {
        const bg = parseRgba(window.getComputedStyle(cur).backgroundColor);
        if (bg && bg.a > 0.85) return bg;
        cur = cur.parentElement;
      }
      const rootBg = parseRgba(window.getComputedStyle(document.body).backgroundColor);
      return (rootBg && rootBg.a > 0.5) ? rootBg : { r: 255, g: 255, b: 255, a: 1 };
    };

    const getSelector = (el) => {
      if (el.id) return `#${el.id}`;
      const tag = el.tagName.toLowerCase();
      const cls = typeof el.className === 'string'
        ? el.className.trim().split(/\s+/).filter(Boolean).slice(0, 3).join('.')
        : '';
      return cls ? `${tag}.${cls}` : tag;
    };

    const isVisible = (el) => {
      const st = window.getComputedStyle(el);
      if (st.display === 'none' || st.visibility === 'hidden' || parseFloat(st.opacity) === 0) return false;
      const r = el.getBoundingClientRect();
      return r.width > 0.5 && r.height > 0.5;
    };

    const fontFamilies = new Set();
    const fontSizes = new Set();
    const textColors = new Set();
    const contrastFailures = [];
    const radiusViolations = [];
    const spacingOffGrid = [];
    const readabilityIssues = [];

    for (const el of Array.from(document.querySelectorAll('*')).filter(isVisible)) {
      const st = window.getComputedStyle(el);

      const directText = Array.from(el.childNodes)
        .filter((n) => n.nodeType === Node.TEXT_NODE)
        .map((n) => n.textContent.trim())
        .join(' ')
        .trim();

      if (directText.length > 0) {
        const ff = st.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
        const fsPx = parseFloat(st.fontSize);
        const fw = parseInt(st.fontWeight, 10) || 400;
        fontFamilies.add(ff);
        fontSizes.add(`${Math.round(fsPx)}px`);
        textColors.add(st.color);

        const fg = parseRgba(st.color);
        const bg = getEffectiveBg(el);
        if (fg && bg) {
          const ratio = contrastRatio(fg, bg);
          const isLarge = fsPx >= 24 || (fsPx >= 18.67 && fw >= 700);
          const minReq = isLarge ? 3.0 : 4.5;
          if (ratio < minReq && contrastFailures.length < 60) {
            contrastFailures.push({
              severity: ratio < 3.0 ? 'P0' : 'P1',
              selector: getSelector(el),
              textPreview: directText.slice(0, 50),
              contrastRatio: ratio,
              requiredRatio: minReq,
              fgColor: st.color,
              bgColor: `rgb(${bg.r}, ${bg.g}, ${bg.b})`,
              fontSizePx: fsPx,
            });
          }
        }

        if (el.tagName === 'P' && directText.length > 80) {
          const lh = parseFloat(st.lineHeight);
          const r = el.getBoundingClientRect();
          if (!Number.isNaN(lh) && lh / fsPx < 1.35) {
            readabilityIssues.push({
              severity: 'P2',
              selector: getSelector(el),
              issue: `Tight paragraph line-height (${(lh / fsPx).toFixed(2)} < 1.35)`,
            });
          }
          if (r.width > fsPx * 50 && readabilityIssues.length < 30) {
            readabilityIssues.push({
              severity: 'P2',
              selector: getSelector(el),
              issue: `Wide prose measure (${Math.round(r.width)}px at ${fsPx}px; keep under ~75ch)`,
            });
          }
        }
      }

      if (['SECTION', 'DIV', 'ARTICLE', 'HEADER', 'FOOTER', 'MAIN', 'ASIDE'].includes(el.tagName)) {
        const pads = [st.paddingTop, st.paddingRight, st.paddingBottom, st.paddingLeft]
          .map((v) => Math.round(parseFloat(v) || 0));
        const off = pads.filter((p) => p > 2 && p % 4 !== 0);
        if (off.length > 0 && spacingOffGrid.length < 40) {
          spacingOffGrid.push({
            severity: 'P2',
            selector: getSelector(el),
            offGridPaddingPx: off,
          });
        }
      }

      const rOuter = parseFloat(st.borderTopLeftRadius) || 0;
      if (rOuter >= 8 && rOuter < 999) {
        const pad = Math.min(parseFloat(st.paddingTop) || 0, parseFloat(st.paddingLeft) || 0);
        if (pad >= 4) {
          for (const ch of el.children) {
            if (!isVisible(ch)) continue;
            const chSt = window.getComputedStyle(ch);
            const rInner = parseFloat(chSt.borderTopLeftRadius) || 0;
            if (rInner >= 6 && rInner < 999) {
              const ideal = Math.max(2, rOuter - pad);
              if (Math.abs(rInner - ideal) > 3 && rInner >= rOuter && radiusViolations.length < 30) {
                radiusViolations.push({
                  severity: 'P2',
                  parentSelector: getSelector(el),
                  childSelector: getSelector(ch),
                  outerRadiusPx: rOuter,
                  paddingPx: pad,
                  actualInnerRadiusPx: rInner,
                  recommendedInnerRadiusPx: ideal,
                });
              }
            }
          }
        }
      }
    }

    return {
      inventory: {
        fontFamilies: Array.from(fontFamilies),
        fontSizeCount: fontSizes.size,
        fontSizes: Array.from(fontSizes).sort((a, b) => parseInt(a, 10) - parseInt(b, 10)),
        uniqueTextColorCount: textColors.size,
      },
      flags: {
        tooManyFontFamilies: fontFamilies.size > 3,
        tooManyFontSizes: fontSizes.size > 9,
      },
      contrastFailures,
      radiusViolations,
      readabilityIssues,
      spacingOffGrid,
    };
  });
}

function routeSlug(route) {
  const cleaned = route.replace(/^https?:\/\/[^/]+/i, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-+|-+$/g, '');
  return cleaned || 'root';
}

async function main() {
  const args = parseArgs(process.argv);
  fs.mkdirSync(args.out, { recursive: true });

  const playwright = loadPlaywright();
  const browser = await playwright.chromium.launch({
    headless: true,
    ...(args.channel ? { channel: args.channel } : {}),
  });

  const routes = args.routes.split(',').map((s) => s.trim()).filter(Boolean);
  if (routes.length === 0) routes.push('/');

  let storageState;
  if (args.storageState) {
    if (!fs.existsSync(args.storageState)) {
      console.error(`Storage state not found: ${args.storageState}`);
      process.exit(2);
    }
    storageState = args.storageState;
  }

  const report = {
    url: args.url,
    routes,
    timestamp: new Date().toISOString(),
    viewport: `${args.width}x${args.height}`,
    colorScheme: args.colorScheme,
    channel: args.channel || 'bundled-chromium',
    results: {},
    totals: { contrastFailures: 0, radiusViolations: 0, spacingOffGrid: 0, readabilityIssues: 0 },
  };

  try {
    for (const route of routes) {
      const target = new URL(route, args.url).toString();
      const context = await browser.newContext({
        viewport: { width: args.width, height: args.height },
        colorScheme: args.colorScheme,
        reducedMotion: 'reduce',
        ...(storageState ? { storageState } : {}),
      });
      const page = await context.newPage();
      try {
        await page.goto(target, { waitUntil: 'networkidle', timeout: 30000 }).catch(async () => {
          await page.goto(target, { waitUntil: 'load', timeout: 30000 });
        });
        await page.evaluate(() => document.fonts.ready).catch(() => {});
        await page.waitForTimeout(600);

        const result = await auditPage(page, target);
        const outPath = path.join(args.out, `design-tokens-${routeSlug(route)}.json`);
        fs.writeFileSync(outPath, JSON.stringify({ url: target, timestamp: new Date().toISOString(), ...result }, null, 2));
        report.results[route] = { ...result, report: outPath };

        report.totals.contrastFailures += result.contrastFailures.length;
        report.totals.radiusViolations += result.radiusViolations.length;
        report.totals.spacingOffGrid += result.spacingOffGrid.length;
        report.totals.readabilityIssues += result.readabilityIssues.length;
      } catch (err) {
        report.results[route] = { error: err.message };
      } finally {
        await context.close();
      }
    }
  } finally {
    await browser.close();
  }

  const outPath = path.join(args.out, 'design-tokens-report.json');
  fs.writeFileSync(outPath, JSON.stringify(report, null, 2));
  console.log(`Design Token Audit complete -> ${outPath}`);
  console.log(`Contrast failures: ${report.totals.contrastFailures} | Radius issues: ${report.totals.radiusViolations} | Off-grid spacing: ${report.totals.spacingOffGrid} | Readability: ${report.totals.readabilityIssues}`);

  if (args.failOn) {
    const threshold = SEVERITY_RANK[args.failOn];
    const all = Object.values(report.results).flatMap((r) => [
      ...(r.contrastFailures || []),
      ...(r.radiusViolations || []),
      ...(r.spacingOffGrid || []),
      ...(r.readabilityIssues || []),
    ]);
    const failed = all.some((f) => (SEVERITY_RANK[f.severity] ?? 9) <= threshold);
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
