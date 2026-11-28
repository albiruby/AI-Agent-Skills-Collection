---
name: uiux-responsive-layout-auditor
description: "Audit responsive and adaptive layouts across viewports, orientation, zoom, text scaling, and input modes. Use when checking breakpoint failures, mobile overflow, cramped tablets, ultra-wide containment, or when a layout works on desktop but breaks on smaller screens."
---

# Responsive & Adaptive Layout Audit

## Use when

- A layout works at 1440px but breaks, overflows, or collapses at 320–768px.
- You need to verify breakpoint transitions, orientation changes, zoom, or text scaling.
- A repair must be proven safe across the responsive matrix.

## Do not use when

- The issue is a single fixed-width component with no responsive behavior.
- You only need a native app check; use the mobile or desktop specialist.

## Mission

Verify that layout rules adapt, not merely shrink.

## Procedure

1. Build a viewport matrix from project breakpoints and real device classes. At minimum inspect narrow phone, common phone, large phone, tablet, laptop, desktop, and wide desktop; include portrait/landscape where relevant.
2. Check content reflow, navigation transformation, grid collapse, card stacking, column order, image crop, typography scaling, control sizing, sticky elements, fixed bars, modals, tables, and charts.
3. Test at intermediate widths around breakpoints, not only named device presets. Look for breakpoint gaps, abrupt jumps, awkward wrapping, oversized whitespace, and layouts that fail between tested endpoints.
4. Inspect horizontal overflow at document and component level. Find the actual overflowing element and cause; distinguish intentional horizontal carousels/data tables from accidental page overflow.
5. Test browser zoom and text enlargement where available, plus safe areas/notches and on-screen keyboard behavior for mobile. Check that dialogs and forms remain reachable when the keyboard is open.
6. Evaluate touch target size/spacing, hover-only interactions, pointer precision assumptions, scroll traps, sticky header height, and bottom navigation interference.
7. Repair with fluid constraints, grid/flex changes, container queries, sensible breakpoints, intrinsic sizing, wrapping, and content prioritization. Avoid device-specific hacks unless the platform requires them.
8. Retest viewport boundaries and nearby sizes after each structural fix. Record all tested viewport dimensions and any intentionally unsupported range.

## Precision defaults

- Minimum width: 320px; also test 375, 768, 1024, 1440, 1920.
- Reflow: content must remain usable at 400% zoom / 320px equivalent (WCAG 1.4.10).
- No horizontal scroll at 320px unless the content is intentionally a data table with its own scroller.
- Touch targets >= 44x44px (iOS) / 48x48dp (Android) where relevant.

## Quality gates

- [ ] No accidental horizontal page overflow at supported widths.
- [ ] Content order and task completion remain coherent after reflow.
- [ ] Fixed/sticky elements do not obscure content or keyboard focus.
- [ ] Intermediate breakpoint widths are included in verification.

## Evidence to capture

- Viewport matrix with pass/fail per breakpoint.
- Overflow offenders and their computed widths.
- Before/after screenshots at the failing and neighboring widths.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/platform-capture-matrix.md`
- `../../templates/viewport-device-matrix.md`
- `../../references/design-laws-formulas.md`
