---
name: pra-reporting-risk
description: Governance layer of an audit - methodology discipline, severity and risk classification, finding documentation with evidence, coverage and verification accounting, remediation planning, and the final production-readiness verdict (READY / READY WITH CONDITIONS / NOT READY / INCONCLUSIVE). Use when compiling or reviewing audit findings, writing the audit report, rating severity, checking whether claims are evidenced, producing the coverage matrix, deciding go/no-go, or when the user asks "buat laporan audit", "launch blocker apa saja?", "siap launch atau belum?". Covers audit domains 90-95.
---

# Methodology, Risk, Evidence, Coverage, Verdict (Domains 90–95)

Parent: `production-readiness-audit`. You are the quality gate on every other skill's output. Use `../production-readiness-audit/templates/*` and `references/`.

## Procedure
1. **Methodology check (90)**: before reporting, confirm the audit was based on actual source/config/dependencies/environments, relationships (frontend↔CMS↔services) were examined, production build and browser behavior were checked where possible, errors/warnings/edge cases/security boundaries/performance/operational risks were covered, and **limitations are written down**. If not, say so in the report — do not paper over.
2. **Normalize findings (92)**: one finding per root cause, unique ID, specific title, all required fields (ID, category, severity, status, affected file/component/route/environment, exact location, evidence, reproduction, expected vs actual, root cause, technical/business/security/user impact, recommended fix, dependencies, complexity, regression risk, verification procedure, references). Reject vague entries ("performance is poor") — send back to the originating skill or rewrite with evidence. Mask secrets/PII.
3. **Verify (Phase 4)**: re-read/reproduce each Critical and High yourself. Statuses: Confirmed / Suspected / Not Reproducible / Not Applicable / Accepted Risk / Resolved / Deferred. Only owners can accept or defer.
4. **Classify (91)**: severity from impact × likelihood in project context (`../production-readiness-audit/references/severity-and-status.md`); record deciding factors (likelihood, impact, exploitability, exposure, business/user impact, data sensitivity, operational impact, remediation complexity, regression risk, launch dependency). Cross-check consistency: same issue pattern → same severity across the report; no inflation.
5. **Coverage (93)**: fill the coverage matrix: domains completed / partial / not tested / N/A / Not Verifiable; routes, endpoints, CMS types, components, environments, browsers, viewports; tests executed/passed/failed/skipped; findings verified vs unverified; evidence completeness; remaining uncertainties. Report source-reading, runtime testing, security testing and production verification **separately**. Never write "100% audited".
6. **Remediation plan (94)**: group by severity; flag launch/security/functional/architectural/CMS blockers, performance bottlenecks, operational gaps; quick wins vs long-term; order of work; map to files; dependent changes; complexity; regression risk; acceptance criteria; tests; rollback; tracking; re-audit/regression plan. Use `remediation-plan.md` template. **Ask for approval** before acting.
7. **Verdict (95)**: apply `../production-readiness-audit/references/verdict-criteria.md`. Provide the verdict, the 2–5 findings/gates that decided it, conditions with owner/date (for READY WITH CONDITIONS), and the explicit statement distinguishing *audit completed*, *tests passed*, *production ready*.

## Report quality bar
- A reader can act without asking you anything: every finding tells where, why it matters, what to do, how to verify.
- Executive summary ≤ 1 page; details after. Counts match the tables. No secrets/PII. Language = user's language.
- Honest about uncertainty: Not Verifiable list is prominent, not buried.
- Recommendations are sized to the project (brochure site vs transactional app).

## Verdict smell tests
READY while any area is Not Verifiable and critical → wrong (INCONCLUSIVE). NOT READY because of Low findings → wrong. READY WITH CONDITIONS without owners/dates → incomplete. Verdict derived from a percentage → wrong.

## Output
`audit-report.md`, `findings-ledger.md`, `coverage-matrix.md`, `remediation-plan.md`.

## Pitfalls
Averaging severity · reporting duplicates as separate findings · hiding limitations · letting the build status stand in for readiness · leaving Suspected findings undistinguished from Confirmed.
