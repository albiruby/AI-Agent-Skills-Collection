---
name: uiux-css-layout-root-cause-specialist
description: "Diagnose and repair CSS/layout root causes: flexbox, grid, sizing, overflow, stacking contexts, positioning, and responsive constraints. Use when a layout bug resists surface patches, when `!important` is spreading, or when the parent layout must be fixed properly."
---

# CSS & Layout Root-Cause Engineering

## Use when

- A layout bug keeps returning after surface patches.
- Flex/grid sizing, min-width, overflow, stacking, or positioning is the suspected cause.
- You need to replace `!important` and magic numbers with a structural fix.

## Do not use when

- The issue is a content or asset problem with no layout cause.
- You need a full design-system audit; use the visual design system specialist.

## Mission

Correct the rule that caused the defect instead of accumulating patch overrides.

## Procedure

1. Inspect the computed style chain: display, position, box-sizing, width/height, min/max dimensions, margin, padding, gap, flex/grid properties, overflow, transform, contain, z-index, and typography.
2. Trace the containing block, formatting context, stacking context, grid tracks, flex sizing, intrinsic content contribution, min-width:auto behavior, and overflow ancestors.
3. Reproduce at the failing viewport and adjacent sizes. Use devtools toggles or isolated test changes to confirm the causal property before writing a permanent fix.
4. Prefer semantic layout primitives: grid for two-dimensional structure, flex for one-dimensional alignment, flow for content, and positioning for intentional overlays. Use container queries when component width is the real dependency.
5. Resolve common problems: centered logo in a header with unequal nav groups, divider constrained to wrong parent, flex child refusing to shrink, grid overflow, 100vw scrollbar overflow, sticky header offset, z-index trapped by stacking context, and content clipped by fixed heights.
6. Avoid magic numbers, excessive !important, negative margins, transforms as structural corrections, fixed heights for text containers, and duplicated media queries.
7. Use design tokens and shared layout components where available. Add regression coverage for the failed viewport and at least one neighboring breakpoint.
8. Explain the root cause and why the chosen fix is stable.

## Precision defaults

- Inspect display, position, box-sizing, width/height, min/max, margin, padding, gap, flex/grid, overflow, transform, contain, z-index.
- Check containing block, formatting context, stacking context, and `min-width: auto`.
- Prefer grid for 2D structure, flex for 1D alignment, flow for content.
- Verify at the failing width and one neighboring breakpoint.

## Quality gates

- [ ] The causal property is identified and verified before final edit.
- [ ] The fix works at failing and neighboring widths.
- [ ] No unnecessary !important or cascade debt is introduced.
- [ ] Structural fixes do not break content expansion or localization.

## Evidence to capture

- Computed style chain and the causal property.
- Before/after geometry and screenshots.
- Why the fix is stable across content expansion/localization.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/surgical-fix-patterns.md`
- `../../references/micro-defect-catalog.md`
