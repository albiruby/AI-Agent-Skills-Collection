# Example: Web / SaaS Dashboard

## 1. Request

> Document this Next.js dashboard and produce a GitHub social card plus README hero from real screenshots. Don't invent features.

## 2. Context

- Stack, scripts, routes, auth, data sources.
- Verified features and limitations.
- Existing brand colors/fonts/logo.
- Target: GitHub + product site + docs.

## 3. Plan

| Deliverable | Details |
|---|---|
| README | Value, hero, quick start, features, architecture link |
| `docs/ARCHITECTURE.md` | Routes, data flow, auth, caching |
| `docs/DEPLOYMENT.md` | Build, env, deploy, rollback |
| Raw captures | Desktop 1440x900, mobile 390x844 |
| Clean assets | Viewport cards, no browser chrome |
| Store/preview | GitHub 1280x640, OG 1200x630, README hero |
| Copy | GitHub About, release notes |
| QA | Links, placeholders, dimensions, clean assets |

## 4. Capture

Use Playwright/Chromium with a deterministic demo account and synthetic data:

```js
await page.setViewportSize({ width: 1440, height: 900 });
await page.addStyleTag({ content: '::-webkit-scrollbar { display: none !important; }' });
await page.screenshot({ path: 'docs/assets/raw/dashboard_desktop.png', fullPage: false });
```

Capture:

- Main dashboard.
- One core workflow.
- Mobile viewport.
- Any state that proves a key feature.

Hide cookie banners, scrollbars, dev overlays, and personal data.

## 5. Clean

```bash
python skills/clean-screenshot-slicer/scripts/slice_clean_device.py \
  --input docs/assets/raw \
  --output docs/assets/clean \
  --preset viewport-card \
  --radius 24
```

Check rounded corners, no clipped content, no browser chrome, no personal data.

## 6. Compose

Use `../templates/web-mobile-manifest.json`:

- `GITHUB_SOCIAL_1280x640.png`
- `OG_1200x630.png`
- Optional feature showcase.

```bash
python skills/store-preview-asset-builder/scripts/compose_store_assets.py \
  --manifest docs/store-assets/manifest.json \
  --output-dir docs/store-assets
```

Keep headline short; verify text contrast and no collision with the dashboard.

## 7. Docs and copy

- README: one-sentence value, verified features, quick start, clean hero.
- Architecture: route/module map, data flow, auth boundaries, persistence.
- Deployment: actual build/env/deploy/rollback steps.
- GitHub About: ~160 chars, no superlatives.

## 8. QA

Run `validate_doc_pack.py`, then check:

- No raw browser chrome.
- OG/social dimensions match filenames.
- Claims match code.
- No secrets or customer data.
- Links resolve with exact casing.

## 9. Handoff

State which screenshots are real, which docs were verified, and whether store/social requirements were checked.
