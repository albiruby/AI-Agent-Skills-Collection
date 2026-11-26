# Project and Business Profiles

Profiles help prioritize scenarios. A project may match multiple profiles. Do not infer that a feature exists merely because it is common in that profile.

For each profile: prioritize the listed areas, then use the "highest-yield blind spots" as starting hypotheses, not as proven defects.

## Marketing / landing page

**Prioritize:** message clarity, CTA behavior, forms, accessibility, responsive layout, content accuracy, SEO, analytics, consent, performance, lead-delivery reliability.

**Highest-yield blind spots**

- Form submits successfully in the UI but the lead never reaches the destination (spam filter, wrong endpoint, silent API error).
- A/B test or CMS variant serves a different price/claim than the canonical page.
- Cookie/consent banner blocks or misreports conversions; analytics fires before consent.
- Preview/staging URL indexed or shared publicly.
- Mobile CTA overlaps chat widget/cookie banner; keyboard users cannot reach it.
- Thank-you page reachable directly, corrupting conversion measurement.

Do not spend time on account, payment, or database checks unless the page actually has them.

## Portfolio / personal site

**Prioritize:** content presentation, navigation, accessible media, project links, contact workflow, responsive layout, metadata, performance, privacy.

**Highest-yield blind spots**

- Contact form delivers to an unmonitored inbox or fails silently.
- External project links rot or point to staging/preview builds.
- Large media blocks interaction on low-end devices; no reduced-motion alternative.
- Personal data (email, phone, location) exposed more widely than intended.
- Domain/redirect changes break old links and social previews.

## Blog / publishing / documentation

**Prioritize:** editorial lifecycle, content integrity, drafts/publication, author attribution, canonical URLs, redirects, search, navigation, code/media rendering, indexing, localization, stale content.

**Highest-yield blind spots**

- Draft or scheduled content exposed by preview links, API, sitemap, or search index.
- Slug change without redirect; inbound links and analytics break.
- Search index stale after unpublish/delete.
- Code blocks or embedded content rendered unsafely.
- Documentation version drift: examples no longer match the current API.
- Translation fallback shows the wrong language or mixed metadata.

## E-commerce

**Prioritize:** catalog accuracy, prices/currency/tax, cart integrity, inventory races, promotions, checkout, payment state, webhooks, refunds, order lifecycle, shipping, customer data, post-purchase notifications.

**Highest-yield blind spots**

- Client-supplied price/discount accepted server-side.
- Duplicate order/charge on retry or double submit.
- Payment webhook processed twice or out of order; fulfillment state diverges.
- Inventory oversell at the last item under concurrency.
- Stale cart price after a price change or currency switch.
- Refund does not revoke access, restore stock, or adjust analytics.
- Guest order lookup exposes another customer's order.
- Test-mode payment keys in production or live keys in test.

Treat payment testing as high risk; use sandbox/test modes only with authorization.

## SaaS / subscription application

**Prioritize:** tenant isolation, account lifecycle, onboarding, entitlements, billing, usage metering, quotas, plan changes, cancellation, access enforcement, data export/deletion, background jobs, audit trails, operational visibility.

**Highest-yield blind spots**

- Entitlement checks cached or computed client-side; downgrade not enforced everywhere.
- Tenant ID from the request trusted instead of derived from session.
- Trial/grace-period boundaries inconsistent across billing, UI, API, and jobs.
- Seats/usage metering double-counts retries or shared sessions.
- Cancellation leaves access active in one surface (API, export, mobile, background job).
- Invite/member removal does not revoke sessions or cached permissions.
- Data export/deletion misses backups, search indexes, analytics, or object storage.
- Support impersonation lacks audit trail or scope limits.

## Marketplace

**Prioritize:** buyer/seller boundaries, listings, moderation, transaction lifecycle, commissions, payouts, disputes, messaging, fraud/abuse, inventory/availability, role conflicts.

**Highest-yield blind spots**

- Seller can read or modify another seller's orders/listings.
- Commission/fee calculation differs between display, charge, payout, and refund.
- Payout runs on an order state that can still be refunded/disputed.
- Buyer and seller see different authoritative order statuses.
- Messaging or review features enable spam, harassment, or off-platform payment scams.
- Listing moderation bypass via edits, duplicates, or API.
- Dispute resolution lacks evidence trail or reversible actions.

## Booking / reservation / scheduling

