---
name: uiux-visual-design-system-auditor
description: "Audit visual craft and design-system mathematics: typography hierarchy, contrast, 4/8px rhythm, concentric radii, elevation, icon consistency, and token drift. Use when evaluating visual polish, color harmony, readability, spacing discipline, or when repeated components drift from the system."
---

# Visual Design System & Token Audit

## Use when

- The interface works but does not look coherent, premium, or consistent.
- Repeated components use different spacing, radii, shadows, type sizes, or colors.
- You need to verify contrast, typographic scale, token discipline, or dark-mode parity.

## Do not use when

- The issue is a single broken layout constraint rather than a repeated system pattern.
- There is no rendered interface and no design tokens to inspect; use code review instead.

## Mission

Audit visual craft using measurable design-system mathematics rather than vague aesthetic opinions. Extract live rendered styles, find the shared rule behind repeated mismatches, and fix systemic drift at the token or component layer.

## Procedure

1. Inventory existing design-system sources: tokens, CSS variables, theme files, component libraries, Storybook, Figma variables, native style resources, or documented standards. Treat the source of truth as evidence, not assumed truth.
2. Extract repeated values for color, type scale, spacing, radius, borders, shadows, elevation, breakpoints, component heights, icon sizes, and motion. Identify near-duplicates and inconsistent aliases.
3. Compare peer components in the same semantic role: primary versus secondary buttons, text fields, cards, table rows, tabs, alerts, badges, modals, and navigation items. Compare default, hover, focus, active, disabled, loading, and error variants.
4. Detect local overrides that drift from the system, duplicated CSS, inconsistent component APIs, and one-off hardcoded values. Distinguish intentional campaign/brand variation from accidental divergence.
5. Run the token audit for measured evidence:

```bash
node ../../scripts/design_token_audit.mjs --url http://localhost:3000 --out ./audit-out --routes /,/pricing
```

6. Audit visual hierarchy with the squint test: at 25% zoom or blur, is there one unmistakable focal point and one clear primary CTA per viewport? Flag 3+ competing high-saturation primaries.
7. Audit Gestalt proximity: macro spacing between sections must be visibly larger (>= 2x) than micro spacing inside cards or between a heading and its own paragraph.
8. Audit elevation physics: one consistent light source (typically top-down, y > 0); in dark mode replace heavy black shadows with surface luminance steps and 1px top/edge highlights.
9. Audit icon consistency: one stroke weight, one corner-cap style, consistent optical box; never mix thin outline icons with chunky filled icons in the same navigation bar.
10. Recommend or implement token-level corrections when multiple instances share the same defect. Avoid broad token changes from a single component without downstream impact review.
11. Validate across multiple pages and states using representative components; update documentation or stories when the project supports them.

## Precision defaults

- **Body contrast:** >= **4.5:1**; large text >= **3.0:1**; UI component boundaries/icons >= **3.0:1**.
- **Type scale:** <= **3** font families and <= **8** arbitrary sizes without a clear modular scale.
- **Body size:** >= **16px** for reading text, >= **14px** for dense UI; line-height >= **1.35** for paragraphs.
- **Measure:** **45–75ch** for prose; flag > 75ch.
- **Spacing:** snap to a **4px** base grid; 8px rhythm for macro spacing; flag 13/19/27px-style drift.
- **Radius:** `R_inner = max(0, R_outer - padding)`, tolerance **2px**.
- **Shadow:** one light direction; avoid pure-black blur in dark mode.
- **Tokens:** if no system exists, label the inferred token map as a proposal, not official brand tokens.

## Quality gates

- [ ] Tokens are sourced or explicitly labeled inferred.
- [ ] Contrast is measured against the effective background, including images and gradients.
- [ ] Shared defects are fixed at the shared component/token layer where safe.
- [ ] State coverage includes hover/focus/active/disabled/loading/error where applicable.
- [ ] A consistency improvement does not erase deliberate hierarchy, brand expression, or semantic variants.

## Evidence to capture

- Current computed value, violated rule/formula, and exact replacement token.
- Contrast pair (foreground, background, ratio) and the tool/formula used.
- Screenshots in light and dark themes where both exist.
- Token inventory and usage samples; components affected.

## Output

Return the standard finding record, a token inventory with proposed corrections, and a verification note for each token or component changed. If no issue is found, state the themes, components, and states actually checked.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/design-laws-formulas.md`
- `../../references/wcag22-quick-reference.md`
- `../../templates/design-token-inventory.md`
- `../../scripts/design_token_audit.mjs`
