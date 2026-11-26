# Read-Only Check Cookbook

Use this as a menu of safe inspection commands. It is not a script to run blindly. Discover the project's actual tooling and scripts first, and run only checks that fit the environment and authorization.

## 1. Rules

1. **Discover before running.** Read `package.json`, `Makefile`, `composer.json`, `pyproject.toml`, CI config, and documentation. Prefer the project's own scripts over invented commands.
2. **Stay read-only.** Do not run `install`, `update`, `migrate`, `deploy`, `seed`, `reset`, `fix`, or commands that write project state unless explicitly authorized.
3. **No network surprises.** Dependency audits, link crawls, and external checks may contact third parties. Confirm this is acceptable.
4. **Never print secrets.** When a scan matches a credential, report path/line and exposure risk, not the value.
5. **Bound output.** Use `--depth`, `--max-count`, `head`, and targeted paths. Do not dump `node_modules`, `.git`, build output, or full database tables.
6. **Record evidence.** Command, environment, timestamp, relevant output excerpt, and limitation.
7. **Stop on impact.** If a check causes unexpected load, state change, or errors, stop and report.

Placeholders: `TARGET_URL`, `REPO`, `SKILL_DIR`, `DB_URL`. Substitute only values provided or confirmed by the user.

## 2. Capability probe

Record what is actually available before relying on it:

```bash
git --version
node --version && npm --version
pnpm --version; yarn --version
php --version; composer --version
psql --version; supabase --version
docker --version
rg --version; jq --version
curl --version
npx playwright --version
npx lighthouse --version
```

A missing tool is a limitation, not a failure. Do not install it without permission.

## 3. Repository inventory

```bash
git -C REPO ls-files | head -200
git -C REPO log --oneline -20
git -C REPO status --short
```

Look for manifests, lockfiles, route definitions, schemas, migrations, CI workflows, environment examples, and infrastructure configuration:

```bash
rg --files REPO -g 'package.json' -g 'pnpm-lock.yaml' -g 'package-lock.json' -g 'yarn.lock'
rg --files REPO -g '*.sql' -g 'migrations/**' -g 'schema.prisma' -g 'drizzle/**'
rg --files REPO -g '.env*' -g '*.example' -g '*.sample'
rg --files REPO -g '.github/workflows/**' -g 'vercel.json' -g 'next.config.*' -g 'vite.config.*'
```

Use `Get-ChildItem -Recurse -File` and `Select-String` in PowerShell when `rg` is unavailable.

## 4. Existing checks and baseline

Read the scripts first, then run only safe ones:

```bash
cat package.json
cat Makefile
cat composer.json
```

Typical read-only checks, if the project defines them:

```bash
npm test
npm run lint
npm run typecheck
npm run build        # may write build output; confirm this is acceptable
```

For a first pass, prefer targeted test files over the full suite if the suite is slow, flaky, or touches external services.

## 5. Dependencies and secrets

Dependency inspection (may require network):

```bash
npm audit --omit=dev
pnpm audit --prod
composer audit
pip-audit            # only if already installed
```

Do not run `audit fix`, `update`, or upgrade commands during an audit.

Targeted secret scan on tracked files:

```bash
git -C REPO grep -nEI '(api[_-]?key|secret|token|password|private[_-]?key)[[:space:]]*[:=]' -- ':!*.lock' ':!*.min.js'
```

Treat matches as leads, not proof. Distinguish placeholders, test fixtures, public keys, and real credentials. Never print the matched value in the report.

## 6. HTTP, headers, cookies, and TLS

```bash
curl -sI TARGET_URL
curl -sI -X GET TARGET_URL
curl -s -D - -o /dev/null TARGET_URL
```

Check applicable headers:

- `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options`
- `Referrer-Policy`, `Permissions-Policy`, `X-Frame-Options` / `frame-ancestors`
- `Cache-Control` on authenticated or personalized responses
- CORS headers on API endpoints

Cookie flags: `Secure`, `HttpOnly`, `SameSite`, `Domain`, `Path`, expiry. Do not test session fixation or cookie tampering against production without authorization.

TLS/certificate observations are usually better checked with the provider's tooling or a read-only scanner the user authorizes.

## 7. Content, SEO, and links

```bash
curl -s TARGET_URL | head -100
curl -s TARGET_URL/robots.txt
curl -s TARGET_URL/sitemap.xml
```

Check title, meta description, canonical, robots directives, Open Graph, structured data, language attributes, and whether primary content exists in the initial HTML (or only after client-side rendering).

Link checking: crawl a bounded set of same-origin pages, use `HEAD` first, rate-limit requests, and record redirects separately from 404s. Do not crawl a production site aggressively or without permission.

## 8. Accessibility and performance

If tools are already available and the target is local/preview:

```bash
npx lighthouse TARGET_URL --only-categories=accessibility,performance --output=json --output-path=lighthouse.json
npx @axe-core/cli TARGET_URL
```

`npx` may download packages; confirm before use. Otherwise, perform a manual pass: keyboard-only navigation, focus visibility, labels, contrast, zoom/reflow, error identification, reduced motion, and screen-reader semantics where possible.