**Prioritize:** availability consistency, concurrent reservation, hold expiration, timezones, DST transitions, cancellation, rescheduling, no-show policies, capacity, notifications, payment/refund interactions.

**Highest-yield blind spots**

- Two users reserve the same final slot under concurrency.
- Hold expires during checkout but payment still succeeds.
- Timezone stored in one layer and interpreted in another; DST creates duplicate/missing slots.
- Reschedule race leaves two active bookings or double charges.
- Capacity changed after availability was shown.
- Cancellation policy applied differently by channel (web, phone, admin).
- Reminder sent at the wrong local time or after cancellation.

## Community / social platform

**Prioritize:** content/account abuse, moderation, reporting, blocking, privacy settings, feed visibility, notification preferences, uploads, rate limits, search indexing, deletion propagation.

**Highest-yield blind spots**

- Blocked/muted users still reachable through search, mentions, or direct links.
- Deleted content persists in caches, search, notifications, or shares.
- Private posts leak through API, embed, RSS, or Open Graph.
- Report/moderation queue lacks audit trail or appeal path.
- Rate limits bypassable via alternate endpoints or clients.
- Upload processing allows unsafe files or public access.
- Notification preferences ignored by one channel.

## Dashboard / internal business tool

**Prioritize:** role separation, data correctness, bulk operations, exports, destructive action safeguards, audit history, operational recovery, data freshness, accessibility.

**Highest-yield blind spots**

- Support/staff role can exceed intended scope; no least privilege.
- Bulk action partially succeeds; no preview, undo, or per-item result.
- Export includes fields or tenants the user should not see.
- Stale dashboard data drives a decision; refresh/ownership unclear.
- Destructive action lacks confirmation, soft delete, or recovery.
- Impersonation/session switching lacks audit trail.
- Internal tool bypasses controls because "it is internal".

## Learning platform

**Prioritize:** enrollment, course access, progression, assessment integrity, grading, completion rules, content availability, certificates, payment/entitlement alignment, learner data privacy.

**Highest-yield blind spots**

- Enrollment revoked but content/API/video URLs remain accessible.
- Completion/grade can be manipulated client-side or replayed.
- Assessment retake/time-limit rules inconsistent across devices.
- Certificate generated before requirements are truly met.
- Course content leaks to non-enrolled users via search/share/direct URL.
- Instructor/assistant permissions exceed intended scope.
- Learner data (grades, identity) exposed to other learners or analytics.

## API-first / developer platform

**Prioritize:** authentication, authorization, versioning, schema contracts, pagination, rate limits, idempotency, error consistency, documentation accuracy, SDK compatibility, observability, abuse prevention.

**Highest-yield blind spots**

- Docs and runtime disagree on required fields, errors, or pagination.
- API key scopes broader than documented; tenant isolation missing on one endpoint.
- Idempotency absent on write endpoints; retries duplicate resources.
- Rate limits per key but not per account/tenant; bypass via multiple keys.
- Breaking change shipped without versioning; old clients fail silently.
- Error responses leak internals or personal data.
- Webhooks unsigned/retried without deduplication.

## AI-enabled product

**Prioritize:** input/data boundaries, prompt injection, output validation, tool permissions, sensitive data disclosure, provider outages, latency, cost controls, rate limits, evaluations, human override, graceful fallback.

**Highest-yield blind spots**

- Retrieved or uploaded content injects instructions into the model.
- Tool calls authorized by the model rather than the application.
- Model output rendered as HTML or executed downstream.
- Cross-tenant leakage through RAG index, memory, or cache.
- PII/prompts logged or sent to a provider without consent/retention review.
- No token/cost cap; abuse or runaway agents exhaust budget.
- Model/prompt version changes without re-running evals.
- High-stakes output presented without uncertainty or human review.

See `adapters/ai-enabled-product.md` for detailed procedures.

## Static site / frontend-only app

**Prioritize:** build/asset integrity, client-side data exposure, accessibility, responsive behavior, routing, forms and third-party services, SEO/indexability, performance, browser compatibility, deployment configuration.

**Highest-yield blind spots**

- SPA fallback returns 200 for every missing route; 404s and SEO break.
- Content invisible without JavaScript when indexability matters.
- Secrets or privileged keys in the bundle.
- API trusts the client for authorization or pricing.
- Service worker serves stale app shell after deployment.
- Deep links break on refresh or shared base URL.
- Third-party forms/scripts fail silently or load before consent.

Mark backend-specific checks Not Applicable only after confirming no such service exists.
