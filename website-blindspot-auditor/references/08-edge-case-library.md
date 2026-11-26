# Edge-Case and Scenario Library

Use relevant scenarios, not all scenarios. Tailor tests to the actual product, permissions, data, and environment. Test only in authorized environments; prefer synthetic data.

## 1. General interaction

- Empty, null, malformed, oversized, boundary, and unexpected input.
- Double click, repeated submit, rapid navigation, concurrent requests.
- Refresh, direct URL, browser back/forward, multiple tabs.
- Stale state, lost response, request timeout, connection interruption.
- Slow network, offline/reconnect, network switch, captive portal.
- Browser zoom, narrow viewport, low-end device, keyboard-only use.
- Autofill, password managers, translation extensions, ad blockers.
- Copy/paste, drag/drop, file picker cancel, print view.
- Session expiry while a form is open; resume after re-login.

## 2. Authentication and account lifecycle

- Expired or revoked session during an action.
- Logout in another tab/device; stale token still accepted.
- Password reset token reuse, expiry, enumeration, or wrong-account delivery.
- Account disabled/deleted while sessions remain active.
- Email/identity change and verification sequencing.
- Concurrent login or recovery requests; race between reset and login.
- Privilege change while a session is active; role cache not refreshed.
- MFA enroll/reset/recovery bypass or lockout.
- OAuth account linking to an existing email; provider email unverified.
- Invitation accepted after revocation or by the wrong account.
- Remember-me/device trust surviving password change.

## 3. Permissions and tenancy

- User changes object ID, tenant ID, or ownership reference.
- UI hides an action but endpoint remains reachable.
- Export, search, cache, background jobs, and storage enforce the same isolation.
- Admin/support impersonation and audit history.
- Role downgrade while a privileged action is in progress.
- Cross-tenant IDs in webhooks, emails, files, or signed URLs.
- Shared caches/CDN keys that omit tenant or user scope.
- API pagination/filtering leaks records outside the tenant.
- Service accounts or API keys with broader scope than intended.
- Deleted team member retains access through tokens, invites, or integrations.

## 4. Forms and uploads

- Empty, partial, invalid, repeated, and concurrent submissions.
- Server-side validation differs from client-side validation.
- Upload interrupted after server receives some/all data.
- Incorrect MIME type, misleading extension, huge file, unusual filename.
- Duplicate upload, orphaned object, inaccessible or public file URL.
- Retry after ambiguous success; duplicate record or double email.
- Parser failure, image decompression bomb, archive traversal, malicious SVG/HTML.
- Virus scan unavailable or asynchronous; file accessible before scan.
- Quota exceeded during upload; partial file left behind.
- Delete/replace does not remove old object or cached derivative.

## 5. Payments and commerce

Use sandbox/test systems only unless production testing has explicit authorization.

- Duplicate checkout, duplicate webhook, late webhook, out-of-order event.
- Payment accepted but order update fails, or vice versa.
- Amount/currency mismatch, rounding, stale cart price, discount edge cases.
- Payment pending, declined, timed out, refunded, disputed, partially refunded.
- Inventory changes during checkout; two buyers compete for last item.
- Subscription renewal, cancellation, grace period, plan downgrade, failed renewal.
- Coupon stacking, reuse, expiry, minimum-spend, and product-scope bypass.
- Tax/shipping recalculated after quote; jurisdiction mismatch.
- Guest checkout order lookup via guessable identifiers.
- Refund/chargeback does not revoke entitlement or restore stock.
- Fulfillment retried after partial success; duplicate shipment.
- Test/live keys mixed across environments.

## 6. Booking and scheduling

- Two users reserve the same final slot.
- Hold expires during checkout.
- Timezone mismatch, daylight-saving transition, midnight boundary.
- Reschedule/cancel race, duplicate booking, partial refund.
- Capacity changes after availability was displayed.
- Recurring event exception/override mishandled.
- No-show/late-cancel policy applied inconsistently.
- Reminder or confirmation sent at the wrong local time.
- Calendar sync duplicates or resurrects cancelled events.
- Waitlist promotion after slot already taken.

## 7. Content and CMS

