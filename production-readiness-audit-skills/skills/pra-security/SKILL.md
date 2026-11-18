---
name: pra-security
description: Security audit for Next.js/Sanity/Vercel web projects - secrets and credential exposure, NEXT_PUBLIC misuse, authentication/authorization, API and route-handler security, input validation and output encoding (XSS, Portable Text, dangerouslySetInnerHTML), security headers/CSP/CORS/cookies, infrastructure and deployment security, preview exposure, supply chain. Use when the user asks for a security audit, "cek keamanan", "ada secret bocor?", pentest-style review (within authorized scope), OWASP review, header check, XSS/CSRF/SSRF/open-redirect checks, webhook signature review, or token/permission review. Covers audit domains 15-22.
---

# Security Posture (Domains 15–22)

Parent: `production-readiness-audit`. Authorization first: static review and read-only requests are default; active probing only within written scope (see master safety rules). Lists: `references/checklist.md`.

## Procedure
1. **Threat model (short)**: assets (CMS content, form submissions, tokens, admin access, brand reputation), actors (anonymous visitor, editor, ex-member, bot), trust boundaries (browser ↔ Next server ↔ Sanity ↔ email/other APIs), entry points (routes, handlers, webhooks, Studio, preview). Note abuse cases (spam via forms, scraping, preview leakage, webhook replay).
2. **Secrets & credentials (domain 16)**
   - `bash ../production-readiness-audit/scripts/secret-grep.sh <repo> --history` (prints locations only).
   - Inspect each `NEXT_PUBLIC_*`: anything secret-like or a **write-capable Sanity token** in client scope is Critical. Public Sanity project id/dataset are not secrets.
   - Check client bundle after build: `grep -R "sk_\|token" .next/static` (names/prefixes only) to confirm server-only values did not leak; check source maps are not exposing server code.
   - Rotation/expiry/scope: tokens should be least-privilege (read-only for rendering, separate preview token, separate write token only server-side/webhook). Ask owner for dashboard confirmation → otherwise Not Verifiable.
   - Logs/errors: no secrets or tokens in `console.*`, error responses, CI logs.
3. **AuthN/AuthZ (domain 17)** — only if auth exists (login, admin, dashboard, protected routes, Studio embedded in app). Verify authorization **server-side on every handler/action**, ownership checks (IDOR), session cookie flags (`HttpOnly`, `Secure`, `SameSite`), CSRF for cookie auth, rate limiting on login/reset, middleware matcher gaps (routes not covered), Draft Mode secret strength and redirect safety. If nothing exists, mark N/A with evidence but still review Sanity Studio and preview endpoints.
4. **API/route handlers/Server Actions (domain 18)**: inventory each (`app/api/**/route.ts`, `'use server'`). For each: method restriction, auth, schema validation (zod), size/time limits, rate limiting, error shape (no stack traces), CORS, SSRF (fetching user-supplied URLs), open redirects (`redirect(searchParams…)`), webhook **signature verification** and replay/idempotency (e.g. `@sanity/webhook` `isValidSignature`), mass assignment, logging without PII.
5. **Input/output (domain 19)**: server-side validation (client validation is UX only) · length/range/type limits · file upload type+size+MIME+filename · Portable Text/Markdown/HTML rendering path · every `dangerouslySetInnerHTML` source traced to sanitized input · URL fields (CMS-provided links) rejecting `javascript:`/`data:` · SVG handling · query/route param validation · JSON-LD injection (`</script>` escaping when serializing).
6. **Browser & HTTP (domain 20)**: `bash ../production-readiness-audit/scripts/check-headers.sh <url> / /some-page`. Evaluate HSTS, CSP (+`frame-ancestors`), `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, cookie flags, CORS, cache-control on sensitive responses, mixed content, info disclosure (`x-powered-by`). CSP must fit the real third parties (Sanity CDN, fonts, analytics, maps) — a copied-in strict CSP that breaks the site is also a finding.
7. **Infra & deployment security (domain 21)**: Vercel preview protection (are previews public and indexable? do they point at production data?), production-branch restrictions, env-var scoping per environment, deployment hooks, WAF/firewall/rate-limit, public source maps, debug/dev endpoints reachable in production, dangling DNS/subdomains. Mostly Not Verifiable without dashboard access — say so.
8. **Supply chain (domain 22)**: use data from `pra-dependencies-build-cicd`; add CVE reachability, malicious/typosquat review, install scripts, lockfile integrity, Actions pinning, SBOM if required.
9. Map to **OWASP Top 10 (2021)** and, where relevant, ASVS levels; state which categories were not testable.

## Calibration
| Condition | Severity |
|---|---|
| Live secret/write token in repo, history, or client bundle | Critical |
| Unauthenticated write/delete endpoint; auth bypass; stored XSS from CMS content | High–Critical |
| Reflected/DOM XSS exploitable | High |
| Previews publicly reachable and indexing/leaking drafts | High |
| Missing HSTS/CSP/Referrer-Policy on brochure site | Low–Medium |
| Form endpoint without rate-limit/spam control | Medium |
| `x-powered-by` disclosure | Low |
Rotation of exposed secrets is the owner's action: recommend, never execute.

## Output
Findings (`SEC-NNN`) with OWASP mapping, attack scenario in one sentence, evidence (masked), fix, verification step. Include a "not tested" list (e.g. active exploitation, WAF efficacy).

## Pitfalls
Declaring "secure" from a clean grep · printing secret values · running scanners against production without approval · demanding enterprise controls on a static brochure · ignoring that Studio/Preview are part of the attack surface.