Performance observations should distinguish measured runtime data from source-level hypotheses. Never run load tests against production without explicit authorization.

## 9. Next.js / Vercel

Inspect:

- `app/` and `pages/` route trees; route handlers and server actions.
- `middleware.ts` matcher and what it actually protects.
- `next.config.*`: headers, redirects, rewrites, image domains, experimental flags.
- Cache behavior: `fetch` cache options, `revalidate`, `dynamic`, `fetchCache`, `unstable_cache`, route segment config.
- `NEXT_PUBLIC_*` usage; anything sensitive must not be client-visible.
- Server actions: authorization inside the action, not only in the UI; origin/CSRF assumptions.
- Preview/draft mode protection and environment separation.
- Error boundaries, loading states, streaming, and partial rendering failures.

```bash
rg -n "NEXT_PUBLIC_|revalidate|fetchCache|dynamic =|use server|middleware" REPO --glob '!node_modules/**' --glob '!.next/**'
```

Build output (`.next`) may be read for route and cache inspection, but do not deploy it.

## 10. WordPress / WooCommerce

Prefer WP-CLI read-only commands when available:

```bash
wp core version
wp plugin list --fields=name,status,version,update
wp theme list --fields=name,status,version,update
wp user list --fields=ID,user_login,roles --number=20
wp cron event list
wp option get home
```

Inspect custom code for:

- `current_user_can()` and capability checks, not only nonces.
- REST routes with `permission_callback` that always returns true or is missing.
- `$wpdb` queries with interpolation, unsafe `unserialize`, file uploads, and SSRF-prone integrations.
- Admin AJAX handlers and direct file access.
- Caching rules that could serve logged-in or personalized content to anonymous users.
- Exposed debug logs, backups, directory listings, and xmlrpc.

Do not install, update, deactivate plugins, or modify options during an audit.

## 11. E-commerce and payments

Review code and configuration for:

- Server-side price, tax, shipping, discount, and currency recomputation.
- Inventory reservation and concurrent checkout.
- Checkout/session idempotency and retry behavior.
- Webhook signature verification, replay protection, ordering, and duplicate delivery.
- Order/payment/fulfillment state machine and reconciliation.
- Refund, partial refund, dispute, cancellation, and subscription lifecycle.
- Sandbox vs live keys; never print either.
- Analytics purchase events and consent.

Use sandbox/test systems only. Do not send real charges, emails, or webhooks to production without explicit authorization.

## 12. Supabase and PostgreSQL

Supabase project inspection (read-only, authorized credentials only):

- Auth providers, redirect URLs, email confirmation, password policy, MFA.
- RLS enabled on every exposed table; policy `USING` and `WITH CHECK` coverage.
- Views and functions that bypass RLS (`security definer`) and their grants.
- Storage bucket policies and public/private access.
- Edge function authorization and service-role usage.
- Realtime subscriptions and row visibility.
- Migrations in the repository vs the live schema.

Read-only PostgreSQL checks:

```sql
SET default_transaction_read_only = on;
SELECT schemaname, tablename, rowsecurity FROM pg_tables WHERE schemaname = 'public';
SELECT schemaname, tablename, policyname, roles, cmd, qual, with_check FROM pg_policies;
SELECT conrelid::regclass, conname, contype FROM pg_constraint ORDER BY 1;
SELECT schemaname, tablename, indexname FROM pg_indexes WHERE schemaname = 'public';
```

Use `LIMIT`, avoid full-table scans on large tables, and never run writes, migrations, or schema changes during the audit.

## 13. Logs and runtime evidence

If logs or analytics are provided, query read-only and narrow:

- Error rate and top error signatures for critical workflows.
- Failed authentication/authorization events.
- Payment/webhook retries and dead letters.
- Background job failures, lag, and duplicate processing.
- Deployment timestamps and version overlap.
- Slow queries or timeouts for critical paths.

Redact user identifiers and sensitive payloads. Report patterns, not raw personal data.

## 14. Evidence capture

For each meaningful probe, record:

- Timestamp and environment.
- Command or action performed (with secrets removed).
- Expected result.
- Observed result (short excerpt or screenshot reference).
- What it proves and what it does not.
- Artifact location and hash if a file/screenshot is retained.

```bash
sha256sum evidence/file.json
```

Use `Get-FileHash` in PowerShell. Keep evidence under the agreed data-handling rules.

## 15. Commands requiring explicit authorization

Do not run these by default:

- `npm install`, `pnpm install`, `composer install`, dependency upgrades.
- Database writes, migrations, seeds, resets, or destructive queries.
- `git push`, deploy, rollback, or infrastructure changes.
- Payment charges, refunds, real emails/SMS, production webhook replays.
- Load, fuzz, brute-force, or denial-of-service tests.
- Production account testing or third-party scanning.
- Any command that changes files, data, permissions, or external state.

When in doubt, propose the check and ask for authorization, or provide a safe plan for the owner to run.