- Missing optional/required field, empty rich text, malformed reference.
- Draft accidentally exposed; preview bypass or stale preview.
- Published document deleted or slug changed without redirect.
- Schema change while old content remains.
- Cache/CDN/search index not invalidated.
- Broken internal reference or unavailable asset.
- Content contains unsafe markup or untrusted embedded media.
- Localized content falls back to the wrong language or mixes locales.
- Scheduled publish fails silently or publishes twice.
- Editorial workflow: reviewer can publish without approval, or approval is not recorded.

## 8. Search and pagination

- Empty query, special characters, very long query, regex-like input.
- No results, huge result set, duplicate records.
- Pagination while records are inserted/deleted; cursor invalidation.
- Sorting tie, unstable order, page drift.
- Access filtering after search; counts reveal hidden records.
- Search index stale compared with source of truth.
- Synonym/typo tolerance changes ranking for critical queries.
- Filter combinations produce impossible or empty states.

## 9. Background work and notifications

- Job runs twice, never runs, runs late, or is retried after partial success.
- Poison message, ordering change, queue backlog, dead-letter recovery.
- User unsubscribes while notification is queued.
- Email/SMS provider accepts request but downstream delivery fails.
- Scheduled event crosses timezone or daylight-saving boundary.
- Worker deploys with old code against new data.
- Queue visibility timeout shorter than job duration; duplicate processing.
- Cancellation requested but job continues and applies side effects.

## 10. Email and SMS deliverability

- SPF/DKIM/DMARC misconfiguration; mail lands in spam.
- Transactional and marketing streams mixed; unsubscribe suppresses critical mail.
- Bounce/complaint handling missing; repeated sends to invalid addresses.
- Link tracking rewrites break deep links or tokens.
- Email rendered differently in clients; plain-text fallback missing.
- Sensitive content in subject/preview or forwarded messages.
- Rate limits/provider outage; no retry or fallback.
- Unsubscribe link expired, one-click missing, or applies to wrong scope.
- Notification sent to the wrong recipient after account/email change.

## 11. Data and migration

- Unique conflict under concurrency.
- Partial migration, interrupted deploy, rollback after schema change.
- Legacy/null values not handled by new code.
- Deletion leaves related data in storage, analytics, cache, or search.
- Backup exists but restore has not been demonstrated.
- Migration ordering across services; old code reads new schema.
- Data export incomplete or includes unauthorized records.
- Import duplicates records or maps enums incorrectly.
- Timezone/precision truncation changes historical reports.
- Soft-deleted rows still counted or exposed.

## 12. Analytics and privacy

- Event fires twice or before the action succeeds.
- Client-side route change drops page-view event.
- Consent denied or withdrawn; events still sent.
- Sensitive values enter URL, analytics payload, logs, or error reporting.
- Ad blockers or network failures alter measurement behavior.
- Server/client events disagree on revenue or conversion.
- User deletion does not propagate to analytics/CRM.
- Event schema change breaks dashboards silently.
- Attribution window/cross-device behavior misread as a bug.

## 13. Reliability, operations, and deployment

- Third-party provider slow, unavailable, rate-limited, or schema-changed.
- Missing environment variable or wrong environment binding.
- Secret rotation, expired certificate/token, quota exhaustion.
- Logging/alerting absent for a failed critical workflow.
- Deployment succeeds but migration, worker, cache, or webhook configuration fails.
- Rollback after irreversible data change.
- Health check passes while dependencies are degraded.
- Disk/memory/connection exhaustion; retry storms.
- Runbook missing or ownership unclear during an incident.
- Time sync/clock skew affects tokens, signatures, or schedules.

## 14. Caching, CDN, and version skew

- Personalized/authenticated content cached publicly.
- Cache key omits tenant, locale, currency, or experiment variant.
- Publish/update does not invalidate CDN or ISR cache.
- HTML cached longer than hashed assets; stale price/content.
- Old and new deployments coexist; API/event payload incompatible.
- Service worker serves old shell against new API.
- Open tab requests deleted chunk after deploy.
- Preview/staging cache shared with production.
- Cache purge fails silently; stale content persists.
- CDN geo/language redirect loops.

## 15. Internationalization, timezone, and currency

- Locale fallback shows wrong language or mixed translations.
- Pluralization, gender, and grammar rules break in some locales.
- Date/time formatting differs between display, API, and storage.
- Timezone stored without offset; DST creates duplicate/missing slots.
- Currency minor units/rounding differ; conversion applied twice.
- Tax-inclusive vs exclusive pricing differs by market.
- Address/phone/postal-code validation assumes one country.
- Right-to-left layout, text expansion, and font fallback break UI.
- Sorting/collation differs by locale.
- Translation keys missing or leaking internal identifiers.

