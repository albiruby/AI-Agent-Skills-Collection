---
name: pra-maintenance-governance
description: Audit maintenance strategy, access and ownership governance, and technical debt, and run Maintenance Mode routine checks after launch. Use when the user asks who owns the repo/Vercel/Sanity/domain/billing, offboarding of interns or contractors, shared credentials, MFA and account recovery, update schedule for Next.js/React/Sanity, monthly/quarterly maintenance checklist, technical debt prioritization, or post-launch upkeep ("maintenance bulanan", "siapa pegang akses"). Covers audit domains 74-80.
---

# Maintenance, Ownership, Debt (Domains 74–80)

Parent: `production-readiness-audit`. Many production failures are ownership failures: an expired domain, a departed intern's token, a billing card that lapsed. Lists: `references/checklist.md`.

## Audit procedure
1. **Ownership & access (79)** — build an **access register**: for GitHub org/repo, Vercel team, Sanity org/project, domain registrar, DNS provider, email provider, analytics, monitoring, maps, billing: account owner (business entity vs individual), admins, MFA enforced?, recovery email/phone owner, shared credentials (should be none — use a password manager/SSO), former intern/contractor/employee access removed, offboarding/onboarding procedure, ownership-transfer procedure, bus factor (>1 person can recover every account). Dashboard checks → Not Verifiable unless exported by the owner.
2. **Maintenance strategy (74)**: named owner, schedule, checklist, budget, prioritization method; documented per area (dependencies, framework, CMS, content, security, performance, SEO, infra/domain, backups, monitoring, integrations).
3. **Dependency & framework maintenance (75)**: update cadence for Next.js/React/TypeScript/Tailwind/Sanity SDK/Node LTS (note EOL dates from official release schedules), automated PRs (Dependabot/Renovate) with CI gating, security-patch SLA (e.g. Critical ≤ 48 h, High ≤ 7 d — propose, don't assume), deprecation tracking, compatibility/regression/build verification, rollback plan, upgrade notes.
4. **Content & CMS maintenance (76)**: expired events/outdated content process, archived entities, broken-link checks, hours/contact accuracy owner, unused assets/draft cleanup, editorial ownership and permissions, schema-change procedure, content backups.
5. **Security maintenance (77)**: vulnerability monitoring, secret rotation calendar, quarterly access/permission/MFA reviews, domain/DNS/SSL renewals, header/CSP review, form-abuse and rate-limit review, log review, patch management, vendor/privacy-policy review.
6. **Performance & SEO maintenance (78)**: monthly Web Vitals/Lighthouse, bundle/image/font drift, third-party script review, crawl/index errors, sitemap/robots/canonical/structured-data validity, redirect health, content freshness.
7. **Technical debt (80)**: register of known bugs, unresolved warnings, deprecated APIs/dependencies, duplicate components/logic, unused packages/assets, fragile areas, performance/security/a11y weaknesses, test and monitoring gaps, architecture/scalability limits; prioritize by (risk × frequency of change ÷ effort); propose a roadmap — as recommendations only.

## Maintenance Mode (post-launch routine)
Run on a schedule (suggest: weekly light, monthly standard, quarterly deep):
- **Weekly**: uptime/error digest, failed deploys, form delivery spot-check (authorized), security advisories.
- **Monthly**: `npm outdated` + `npm audit`, Web Vitals trend, broken links/404 report, Search Console coverage, usage vs quota, backup success check, content freshness (events/hours).
- **Quarterly**: access & MFA review, secret rotation, restore drill, DR/rollback drill, privacy/vendor review, tech-debt triage, framework upgrade planning.
- **Annually**: domain/SSL/renewal audit, full production-readiness re-audit, license/asset review.
Output a dated maintenance report with deltas vs the previous one.

## Calibration
- Registrar/Vercel/Sanity owned by a single individual with no recovery path, or ex-members still admin → High.
- Shared passwords in chat/doc → High–Medium. No MFA on registrar/GitHub/Vercel → High.
- Framework two majors behind with known CVEs → Medium–High. No owner for maintenance → Medium.

## Output
Access/ownership register (no secrets), maintenance calendar, debt register with priorities, findings (`GOV-NNN`).

## Pitfalls
Listing passwords or recovery codes in the report · "update everything" advice without regression plan · treating debt as an emergency list.
