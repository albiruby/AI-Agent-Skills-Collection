---
name: uiux-surgical-repair-engineer
description: "Implement verified UI repairs at the correct level and prove them with closed-loop re-render and re-measure. Use when an audit has produced verified findings and the user authorizes repair, when a fix must preserve behavior and design-system consistency, or when you need before/after evidence and a regression gate."
---

# Surgical UI Repair & Closed-Loop Verification

## Use when

- An audit has produced verified findings and the user authorizes repair.
- The fix must preserve behavior, semantics, accessibility, and design-system consistency.
- You need before/after evidence and a regression gate, not just a code edit.

## Do not use when

- The user asked for audit only; report and propose fixes without editing.
- The finding is still an unverified hypothesis; gather evidence first.

## Mission

Turn verified audit findings into clean, maintainable, production-grade fixes and prove every fix with re-render, re-measure, and regression checks.

## Engineering philosophy

- No `!important` hacks, magic pixel nudges, or fragile absolute positioning to hide a broken parent layout.
- Fix the root cause at the correct layer: asset, token, parent layout, shared component, semantic markup, state logic, or platform constraint.
- Respect the project's existing styling system (Tailwind, CSS Modules, styled-components, SwiftUI, Flutter, Qt, etc.) and design tokens.
- Keep the change atomic. Do not rewrite unrelated business logic, rename props gratuitously, or break existing tests.

## Procedure

1. **Group findings by root cause and prioritize.** Sort P0 → P1 → P2 → P3. Cluster defects that share one structural parent so one clean architecture fix replaces several conflicting micro-patches.
2. **Read the target component and its context.** Inspect the component, parent layout, stylesheet, theme/tokens, and meaningful call sites before editing its API, props, state, styling, or markup.
3. **Classify repair scope.** Local style, shared component, token, interaction logic, semantic markup, asset, or layout architecture. Estimate blast radius before editing.
4. **Choose the smallest robust correction.** Prefer a shared component/token fix for repeated defects. Avoid widening a one-off fix if reuse is not real. Do not add a dependency for a small repair.
5. **Apply the canonical pattern.** Use `../../references/surgical-fix-patterns.md`:
   - True centering: CSS Grid `1fr auto 1fr` (or symmetric side slots), not padding nudges.
   - Divider: decide full-bleed vs content-aligned; use `w-full self-stretch` or negative margin matching parent padding.
   - Concentric radius: `R_inner = max(0, R_outer - padding)`.
   - Overflow: fix the offending child; use `overflow-x: clip` for decorative wrappers, not `hidden` on `body` (it breaks sticky).
   - Dark mode: semantic tokens for text/border/surface, not hardcoded light values.
6. **Preserve behavior and semantics.** Keep accessible names, keyboard behavior, focus management, loading/error states, responsive variants, and public component contracts.
7. **Re-render and re-measure.** Rebuild/hot-reload; confirm zero build/type/console errors. Re-run the exact audit script(s) that flagged the defect. Re-capture the affected viewports and compare before/after.
8. **Regression check.** Test adjacent breakpoints, shared component instances, relevant states, keyboard paths, and key flows. If a patch regresses another view, revert and apply a cleaner structural fix.
9. **Cap the loop.** Maximum 2 verification rounds per cluster; if blocked by a design/brand trade-off, mark `PARTIAL_NEEDS_DESIGN_DECISION` and present options.
10. **Record the change ledger.** Files/components/screens touched, rationale, side effects considered, tests run, and rollback-sensitive changes.

## Precision defaults

- Centering tolerance 1.5px; divider asymmetry 2px; radius tolerance 2px.
- Contrast: 4.5:1 body, 3:1 large text/UI; verify both themes.
- Spacing: 4/8px grid; no arbitrary 13/19/27px values.
- Touch: 44/48px; focus ring >= 2px and >= 3:1.
- Re-test at 320px and one neighboring breakpoint for every responsive fix.
- Never declare fixed without comparable before/after evidence.

## Quality gates

- [ ] The causal property/layer is identified and verified before the final edit.
- [ ] No unnecessary `!important`, magic numbers, or cascade debt.
- [ ] Component API changes are assessed for all consumers.
- [ ] Semantics, keyboard, focus, states, and responsive behavior survive.
- [ ] Formatting, type checks, lint, and relevant tests are run or explicitly reported as unavailable.
- [ ] Before/after evidence exists for every claimed fix.

## Evidence to capture

- Finding ID and the exact file/component changed.
- Before/after screenshots at the same route, state, viewport, theme, and DPR.
- Re-run audit output and test results.
- Blast radius and regression checks.

## Output

A change summary with files, rationale, before/after evidence, verification results, residual risks, and rollback notes. Status per finding: Verified fixed / Partially fixed / Not fixed / Regression introduced / Blocked / Unable to verify.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/surgical-fix-patterns.md`
- `../../references/micro-defect-catalog.md`
- `../../templates/repair-plan-template.md`
- `../../templates/implementation-handoff-template.md`
