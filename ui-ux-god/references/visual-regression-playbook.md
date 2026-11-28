# Visual Regression Playbook

Use this reference when building or operating screenshot-based visual tests for a UI audit or repair.

## 1. Before adding tooling

1. Inspect the existing stack: Playwright, Cypress, Storybook, Chromatic, Percy, BackstopJS, or a custom diff.
2. Follow the project’s existing configuration and CI conventions.
3. If nothing exists, propose the smallest viable Playwright setup; do not add a platform without approval.

## 2. What to cover

Prioritize:

- Critical routes and the primary task flow.
- Repeated shared components (button, input, card, table, modal, nav).
- Historically fragile areas: header, pricing cards, checkout summary, data tables.
- Key states: default, hover, focus, disabled, loading, empty, error, long content.
- Viewports: 320, 375, 768, 1024, 1440; add product-specific sizes.
- Themes/locales where the product supports them.

Do not snapshot every route blindly. A small, owned, reviewed suite beats a giant ignored one.

## 3. Stabilize capture

- Pin browser/version, viewport, DPR, OS/fonts (containerize where possible).
- Disable animations/transitions and caret; wait for `document.fonts.ready`.
- Freeze time/timezone/locale; seed random data; stub volatile network responses.
- Hide or mask only truly volatile regions: timestamps, ads, avatars, live counters, maps.
- Capture at a deterministic scroll position; for full-page shots, account for sticky headers.
- Use the same auth/storage state for baseline and candidate.

## 4. Playwright starting point

```ts
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/visual',
  snapshotDir: './tests/visual/__screenshots__',
  expect: {
    toHaveScreenshot: {
      maxDiffPixelRatio: 0.002,
      animations: 'disabled',
      caret: 'hide',
    },
  },
  use: {
    baseURL: process.env.BASE_URL ?? 'http://localhost:3000',
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    colorScheme: 'light',
    locale: 'en-US',
    timezoneId: 'UTC',
    reducedMotion: 'reduce',
  },
});
```

```ts
test('pricing cards — desktop', async ({ page }) => {
  await page.goto('/pricing');
  await page.evaluate(() => document.fonts.ready);
  await expect(page).toHaveScreenshot('pricing-1440.png', {
    fullPage: true,
    mask: [page.locator('[data-visual-mask]')],
  });
});
```

## 5. Thresholds

- Start strict: **0.1–0.2%** pixel ratio, or a per-region threshold.
- Tune only with evidence; document why.
- A zero threshold is often flaky across OS/font rendering; a loose threshold hides real defects.
- Prefer **region-level** assertions for critical components over one giant full-page diff.
- Never use a diff score as the sole definition of quality; review the image.

## 6. Baseline policy

- A baseline is created only from an **accepted, reviewed** product state.
- Baseline updates are reviewed like code; do not auto-approve in CI.
- Keep baselines in version control; organize by browser/viewport/theme/state.
- Define an owner for baseline changes.
- When a diff appears, triage: intended change / regression / environmental noise.

## 7. CI integration

- Run visual tests on PRs that touch UI, tokens, or shared components.
- Upload the diff, expected, actual, and trace as artifacts.
- Fail the job on unexpected diffs; allow an explicit “update snapshots” workflow.
- Do not let a flaky visual job block unrelated PRs; quarantine and fix flakiness.
- Keep runtime reasonable: shard by route/viewport if needed.

## 8. Triage checklist

| Question | Action |
|---|---|
| Is the change intended and reviewed? | Approve baseline update with a reason |
| Is it a real regression? | File a finding; link the diff |
| Is it environmental (font/OS/DPR)? | Pin the environment; do not update blindly |
| Is only a masked region different? | Review the mask; it may be hiding content |
| Is the diff score tiny but the visual change meaningful? | Trust the image, not the score |
| Is the baseline stale? | Recreate from an accepted build, not from the failing run |

## 9. Anti-patterns

- Auto-updating snapshots to make CI green.
- Masking large content areas to avoid flakiness.
- Comparing screenshots captured under different themes, locales, or DPRs.
- Using a full-page diff as the only visual test.
- Ignoring a diff because the percentage is low.
- Storing baselines outside version control.
- Running visual tests only locally, never in CI.
