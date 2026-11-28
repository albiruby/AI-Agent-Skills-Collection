---
name: uiux-audit-governance-risk-triage
description: "Triage UI/UX findings, set audit scope, manage change risk, protect brand intent, and decide when to fix, defer, or request clarification. Use when findings compete for priority, when a repair is risky or ambiguous, or when audit scope and authorization need explicit decisions."
---

# Audit Governance, Risk & Prioritization

## Use when

- Findings compete for a limited repair budget.
- A fix is ambiguous, brand-sensitive, or high blast-radius.
- Audit scope, authorization, or acceptance criteria need to be explicit.

## Do not use when

- There is a single obvious low-risk fix; just do it within authorization.
- The user has already provided a complete, prioritized backlog.

## Mission

Prevent noisy audits and risky redesigns disguised as polish.

## Procedure

1. Confirm requested mode: Audit Only, Audit + Safe Repairs, Full Repair Authorization, Reference Match, or Regression Check. Do not assume permission for broad redesign from a request to review.
2. Define in-scope surfaces, routes/screens, roles, environments, design references, target accessibility level, supported platforms, and known product constraints. State unknowns rather than inventing them.
3. Classify each finding by confidence and risk. High-confidence, low-risk defects (obvious overflow, broken alignment against a clear rule, wrong asset variant) can be repaired in authorized repair mode; uncertain brand or product decisions should be proposed.
4. Assess blast radius: shared token, global CSS, component library, route-local style, state logic, native platform control, or content. Require broader checks for global/shared changes.
5. Protect business-critical content, legal copy, brand assets, analytics instrumentation, security controls, and user data. Never remove consent, warnings, security steps, or accessibility features to improve aesthetics.
6. Avoid cosmetic churn when the current design is intentional, consistent, or constrained by platform behavior. Explain tradeoffs where design preferences conflict.
7. Prioritize fixes by impact, frequency, critical task, user group, recurrence, confidence, and effort. Distinguish must-fix defects from subjective enhancement ideas.
8. Maintain a change ledger: issue ID, decision, owner/specialist, files or screens touched, tests required, approval needs, and rollback consideration.

## Precision defaults

- Priority = impact × reach × confidence / effort, adjusted for release timing and dependencies.
- Classify fix / defer / clarify / reject; record the reason.
- Protect brand intent: distinguish intentional asymmetry from accidental drift.
- High-risk changes need explicit approval and a rollback plan.

## Quality gates

- [ ] Audit and repair permissions are explicit.
- [ ] High-risk or ambiguous product decisions are not silently changed.
- [ ] Shared/global changes receive expanded regression scope.
- [ ] Severity and priority are not conflated with visual preference.

## Evidence to capture

- Scope and authorization record.
- Impact/reach/confidence/effort rationale.
- Decision log with owner and follow-up.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../templates/repair-plan-template.md`
- `../../references/severity-and-priority.md`
