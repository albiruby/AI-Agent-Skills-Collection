---
name: uiux-post-repair-verification-engineer
description: "Verify that UI/UX fixes resolve the reported defect without regressions across screens, states, breakpoints, and platforms. Use when a repair has been implemented and must be proven, when a regression gate is needed, or when a finding's status must be evidence-backed before release."
---

# Post-Repair Verification & Regression Gate

## Use when

- A repair has been implemented and must be proven.
- You need a regression gate across adjacent screens, states, and breakpoints.
- A finding's status must be evidence-backed before release.

## Do not use when

- The fix has not been implemented yet.
- You only need a visual diff; use the visual regression specialist.

## Mission

Close the loop with evidence after every repair.

## Procedure

1. Retrieve the original issue statement, baseline evidence, affected route/screen, state, viewport/device, and expected outcome. If these are missing, reconstruct the narrowest reproducible case and mark it.
2. Run the same reproduction steps and capture after-state evidence under matching conditions. Compare measured geometry and behavior, not only subjective impression.
3. Check neighboring components and pages that share the same CSS, token, or component. Include at least one unaffected control case.
4. Re-run relevant responsive widths, interaction states, keyboard paths, accessibility checks, and visual snapshots according to the defect's blast radius.
5. Verify no new clipping, overflow, wrapping, focus loss, layout shift, console errors, failed assets, or change in intended product behavior.
6. Classify result: verified fixed, partially fixed, not fixed, regression introduced, blocked, or unable to verify. Never mark complete from code inspection alone when the defect is only visible at runtime.
7. If verification fails, return evidence and likely root cause to the implementation specialist rather than repeatedly applying random CSS tweaks.
8. Update the issue ledger with before/after references, tested environments, tests run, and remaining risks.

## Precision defaults

- Recreate the original route, state, viewport, theme, DPR, and data.
- Compare before/after under identical conditions.
- Test adjacent breakpoints, shared components, keyboard paths, and error states.
- Status: Verified fixed / Partially fixed / Not fixed / Regression introduced / Blocked / Unable to verify.

## Quality gates

- [ ] Each repaired finding receives an explicit verification status.
- [ ] Before/after conditions are comparable.
- [ ] Shared-component blast radius is checked.
- [ ] Unverified fixes are never reported as complete.

## Evidence to capture

- Before/after screenshots and measurements.
- Re-run audit/test output.
- Regression blast-radius checklist.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/evidence-schema.md`
- `../../templates/ui-qa-checklist.md`
