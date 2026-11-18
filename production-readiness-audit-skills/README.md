# Production Readiness Audit — Skills Pack

A set of agent skills (Markdown) that make an AI coding agent perform a **thorough, evidence-based, non-destructive production-readiness / pre-launch audit** of a web project, report the findings in a decision-ready format, and — only with approval — remediate and verify.

Built from the *Master Audit Scope* (99 audit domains, 16 parts) for **Next.js App Router · React · TypeScript · Tailwind · Sanity · GitHub · Vercel · DNS · third-party integrations**, generalized so it also works for other CMS-driven or corporate/hospitality/portfolio/editorial sites.

## What you get
| Path | Content |
|---|---|
| `SKILLS.md` | Catalogue + routing + how to install/use |
| `skills/production-readiness-audit/` | **Master skill**: principles, modes, workflow, evidence standard, verdict criteria, 5 templates, 3 read-only scripts, 99-domain index |
| `skills/pra-*/` (18) | Domain sub-skills, each with `SKILL.md` + full `references/checklist.md` |
| `tools/validate_pack.py` | Lints the pack (frontmatter, links, domain coverage) |
| `CHANGELOG.md`, `CONTRIBUTING.md` | Maintenance docs |

All 99 source domains are covered: every checklist item from the scope was carried into a `checklist.md`, and each `SKILL.md` adds the *how* (commands, calibration, pitfalls).

## Design principles
1. Audit the **actual repo and configuration**; never assume features.
2. **Audit-Only by default** — no source edits, no production writes, no real form submissions, no load/pen tests without approval.
3. Every finding has **evidence, location, impact, severity, recommendation**; Confirmed vs Suspected vs improvement are kept apart.
4. Applicability triage per domain: **Applicable / Not Applicable / Not Verifiable** — no padding with irrelevant checks.
5. Verdict from evidence: **READY / READY WITH CONDITIONS / NOT READY / INCONCLUSIVE**.
6. *Audit completed ≠ tests passed ≠ production ready.*
7. Secrets and personal data are never written into reports (masked).

## Quick start
1. Install (see `SKILLS.md` → *Using the pack*).
2. In your project, tell the agent, e.g.:
   - EN: *"Run a production readiness audit on this repo (Audit-Only). Staging is at https://… Report in English."*
   - ID: *"Audit project ini sebelum launch, mode Audit-Only. Repo ini Next.js + Sanity + Vercel. Buat laporan dalam Bahasa Indonesia."*
   - Focused: *"Security audit saja"*, *"cek konten CMS dan skalabilitas brand baru"*, *"siap production belum?"*
3. The agent runs discovery, triages the 99 domains, audits, verifies, and delivers `audit-report.md`, `findings-ledger.md`, `coverage-matrix.md`, `remediation-plan.md`.
4. Approve specific findings → the agent switches to Remediation Mode, fixes on a branch, verifies, re-audits.

## Scripts (read-only)
```bash
bash skills/production-readiness-audit/scripts/inventory.sh .            # stack, routes, env var names, CI, git hygiene
bash skills/production-readiness-audit/scripts/secret-grep.sh . --history # secret patterns: locations only, never values
bash skills/production-readiness-audit/scripts/check-headers.sh https://example.com / /some-page  # authorized URLs only
```

## Limits & honesty
- Dashboard-level facts (Vercel, Sanity permissions, registrar, billing) need the owner's access or exports; otherwise they are reported as **Not Verifiable**, not guessed.
- Vendor limits, prices and framework conventions change — the skills tell the agent to verify against current official docs for the installed versions.
- Privacy/legal output is a gap analysis, not legal advice. Accessibility output cannot certify WCAG conformance.
- The skills are written in English (agent-facing) with Indonesian trigger phrases; reports follow the user's language.

## Validate the pack
```bash
python3 tools/validate_pack.py
```

## License
Add the license of your choice before publishing (e.g. MIT).
