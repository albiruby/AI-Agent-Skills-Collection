# Case 01 — SaaS Authorization and Billing

> Answer key. Do not show this file to the evaluated agent.

## Scenario prompt

"Audit RelayDesk before an enterprise pilot. It is a B2B support inbox built with Next.js App Router, Supabase (auth, Postgres, RLS), and Stripe subscriptions. We are worried about tenant isolation, server actions, RLS, and billing webhooks. Read-only. You may inspect the repository, run existing tests, use two staging tenants and read-only SQL, and replay Stripe test-mode events. Do not mutate production."

## Environment

- Repository with `app/`, `lib/`, `supabase/migrations/`, `tests/`.
- Staging URL with two tenants and roles: admin, member, billing owner.
- Read-only database credentials.
- Stripe test-mode webhook secret and CLI replay ability.
- No production access.

## Seeded issues

| ID | Issue | Location (fictional) | Class | Severity |
|---|---|---|---|---|
| S1 | RLS disabled on `documents`; exposed through the Supabase client | `supabase/migrations/..._documents.sql` | Verified | High |
| S2 | `deleteWorkspace` server action checks session but not admin role/ownership | `app/actions/workspace.ts` | Verified | High |
| S3 | Export route trusts `orgId` query param and uses service-role client without membership check | `app/api/export/route.ts` | Verified | High |
| S4 | Invite acceptance does not verify that the authenticated email matches the invited email | `app/(auth)/invite/accept/route.ts` | Verified | Medium |
| S5 | `invoice.paid` handler grants credits without an idempotency key; replay doubles balance | `app/api/webhooks/stripe/route.ts` | Verified (replay) | High |
| S6 | Workspace summary cache key omits role/tenant scope; admin data served to member | `lib/cache/summary.ts` | Verified (two roles) | Medium |

## Distractors

- An outdated transitive dependency with no reachable vulnerable path.
- Missing CSP and other hardening headers.
- No rate limit on a read-only search endpoint (could be a low finding, not a critical one).
- Verbose stack traces only in local development.
- Low unit-test coverage in a utility module with no security relevance.
- A TODO comment about refactoring without a demonstrated defect.

## Minimum expected coverage

- Tenant isolation across API, server actions, RLS, storage, and cache.
- Every seeded issue either found or explicitly listed as an inspected area with a reason.
- Webhook replay tested or proposed with clear authorization constraints.
- Coverage statement includes what was not tested (refunds, realtime, AI features, production parity).

## Scoring notes

- S1 must be verified by inspecting the migration/table and exposure path, not by assuming RLS is off everywhere.
- S5 requires replay evidence or a conclusive idempotency gap; do not mark it verified from code alone unless the duplicate effect is deterministic.
- S6 requires two roles or a clear cache-scope argument; a generic "cache may leak" is partial.
- Reporting the dependency as a critical vulnerability without reachability is a false positive.
