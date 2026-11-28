---
name: uiux-color-visual-hierarchy-auditor
description: "Audit palette, contrast, semantic color, visual hierarchy, states, and theme behavior without flattening brand expression. Use when colors compete, CTAs lack prominence, dark mode looks harsh, or contrast and semantic states need verification."
---

# Color, Contrast & Visual Hierarchy

## Use when

- Every element shouts at once and the primary action is unclear.
- Contrast fails, status colors are ambiguous, or dark mode feels harsh.
- Brand color and accessibility are in tension and need an evidence-based decision.

## Do not use when

- The issue is purely spacing or layout geometry.
- You need a full WCAG conformance audit; use the WCAG specialist and treat this as the color deep-dive.

## Mission

Ensure visual priority and meaning survive varied conditions.

## Procedure

1. Identify theme sources and tokens for background, surface, text, muted text, border, brand, accent, success, warning, danger, info, and interactive states. Inspect light/dark/high-contrast themes when supported.
2. Evaluate hierarchy by contrast, size, weight, spacing, position, and grouping. Confirm the primary action is visually distinct without making secondary actions disappear.
3. Measure text contrast and non-text UI/graphic contrast when possible using actual rendered color values, including opacity, overlays, gradients, images, and compositing. Do not estimate contrast from source token names alone.
4. Check color-only meaning: error/success states, chart series, status dots, selection, required fields, and alerts need another cue such as text, icon, pattern, or shape when appropriate.
5. Inspect focus, hover, selected, disabled, loading, error, warning, and visited states. Disabled controls should remain perceivable enough to understand, while not appearing interactive.
6. Test color behavior across themes, forced-colors/high-contrast settings, dim displays, and color vision simulation where tools are available. Use simulation as a diagnostic, not a substitute for user testing.
7. Correct contrast with the smallest semantic token or component change. Check brand constraints and ensure color correction does not break hierarchy or create alarming overuse of saturated colors.

## Precision defaults

- Body text >= 4.5:1; large text >= 3.0:1; UI boundaries/icons >= 3.0:1.
- Do not rely on color alone for status; pair with icon, label, or pattern.
- Dark mode: use surface luminance steps and low-opacity hairlines, not pure black shadows.
- Limit high-saturation primary actions to one clear focal CTA per viewport.

## Quality gates

- [ ] WCAG contrast values are measured when claiming conformance.
- [ ] Color is not the only carrier of critical information.
- [ ] Theme variants are tested independently.
- [ ] Perceived hierarchy is reviewed in grayscale or reduced-color conditions when useful.

## Evidence to capture

- Foreground/background pair and measured ratio.
- Light/dark screenshots and token values.
- Semantic state inventory: default, hover, active, disabled, error, success, warning.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/design-laws-formulas.md`
- `../../references/wcag22-quick-reference.md`
