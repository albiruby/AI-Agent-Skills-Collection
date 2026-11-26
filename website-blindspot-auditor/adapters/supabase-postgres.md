# Adapter: Supabase and PostgreSQL

## Purpose

Inspect applications backed by Supabase or PostgreSQL. Focus on row-level security, tenant isolation, authentication and session behavior, storage policies, edge functions, migrations, constraints, query behavior, and operational recovery.

The adapter covers two related cases: a Supabase project (auth, database, storage, realtime, edge functions) and direct PostgreSQL access behind a custom backend.

## Detection signals

- `@supabase/supabase-js`, `supabase/` directory, `config.toml`, migrations, seed files.
- `NEXT_PUBLIC_SUPABASE_*` or similar client configuration.
- RLS policies, `auth.users`, `storage.objects`, `pg_policies`, `security definer` functions.
- Edge functions (`supabase/functions/`), realtime subscriptions, storage buckets.
- PostgreSQL connection strings, ORM models/migrations (Prisma, Drizzle, Knex, raw SQL).
- Supabase CLI or dashboard configuration.

False positives: a project may use PostgreSQL without Supabase; apply the database portions only. A Supabase anon key in the browser is expected; a service-role key is not.

## Applicability

Load when the target uses Supabase or PostgreSQL for application data, authentication, storage, or realtime behavior.

For static sites with no database, mark database domains Not Applicable. For a CMS that abstracts the database, inspect the CMS layer first and use this adapter only for direct database access or custom SQL.

## Boundaries and data flows

1. Browser/client ↔ Supabase API (PostgREST, auth, storage, realtime).
2. Client or server ↔ edge function ↔ database/external service.
3. Application server ↔ PostgreSQL (connection pool, ORM, raw SQL).
4. Auth provider ↔ session/JWT ↔ authorization claims.
5. Storage bucket ↔ object metadata ↔ application access.
6. Realtime channel ↔ RLS-filtered rows ↔ subscribers.
7. Migration tooling ↔ live schema ↔ deployed application version.
8. Backups/PITR ↔ restore process ↔ retention policy.

Identify the role used by each path: anonymous, authenticated user, service role, or a custom database role. Authorization depends on which role actually executes the query.

## Audit procedures

### A. Row-level security and tenant isolation

- Confirm RLS is enabled on every table exposed through the API, including new tables.
- Inspect each policy: command (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), roles, `USING`, and `WITH CHECK`.
- Check whether `WITH CHECK` is missing, allowing writes that the policy later hides.
- Check ownership predicates: `auth.uid()`, tenant IDs, membership tables, and joins. Verify they cannot be bypassed by client-supplied values.
- Inspect views and functions marked `security definer`; they can bypass RLS if grants and search paths are unsafe.
- Check `anon` and `authenticated` grants on tables, views, functions, and sequences.
- Verify realtime subscriptions respect RLS and do not leak rows across users/tenants.
- Check storage bucket policies for read, insert, update, delete, and public access.

### B. Authentication and sessions

- Review signup, email confirmation, password reset, magic links, OAuth, MFA, and account linking.
- Check redirect URLs and allowed origins for auth flows.
- Verify session refresh, logout, revocation, and behavior after role/tenant changes.
- Check whether protected routes rely on client-side checks or JWT claims that are not revalidated server-side.
- Verify admin/support access and service-role usage are server-only and audited.
- Check auth triggers and database functions that create profiles/tenants for failure modes and privilege mistakes.

### C. Data integrity and schema

- Check primary keys, foreign keys, unique constraints, not-null constraints, and check constraints.
- Verify money, quantity, status, and ownership fields have appropriate types and constraints.
- Check transactions around multi-step writes; look for partial updates.
- Check concurrency: unique conflicts, upserts, race conditions, and lost updates.
- Check soft-delete semantics and whether deleted rows remain accessible through other paths.
- Inspect migrations for destructive changes, lock-heavy operations, and rollback compatibility.
- Verify the repository schema matches the live schema; drift is a risk, not automatically a defect.

### D. Queries, performance, and operations

- Look for N+1 queries, missing indexes on frequent filters/joins, and unbounded result sets.
- Check pagination correctness and access filtering after fetch.
- Inspect long-running queries, lock contention, and connection-pool limits.
- Check backup/PITR configuration and whether restore has been demonstrated.
- Review logs for errors, slow queries, auth failures, and unusual access patterns.
- Check database roles, network exposure, SSL requirements, and credential rotation.

### E. Edge functions and integrations

- Verify authentication and authorization inside each function; do not rely on the caller.
- Check input validation, SSRF, secret handling, timeout, retries, and idempotency.
- Check service-role usage: it bypasses RLS, so every query must enforce tenant/user scope explicitly.
- Check webhook endpoints for signature verification and replay protection.
- Check function logs for sensitive data leakage.

## Verification methods

- Static inspection of migrations, policies, functions, client queries, and edge functions.
- Read-only SQL with `SET default_transaction_read_only = on;` and `LIMIT`.
- Supabase CLI/dashboard inspection with authorized read-only credentials.
- Browser inspection of authenticated flows using test accounts; attempt cross-tenant access only in an authorized test environment.
- Log inspection for auth failures, policy denials, and slow queries.

## Common failure modes

- RLS disabled on a table added after launch.
- Policy `USING (true)` on sensitive data or missing `WITH CHECK` on writes.
- `security definer` function/view bypassing RLS with broad grants.
- Service-role key shipped to the client or used in a function without scoping.
- Storage bucket public when it should be private, or policies allowing cross-user access.
- Realtime subscription leaking rows because RLS is absent or too broad.
- Auth redirect/origin misconfiguration enabling token or session leakage.
- Missing unique constraint causing duplicate orders/memberships.
- Migration drift or destructive migration without rollback.
- Missing FK/index causing orphaned data or slow queries.
- Backup configured but restore never tested.

## Evidence requirements

- For RLS findings: table, policy, role, command, predicate, and the actor/data path that bypasses the intended boundary.
- For auth findings: flow, token/session behavior, and the condition under which access is granted incorrectly.
- For integrity findings: schema/constraint, write path, and the resulting duplicate/orphan/partial state.
- For secret exposure: key type and location, never the key value. An anon key alone is not a finding.

A policy that looks broad may be constrained by another layer; verify the actual exposed API and role before claiming a bypass.

## Safety constraints

- Use read-only SQL; never run writes, migrations, or schema changes during an audit.
- Do not use service-role credentials unless explicitly provided for a scoped, authorized task.
- Do not test cross-tenant access against production.
- Do not print keys, tokens, connection strings, or personal data.
- Do not run load tests or unbounded queries on production.

## Related modules

- `adapters/nextjs-vercel.md` for server/client boundaries and secret exposure.
- `adapters/ecommerce-and-payments.md` for order/inventory integrity.
- `references/07-cross-layer-analysis.md` for auth/storage/realtime boundaries.
- `references/08-edge-case-library.md` for tenancy and data lifecycle scenarios.
