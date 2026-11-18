---
name: pra-infrastructure-deployment
description: Audit hosting, domain/DNS, SSL/TLS, Vercel project configuration, environment configuration, deployment strategy and the production launch configuration. Use when the user asks if the Vercel/DNS/domain setup is correct, "cek DNS", SPF/DKIM/DMARC, certificate or HSTS, preview vs production env vars, Node version, function limits/regions, rollback and promotion procedure, "konfigurasi production sebelum launch", or domain/registrar security and expiry. Covers audit domains 50-56.
---

# Hosting, DNS, SSL, Vercel, Env, Deploy, Launch (Domains 50–56)

Parent: `production-readiness-audit`. Much of this is dashboard-level: ask the owner for screenshots/exports or mark **Not Verifiable**. Never change DNS, domains, env vars, or deployments. Lists: `references/checklist.md`.

## Procedure
1. **Hosting & limits (50)**: plan (Hobby/Pro/Enterprise — Hobby is non-commercial per Vercel terms; flag for a commercial site), function region vs audience/CMS region (Jakarta audience ↔ Singapore/other region latency), max duration/memory, bandwidth/image-optimization/build-minute quotas, edge vs Node runtime, provider status/reliability dependency, cost ceiling. Confirm current limits from official docs at audit time — they change.
2. **Domain & DNS (51)** — `dig +short A|AAAA|CNAME|MX|TXT|NS <domain>`, `dig +short CAA`, `whois`/RDAP for expiry & registrar: ownership under the business (not a freelancer/intern account), auto-renew on, registrar MFA, transfer lock, DNS provider access/MFA, apex + `www` both resolve and one redirects to the canonical, no orphaned records (pointing to deleted Vercel projects/Netlify/etc. → takeover risk), TTL sensible before cutover, DNSSEC if supported, **email auth for any sending domain**: SPF single record and within 10 lookups, DKIM selector present, DMARC policy (start `p=none` → `quarantine`/`reject`), MX correct.
3. **SSL/TLS (52)**: `curl -vI https://domain` / `openssl s_client -connect domain:443 -servername domain`: valid chain, expiry, SAN covers apex+www+subdomains, TLS ≥1.2, HTTP→HTTPS redirect, HSTS (and `includeSubDomains`/preload only with intent), no mixed content, third-party/API/webhook endpoints HTTPS, auto-renew mechanism (Vercel-managed vs custom) and monitoring.
4. **Vercel config (53)**: project/team ownership and seats (ex-members removed), Git connection and **production branch**, root directory, framework preset, build/install commands, Node.js version (matches `engines`/local), env vars per environment (Production/Preview/Development) with correct values and no secrets marked public, custom domains + verification, deployment protection for previews (Standard/Password/Vercel Auth), `vercel.json` (headers, redirects, crons, functions), firewall/WAF/Attack Challenge Mode, spend management & usage alerts, Analytics/Speed Insights, log drains, deployment history and **instant rollback**, production promotion procedure, notifications.
5. **Env config (54)**: reconcile three lists — variables used in code (inventory), variables in `.env.example`/docs, variables set in each environment. Flag missing, unused, mis-scoped (secret as `NEXT_PUBLIC_`), identical prod/dev values (dataset!), fallbacks that hide misconfiguration (`process.env.X || 'dev-value'`), absent runtime validation (fail fast at startup, e.g. zod env schema), configuration drift.
6. **Deployment strategy (55)**: branch → preview → review → production flow, who can deploy, required checks, atomic deployments, concurrency/cancellation, release tags/notes, hotfix and **emergency rollback** procedure (documented and *tested*), post-deploy verification (smoke test), notifications.
7. **Production launch config (56)**: run through: production domain; production Sanity dataset and CORS origins; API endpoints; env vars; analytics/consent; monitoring; redirects (old URLs → new); robots/sitemap/metadata for the production host; error pages; cache settings; security headers; third-party prod keys (maps referrer restriction, email domain verified, CAPTCHA domains); form recipients; image delivery; preview isolation; ownership of every account.

## Calibration
- Domain at a personal/former-contractor account without MFA, or expiring < 30 days with no auto-renew → High.
- Preview deployments public and using production dataset write token → High–Critical.
- Dangling CNAME to unclaimed service → High (takeover).
- Missing DMARC for a domain that sends form emails → Medium.
- Hobby plan on a commercial site → Medium (terms/limits), confirm with owner.
- No tested rollback → Medium–High depending on launch risk.

## Output
Infrastructure register (account · owner · MFA · plan · limits), DNS table (record · value · purpose · risk), TLS report, env reconciliation table, deploy/rollback procedure review, launch checklist state, findings (`INFRA-NNN`).

## Pitfalls
Changing DNS to "test" · trusting that the dashboard matches the repo · forgetting preview env · leaving TTL high before a cutover · verifying SPF without counting lookups.
