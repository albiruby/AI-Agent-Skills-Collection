---
name: pra-discovery
description: Project discovery, scope/requirements validation, documentation audit and Git repository hygiene for a web project - the mandatory first step of any production-readiness audit. Use when starting every audit, or when the user says "pahami project ini", "inventory", "what is this repo", "cek dokumentasi", "cek git", "apakah sesuai brief", or when you need the stack, routes, environments, integrations, unfinished features, placeholders, mock data, committed credentials or branch protection status. Covers audit domains 1-4.
---

# Discovery, Scope, Docs, Git (Domains 1–4)

Parent: `production-readiness-audit`. Run first; every other skill depends on its inventory.

## Inputs
Repo path; optional brief/requirements; optional URLs. Full item lists: `references/checklist.md`.

## Procedure
1. **Run the inventory** — `bash ../production-readiness-audit/scripts/inventory.sh <repo>`. It is read-only and prints env var *names* only.
2. **Identify the application**: purpose, type (brochure, editorial, hospitality, app), framework/runtime, router (App vs Pages), versions (Next, React, TS, Node, package manager — check `engines`, `.nvmrc`, `packageManager`, lockfile).
3. **Map structure**: top-level folders, entry points (`app/layout.tsx`, `middleware`/`proxy`), all routes (static, dynamic `[slug]`, catch-all, route groups), route handlers (`route.ts`) and Server Actions, Server vs Client component split (`'use client'` boundaries).
4. **Map data & services**: CMS (Sanity project id/dataset in code, not values from secrets), external APIs, forms/email, maps, analytics, auth, storage, webhooks. Read `.env.example` and code for variable names; classify each as public/server/secret.
5. **Map environments & pipeline**: dev/preview/staging/production, deployment platform, `vercel.json`, GitHub workflows, build/test/lint scripts.
6. **Classify features**: finished / unfinished / experimental / unused (dead routes, unused components, unreferenced env vars, unused dependencies).
7. **Validate scope** (domain 2): compare implementation with the brief. Look for placeholders (`lorem`, `TODO`, `example.com`, `#` hrefs), mock data/fixtures in production paths, dev-only code (`process.env.NODE_ENV !== 'production'` branches), features not wired to CMS/backend, undocumented scope changes, conflicting requirements, requirements lacking acceptance criteria.
8. **Audit documentation** (domain 3): which of README/ARCHITECTURE/ENVIRONMENT/DEPLOYMENT/SECURITY/etc. exist; is each accurate against the code? Can another developer set up and deploy from the docs alone? Env vars documented? Rollback/recovery/ownership documented?
9. **Audit Git** (domain 4): default/production branch, branch protection & required reviews/checks (needs GitHub access — otherwise Not Verifiable), `.gitignore`/`.gitattributes`, tracked `.env*`, large/binary files, build artifacts committed, lockfile consistency, conflict markers, commit-message quality, release tags, rollback commit availability. Run `scripts/secret-grep.sh --history` for credentials (details in `pra-security`).
10. **Record** inventory + feature list + applicability triage (see master Phase 2) + initial findings.

## What is a finding here
- Committed `.env` with real values → Critical (hand to `pra-security` for rotation advice).
- Production path serving mock/placeholder data → High (launch dependency).
- Docs that make deployment impossible for someone else → Medium.
- Missing branch protection on the production branch → Medium (High if team > 1 and auto-deploys production).
- Unused dependency/feature → Low/Informational.

## Not verifiable (typical)
Branch protection, repo permissions, Vercel project settings, undocumented scope changes (ask the user).

## Output
Project inventory table (stack, versions, routes, integrations, env vars with classification, environments, pipelines), feature status list, doc gap list, git hygiene results, findings (`DISC-NNN`).

## Pitfalls
Assuming App Router from a `pages/` folder name · treating `NEXT_PUBLIC_` as private · calling a feature "used" because a package is installed · reading only README instead of code · printing env values.
