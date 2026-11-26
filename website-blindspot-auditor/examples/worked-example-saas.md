# Worked Example: SaaS Audit (Fictional)

This example shows the expected depth and evidence discipline. The product, code, and findings are fictional. Use it to calibrate report quality, not as a checklist for real code.

## Scenario

**Request:** "Audit LumenDesk before our enterprise pilot. We use Next.js on Vercel, Supabase for auth/data, and Stripe for billing. We are worried about tenant isolation and billing edge cases. Read-only; staging access is allowed."

**Mode:** Deep Audit, narrowed by the request to security, tenancy, billing, and their adjacent flows.

**Authorization:** Read repository, run existing tests, inspect staging with two test tenants, read-only SQL, read Stripe test-mode events. No production mutation, no live charges, no load tests.

## 1. Context reconstructed

- Product: B2B support inbox with shared workspaces, seats, and AI-assisted replies.
- Actors: anonymous visitor, invited member, workspace admin, billing owner, support impersonator, platform operator.
- Stack: Next.js App Router, server actions, Supabase auth/Postgres/RLS, Stripe subscriptions, Vercel cron, Resend email.
- Critical journeys: signup/invite → workspace access → inbox actions → plan upgrade → seat change → cancellation → data export/deletion.
- Invariants:
  - A member sees only workspaces they belong to.
  - A paid entitlement is active only while the subscription is entitled, including grace/cancel boundaries.
  - One Stripe invoice event must not grant credits twice.
  - Removing a member revokes access in UI, API, realtime, exports, and background jobs.

## 2. Domains and adapters selected

| Domain | Why | Depth |
|---|---|---|
| Security/privacy | Multi-tenant B2B data | Deep |
| Data integrity/lifecycle | Seats, entitlements, webhooks | Deep |
| Functional journeys | Invite/upgrade/cancel/export | Deep |
| Reliability/operations | Cron, webhook retries, deploy skew | Medium |
| Analytics | Billing/seat events | Light |
| Accessibility/content/SEO | Marketing surface | Light |

Adapters: `nextjs-vercel`, `supabase-postgres`, `ecommerce-and-payments` (subscription scope), `ai-enabled-product` (light, for the reply assistant).

## 3. Findings

### LD-001 — Tenant ID accepted from the request in the export route

- **Class:** Verified Finding
- **Severity:** High · **Confidence:** High
- **Location:** `app/api/workspaces/[id]/export/route.ts:18`
- **Evidence:** The route reads `workspaceId` from the URL and queries with the service-role client. It checks `session.user` exists but never verifies membership or that the workspace belongs to the caller's organization.
- **Expected:** Export is limited to workspaces the authenticated member can access.
- **Observed:** Any authenticated user can supply another workspace ID and receive its export.
- **Impact:** Cross-tenant data disclosure of tickets, customer emails, and internal notes.
- **Verification:** In staging, authenticated as tenant A and requested tenant B's export with tenant B's ID; response contained tenant B rows (redacted).
- **Recommendation:** Derive tenant/workspace from the session and enforce membership in the query; add an integration test with two tenants. Do not rely on the service-role client for authorization.
- **Acceptance criteria:** A member of tenant A receives 403/404 for tenant B export; test covers both roles; no service-role query without an explicit tenant predicate.
- **Regression risk:** Export performance may change if the membership join is inefficient; verify query plan.
- **Remaining uncertainty:** None for the staging path; production parity assumed.

### LD-002 — Workspace summary cache key omits tenant

- **Class:** Verified Finding
- **Severity:** High · **Confidence:** High
- **Location:** `lib/cache/workspace-summary.ts:12`
- **Evidence:** `unstable_cache` wraps a summary fetch with key `["workspace-summary", workspaceId]`, while the fetch itself uses a session-scoped client. The cache is shared across requests, and the key does not include the user or role.
- **Expected:** Cached summaries are scoped to the workspace and the permission context that produced them.
- **Observed:** In staging, a summary generated for an admin was served to a restricted member after cache warm-up.
- **Impact:** Hidden counts, customer names, or admin-only metrics could leak to lower-privileged members.
- **Verification:** Two test users, same workspace, different roles; second request returned cached admin values.
- **Recommendation:** Include the authorization scope in the key or cache only non-sensitive, role-independent data; invalidate on membership/role changes.
- **Acceptance criteria:** Restricted member never sees admin-only fields; cache test covers role change and membership revocation.
- **Regression risk:** More cache misses; measure before/after.
- **Remaining uncertainty:** Whether production cache configuration matches staging; verify.

### LD-003 — Stripe invoice webhook is not idempotent

- **Class:** Verified Finding
- **Severity:** High · **Confidence:** Medium
- **Location:** `app/api/webhooks/stripe/route.ts:41`
- **Evidence:** On `invoice.paid`, the handler inserts a credit ledger row and increments the workspace balance. There is no unique constraint on `stripe_invoice_id`, and the handler returns 200 even when the insert fails.
- **Expected:** A repeated delivery of the same invoice event grants credits once and reports failure for retry when processing fails.
- **Observed:** Replaying the same test-mode event twice created two ledger rows and doubled the balance in staging.
- **Impact:** Customers can receive duplicate credits; reconciliation and revenue reporting diverge.
- **Verification:** Stripe CLI replay in test mode against staging; ledger query before/after.
- **Recommendation:** Add a unique key on the provider event/invoice ID, make the handler transactional, and return non-2xx on failure so the provider retries. Add a reconciliation job for orphaned events.
- **Acceptance criteria:** Replaying the same event produces one ledger row; failed processing returns an error; duplicate delivery test passes.
- **Regression risk:** Retries may surface previously hidden failures; monitor webhook error rate after release.
- **Remaining uncertainty:** Whether other event types share the same handler pattern; audit adjacent events.

### LD-004 — Cancellation does not revoke AI reply entitlement everywhere

- **Class:** Potential Risk
- **Severity:** Medium · **Confidence:** Medium
- **Location:** `lib/entitlements.ts:27`, `app/api/ai/reply/route.ts:12`
- **Evidence:** The UI and dashboard check `plan.status === "active"`, but the AI reply route checks only `workspace.ai_enabled`, which is set at purchase and not updated on cancellation. The cancellation webhook updates the subscription row but not the workspace flag.
- **Expected:** AI features stop or degrade according to the cancellation/grace policy across all surfaces.
- **Observed:** Static trace shows the route would still allow AI replies after cancellation until another job updates the flag. The job exists but its schedule and failure handling were not verified.
- **Impact:** Continued paid-feature usage after cancellation; cost and entitlement mismatch.
- **Verification:** Static path trace; staging cancellation not performed because it would mutate test billing state beyond the authorized scope.
- **Recommendation:** Make entitlement checks derive from one authoritative subscription state; update or remove the denormalized flag. Add a post-cancellation test.
- **Acceptance criteria:** After cancellation/grace expiry, AI route denies or limits access; all surfaces agree; job failure is visible.
- **Regression risk:** Legitimate grace-period users could lose access prematurely; encode policy explicitly.
- **Remaining uncertainty:** Exact grace policy and job schedule.

### LD-005 — Member removal leaves realtime subscription active

- **Class:** Potential Risk
- **Severity:** Medium · **Confidence:** Medium
- **Location:** `lib/realtime/workspace-channel.ts:33`
- **Evidence:** The client subscribes to a workspace channel and authorization is checked when the channel is joined. Removing a member updates the membership table, but there is no channel eviction or token revocation; the existing subscription continues until reconnect.
- **Expected:** Removal revokes access to new events promptly.
- **Observed:** Not reproduced within the time box; Supabase realtime behavior with RLS and existing connections needs a staging test with two users.
- **Impact:** A removed member could continue receiving workspace events until their session/channel ends.
- **Recommendation:** Verify RLS on realtime rows, shorten token/channel lifetime, and trigger re-auth or disconnect on membership change.
- **Acceptance criteria:** Removed member stops receiving events within the documented window; test covers role change and removal.
- **Remaining uncertainty:** Provider behavior and current RLS policy on the realtime publication.

### LD-006 — Coverage gap: audit log writes bypass application checks

- **Class:** Coverage Gap
- **Severity:** Medium · **Confidence:** High (that coverage is missing)
- **Location:** `supabase/migrations/*_audit_logs.sql`, admin console
- **Evidence:** Audit-log inserts use a database trigger with `security definer`. The trigger was inspected, but the admin console's read path and retention job were not available in staging. No test covers log tampering or cross-tenant reads.
- **Impact:** Cannot conclude whether audit history is complete, tenant-scoped, or trustworthy.
- **Recommendation:** Add read-path tests and a retention/tamper review; verify grants on the definer function.
- **Acceptance criteria:** Cross-tenant read denied; trigger failure visible; retention verified.

### LD-007 — Opportunity: surface plan/seat limits before upgrade

- **Class:** Improvement Opportunity
- **Severity:** Informational · **Confidence:** Medium
- **Evidence:** Support macros and onboarding copy mention seat limits, but the invite screen only fails after submission. Three support threads in the provided sample describe the same confusion.
- **Expected benefit:** Fewer failed invites and support contacts; clearer upgrade path.
- **Effort:** Small.
- **Recommendation:** Show remaining seats and an upgrade CTA before the invite form; keep server enforcement unchanged.

## 4. Coverage excerpt

| Area | Status | Note |
|---|---|---|
| Tenant isolation | Verified gap | Found LD-001, LD-002; RLS policies otherwise sampled |
| Billing/webhooks | Verified gap | LD-003 reproduced; refunds not exercised |
| Entitlement | Partial | LD-004 static trace; cancellation mutation not authorized |
| Realtime | Blocked | LD-005 needs provider-level test |
| Admin/audit | Blocked | No admin staging access |
| AI assistant | Light | Prompt/tool authorization sampled; no adversarial testing |
| Marketing/SEO/a11y | Light | Not the focus of this request |

Coverage score: context 2, domain selection 2, journeys 1, cross-layer 2, security 2, money/identity 2, failure/recovery 1, execution 1, evidence 2, transparency 2. Main limitation: cancellation and realtime could not be exercised.

## 5. What a shallow audit would have missed

- The export route "looks protected" because it requires a session; the missing membership check is one line deeper.
- The cache key looks fine until you compare two roles in the same workspace.
- The webhook "works" in the happy path; only replay reveals duplicate credits.
- The entitlement flag looks authoritative until you trace cancellation across surfaces.
- Realtime removal looks handled by RLS until you consider already-open channels.

## 6. Lessons for the skill

- Always trace authorization to the data query, not to the presence of a session.
- Replay, duplicate, and role-change scenarios are high-yield for SaaS.
- A static trace can justify a Potential Risk but not a Verified Finding of runtime impact.
- Coverage gaps are first-class results when access is the limiting factor.
