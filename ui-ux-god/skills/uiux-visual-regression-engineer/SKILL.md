---
name: uiux-visual-regression-engineer
description: "Build and operate visual regression checks with stable screenshots, baselines, masks, thresholds, and reviewable diffs. Use when establishing visual test coverage, investigating snapshot failures, or preventing repair regressions."
---

# Visual Regression Engineering

## Use when

- You need to prevent future visual regressions across routes, states, and viewports.
- A snapshot diff needs triage: intended change, regression, or environmental noise.
- A repair must be protected by a repeatable visual gate.

## Do not use when

- There is no stable rendering environment and the diff would be noise.
- You need functional E2E coverage; use the E2E specialist.

## Mission

Catch unintended appearance changes across pages, states, and viewports.

## Procedure

1. Identify an existing visual test stack before adding tooling. If Playwright or an equivalent is present, follow its configuration; otherwise propose the smallest viable setup.
2. Choose representative routes, component states, viewports, themes, and data fixtures. Cover critical pages and historically fragile components rather than blindly snapshotting every route.
3. Stabilize capture conditions: fonts, animations, caret, timestamps, random values, network data, locale, timezone, DPR, browser version, and viewport. Mask only truly volatile regions.
4. Create baseline screenshots only from an accepted and reviewed product state. Do not update snapshots simply to make a failing test pass.
5. Set thresholds deliberately. Review both pixel diffs and structural context; browser rendering variation can create harmless differences, while small localized changes may still be important.
6. Organize snapshots by platform/browser/viewport/state and define ownership for baseline changes. Keep reference updates in version control.
7. When a diff occurs, isolate the affected region, map it to a component, and determine whether it is intended, a regression, or environmental noise.
8. Run the visual suite after repairs and include the diff result in the release/audit report.

## Precision defaults

- Pin fonts, animations, caret, timestamps, random data, locale, timezone, DPR, browser version.
- Mask only volatile regions; never mask meaningful content.
- Threshold: start strict (0.1–0.2% or per-region), tune with evidence.
- Baselines are created only from an accepted, reviewed state; never auto-update to silence failures.

## Quality gates

- [ ] Baselines are reviewed, not blindly regenerated.
- [ ] Test environment is pinned as much as practical.
- [ ] Masks do not conceal meaningful content or layout.
- [ ] Diffs are triaged with context and not judged only by raw pixel count.

## Evidence to capture

- Baseline/diff paths and capture conditions.
- Threshold and mask rationale.
- Triage: intended / regression / environmental.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/visual-regression-playbook.md`
- `../../templates/viewport-device-matrix.md`
