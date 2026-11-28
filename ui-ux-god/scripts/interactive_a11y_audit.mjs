#!/usr/bin/env node
/**
 * interactive_a11y_audit.mjs
 * Audits mobile touch targets, keyboard focus-visible rings, broken/stretched images,
 * semantic labels, and heading hierarchy using Playwright.
 *
 * Resolves Playwright from the current project first, then from the global npm root.
 *
 * Usage:
 *   node interactive_a11y_audit.mjs --url http://localhost:3000 --out ./audit-out
 *   node interactive_a11y_audit.mjs --url http://localhost:3000 --routes /,/checkout --channel msedge
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

function routeSlug(route) {
  const cleaned = route.replace(/^https?:\/\/[^/]+/i, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-+|-+$/g, '');
  return cleaned || 'root';
}

async function touchTargets(page) {
  return page.evaluate(() => {
    const issues = [];
    const getSel = (el) => el.id
      ? `#${el.id}`
      : `${el.tagName.toLowerCase()}.${(typeof el.className === 'string' ? el.className.trim().split(/\s+/).slice(0, 2).join('.') : '')}`;

    for (const el of document.querySelectorAll('a, button, input, select, textarea, [role="button"]')) {
      const st = window.getComputedStyle(el);
      if (st.display === 'none' || st.visibility === 'hidden' || parseFloat(st.opacity) === 0) continue;
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      if (el.tagName === 'A' && el.closest('p')) continue;
      if (r.width < 44 || r.height < 44) {
        issues.push({
          severity: (r.width < 24 || r.height < 24) ? 'P0' : 'P1',
          selector: getSel(el),
          text: (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 40),
          sizePx: `${Math.round(r.width)}x${Math.round(r.height)}`,
          recommendedMinPx: '44x44',
        });
      }
    }
    return issues.slice(0, 60);
  });
}

async function staticA11y(page) {
  return page.evaluate(() => {
    const brokenImages = [];
    const a11y = [];
    const getSel = (el) => el.id
      ? `#${el.id}`
      : `${el.tagName.toLowerCase()}.${(typeof el.className === 'string' ? el.className.trim().split(/\s+/).slice(0, 2).join('.') : '')}`;

    for (const img of document.querySelectorAll('img')) {
      const st = window.getComputedStyle(img);
      if (st.display === 'none' || st.visibility === 'hidden') continue;
      const r = img.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;

      if (!img.complete || img.naturalWidth === 0) {
        brokenImages.push({ severity: 'P0', selector: getSel(img), src: img.src, issue: 'Broken image (naturalWidth === 0)' });
      } else if (st.objectFit === 'fill' || st.objectFit === '') {
        const natRatio = img.naturalWidth / img.naturalHeight;
        const renRatio = r.width / r.height;
        const distortion = Math.abs(natRatio - renRatio) / natRatio;
        if (distortion > 0.12) {
          brokenImages.push({
            severity: 'P1',
            selector: getSel(img),
            src: img.src,
            issue: `Image aspect ratio distorted by ${(distortion * 100).toFixed(1)}% (add object-cover or object-contain)`,
          });
        }
      }
      if (!img.hasAttribute('alt')) {
        a11y.push({ severity: 'P1', selector: getSel(img), issue: 'Missing alt attribute on <img>' });
      }
    }

    for (const btn of document.querySelectorAll('button, [role="button"]')) {
      const text = (btn.textContent || '').trim();
      const label = btn.getAttribute('aria-label') || btn.getAttribute('aria-labelledby') || btn.getAttribute('title');
      if (!text && !label) {
        a11y.push({ severity: 'P1', selector: getSel(btn), issue: 'Icon-only button missing aria-label or accessible name' });
      }
    }

    for (const inp of document.querySelectorAll('input:not([type="hidden"]), textarea, select')) {
      const id = inp.id;
      const hasLabel = (id && document.querySelector(`label[for="${CSS.escape(id)}"]`)) || inp.closest('label') || inp.getAttribute('aria-label') || inp.getAttribute('aria-labelledby');
      if (!hasLabel) {
        a11y.push({ severity: 'P1', selector: getSel(inp), issue: 'Form control missing associated <label> or aria-label' });
      }
    }

    let prevLevel = 0;
    for (const h of document.querySelectorAll('h1, h2, h3, h4, h5, h6')) {
      const level = Number(h.tagName[1]);
      if (prevLevel > 0 && level > prevLevel + 1) {
        a11y.push({ severity: 'P2', selector: getSel(h), issue: `Heading level skipped from H${prevLevel} to H${level}` });
      }
      prevLevel = level;
    }

    return { brokenImages, a11y };
  });
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
    colorScheme: args.colorScheme,
    channel: args.channel || 'bundled-chromium',
    results: {},
    totals: { touchTargets: 0, media: 0, a11y: 0, focusRings: 0 },
  };

  try {
    for (const route of routes) {
      const target = new URL(route, args.url).toString();
      const result = {
        route,
        target,
        mobileTouchTargets: [],
        brokenOrStretchedImages: [],
        a11yViolations: [],
        focusRingIssues: [],
      };

      // 1. Mobile touch targets
      const mobileCtx = await browser.newContext({
        viewport: { width: 375, height: 812 },
        deviceScaleFactor: 2,
        colorScheme: args.colorScheme,
        reducedMotion: 'reduce',
        ...(storageState ? { storageState } : {}),
      });
      const mobilePage = await mobileCtx.newPage();
      try {
        await mobilePage.goto(target, { waitUntil: 'networkidle', timeout: 30000 }).catch(async () => {
          await mobilePage.goto(target, { waitUntil: 'load', timeout: 30000 });
        });
        await mobilePage.evaluate(() => document.fonts.ready).catch(() => {});
        await mobilePage.waitForTimeout(500);
        result.mobileTouchTargets = await touchTargets(mobilePage);
        const slug = routeSlug(route);
        await mobilePage.screenshot({ path: path.join(args.out, `${slug}-mobile-375.png`), fullPage: true }).catch(() => {});
      } catch (err) {
        result.mobileError = err.message;
      } finally {
        await mobileCtx.close();
      }

      // 2. Desktop a11y + keyboard focus
      const desktopCtx = await browser.newContext({
        viewport: { width: 1440, height: 900 },
        colorScheme: args.colorScheme,
        reducedMotion: 'reduce',
        ...(storageState ? { storageState } : {}),
      });
      const page = await desktopCtx.newPage();
      try {
        await page.goto(target, { waitUntil: 'networkidle', timeout: 30000 }).catch(async () => {
          await page.goto(target, { waitUntil: 'load', timeout: 30000 });
        });
        await page.evaluate(() => document.fonts.ready).catch(() => {});
        await page.waitForTimeout(500);

        const statics = await staticA11y(page);
        result.brokenOrStretchedImages = statics.brokenImages;
        result.a11yViolations = statics.a11y;

        for (let i = 0; i < 15; i++) {
          await page.keyboard.press('Tab');
          const focusCheck = await page.evaluate(() => {
            const el = document.activeElement;
            if (!el || el === document.body) return null;
            const st = window.getComputedStyle(el);
            const hasOutline = st.outlineStyle !== 'none' && parseFloat(st.outlineWidth) > 0;
            const hasShadow = st.boxShadow && st.boxShadow !== 'none';
            if (!hasOutline && !hasShadow) {
              return {
                severity: 'P2',
                selector: el.id ? `#${el.id}` : el.tagName.toLowerCase(),
                text: (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 40),
                issue: 'Focused element has no visible outline or box-shadow focus ring',
              };
            }
            return null;
          });
          if (focusCheck && !result.focusRingIssues.some((x) => x.selector === focusCheck.selector && x.text === focusCheck.text)) {
            result.focusRingIssues.push(focusCheck);
          }
        }
      } catch (err) {
        result.desktopError = err.message;
      } finally {
        await desktopCtx.close();
      }

      report.results[route] = result;
      report.totals.touchTargets += result.mobileTouchTargets.length;
      report.totals.media += result.brokenOrStretchedImages.length;
      report.totals.a11y += result.a11yViolations.length;
      report.totals.focusRings += result.focusRingIssues.length;
    }
  } finally {
    await browser.close();
  }

  const outPath = path.join(args.out, 'a11y-interaction-report.json');
  fs.writeFileSync(outPath, JSON.stringify(report, null, 2));
  console.log(`Interactive & A11y Audit complete -> ${outPath}`);
  console.log(`Touch targets: ${report.totals.touchTargets} | Media: ${report.totals.media} | A11y: ${report.totals.a11y} | Focus rings: ${report.totals.focusRings}`);

  if (args.failOn) {
    const threshold = SEVERITY_RANK[args.failOn];
    const all = Object.values(report.results).flatMap((r) => [
      ...(r.mobileTouchTargets || []),
      ...(r.brokenOrStretchedImages || []),
      ...(r.a11yViolations || []),
      ...(r.focusRingIssues || []),
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