## 16. Accessibility and assistive technology

- Keyboard trap or unreachable control; focus lost after dialog closes.
- Focus order does not match visual order; skip link missing.
- Dynamic updates not announced; errors not associated with fields.
- Low contrast, color-only meaning, zoom/reflow failure.
- Touch targets too small; hover-only interactions.
- Motion without reduced-motion alternative; autoplay media.
- Captions/transcripts missing; alt text misleading.
- Custom widgets lack roles/states; screen reader reads duplicate labels.
- Accessible name changes after state change without announcement.
- PDF/export loses tags, reading order, or form labels.

## 17. Mobile, webview, and deep links

- Deep link opens wrong screen when unauthenticated or after logout.
- Universal/app links conflict between web and app.
- Webview lacks cookies/storage; login loop.
- Back button exits flow or loses state.
- Push notification opens stale/deleted content.
- Camera/file permissions denied; no fallback.
- Background/foreground transition loses in-progress payment or form.
- Mobile keyboard obscures input/CTA; viewport resize breaks layout.
- App version older than API; forced update missing.
- Shared link preview leaks private content.

## 18. AI and model features

- Indirect prompt injection via retrieved document, web page, email, or upload.
- Model reveals system prompt, tool schema, or another tenant's data.
- Tool call authorized by the model instead of the application.
- Model output rendered as HTML, executed, or trusted for pricing/eligibility.
- Cross-tenant RAG/memory leakage; retrieval filter missing.
- PII/prompts logged or sent to provider without consent/retention review.
- No token/cost cap; retry/agent loop duplicates side effects.
- Provider timeout/rate limit; partial stream or silent fallback.
- Model/prompt version changed without re-running evals.
- High-stakes answer presented without uncertainty or human review.
- Uploaded content poisons future answers; deletion not propagated.
- Citation/source does not support the generated claim.

## 19. Integrations, APIs, and webhooks

- Webhook unsigned, replayable, or trusting payload fields for authorization.
- Duplicate/out-of-order events; retry after partial success.
- API version change breaks old clients silently.
- Pagination/cursor invalidation; rate limit headers inaccurate.
- SSRF through callback/fetch URL; allowlist bypass.
- OAuth scope broader than needed; token leakage in logs/URLs.
- Third-party outage handled as success or infinite retry.
- Sandbox/production endpoint mismatch.
- Integration deletes/overwrites data without reconciliation.
- Export/import mapping loses required fields.

## 20. Abuse, rate limits, and quotas

- Limit enforced per IP only; bypass via headers, accounts, or keys.
- Concurrent requests exceed quota due to race.
- Expensive endpoint unauthenticated or under-authenticated.
- Enumeration via timing, error text, or IDs.
- Spam/automation through forms, invites, comments, or AI features.
- File/url fetch used for SSRF or resource exhaustion.
- Coupon/referral/trial abuse across accounts.
- Quota exhausted silently; paid user downgraded without notice.
- Admin bulk action used to trigger mass email or deletion.

## 21. Admin, support, and operations

- Support impersonation without consent, scope limit, or audit trail.
- Bulk actions partially succeed; no preview/undo/per-item result.
- Admin can change data that bypasses business rules.
- Export includes fields or tenants the operator should not see.
- Destructive action lacks confirmation, soft delete, or recovery.
- Role assignment errors grant excess privilege.
- Manual override not reconciled with automated state.
- Incident tooling cannot identify affected users/orders.
- Audit log can be edited/deleted by the actor it records.

## 22. Business claims and legal surface

- Marketing claim (price, guarantee, security, compliance) contradicted by behavior.
- Pricing page, checkout, invoice, and terms disagree.
- Cancellation/refund policy not reflected in product flows.
- Consent copy differs from actual data use.
- Required disclosures missing for the jurisdiction/audience.
- Asset/media/font license incompatible with usage.
- Age-gated or regulated content reachable without checks.
- Deletion/export promise not implemented end-to-end.
- Testimonials/statistics unsupported or stale.
- Affiliate/referral disclosure missing.
