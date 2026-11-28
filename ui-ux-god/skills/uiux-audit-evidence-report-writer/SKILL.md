---
name: uiux-audit-evidence-report-writer
description: "Produce actionable UI/UX audit reports with evidence, measurements, severity, reproduction steps, recommendations, and repair status. Use when findings must be documented for engineers, stakeholders, or a release gate, or when audit coverage and limitations need a clear record."
---

# Audit Evidence & Reporting

## Use when

- Findings must be handed to engineers or stakeholders.
- A release gate needs a clear, evidence-backed report.
- You must document coverage, limitations, and repair status.

## Do not use when

- You only need an informal chat summary with no artifact.
- The findings are still unverified hypotheses; label them or gather evidence first.

## Mission

Turn observations into traceable engineering work.

## Procedure

1. Use a finding schema: ID, title, category, page/screen, state, viewport/device, severity, frequency/scope, user impact, evidence reference, reproduction steps, suspected cause, recommendation, confidence, and status.
2. Separate observed fact, inferred cause, and proposed fix. Label uncertainty. Do not write speculative causes as confirmed facts.
3. Attach screenshots/crops, DOM selector or native element identifier, bounding box, computed values, accessibility node, console trace, or test output as available. Never fabricate evidence references.
4. Use consistent severity: Critical (blocks core task or creates severe accessibility/security/safety issue), High (major task or broad UI defect), Medium (meaningful friction or localized defect), Low (minor polish), Informational (observation or improvement opportunity). Explain severity in context.
5. Prioritize by impact, reach, task criticality, recurrence, and remediation effort. Avoid false precision in scores; use explicit rationale.
6. Provide an executive summary, coverage statement, top risks, categorized findings, recommended repair sequence, and verification status. Include pages/states not tested.
7. Write each issue so an engineer can reproduce it without asking what 'looks off' means. Include coordinates/dimensions when visual geometry matters.
8. Do not claim WCAG conformance, device coverage, completion, or performance improvements unless the evidence supports the claim.

## Precision defaults

- Every finding: ID, category, severity, route/screen, state, viewport/device, evidence, impact, repro, cause, fix, confidence, status.
- Separate observed fact, inferred cause, and proposed fix.
- Include coverage: inspected, partial, blocked, not in scope.
- Use consistent severity and explain it in context.

## Quality gates

- [ ] Every actionable finding is reproducible.
- [ ] Evidence references are real and accessible.
- [ ] Facts, hypotheses, and fixes are distinct.
- [ ] Coverage limitations and untested areas are explicit.

## Evidence to capture

- Screenshot/crop paths, selectors/bounds, computed values, accessibility nodes, logs, test output.
- Reproduction steps that an engineer can follow.
- Verification status and residual risk.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../templates/audit-report-template.md`
- `../../templates/issue-evidence-template.md`
- `../../references/evidence-schema.md`
