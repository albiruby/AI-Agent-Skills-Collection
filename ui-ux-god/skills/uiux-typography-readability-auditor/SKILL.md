---
name: uiux-typography-readability-auditor
description: "Audit type choice, scale, hierarchy, line length, wrapping, line height, weights, and readability across languages and screens. Use when text feels cramped, inconsistent, or hard to read, or when verifying typography before launch."
---

# Typography & Readability Audit

## Use when

- Headings and body text do not form a clear hierarchy.
- Text is cramped, too wide, too small, or wraps awkwardly on mobile.
- You need to verify readability across languages, zoom, or long content.

## Do not use when

- The problem is missing content or a broken asset rather than typography.
- You are only checking color contrast; use the color or WCAG specialist.

## Mission

Make text hierarchy clear, consistent, and robust to real content.

## Procedure

1. Inventory font families, loaded font files, variable axes, fallbacks, weights, sizes, line heights, letter spacing, text transforms, and semantic text styles.
2. Check hierarchy across page title, section heading, subsection, body, labels, helper text, metadata, captions, tables, navigation, and buttons. Verify semantic HTML/native text roles alongside visual styling.
3. Inspect font loading failures, synthetic weights, fallback jumps, missing glyphs, emoji substitution, numeral alignment, and language/script coverage. Do not assume a font file supports every locale.
4. Review line length, paragraph measure, line height, paragraph spacing, heading wraps, orphan/widow lines, truncation, ellipsis, dense tables, and long unbroken strings such as URLs or IDs.
5. Evaluate real content at narrow and wide widths, 200% zoom/text scaling when supported, localization expansion, and user-generated content. Placeholder strings alone are insufficient.
6. Check contrast and hierarchy as a joint system with color and spacing specialists. Do not solve hierarchy exclusively by making every heading larger or heavier.
7. Prefer semantic styles/tokens and responsive typography over per-element overrides. Preserve user font-size preferences and native platform scaling where applicable.
8. After repairs, check line wrapping, clipping, card heights, alignment with adjacent icons, and layout shifts caused by font loading.

## Precision defaults

- Body >= 16px for reading text; dense UI >= 14px.
- Line-height 1.35–1.6 for body; headings can be tighter.
- Measure 45–75ch; flag > 75ch.
- <= 3 font families and <= 8 sizes without a modular scale.
- Use `text-wrap: balance` for headlines and `tabular-nums` for KPIs/prices.

## Quality gates

- [ ] Typography roles map to semantic purpose.
- [ ] Text remains readable with realistic and expanded content.
- [ ] No clipping or overlap after font loading or scaling.
- [ ] Fallback and localization behavior are considered.

## Evidence to capture

- Computed font-family, size, weight, line-height, and measure per text style.
- Screenshots at 320/375/768/1440 and at 200% zoom.
- Long-content and localized-string stress results.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/design-laws-formulas.md`
- `../../references/wcag22-quick-reference.md`
