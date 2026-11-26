# Intake and Scope Contract

Use for audits that are production-facing, multi-tenant, payment-related, regulated, or likely to expand. For small read-only requests, a short assumption list in the report may be enough.

## 1. Request summary

- Requester and date:
- Target (repository, site, feature, artifact):
- Environment(s): local / test / staging / preview / production
- Requested mode: Deep / Focused / Blind-Spot Hunt / Re-audit
- Decision or outcome this audit supports:

## 2. Objective and success criteria

- Primary question:
- What must be true for this audit to be useful?
- What would be out of scope even if discovered?

## 3. Targets and versions

| Target | Type | Environment | Version/commit | Notes |
|---|---|---|---|---|
| | | | | |

## 4. Authorization matrix

| Action class | Allowed | Limits / conditions |
|---|---|---|
| Read repository, docs, configuration | | |
| Run existing tests/lint/type-check | | |
| Run local build | | |
| Dependency/static analysis | | |
| Browser inspection | | |
| Use test accounts / synthetic data | | |
| Read-only database queries | | |
| Read logs/metrics/analytics | | |
| Send test emails/webhooks/payments | | |
| Modify code/data/config/dependencies | | |
| Load/fuzz/state-changing tests | | |
| Test production/third-party systems | | |

Default when not explicitly allowed: **read-only, non-destructive, no production mutation**.

## 5. Data handling

- Personal/confidential data involved:
- Test data: synthetic / anonymized / production (justify)
- Redaction rules:
- Evidence storage location and retention:
- External tools/model providers allowed:
- Secret handling: never print values; report location and exposure risk.

## 6. Constraints

- Time box and checkpoints:
- Maintenance window / freeze:
- Known incidents or fragile areas:
- Tooling limitations:
- Legal/contractual boundaries:

## 7. Deliverables

- [ ] Executive summary
- [ ] Full report
- [ ] Coverage matrix and score
- [ ] Findings JSON (`findings.schema.json`)
- [ ] Remediation plan
- [ ] Re-audit/verification
- Recipients and distribution limits:

## 8. Stop conditions and escalation

Stop and notify when:

- A test could affect real users, money, production data, or third parties.
- An active incident, data exposure, or ongoing loss is suspected.
- Scope or authorization becomes ambiguous.
- A critical finding requires immediate action.

- Escalation contact/channel:
- Restricted-reporting needs:

## 9. Assumptions and sign-off

- Assumptions made to avoid blocking:
- Items still unknown:
- Requester approval (name/date):
- Auditor acknowledgment:
