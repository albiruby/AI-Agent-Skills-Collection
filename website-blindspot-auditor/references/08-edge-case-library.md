# Edge-Case and Scenario Library

Use relevant scenarios, not all scenarios. Tailor tests to the actual product, permissions, data, and environment.

## General interaction

- Empty, null, malformed, oversized, boundary, and unexpected input.
- Double click, repeated submit, rapid navigation, concurrent requests.
- Refresh, direct URL, browser back/forward, multiple tabs.
- Stale state, lost response, request timeout, connection interruption.
- Slow network, offline/reconnect, network switch.
- Browser zoom, narrow viewport, low-end device, keyboard-only use.

## Authentication and account lifecycle

- Expired or revoked session during an action.
- Logout in another tab/device.
- Password reset token reuse/expiry.
- Account disabled/deleted while sessions remain active.
- Email/identity change and verification sequencing.
- Concurrent login or recovery requests.
- Privilege change while a session is active.

## Permissions and tenancy

- User changes object ID, tenant ID, or ownership reference.
- UI hides an action but endpoint remains reachable.
- Export, search, cache, background jobs, and storage enforce the same isolation.
- Admin/support impersonation and audit history.
- Role downgrade while privileged action is in progress.

## Forms and uploads

- Empty, partial, invalid, repeated, and concurrent submissions.
- Server-side validation differs from client-side validation.
- Upload interrupted after server receives some/all data.
- Incorrect MIME type, misleading extension, huge file, unusual filename.
- Duplicate upload, orphaned object, inaccessible or public file URL.
- Retry after ambiguous success.

## Payments and commerce

Use sandbox/test systems only unless production testing has explicit authorization.

- Duplicate checkout, duplicate webhook, late webhook, out-of-order event.
- Payment accepted but order update fails, or vice versa.
- Amount/currency mismatch, rounding, stale cart price, discount edge cases.
- Payment pending, declined, timed out, refunded, disputed, partially refunded.
- Inventory changes during checkout; two buyers compete for last item.
- Subscription renewal, cancellation, grace period, plan downgrade, failed renewal.

## Booking and scheduling

- Two users reserve the same final slot.
- Hold expires during checkout.
- Timezone mismatch, daylight-saving transition, midnight boundary.
- Reschedule/cancel race, duplicate booking, partial refund.
- Capacity changes after availability was displayed.

## Content and CMS

- Missing optional/required field, empty rich text, malformed reference.
- Draft accidentally exposed; preview bypass or stale preview.
- Published document deleted or slug changed.
- Schema change while old content remains.
- Cache/CDN/search index not invalidated.
- Broken internal reference or unavailable asset.
- Content contains unsafe markup or untrusted embedded media.

## Search and pagination

- Empty query, special characters, very long query.
- No results, huge result set, duplicate records.
- Pagination while records are inserted/deleted.
- Sorting tie, cursor invalidation, access filtering after search.
- Search index stale compared with source of truth.

## Background work and notifications

- Job runs twice, never runs, runs late, or is retried after partial success.
- Poison message, ordering change, queue backlog, dead-letter recovery.
- User unsubscribes while notification is queued.
- Email/SMS provider accepts request but downstream delivery fails.
- Scheduled event crosses timezone or daylight-saving boundary.

## Data and migration

- Unique conflict under concurrency.
- Partial migration, interrupted deploy, rollback after schema change.
- Legacy/null values not handled by new code.
- Deletion leaves related data in storage, analytics, cache, or search.
- Backup exists but restore has not been demonstrated.

## Analytics and privacy

- Event fires twice or before the action succeeds.
- Client-side route change drops page-view event.
- Consent denied or withdrawn.
- Sensitive values enter URL, analytics payload, logs, or error reporting.
- Ad blockers or network failures alter measurement behavior.

## Reliability and operations

- Third-party provider slow, unavailable, rate-limited, or schema-changed.
- Missing environment variable or wrong environment binding.
- Secret rotation, expired certificate/token, quota exhaustion.
- Logging/alerting absent for a failed critical workflow.
- Deployment succeeds but migration, worker, cache, or webhook configuration fails.
