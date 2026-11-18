# SKILLS.md — Production Readiness Audit Skill Pack

Entry point and catalogue. **Start with `skills/production-readiness-audit/SKILL.md`** (the master skill); it loads the sub-skills below on demand.

- **Version:** 1.0.0 · **Agent-agnostic:** plain Markdown + read-only shell scripts; works with Claude (Skills / Claude Code / Cowork), Cursor, Codex, Gemini CLI, or any agent that can read files.
- **Reference stack:** Next.js App Router · React · TypeScript · Tailwind CSS · Sanity CMS · GitHub · Vercel · domain/DNS · third-party services. Non-matching stacks: keep the method, skip inapplicable checks (the applicability triage exists for this).
- **Reference case:** Samsara Group multi-brand website (5 brands) — used only as an example in the CMS scalability matrix.

## How it fits together
```
production-readiness-audit  (master: principles, modes, workflow, verdict, templates, scripts)
   ├── pra-discovery                  domains  1–4
   ├── pra-codebase-architecture      domains  5–11
   ├── pra-dependencies-build-cicd    domains 12–14
   ├── pra-security                   domains 15–22
   ├── pra-privacy-legal              domains 23–24
   ├── pra-cms-sanity                 domains 25–32
   ├── pra-functionality-ux           domains 33–37
   ├── pra-accessibility-responsive   domains 38–39
   ├── pra-performance-caching        domains 40–45
   ├── pra-seo-i18n                   domains 46–49
   ├── pra-infrastructure-deployment  domains 50–56
   ├── pra-monitoring-observability   domains 57–64
   ├── pra-backup-recovery-incident   domains 65–69
   ├── pra-cost-scalability           domains 70–73
   ├── pra-maintenance-governance     domains 74–80
   ├── pra-testing-acceptance         domains 81–89
   ├── pra-reporting-risk             domains 90–95
   └── pra-remediation-verification   domains 96–99
```
Every sub-skill has `SKILL.md` (procedure, calibration, output, pitfalls) and `references/checklist.md` (the complete domain checklist). The full 99-domain map is in `skills/production-readiness-audit/references/domain-index.md`.

## Catalogue
| Skill | Domains | Use for |
|---|---|---|
| `production-readiness-audit` | — | Orchestrating any audit; modes; verdict |
| `pra-discovery` | 1–4 | Inventory, scope vs brief, docs, Git hygiene |
| `pra-codebase-architecture` | 5–11 | Code quality, architecture, Next.js, React, TS, styling, UI |
| `pra-dependencies-build-cicd` | 12–14 | Packages, production build, GitHub Actions |
| `pra-security` | 15–22 | Secrets, authN/Z, API, XSS/injection, headers, infra, supply chain |
| `pra-privacy-legal` | 23–24 | Personal data, cookies, UU PDP, licensing |
| `pra-cms-sanity` | 25–32 | Schema, GROQ, tokens, content, media, multi-entity scalability, lifecycle |
| `pra-functionality-ux` | 33–37 | Routes, flows, forms, integrations, UX |
| `pra-accessibility-responsive` | 38–39 | WCAG 2.2 AA, 16 viewports, browsers |
| `pra-performance-caching` | 40–45 | Web Vitals, media, bundles, fetching, ISR/CDN |
| `pra-seo-i18n` | 46–49 | Technical/content SEO, JSON-LD, hreflang |
| `pra-infrastructure-deployment` | 50–56 | Hosting, DNS/SPF/DKIM/DMARC, TLS, Vercel, env, deploy, launch config |
| `pra-monitoring-observability` | 57–64 | Uptime, errors, logs, RUM, analytics, alerts |
| `pra-backup-recovery-incident` | 65–69 | Backups, restore, DR, rollback, incident mode |
| `pra-cost-scalability` | 70–73 | Billing, quotas, growth, safe load testing |
| `pra-maintenance-governance` | 74–80 | Ownership, offboarding, maintenance mode, tech debt |
| `pra-testing-acceptance` | 81–89 | Test strategy, E2E, visual, smoke test, UAT |
| `pra-reporting-risk` | 90–95 | Findings quality, severity, coverage, verdict |
| `pra-remediation-verification` | 96–99 | Modes, change-control, fixing and verifying |

## Audit modes → skills
Discovery → `pra-discovery` · Audit-Only → all relevant · Deep Audit → + `pra-testing-acceptance` · Security Audit → `pra-security` + `pra-dependencies-build-cicd` + `pra-privacy-legal` · Performance Audit → `pra-performance-caching` · CMS Audit → `pra-cms-sanity` · Production Readiness → all + `pra-reporting-risk` · Remediation / Verification → `pra-remediation-verification` · Maintenance → `pra-maintenance-governance` · Incident → `pra-backup-recovery-incident`.

## Using the pack
**Claude (claude.ai / Claude Code / Cowork):** copy each folder under `skills/` into your skills directory (e.g. `~/.claude/skills/` or the project's `.claude/skills/`), or upload via Settings → Capabilities → Skills. The `description` fields are written to trigger on both English and Indonesian phrasing.
**Other agents:** put the `skills/` folder in the repo (or a sibling folder), then add one line to your agent instructions (`AGENTS.md`, `.cursorrules`, system prompt):
> For any production-readiness, pre-launch, or website audit task, read `skills/production-readiness-audit/SKILL.md` first and follow it; load `skills/pra-*/SKILL.md` as it directs.

## Core rule
**Audit completed ≠ tests passed ≠ production ready.** The agent must keep these three statuses separate in every report.
