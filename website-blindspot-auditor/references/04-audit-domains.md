# Audit Domains Catalogue

Use this as a menu of investigation questions, not a universal checklist to exhaust blindly. Select relevant questions based on detected capabilities and risk.

## 1. Requirements and business logic

- Are requirements explicit, complete, and internally consistent?
- Does implementation match the apparent business policy, not merely its own code path?
- Are state transitions valid and reversible where required?
- Are price, quota, permission, eligibility, and ownership rules enforced at trusted boundaries?
- Are exceptional workflows, manual overrides, cancellations, and recovery paths defined?
- Are there hidden manual processes or role dependencies?

## 2. Functional behavior and user journeys

- Do primary and secondary flows work end-to-end?
- Are loading, empty, success, error, timeout, retry, and cancellation states represented?
- Can refresh, direct navigation, back/forward, or multiple tabs create inconsistent state?
- Are inputs normalized and validated at the correct boundary?
- Do buttons, links, keyboard actions, and form submission behave consistently?
- Are duplicate actions safe?

## 3. Security and privacy

- Authentication, session lifecycle, account recovery, and logout behavior.
- Authorization at server/data boundaries; object-level and tenant-level access.
- Injection, XSS, CSRF, SSRF, path traversal, insecure deserialization, and unsafe redirects where relevant.
- Rate limits, brute-force controls, abuse prevention, and resource exhaustion.
- Secrets, tokens, logs, error messages, source maps, and client bundles.
- File handling, content rendering, webhooks, CORS, security headers, and dependency risks.
- Data minimization, consent, retention, deletion, export, and third-party sharing.

Do not claim a vulnerability solely because a category is theoretically relevant. Identify an actionable path and evidence.

## 4. Data integrity and lifecycle

- Validation, canonicalization, constraints, uniqueness, and referential integrity.
- Atomicity, transactions, concurrency, race conditions, and idempotency.
- Duplicate/orphan records and partial writes.
- Migration safety, rollback compatibility, and old/new schema coexistence.
- Retention, archival, deletion, export, backup, and restore.
- Ownership and access controls across queries, exports, caches, and storage.
- Historical consistency and timezone/precision issues.

## 5. UX, usability, and trust

- Is the value proposition and next action clear?
- Is navigation predictable and information findable?
- Are error messages actionable and privacy-safe?
- Are irreversible actions explained and recoverable where appropriate?
- Is there appropriate feedback after user actions?
- Do empty states guide users instead of dead-ending them?
- Are trust signals, pricing, terms, and expectations clear and consistent?
- Are there unnecessary steps, friction, confusing terminology, or dark patterns?

## 6. Performance and resource efficiency

- Rendering, hydration, interaction latency, bundle weight, code splitting.
- Image/media sizes, formats, responsive delivery, font loading.
- Network waterfalls, duplicate requests, caching strategy, invalidation.
- Database query patterns, pagination, N+1 behavior, indexes.
- Memory leaks, long tasks, expensive computation, unnecessary polling.
- Low-end device and constrained network behavior.
- Infrastructure, API, storage, and third-party cost drivers.

Measure where possible. Avoid declaring a performance problem from source patterns alone when runtime behavior is unknown.

## 7. Accessibility and compatibility

- Semantic structure, labels, accessible names, landmarks.
- Keyboard navigation, focus order, focus visibility, dialogs, menus.
- Contrast, zoom/reflow, touch targets, error identification.
- Screen-reader announcements and dynamic state where applicable.
- Reduced motion, motion sensitivity, captions/transcripts for media.
- Browser/device differences and progressive enhancement.

Use recognized accessibility standards where relevant, but do not claim full conformance without appropriate testing.

## 8. Content, SEO, and discoverability

- Accuracy, freshness, duplication, contradictions, placeholders, broken links.
- Metadata, titles, descriptions, canonical URLs, robots directives, sitemap.
- Structured data correctness and eligibility.
- Semantic headings, internal linking, indexability, rendered content.
- Open Graph/social preview, image alt text, pagination, redirects.
- Localization and content fallbacks.
- Copyright, attribution, and media/font/icon licensing where assessable.

## 9. Reliability and production operations

- Error handling, timeouts, retries, circuit breakers where appropriate.
- Logging, metrics, traces, alerting, health checks, incident diagnosis.
- Background jobs, queues, scheduled work, webhook delivery.
- Backup/restore and disaster recovery evidence.
- Deployment safety, migrations, rollback, environment separation.
- Capacity, quotas, dependency outages, graceful degradation.
- Runbooks, operational ownership, admin recovery, audit trails.

## 10. Architecture and maintainability

- Clear boundaries, cohesion, coupling, duplication, dead code.
- Source of truth for shared business rules and types.
- Dependency hygiene, version drift, abandoned packages, licenses.
- Test strategy, observability, extension points, complexity hotspots.
- Compatibility during incremental releases and schema evolution.
- Whether proposed abstraction is justified by actual variation.

## 11. Analytics and measurement integrity

- Are events defined around meaningful user actions?
- Are they duplicated, dropped, misattributed, or emitted at the wrong lifecycle stage?
- Do client/server events reconcile where necessary?
- Are consent and privacy rules respected?
- Are sensitive values excluded from event payloads?
- Are funnels and conversion definitions internally consistent?

## 12. Compliance and digital rights

- Identify applicable jurisdiction, business context, data types, and legal obligations before assessing compliance.
- Check required disclosures, privacy notice, terms, cookies/consent, marketing preferences, retention, data subject processes, and vendor disclosures where relevant.
- Review ownership, licensing, attribution, and usage rights of media and dependencies when evidence is available.
- Treat legal conclusions as requiring qualified review. Report observable gaps and questions, not unsupported legal certifications.

## 13. Product and business opportunities

- Friction reduction, onboarding, activation, conversion, retention.
- Self-service and support workload reduction.
- Better search, filtering, navigation, and content discovery.
- Feature discoverability and progressive disclosure.
- Pricing clarity, plan fit, quota communication.
- Operational automation and reduction of manual error.
- More useful measurement and feedback loops.

Separate hypotheses from opportunities supported by user research, analytics, or direct evidence.
