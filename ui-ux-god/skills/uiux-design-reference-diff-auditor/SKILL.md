---
name: uiux-design-reference-diff-auditor
description: "Compare a live implementation against design references, screenshots, mockups, or design-system specs and quantify deviations. Use when a build must match Figma or a visual reference, or when pixel and geometry differences need evidence."
---

# Design Reference & Implementation Diff

## Use when

- A build must match Figma, a mockup, or a supplied screenshot.
- You need measured deviations rather than subjective 'looks different'.
- A redesign or handoff needs a reference-vs-live diff.

## Do not use when

- There is no authoritative reference; use the visual audit specialists instead.
- The reference is outdated or contradicts the current design system.

## Mission

Use the intended design as a measurable reference without treating every pixel difference as a defect.

## Procedure

1. Identify authoritative reference(s), target screen, viewport, state, device scale, font environment, theme, and content. Ask no questions when references already define these; otherwise record assumptions.
2. Normalize comparison conditions: viewport dimensions, DPR, zoom, scroll position, locale, theme, loaded fonts, image assets, and dynamic content. Capture the live implementation under matching conditions.
3. Compare macro composition first: page frame, header height, container width, columns, hero proportions, section positions, and fold. Then compare component geometry and micro-details.
4. Use overlays, side-by-side screenshots, image diff, and element geometry where available. Separate geometric difference, color difference, text/content difference, and runtime/environment noise.
5. Measure key bounds, spacing, text wrapping, font weight/size, radii, borders, shadows, image crop, and icon positioning. Provide region/element-specific observations rather than a single similarity score.
6. Classify deviations as defect, intentional adaptation, content variation, responsive variation, or reference ambiguity. Ask for clarification only where the intended target is genuinely indeterminate.
7. Translate verified deviations into concrete component/token/code changes. Do not distort responsive behavior to match a single screenshot at all widths.
8. Re-capture under the same conditions and compare again; preserve both baseline and after evidence.

## Precision defaults

- Match viewport, DPR, theme, locale, zoom, and content state before comparing.
- Measure position, size, spacing, type, color, radius, and asset differences.
- Tolerance 1–2px for geometry; flag larger deviations with evidence.
- Separate intentional responsive/content differences from defects.

## Quality gates

- [ ] Reference and implementation use matched test conditions.
- [ ] Difference reports identify region and likely cause.
- [ ] Intentional responsive behavior is not mistaken for a defect.
- [ ] No universal percentage score substitutes for detailed analysis.

## Evidence to capture

- Reference and live screenshots at identical conditions.
- Overlay/diff and measured deltas.
- Deviation list with severity and intended rule.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/evidence-schema.md`
- `../../templates/audit-report-template.md`
