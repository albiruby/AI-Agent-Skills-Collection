# Coverage, Scoring, and Definition of Done

An audit is a bounded sample of a system. Coverage is part of the result: it tells the reader how much assurance the findings actually provide.

## 1. Coverage dimensions

Assess coverage separately from finding quality:

| Dimension | Question |
|---|---|
| Scope coverage | Which targets, routes, services, environments, and data were in scope? |
| Domain coverage | Which audit domains were Applicable, Not Applicable, or Unknown — and why? |
| Journey coverage | Which critical user journeys were traced end-to-end? |
| Layer coverage | Which layers were inspected: UI, transport, auth, business logic, persistence, async work, cache/search, operations? |
| Evidence depth | Was each important claim inspected, executed, reproduced, or only inferred? |
| Risk coverage | Were the highest-impact areas investigated before lower-risk breadth? |
| Execution coverage | Which checks actually ran, and which were blocked by access or safety? |
| Limitation disclosure | Are inaccessible, untested, and uncertain areas explicit? |

## 2. Item status vocabulary

Use one status per row in the coverage ledger:

- **Not assessed:** no decision or inspection yet.
- **Not applicable:** evidence shows the domain is outside the project's actual scope.
- **Inspected:** relevant files/configuration/behavior were examined.
- **Executed:** a check or test actually ran.
- **Verified:** a specific claim was confirmed with sufficient evidence.
- **Blocked:** access, authorization, environment, or safety prevented work.
- **Unknown:** insufficient evidence to decide applicability or result.

Do not use "Passed" as a substitute for saying what was tested and how.

## 3. Scoring model (0–2 per dimension)

Use scores to summarize, not to replace narrative. Keep the evidence behind each score.

- **0 — Absent:** not done, not possible, or no meaningful evidence.
- **1 — Partial:** relevant work done, but a material gap, limitation, or unverified assumption remains.
- **2 — Strong:** appropriate work done for the stated scope, with evidence and disclosed limits.

Score these dimensions:

1. Context reconstruction.
2. Domain selection and applicability reasoning.
3. Critical journey tracing.
4. Cross-layer analysis.
5. Security, privacy, and trust-boundary coverage.
6. Money, identity, content, and irreversibility coverage (when applicable).
7. Failure, retry, concurrency, and recovery coverage.
8. Execution and verification depth.
9. Evidence quality and reproducibility.
10. Coverage transparency.

If a dimension does not apply, mark it N/A rather than scoring it 0. Do not average scores into a precision-looking percentage unless the consumer explicitly wants an aggregate and understands its limits.

## 4. Coverage ledger

Use `templates/coverage-matrix.md` and add rows for:

- Each critical journey.
- Each major integration or async boundary.
- Each high-risk domain sub-area (for example, tenant isolation, webhook replay, refunds, cache invalidation).
- Each environment or runtime that could not be inspected.

Every row should state the method, result, evidence, and limitation. "Inspected" with no method is not coverage.

## 5. Unknown budget

Unknown is not failure by itself; unexplained Unknown is.

At the start of a Deep Audit, decide a practical budget for unresolved unknowns, for example:

- Critical/high-risk area: resolve or explicitly block; do not leave silent.
- Medium-risk area: at most a small number of material unknowns, each with a next step.
- Low-risk area: unknowns acceptable if disclosed.

If the budget is exceeded, either narrow the assurance claim or ask for the access/time needed to close the gaps.

## 6. Minimum coverage by mode

### Deep Audit

- Scope and authorization recorded.
- All domains classified; Unknown reasons recorded.
- All critical journeys traced to available depth.
- Security/privacy and money/identity/irreversibility paths assessed when present.
- Failure/retry/concurrency/recovery considered for critical flows.
- Coverage matrix completed; limitations explicit.

### Focused Audit

- Target mapped in the real system.
- Every actor who can reach the target considered.
- Failure, duplicate, retry, and partial-success paths considered.
- Adjacent dependencies identified; inspected vs skipped disclosed.
- Findings scoped to the target or explicitly flagged as broader.

### Blind-Spot Hunt

- At least three method families used.
- Hypothesis backlog with status for each item.
- At least two cross-boundary or end-to-end traces.
- Rejected hypotheses documented where useful.
- No claim of exhaustive coverage.

### Re-audit

- Every prior finding has a status and evidence.
- Fixes checked against acceptance criteria.
- Immediate adjacent flows checked for regression.
- New findings separated from prior findings.
- Residual risk stated.

## 7. Definition of done checklist

Use this before delivering:

- [ ] Target, environment, and authorization are explicit.
- [ ] Mode and success criteria are stated.
- [ ] Context model includes actors, journeys, invariants, and trust boundaries.
- [ ] Domain applicability is recorded with reasons.
- [ ] Adapters used are named; unsupported technology is disclosed.
- [ ] Every critical journey has a trace or a stated limitation.
- [ ] Findings are classified, deduplicated, and evidence-linked.
- [ ] Severity and confidence are separated.
- [ ] Each actionable finding has a verification method and a recommendation.
- [ ] Coverage matrix and score are complete.
- [ ] Limitations and unknowns are explicit.
- [ ] The conclusion does not exceed the evidence.

## 8. Re-audit closure criteria

A prior item can be marked **fixed** only when:

- The original failure mode no longer reproduces, or the implementation change conclusively removes it.
- The fix was verified in the environment where the risk exists (or the limitation is stated).
- Adjacent flows were checked for regressions.
- The evidence is linked.

Otherwise use **partially fixed**, **unchanged**, **regressed**, **not reproducible**, or **unverifiable**. Do not mark an item fixed because code changed, a ticket closed, or a test was added without checking what it actually proves.

## 9. Reporting language

Prefer:

- "Within the inspected scope, no evidence of X was found."
- "Y was not verifiable because Z access was unavailable."
- "This finding is confirmed by a reproduced behavior in the staging environment."
- "This remains a hypothesis; the next verification step is W."
- "Coverage was strong for journeys A and B; the admin bulk-export path was not inspected."

Avoid:

- "The site is secure."
- "No bugs found."
- "Fully compliant."
- "100% coverage."
- "All critical paths tested" without naming them.
