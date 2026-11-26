# Adaptive Selection Engine

## 1. Selection model

Select audit work using four independent inputs:

1. **Project profile:** what kind of product it is.
2. **Capabilities:** what features and workflows it has.
3. **Technology and architecture:** how those capabilities are implemented.
4. **Risk and scope:** what matters most and what is authorized.

Never select a profile from the framework alone. A React project might be a marketing site, SaaS product, store, or internal tool.

## 2. Universal baseline

Consider the following for every website or web application, adapting depth to the project:

- Requirements and intended behavior.
- Functional correctness and user journeys.
- Failure states and edge cases.
- Security, privacy, and trust boundaries.
- UX, responsive behavior, and accessibility.
- Performance and resource efficiency.
- Reliability and maintainability.
- Content integrity and discoverability where content exists.
- Observability and operational readiness where deployment/runtime exists.
- Blind spots, assumptions, and improvement opportunities.

## 3. Capability triggers

| Capability detected | Activate relevant investigation |
|---|---|
| Accounts / authentication | Signup, login, recovery, session, MFA if present, authorization, account lifecycle |
| Roles / permissions | Server-side enforcement, role transitions, least privilege, object-level access |
| Multi-tenancy | Tenant isolation in queries, storage, caches, jobs, exports, logs, and admin paths |
| Payments / billing | Amount integrity, idempotency, webhook verification, retries, refunds, invoices, entitlements |
| Inventory / scarce resources | Atomic updates, overselling/overbooking, reservation expiry, concurrent changes |
| Booking / scheduling | Timezones, availability races, cancellation, reschedule, DST, duplicate bookings |
| User-generated content | Validation, abuse, moderation, uploads, rendering safety, deletion, reporting |
| File uploads / media | Type validation, size, storage access, malware controls where appropriate, metadata, lifecycle |
| CMS / publishing | Draft/publish boundaries, preview, schema drift, content fallback, cache and search indexing |
| Search | Query safety, relevance, empty results, pagination, stale index, access filtering |
| Background jobs / queues | Idempotency, retry, poison messages, ordering, observability, dead-letter/recovery |
| Email / notifications | Delivery state, retries, preferences, unsubscribe, duplicate messages, sensitive content |
| Webhooks | Authentication/signature, replay, idempotency, ordering, retry, delivery visibility |
| Analytics / tracking | Event accuracy, duplication, consent, attribution, sensitive data, route changes |
| Localization | Locale fallback, date/number formats, currencies, pluralization, translated content |
| Public content / SEO | Crawlability, metadata, canonicalization, structured data, broken links, content accuracy |
| Admin / internal operations | Privilege separation, audit trail, bulk actions, recovery, accidental destructive changes |
| Real-time / collaborative features | Ordering, stale state, reconnect, conflict resolution, authorization, fan-out costs |
| AI / model-powered features | Prompt/data boundaries, output validation, abuse, cost controls, privacy, fallback, evaluation |
| Subscriptions / entitlements | Renewal, cancellation, grace periods, plan changes, usage limits, access consistency |
| API product / public API | Authentication, versioning, schema compatibility, quotas, error contracts, abuse controls |

A trigger indicates relevance, not proof that a defect exists.

## 4. Technology adapter activation

Activate technology-specific guidance only when the technology is confirmed or strongly indicated. An adapter must sharpen the verification method, not replace the universal audit.

For example, if a project uses a relational database, inspect constraints, transactions, isolation, migrations, and query patterns. If it uses a document store, inspect document boundaries, access rules, indexing, consistency, and query constraints. Do not assume all databases behave alike.

If a detected technology has no adapter:

1. Identify its role and boundaries from local evidence.
2. Use official/local documentation only when available and authorized.
3. Inspect its public contracts, configuration, data flow, and failure behavior.
4. Apply standard protocol and security principles.
5. State technology-specific unknowns and avoid unsupported claims.

## 5. Applicability matrix

For every major domain record:

- Applicable / Not Applicable / Unknown.
- Reason for selection or exclusion.
- Inspection depth.
- Available verification methods.
- Limitations.

Do not mark a domain Not Applicable merely because it was not inspected.

## 6. Adaptive prioritization

Prioritize based on:

- Potential severity and blast radius.
- Likelihood and exposure.
- Importance of the user journey.
- Sensitivity or value of affected data/assets.
- Evidence strength.
- Cost and safety of verification.
- User-requested scope.

For a small static website, avoid spending disproportionate effort on queues or payment workflows that do not exist. For a payment-enabled SaaS product, those workflows deserve deep investigation.
