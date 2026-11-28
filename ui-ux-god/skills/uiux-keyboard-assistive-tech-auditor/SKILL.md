---
name: uiux-keyboard-assistive-tech-auditor
description: "Test keyboard-only operation, focus order, screen-reader semantics, accessible names, announcements, and assistive-technology interaction. Use when verifying tab order, focus traps, custom widgets, ARIA, or screen-reader behavior."
---

# Keyboard & Assistive Technology Audit

## Use when

- A core task must be possible without a pointer.
- Focus order, focus traps, ARIA names, or live announcements are suspect.
- You need to verify custom widgets against authoring-practice patterns.

## Do not use when

- You need a full WCAG conformance audit; use the WCAG specialist and treat this as AT deep-dive.
- No keyboard or assistive technology is available and the claim would be speculative.

## Mission

Verify that non-pointer users can perceive and operate the product.

## Procedure

1. Navigate the entire critical flow using keyboard only. Check Tab/Shift+Tab, Enter, Space, Escape, arrow keys, shortcuts, and expected widget-specific patterns.
2. Inspect focus visibility, focus order, focus trapping, focus restoration, skip links, hidden content, disabled states, and whether focus is obscured by sticky bars or overlays.
3. Inspect semantic role, accessible name, value, state, description, group relationship, heading/landmark structure, and announcement of dynamic status changes.
4. Test dialogs, menus, tabs, comboboxes, autocomplete, tree views, listboxes, accordions, drag/drop alternatives, and custom widgets against appropriate authoring patterns.
5. Where available, test with screen readers and platform combinations relevant to the product (for example browser/screen-reader pairs or native platform readers). Record actual announcements, not assumed behavior.
6. Check live regions and validation announcements for useful timing and non-duplication. Avoid over-announcing large regions or making hidden updates inaccessible.
7. Use native semantic elements and platform controls where possible. Add ARIA only to fill a real semantic gap and implement the required keyboard behavior along with it.
8. Document tool and AT combinations tested, plus limitations. A single screen-reader pass is not proof of universal compatibility.

## Precision defaults

- Tab/Shift+Tab, Enter, Space, Escape, and arrow keys tested per widget.
- Focus visible: >= 2px ring, >= 3:1 contrast; focus restored after overlays.
- Accessible name, role, value, state, and description must match visible function.
- Do not add ARIA without the required keyboard behavior.

## Quality gates

- [ ] Core tasks are possible without pointer input.
- [ ] Focus is visible, logical, and not lost behind overlays.
- [ ] Accessible names and states match visible function.
- [ ] AT behavior is described only for configurations actually tested.

## Evidence to capture

- Keyboard path and focus-order list.
- Accessibility tree/snapshot and screen-reader announcements.
- AT/browser/OS versions actually tested.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/wcag22-quick-reference.md`
- `../../references/state-and-ux-heuristics.md`
