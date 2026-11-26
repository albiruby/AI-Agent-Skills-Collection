# Re-audit and Verification Report

Use when checking whether prior findings were fixed and whether the fix introduced new risk.

## 1. Baseline

- Prior report/version/date:
- Prior scope and environment:
- Findings included in this re-audit:
- Current target/version/commit:
- Current environment:
- Authorization and limitations:

## 2. Status summary

| Status | Count |
|---|---:|
| Fixed | |
| Partially fixed | |
| Regressed | |
| Unchanged | |
| Not reproducible | |
| Unverifiable | |
| New findings | |

## 3. Item-by-item verification

### [ID] — Original title

- Original severity/confidence:
- Original evidence:
- Claimed fix/change:
- Verification performed:
- Result: Fixed / Partially fixed / Regressed / Unchanged / Not reproducible / Unverifiable
- Evidence:
- Acceptance criteria met? Yes / Partially / No
- Residual risk:
- Follow-up required:

Repeat per finding. Do not mark fixed because code changed; mark fixed because the failure mode no longer reproduces or the change conclusively removes it.

## 4. Regression and blast-radius check

| Area affected by fix | Check performed | Result | Notes |
|---|---|---|---|
| | | | |

Include adjacent flows, data migration, cache/version skew, error handling, analytics, and permissions where relevant.

## 5. New findings

New issues discovered during verification, separated from prior findings:

- [NEW-ID] — class, severity, confidence, evidence, recommendation.

## 6. Coverage and limitations

- What was re-tested vs inspected statically:
- What could not be verified:
- Environment differences from the original audit:
- Assurance statement (bounded):

## 7. Closure recommendation

- Prior risk status: Closed / Partially closed / Open
- Conditions for full closure:
- Re-audit required? Yes / No, because:
- Report distribution/restrictions:
