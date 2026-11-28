---
name: uiux-user-flow-usability-auditor
description: "Evaluate end-to-end task flows for usability, friction, cognitive load, error recovery, and completion clarity. Use when a signup, checkout, onboarding, or core workflow feels slow, confusing, or hard to recover from."
---

# Task Flow & Usability Audit

## Use when

- A core task takes too many steps or loses users mid-flow.
- Error recovery, back behavior, progress, or completion feedback is unclear.
- You need to verify a workflow end to end, not just individual screens.

## Do not use when

- The task is a single static screen with no flow.
- You need statistical usability research; this is an expert review.

## Mission

Judge the experience by whether users can complete real goals.

## Procedure

1. Define personas or user contexts only when supported by product evidence. Otherwise state the assumed user and task; do not invent research findings.
2. Choose critical tasks such as sign-up, onboarding, search, purchase, upload, create/edit, settings, invite, export, or recovery. Include first-time and returning-user paths.
3. Walk each flow from entry point to successful completion. Record steps, decisions, required data, waiting, navigation changes, interruptions, error points, and user-visible confirmation.
4. Evaluate effort and cognitive load: unnecessary steps, repeated entry, hidden prerequisites, unclear options, poor defaults, context switching, ambiguous controls, and memory burden.
5. Test failure paths: invalid data, network loss, session expiry, denied permissions, cancellation, duplicate action, and recovery. Confirm users can understand and continue without losing work.
6. Check progress communication, reversibility, destructive-action safeguards, confirmation language, and post-completion next steps.
7. Prioritize findings by task criticality, frequency, impact, and recoverability. Avoid claiming measured conversion improvement without analytics or user research.
8. Propose flow-level fixes and verify the complete task again after implementation, not just the changed screen.

## Precision defaults

- Count steps and decisions per task; flag unnecessary branches.
- Every destructive action needs confirmation or undo.
- Progress must be visible for multi-step flows.
- Error states must explain what happened and how to recover.

## Quality gates

- [ ] Critical tasks are documented with start, success, and failure conditions.
- [ ] No unsupported claims about user behavior or conversion.
- [ ] Error recovery and cancellation are tested.
- [ ] Post-repair task completion is verified end to end.

## Evidence to capture

- Flow diagram with steps/screens.
- Step count, time-on-task proxies, and friction points.
- Error/empty/loading states encountered.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/state-and-ux-heuristics.md`
- `../../templates/ui-qa-checklist.md`
