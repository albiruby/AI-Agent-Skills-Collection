---
name: uiux-responsive-interaction-auditor
description: "Audit responsive behavior, interactive states, touch targets, focus visibility, and practical accessibility on rendered interfaces. Use when checking the 9 mandatory UI states, mobile ergonomics, keyboard focus, hover/pressed/disabled feedback, or responsive interaction bugs."
---

# Responsive, Interaction & Accessibility Audit

## Use when

- A component looks fine at rest but fails on hover, focus, press, disabled, loading, empty, or error.
- Mobile touch targets, keyboard focus, or responsive interaction behavior need verification.
- You need one practical pass across responsiveness, states, and baseline accessibility before deep WCAG work.

## Do not use when

- You need a full WCAG 2.2 conformance audit; use the WCAG specialist.
- The issue is purely static layout geometry with no interaction component.

## Mission

Verify that an interface does not just look good in a static desktop screenshot, but holds up across mobile viewports, keyboard navigation, touch ergonomics, edge-case data states, and baseline accessibility.

## Procedure

1. Build the viewport matrix: **320, 375, 768, 1024, 1440, 1920** (add product-specific sizes). Test portrait and landscape where relevant.
2. For each core component/screen, inspect the **9 mandatory states**: default, hover, focus-visible, active/pressed, disabled, loading/pending, empty, error, and overflow/stress (long names, 3-line titles, 0 items, 999+ badges, slow network).
3. Run the automated interaction/a11y audit:

```bash
node ../../scripts/interactive_a11y_audit.mjs --url http://localhost:3000 --out ./audit-out --routes /,/checkout
```

4. Verify touch targets on mobile: **>= 44x44px** (Apple HIG) / **>= 48x48dp** (Material), with adequate spacing between adjacent targets. WCAG 2.2 SC 2.5.8 sets a **24x24px** minimum; treat that as a floor, not a goal.
5. Verify keyboard focus: Tab/Shift+Tab order, visible focus ring (>= 2px, >= 3:1 contrast), no focus lost behind sticky bars/overlays, Escape closes dialogs, focus returns to the trigger.
6. Verify focus traps in drawers/modals; arrow-key behavior in menus, tabs, comboboxes, and listboxes; skip links; disabled-state semantics.
7. Verify responsive integrity: no horizontal scroll at 320px; tables scroll inside their own wrapper; sticky headers do not cover anchor targets (`scroll-margin-top`); mobile nav closes on Escape.
8. Verify media: broken images (`naturalWidth === 0`), distorted aspect ratio, missing `alt`, icon-only buttons without accessible names, inputs without labels, skipped heading levels.
9. Verify text stress: long localized strings (+30%), 200% zoom, 400% reflow, and increased text spacing.
10. Re-test every repaired state at the failing viewport and at least one neighboring breakpoint.

## Precision defaults

- **Touch:** 44/48px recommended; 24px WCAG floor; spacing between targets >= 8px.
- **Focus:** visible ring >= 2px, contrast >= 3:1 against adjacent colors.
- **Reflow:** usable at 320px / 400% zoom; no two-dimensional scrolling except data tables.
- **Text spacing:** line-height >= 1.5x, paragraph spacing >= 2x font size, letter/word spacing adjustable without clipping.
- **States:** if a state is missing, record it as a state gap, not just a visual nit.
- **Motion:** honor `prefers-reduced-motion`; no essential information only in animation.

## Quality gates

- [ ] Every core component has all 9 states or an explicit "not applicable" note.
- [ ] Touch and keyboard operation are tested, not assumed.
- [ ] Focus is visible, logical, and restored after overlays.
- [ ] Responsive checks include 320px and one intermediate width, not just mobile/desktop.
- [ ] Automated findings are verified manually before being reported as failures.

## Evidence to capture

- State matrix per component: state, viewport, result, evidence.
- Touch target dimensions and spacing.
- Focus-ring screenshot and computed outline/box-shadow.
- Keyboard path and focus order.
- Responsive screenshots at the failing width and neighbor.

## Output

Return the standard finding record, a state-coverage matrix, and a verification note for each repaired state. State which states/viewports were not tested.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/state-and-ux-heuristics.md`
- `../../references/wcag22-quick-reference.md`
- `../../scripts/interactive_a11y_audit.mjs`
- `../../templates/ui-qa-checklist.md`
