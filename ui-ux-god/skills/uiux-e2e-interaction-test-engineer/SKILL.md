---
name: uiux-e2e-interaction-test-engineer
description: "Design and execute end-to-end tests for critical UI tasks, state transitions, navigation, forms, and failure recovery. Use when a flow needs repeatable browser or device verification, or when a repair must be proven end to end."
---

# End-to-End Interaction Test Engineering

## Use when

- A critical task needs repeatable browser/device verification.
- A repair touches navigation, forms, state transitions, or failure recovery.
- You need artifacts and assertions that prove the user journey works.

## Do not use when

- A unit/component test is sufficient and faster.
- The flow cannot be automated reliably; use a documented manual protocol.

## Mission

Prove that the product works through realistic user journeys after visual repair.

## Procedure

1. Select critical journeys from product behavior: onboarding, login, search, create/edit, upload, checkout, settings, invite, export, and recovery as relevant.
2. Define preconditions, test data, user role, viewport, start state, expected transitions, final state, and cleanup. Do not rely on hidden prior state.
3. Prefer accessible role/name locators and stable test IDs over brittle DOM paths or coordinate-only clicks. Re-discover elements after navigation or major state changes.
4. Assert user-visible outcomes: route, title, content, state, accessible feedback, enabled/disabled status, persistence, and error handling.
5. Cover success and failure paths, slow network, invalid input, expired session, permission denial, cancellation, retry, duplicate submission, and keyboard navigation where applicable.
6. Keep tests deterministic. Mock only external dependencies that are not the subject of the test; do not mock away the behavior being audited.
7. Capture trace, screenshot, logs, and failed assertion context. Avoid hiding flaky tests by increasing timeouts without diagnosing the cause.
8. Run the journey after repair from a clean state and record exact test command/environment and result.

## Precision defaults

- Cover critical paths first: auth, search, checkout, submit, recover.
- Use deterministic fixtures; isolate test data; clean up.
- Assert user-visible outcomes, not implementation details.
- Capture trace, screenshot, and console/network on failure.

## Quality gates

- [ ] Tests assert observable task outcome, not implementation details only.
- [ ] Critical error/recovery paths are included.
- [ ] Flakiness is investigated rather than masked by timeouts.
- [ ] Test data and environment are repeatable.

## Evidence to capture

- Test list with preconditions and expected outcomes.
- Run output, trace, and artifacts.
- Known flakiness and retry policy.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/visual-regression-playbook.md`
- `../../references/state-and-ux-heuristics.md`
