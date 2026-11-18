# Severity, Factors & Finding Status

Source: domain 91.

## Severity
| Severity | Definition | Examples |
|---|---|---|
| Critical | Very high risk; likely compromise or serious failure | Exposed production secret, remote code execution, public write token, open production dataset with private data |
| High | Must be fixed before launch | Broken access control, exploitable XSS, missing auth on an admin route, no way to roll back, domain without registrar MFA |
| Medium | Real risk, more limited impact | Missing security header, weak error handling, no uptime monitoring, unbounded form submissions |
| Low | Minor issue or quality improvement | Minor accessibility issue, redundant dependency, inconsistent naming |
| Informational | Observation or recommendation | Documentation could be better, optional hardening |

## Factors to weigh (record the ones that decided the rating)
Likelihood · Impact · Exploitability · Exposure · Business impact · User impact · Data sensitivity · Operational impact · Remediation complexity · Regression risk · **Launch dependency** (does it block launch?).

Calibration tips:
- Severity = impact × likelihood in *this* project's context. A missing CSP on a static brochure site is Medium at most; on an app with user content it can be High.
- Exposure matters: a bug on an unauthenticated public route outranks the same bug behind admin login.
- Cap severity for **Suspected** findings at what you can justify; state the confirming step.
- Do not inflate: ten Low findings are not a High.
- A launch blocker is any Critical, any High marked launch-dependent, and any missing item the verdict criteria list as mandatory.

## Status
| Status | Meaning |
|---|---|
| Confirmed | Proven with evidence |
| Suspected | Indication exists; not verified |
| Not Reproducible | Could not be reproduced |
| Not Applicable | Irrelevant to this project |
| Accepted Risk | Explicitly accepted by a person with authority (record who/when) |
| Resolved | Fixed **and verified** |
| Deferred | Postponed with a reason and a target date |

Lifecycle: Suspected → Confirmed | Not Reproducible; Confirmed → Resolved | Accepted Risk | Deferred. Only the user/owner can set Accepted Risk or Deferred.

## Finding ID convention
`<CATEGORY>-<NNN>` e.g. `SEC-001`, `CMS-004`, `PERF-002`. Categories: DISC, CODE, DEP, SEC, PRIV, CMS, FUNC, A11Y, PERF, SEO, INFRA, MON, BCP, COST, GOV, TEST, REP.
