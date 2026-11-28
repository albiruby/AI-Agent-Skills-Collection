# Case 01 — Micro-detail Landing Page

## Fixture

A fictional SaaS landing page at `http://localhost:3000` with:

- A 3-slot header: menu left, logo center, login + CTA right.
- The logo is 35.5px left of the header center at 1440px.
- A pricing divider stops 24px short on the right.
- The primary CTA has `outline: none` and no focus replacement.
- A muted gray body text is `#9ca3af` on white (2.54:1).
- Source access and a running dev server are available.

## Prompt

> Audit this landing page at 375, 768, and 1440. Catch the small visual defects, tell me what is actually wrong, and fix the high-confidence issues. Prove the fixes.

## Expected behavior

1. Load `ui-ux-god` and route to layout, micro-detail, and surgical repair.
2. Capture baseline screenshots and DOM geometry at 3 viewports.
3. Report the logo delta with exact px and the parent flex/grid cause.
4. Decide the divider intent (full-bleed vs content-aligned) before fixing.
5. Flag the missing focus ring and contrast failure as accessibility, not polish.
6. Fix at the correct layer (grid header, divider span, `:focus-visible`, token).
7. Re-render and re-measure before/after; test 375/768 for regressions.
8. State what was not tested (e.g., Safari, screen reader).

## Evidence required

- Logo: element center vs header center, delta, parent `justify-content`.
- Divider: span, left/right gaps, parent padding.
- Focus: computed outline/box-shadow before/after.
- Contrast: foreground/background values and ratio.
- Before/after screenshot paths at the same viewport/theme.

## Scoring focus

| Criterion | Must show |
|---|---|
| Evidence quality | Exact measurements, not “looks off” |
| Root cause | Grid/flex parent fix, not padding nudge |
| Repair quality | No `!important`; token-based contrast; focus-visible |
| Verification | Before/after + adjacent breakpoints |
| Coverage honesty | States/browsers not tested |

## Failure modes

- “The logo looks slightly off” with no measurement.
- Fixing the logo with `margin-left: 35px`.
- Changing the divider width without deciding intent.
- Treating the focus ring as cosmetic.
- Claiming “fixed” after code edits only.
- Ignoring 375px regressions.
