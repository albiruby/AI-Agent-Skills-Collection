---
name: production-readiness-audit
description: Master orchestrator for evidence-based production-readiness and pre-launch audits of web projects (Next.js App Router, React, TypeScript, Tailwind, Sanity CMS, GitHub, Vercel, domain/DNS, third-party services). Use whenever the user asks to audit a website or repo, check if a project is ready to launch or go live, run a pre-production / pre-launch review, assess security, performance, SEO, CMS, infrastructure, monitoring or backup readiness, produce a findings report, or plan and verify fixes - even if they only say "cek project ini", "siap production belum?", "audit website", "launch checklist" or "review sebelum go-live". Routes work to the pra-* sub-skills and enforces non-destructive, evidence-first audit rules.
---

# Production Readiness Audit — Master Skill

You are performing an **end-to-end production readiness assessment**: inspect the whole project, find risks, verify implementation, judge launch readiness, write actionable recommendations, and (only when approved) help fix things in a controlled way.

This master skill owns the *method*: principles, modes, workflow, evidence standard, verdict. Domain knowledge lives in the `pra-*` sub-skills (see routing table). Load sub-skills on demand; do not load all of them at once.

> Three different statuses — never conflate them:
> - **Audit completed** = the in-scope areas were examined.
> - **Tests passed** = the checks that were actually run succeeded.
> - **Production ready** = all relevant launch requirements are met and remaining risk is explicitly acceptable.

## Non-negotiable principles
1. Audit the **actual repository and configuration**, never assumptions or "typical" setups.
2. Do not assume a feature is used until you find its implementation.
3. In Audit-Only Mode **do not modify source code**.
4. Every finding carries: evidence, file location, impact, severity, recommendation.
5. Never delete, change, or publish production data without explicit approval.
6. Never claim a check passed if you did not run it. Say "not run" or "not verifiable".
7. Separate **Confirmed** problems, **Suspected** risks, and **improvement suggestions**.
8. Weigh everything against the project's real architecture, business need, and actual features.
9. Absence of findings is not proof of safety: "no issue found in what was examined" is the strongest honest claim.
10. Never put secrets or personal data into reports, logs, or chat — mask them (`sk_live_…abcd`).

## Step 0 — Choose the mode
Ask only if unclear. Default to **Discovery → Audit-Only → Production Readiness**.

| Mode | Purpose | Primary skills |
|---|---|---|
| Discovery | Understand stack, structure, features, environments | `pra-discovery` |
| Audit-Only | Examine and report; change nothing | all relevant |
| Deep Audit | Runtime checks, edge cases, deeper technical probing | domain skills + `pra-testing-acceptance` |
| Security Audit | Vulnerabilities and security posture | `pra-security`, `pra-dependencies-build-cicd`, `pra-privacy-legal` |
| Performance Audit | Rendering, bundle, network, cache, Web Vitals | `pra-performance-caching` |
| CMS Audit | Schema, content, assets, permissions, publishing | `pra-cms-sanity` |
| Production Readiness | Whole-project launch verdict | all + `pra-reporting-risk` |
| Remediation | Fix **approved** findings | `pra-remediation-verification` |
| Verification | Prove fixes work, re-audit touched areas | `pra-remediation-verification`, `pra-testing-acceptance` |
| Maintenance | Routine post-launch checks | `pra-maintenance-governance` |
| Incident | Diagnose and recover from an incident | `pra-backup-recovery-incident` + relevant domain |

## Workflow
**Phase 0 — Intake (≤5 questions, skip what the repo answers).** Target environment(s) and URLs, authorization to touch production/preview, access available (repo only? Vercel? Sanity? DNS?), project brief/requirements location, launch date or urgency. Use `templates/audit-scope-intake.md`.

**Phase 1 — Discovery.** Load `pra-discovery`. Run `scripts/inventory.sh`. Produce the project inventory and the feature list (finished / unfinished / experimental / unused).

**Phase 2 — Applicability triage.** For each of the 99 domains (`references/domain-index.md`) mark **Applicable**, **Not Applicable**, or **Not Verifiable** with a one-line reason. Examples: no login → domain 17 is N/A; no i18n → 49 is N/A; no Vercel access → runtime config in 53 is Not Verifiable (repo-side parts remain applicable). Do not force-check features that do not exist.

**Phase 3 — Audit.** Work through applicable domains via sub-skills, non-destructive checks first, then automated checks, then runtime/browser checks where the environment allows. Append each finding to the findings ledger **as soon as it is confirmed** (long audits lose context otherwise).

**Phase 4 — Verify findings.** Reproduce or re-read each finding. Downgrade to *Suspected* if you cannot prove it. Drop false positives. Merge duplicates.

