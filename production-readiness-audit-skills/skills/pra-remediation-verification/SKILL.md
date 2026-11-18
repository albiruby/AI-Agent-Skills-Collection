---
name: pra-remediation-verification
description: Controlled remediation and verification after an audit - audit modes, execution order, change-control rules, fixing approved findings in prioritized batches, adding regression tests, running lint/typecheck/build/tests, re-auditing touched areas and updating the findings ledger. Use when the user says "perbaiki temuan audit", "fix the findings", "lanjut remediation", "verifikasi perbaikan", "re-audit", or approves a remediation plan; also use to decide which audit mode applies. Covers audit domains 96-99.
---

# Modes, Change-Control, Fixing, Verifying (Domains 96–99)

Parent: `production-readiness-audit`. Enter only after an audit report exists **and** the user approved specific findings (or the whole plan). Without approval, stay in Audit-Only. Lists: `references/checklist.md`.

## Modes (96)
Discovery · Audit-Only · Deep Audit · Security Audit · Performance Audit · CMS Audit · Production Readiness · **Remediation** · **Verification** · Maintenance · Incident. State the current mode at the start of each work block and switch explicitly (e.g. "Switching to Remediation Mode for SEC-001, SEC-003").

## Remediation procedure (99)
1. **Confirm scope**: list the approved finding IDs, files likely touched, and rollback approach. Create a branch (e.g. `audit/fix-<ids>`); never commit to the production branch; never push/deploy unless asked.
2. **Order by priority**: security & data-loss blockers → functional launch blockers → CMS/data integrity → performance/accessibility → operational gaps → quick wins → long-term. Fix **one group at a time**; one logical change per commit with the finding ID in the message.
3. **Stay minimal**: no unrelated refactors; preserve the design system, existing functionality, CMS data contract, route compatibility (add redirects if URLs change), and backward compatibility where needed. If a fix requires a decision (e.g. CSP strictness vs third-party scripts), ask.
4. **Add a test for each fixed bug** where feasible (unit for logic, Playwright for flows, a query test for GROQ) so it cannot silently regress.
5. **Verify after each group**: `lint` → `typecheck` → `build` → unit/integration tests → E2E if available → visual/responsive check of touched UI → security implication check (does the fix open something new?) → production-configuration check (env vars, headers, caching). Capture command output as evidence.
6. **Production-affecting actions need separate explicit approval and are performed by/with the owner**: secret rotation, env var changes, DNS/domain changes, CMS data edits, deployment, cache purge. Provide exact steps and rollback; do not execute silently.
7. **Document**: update the findings ledger (status → *Resolved* only after verification, with evidence and date), changelog/docs/runbooks touched, remediation notes.
8. **Re-audit** the areas touched (and their neighbors): run the relevant sub-skill checks again; confirm the original finding no longer reproduces and no new finding appears. Update coverage and, if scope allows, re-issue the verdict.
9. **Prepare rollback** for risky changes (revert commit, feature flag, previous deployment ID).

## Verification mode (stand-alone)
Given a list of "fixed" findings from someone else: reproduce original evidence, confirm fix, run regression checks, record result per finding (Resolved / Not Resolved / Partially). Do not mark Resolved from a diff alone.

## Hard rules (also in master `principles-and-rules.md`)
Never claim success before verification · never skip failing tests by disabling them · never `--force` upgrade dependencies · never commit secrets (use `git rm` + advise rotation + history cleanup as an owner decision) · never touch production data · stop and ask when scope, risk or intent is unclear.

## Output
Per-batch summary: findings addressed · files changed · tests added · commands run + results · remaining risks · rollback · next batch. Final: updated ledger and verdict delta.

## Pitfalls
Fixing during audit without approval · "while I'm here" refactors · declaring Resolved because the build is green · forgetting redirect/compat for renamed routes · changing CMS schema without migration/compat plan.
