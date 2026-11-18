---
name: pra-dependencies-build-cicd
description: Audit npm/pnpm/yarn dependencies (outdated, deprecated, vulnerable, unused, duplicate, suspicious, licenses), the production build and compilation (TypeScript, ESLint, warnings, env availability, reproducibility, source maps) and CI/CD pipelines (GitHub Actions permissions, pinning, secrets, gating, rollback). Use when the user mentions npm audit, package vulnerabilities, "cek dependency", build fails or warns, next build, lockfile problems, GitHub Actions, workflows, Dependabot, or supply-chain risk. Covers audit domains 12-14.
---

# Dependencies, Build, CI/CD (Domains 12–14)

Parent: `production-readiness-audit`. Supply-chain *security* depth lives in `pra-security` (domain 22); this skill produces the raw data. Lists: `references/checklist.md`.

## Procedure
1. **Dependencies** (read-only)
   - Detect the manager from lockfile; never mix managers. Verify exactly one lockfile and that it matches `package.json` (`npm ci --dry-run` / `pnpm install --frozen-lockfile --lockfile-only` in a scratch copy).
   - `npm ls --all` (conflicts, peer warnings, duplicates) · `npm outdated` · `npm audit --omit=dev` and full `npm audit` (distinguish runtime vs dev exposure; judge reachability — a dev-only CVE in a build tool is not a runtime Critical).
   - Unused/missing: `npx depcheck` or `npx knip`.
   - Deprecated/abandoned: `npm view <pkg> deprecated time.modified`; low-maintenance heuristics (no release in 2+ years, archived repo).
   - Suspicious: typosquats (names one char off a popular package), packages with `postinstall`/`preinstall` scripts (`npm query ':attr(scripts, [postinstall])'`), unpinned git/URL dependencies, unexpected registries in lockfile.
   - Licenses: `npx license-checker --summary` — flag GPL/AGPL/unknown in a proprietary site.
   - Compatibility: Next ↔ React ↔ Node ↔ TypeScript ↔ `next-sanity`/`sanity` matrix per official docs for installed versions.
   - Bundle weight offenders: see `pra-performance-caching`.
2. **Build** — work in a scratch copy or ensure no tracked files change.
   - Clean install, then `npm run lint`, `npx tsc --noEmit`, `npm run build` with **production-like env** (names from the inventory; use dummy non-secret values or the user's staging values). Capture warnings and errors verbatim.
   - Check: missing env at build time, static generation failures, dynamic route generation, invalid imports/case-sensitivity (build on Linux), missing assets, dev/prod differences, determinism (two builds, same lockfile), build time and memory, `productionBrowserSourceMaps`, artifacts that leak (source maps publicly reachable).
   - Run the built app (`next start`) for runtime smoke tests where possible.
3. **CI/CD** — read `.github/workflows/*`.
   - Triggers & branch filters; `pull_request` vs `pull_request_target` (the latter with checkout of PR head = injection risk).
   - Stages present: lint, typecheck, unit, integration, E2E, build, dependency/secret scanning.
   - `permissions:` least privilege (default `contents: read`); secrets only where needed; no secrets echoed; third-party actions **pinned to commit SHA**; no `curl | bash`; artifact handling; concurrency groups; production deploy restricted (environment protection, approvals); preview vs production separation; failed-deploy behavior; rollback path; notifications.
   - Vercel Git integration vs Actions: who actually deploys? Avoid double deploys.
   - Update automation: Dependabot/Renovate configured with sensible grouping.

## Calibration
- Critical/High advisories that are reachable in runtime code → High (Critical if unauthenticated RCE/auth bypass and reachable).
- Advisories only in dev tooling → Low/Info (state why).
- Build passes only with a local-only env/file → High (not reproducible).
- Unpinned third-party Action with write permissions + secrets → Medium–High.
- Lockfile absent or two lockfiles → Medium.

## Output
Dependency health table (package · current · latest · issue · runtime/dev · severity), build report (commands, durations, warnings), CI/CD review, findings (`DEP-NNN`). Never run `npm audit fix --force` or upgrade packages in audit mode.

## Pitfalls
Treating `npm audit` count as risk · upgrading during the audit · building with real production secrets · forgetting that Vercel may use a different Node version than local.
