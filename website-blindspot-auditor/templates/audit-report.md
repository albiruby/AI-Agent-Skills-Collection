# Website Blind-Spot Audit Report

Machine-readable companion: `templates/findings.schema.json`. One-page decision summary: `templates/exec-summary.md`. Evidence index: `templates/evidence-log.md`.

## 1. Executive summary

- Overall assessment:
- Highest-priority verified findings:
- Highest-priority potential risks:
- Most important coverage gaps:
- Best improvement opportunities:
- Recommended decision / launch posture:

## 2. Scope and method

- Target and environment:
- Audit mode:
- Authorized scope:
- Methods actually used:
- Important exclusions:
- Time box and checkpoints:

## 3. Detected project context

- Product profile(s):
- Technology and architecture:
- Capabilities:
- Critical user journeys:
- Adapters/profiles used and why:
- Assumptions / confidence:

## 4. Prioritized findings

### [ID] Finding title

- Classification: Verified Finding / Potential Risk / Coverage Gap / Improvement Opportunity
- Status: Open / In progress / Fixed / Partially fixed / Regressed / Unchanged / Not reproducible / Unverifiable
- Domain:
- Severity:
- Confidence:
- Location/component:
- Evidence (link to evidence log; redact secrets):
- Expected behavior:
- Actual behavior or observed condition:
- Impact and realistic scenario:
- Reproduction / verification steps:
- Recommendation:
- Acceptance criteria:
- Dependencies:
- Regression / second-order considerations:
- Remaining uncertainty:
- Related findings:

Repeat per finding. Lead with the most consequential verified findings.

## 5. Blind-spot discoveries

Describe non-obvious assumptions, interaction failures, unusual scenarios, and second-order effects. Separate verified facts from hypotheses. Include hypotheses that were tested and rejected when they explain the system's boundaries.

## 6. Improvement opportunities

| Opportunity | Evidence / rationale | Expected benefit | Effort | Confidence | Dependencies |
|---|---|---|---|---|---|
| | | | | | |

## 7. Coverage and limitations

Attach or summarize the coverage matrix. State what was inspected, executed, verified, inferred, inaccessible, and not tested. Include the coverage score and dimension scores from `templates/coverage-matrix.md`.

## 8. Recommended remediation sequence

| Order | Finding / task | Reason | Dependencies | Validation after fix |
|---|---|---|---|---|
| | | | | |

For execution-ready planning, use `templates/remediation-plan.md`.

## 9. Re-audit status (if applicable)

| Prior ID | Status | Evidence | Residual risk |
|---|---|---|---|
| | | | |

If this is a re-audit, use `templates/re-audit.md` as the primary report and attach this report's updated findings.

## 10. Closing statement

State the bounded conclusion. Do not imply the site is fully secure, bug-free, compliant, or production-ready unless a suitable independent basis exists — and even then state the scope. Mention the most important thing this audit did not cover.
