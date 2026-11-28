---
name: uiux-microdetail-polish-specialist
description: "Detect and polish high-salience micro-defects: optical centering, 1px misalignment, divider length, border and radius joins, icon offsets, baseline drift, and pixel-level spacing. Use when the macro layout is stable and the interface needs flagship-grade finish, or when the user reports small visual imperfections."
---

# Micro-detail & Pixel Polish

## Use when

- The layout is structurally sound but the interface still feels rough or amateur.
- The user reports a logo that looks off-center, a divider that stops short, an icon sitting high, or a border that looks wrong.
- You are doing the final precision pass before launch or handoff.

## Do not use when

- The page still has broken macro layout, overflow, or missing states; fix those first.
- A change would only satisfy a screenshot at one viewport while damaging others.

## Mission

Perform the final precision pass after major layout and component behavior are stable.

## Procedure

1. Inspect high-salience details first: brand mark and wordmark alignment, navigation icons, buttons, input adornments, avatar stacks, badges, tabs, table actions, and repeated card corners.
2. Use screenshot crops at native scale and enlarged inspection where appropriate. Cross-check with bounding boxes and computed styles; do not rely on enlargement alone because resampling can create misleading apparent edges.
3. Check optical alignment separately from mathematical alignment. Account for glyph shapes, icon visual mass, transparent padding in SVG/PNG assets, font ascenders/descenders, and asymmetric shapes before applying an offset.
4. Inspect borders and dividers for 1px/2px thickness consistency, full-bleed versus inset intent, joins, radius intersections, clipping, antialiasing, and contrast against adjacent surfaces.
5. Check micro-spacing: icon-to-label gap, label-to-control gap, badge padding, button content centering, list row rhythm, caption offsets, breadcrumb separators, table cell alignment, and focus-ring clearance.
6. Check component polish: consistent corner radii, shadow blur/spread/opacity, border color, disabled opacity, hover transitions, icon stroke weight, and line-height. Keep these choices aligned with existing design tokens.
7. Prioritize actual defects over aesthetic preference. Preserve intentional asymmetry, brand-specific optical adjustments, platform conventions, and content-driven variation.
8. Apply a correction only when the intended alignment is supported by repeated patterns, design references, tokens, or strong geometry evidence. Record before/after evidence and the CSS/component cause.

## Precision defaults

- Centering tolerance 1.5px; optical nudge usually 1–2px, never a blind `translateX`.
- Border hairline: 1px; check 125/150/200% DPI for blur or disappearance.
- Concentric radius: `R_inner = max(0, R_outer - padding)`, tolerance 2px.
- Icon-to-label: use `inline-flex; align-items:center; gap`; check midpoint delta, not just bounding boxes.
- Inspect at 100% scale and at device pixel ratio 2; do not judge from enlarged crops alone.

## Quality gates

- [ ] Every micro-fix has an explicit visual rule or reference.
- [ ] No blind transform: translateX/Y patching without understanding the asset or layout cause.
- [ ] No needless subpixel churn that causes blurry text or inconsistent rasterization.
- [ ] The result is checked at 100% scale and relevant device pixel ratios.

## Evidence to capture

- Screenshot crop at native scale and DPR 2.
- Element bounds, computed line-height, and SVG viewBox/transparent padding.
- The intended rule or reference that justifies the correction.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/micro-defect-catalog.md`
- `../../references/surgical-fix-patterns.md`
