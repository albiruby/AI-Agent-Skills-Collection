# Example 1 — Landing Page Micro-detail Audit

A worked example showing the evidence, findings, repair, and verification for a marketing landing page. The product is fictional; the measurements and method are the point.

## 1. Scope

- **Mode:** Audit + Repair
- **Surfaces:** `/` (home), `/pricing`
- **Viewports:** 375x812 (DPR 2), 768x1024 (DPR 2), 1440x900 (DPR 1)
- **Themes:** light, dark
- **Tools:** Playwright (Chromium), DOM geometry script, pixel inspector, manual screenshot review

## 2. Baseline

```bash
node ../../scripts/dom_geometry_audit.mjs \
  --url http://localhost:3000 \
  --routes /,/pricing \
  --viewports mobile,tablet,desktop \
  --out ./audit-out

python ../../scripts/pixel_precision_audit.py \
  --image ./audit-out/root-desktop-1440.png \
  --out ./audit-out/root-desktop-1440-annotated.png \
  --json ./audit-out/pixel-report.json
```

## 3. Findings

### [GEO-001] Header logo drifts 35.5px left of center

- **Category:** layout
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/`, guest, default
- **Environment:** 1440x900, DPR 1, Chromium, light, en-US, 100%
- **Evidence:** `.brand-logo` center 684.5px vs header center 720px; delta **-35.5px**; parent `display:flex; justify-content:space-between`; left slot 112px, right slot 183px
- **Observed:** Logo is 35.5px left of the header center at >=1024px.
- **Impact:** The brand mark reads as misaligned; the header feels unfinished.
- **Reproduction:** Open `/` at 1440x900; inspect `.brand-logo`; compare centers.
- **Cause:** Confirmed — asymmetric flex side slots with `justify-between`.
- **Fix:** Header grid `1fr auto 1fr`; logo in the middle track.
- **Verification:** `FIXED_AND_VERIFIED` — delta 0.0px at 1440; 375/768 re-checked.

### [GEO-002] Section divider stops 24px short on the right

- **Category:** layout
- **Severity:** P2
- **Confidence:** High
- **Surface:** `/pricing`, default
- **Environment:** 1440x900, DPR 1, light
- **Evidence:** `<hr>` span 1101px of 1344px content box; left gap 100px, right gap 124px; asymmetry **24px**
- **Observed:** Divider is inset asymmetrically; the right edge floats.
- **Impact:** Section separation looks accidental; the eye catches the uneven gap.
- **Cause:** Parent card has `padding-inline: 24px`; the `<hr>` is inside the padded content but was given an extra `mr-6`.
- **Fix:** Remove the asymmetric margin; use `w-full self-stretch` for a content-aligned divider, or `-mx-6 w-[calc(100%+3rem)]` for full-bleed.
- **Verification:** `FIXED_AND_VERIFIED` — left/right gap 24/24px; 375/768 re-checked.

### [A11Y-001] Focus ring missing on primary CTA

- **Category:** accessibility
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/`, default, keyboard
- **Environment:** 1440x900, Chromium, light
- **Evidence:** Focused `.btn-primary` has `outline: none`; `box-shadow: none`; screenshot `focus-cta.png`
- **Observed:** Keyboard focus is invisible on the main CTA.
- **Impact:** Keyboard users lose their place; the CTA is hard to operate confidently.
- **Cause:** Global reset removes outlines; no `:focus-visible` replacement on the button.
- **Fix:** Add `:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; }`, with a dark-surface token.
- **Verification:** `FIXED_AND_VERIFIED` — 2px ring, 4.8:1 against the CTA surface; tab order re-checked.

### [COL-001] Muted body text fails 4.5:1

- **Category:** color
- **Severity:** P1
- **Confidence:** High
- **Surface:** `/pricing`, plan descriptions
- **Environment:** 1440x900, light
- **Evidence:** `#9ca3af` on `#ffffff` = **2.54:1** (required 4.5:1)
- **Observed:** Plan description text is too light.
- **Impact:** Low-vision users struggle to read the plan details.
- **Cause:** A decorative gray token was reused for body copy.
- **Fix:** Use `#6b7280` on white = **4.83:1**; keep `#9ca3af` for disabled/decorative only.
- **Verification:** `FIXED_AND_VERIFIED` — 4.83:1; dark mode checked separately.

## 4. Repair order

1. `GEO-001` — structural header fix (unblocks visual trust).
2. `A11Y-001` — focus ring (accessibility).
3. `COL-001` — contrast token (accessibility).
4. `GEO-002` — divider alignment (polish).

## 5. Verification summary

| Finding | Before | After | Status |
|---|---|---|---|
| GEO-001 | delta -35.5px | delta 0.0px | FIXED_AND_VERIFIED |
| GEO-002 | 100/124px gaps | 24/24px gaps | FIXED_AND_VERIFIED |
| A11Y-001 | no focus ring | 2px ring, 4.8:1 | FIXED_AND_VERIFIED |
| COL-001 | 2.54:1 | 4.83:1 | FIXED_AND_VERIFIED |

## 6. What this example demonstrates

- Measure before judging: the logo looked “a bit off”; the actual delta was 35.5px.
- Decide the divider’s intent before changing its width.
- A focus ring is not cosmetic; it is a P1 accessibility defect.
- Every claimed fix has a comparable before/after measurement.