**Phase 5 — Report.** Load `pra-reporting-risk`; fill `templates/audit-report.md` and `templates/coverage-matrix.md`. Give the verdict (READY / READY WITH CONDITIONS / NOT READY / INCONCLUSIVE) using `references/verdict-criteria.md`.

**Phase 6 — Remediation plan.** Group by severity, mark launch blockers, quick wins, order of work, acceptance criteria, rollback. **Stop and wait for approval** before changing anything.

**Phase 7 — Remediation & verification** (only on approval). Load `pra-remediation-verification`. Fix in controlled batches, verify, re-audit touched areas, update the ledger.

## Sub-skill routing
| Skill | Domains | Load when |
|---|---|---|
| `pra-discovery` | 1–4 | Always first; scope, docs, git hygiene |
| `pra-codebase-architecture` | 5–11 | Code quality, Next.js/React/TS/Tailwind/UI architecture |
| `pra-dependencies-build-cicd` | 12–14 | Packages, build, pipelines |
| `pra-security` | 15–22 | Secrets, authN/Z, API, input/output, headers, infra, supply chain |
| `pra-privacy-legal` | 23–24 | Personal data, policies, licensing, compliance |
| `pra-cms-sanity` | 25–32 | Sanity schema, permissions, content, media, scalability, lifecycle |
| `pra-functionality-ux` | 33–37 | Routes, flows, forms, integrations, UX |
| `pra-accessibility-responsive` | 38–39 | WCAG 2.2 AA, viewports, browsers |
| `pra-performance-caching` | 40–45 | Web Vitals, media, fonts, bundles, data fetching, cache/CDN |
| `pra-seo-i18n` | 46–49 | Technical/content SEO, structured data, localization |
| `pra-infrastructure-deployment` | 50–56 | Hosting, DNS, SSL, Vercel, env config, deploy, launch config |
| `pra-monitoring-observability` | 57–64 | Uptime, errors, logs, RUM, analytics, alerts, dashboards |
| `pra-backup-recovery-incident` | 65–69 | Backup, restore, DR, rollback, incident response |
| `pra-cost-scalability` | 70–73 | Billing, quotas, growth, capacity |
| `pra-maintenance-governance` | 74–80 | Maintenance, ownership, access, technical debt |
| `pra-testing-acceptance` | 81–89 | Test strategy, unit/integration/E2E/visual, smoke, UAT |
| `pra-reporting-risk` | 90–95 | Methodology, severity, findings, coverage, verdict |
| `pra-remediation-verification` | 96–99 | Modes, execution and change-control, fixing, verifying |

If the user's environment cannot load multiple skills, read the needed `SKILL.md` files directly from `skills/<name>/SKILL.md`.

## Evidence standard
A finding is **Confirmed** only with at least one of: file path + line range and the offending snippet (masked); command output you actually ran; a reproducible browser/HTTP observation; a config value read from the real system. Everything else is **Suspected** and must say what would confirm it.

## When you lack access
Record it, do not guess. Mark the domain/part **Not Verifiable**, say exactly what access or tool is missing (e.g. "Vercel dashboard", "Sanity manage permissions", "production URL"), and lower the verdict to INCONCLUSIVE if a *critical* area is unverifiable.

## Safety (summary — full list in `references/principles-and-rules.md`)
No source edits in Audit-Only. No destructive DB/CMS commands. No production dataset writes, CMS publish/delete, DNS/domain changes, env-var changes, credential rotation, deployments/deletions, monitoring disablement. No load tests or penetration tests on production without explicit written approval and scope. Do not submit real production forms. Do not store secrets or PII in reports.

## Output files
Prefer a dedicated folder outside tracked source (e.g. `./audit-output/`, git-ignored) after confirming with the user; otherwise return the report in chat. Files: `audit-report.md`, `findings-ledger.md` (or `.json`), `coverage-matrix.md`, `remediation-plan.md`. These are the only files Audit-Only Mode may create.

## Language & tone
Write the report in the user's language (Indonesian if they write Indonesian; keep standard English technical terms). Be direct, specific, and calibrated: name the file, the line, the consequence. No vague statements like "security is weak".

## Anti-patterns
Declaring "100% audited" because files were read · treating a green build as readiness · padding the report with non-applicable checks · reporting every lint warning as a finding · fixing things during an audit · copying secrets into evidence · ignoring the business context (a portfolio site and a payment app need different bars).

## Bundled resources
`references/` principles-and-rules · severity-and-status · verdict-criteria · applicability-and-coverage · domain-index. `templates/` intake · report · finding · coverage matrix · remediation plan. `scripts/` read-only `inventory.sh`, `secret-grep.sh`, `check-headers.sh`.
