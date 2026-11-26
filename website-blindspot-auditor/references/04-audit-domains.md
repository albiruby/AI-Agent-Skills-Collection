# Audit Domain Briefs

Use this as a menu of investigation paths, not a checklist to exhaust blindly. Select relevant domains based on detected capabilities and risk. Each brief gives you: what to ask, how to verify, what evidence to capture, and where naive audits go wrong.

## 1. Requirements and business logic

**Key questions**

- Are requirements explicit, complete, and internally consistent?
- Does implementation match the apparent business policy, not merely its own code path?
- Are state transitions valid, reversible where required, and guarded at trusted boundaries?
- Are price, quota, permission, eligibility, and ownership rules enforced server-side?
- Are exceptional workflows, manual overrides, cancellations, and recovery paths defined?
- Are there hidden manual processes or role dependencies?

**Verification**

- Derive invariants from pricing pages, terms, onboarding copy, support documentation, and observed behavior. Compare each claim to implementation.
- Build a state machine for the most important entity (order, booking, subscription, account) and test allowed, forbidden, repeated, and skipped transitions.
- Build a permission matrix: anonymous, user, owner, member of another tenant, staff, admin. Check UI affordance vs server enforcement.
- Look for rules implemented twice with different logic (client/server, API/worker, CMS/frontend).

**Evidence to capture**

- The stated rule and its source (URL, document, screenshot, code).
- The implementation path and the point where behavior diverges.
- The affected actor, entity, and business consequence.

**False-positive traps**

- An undocumented policy may be intentional. Report the ambiguity as a requirement gap rather than inventing the rule.
- Legacy behavior may be kept for compatibility. Verify before calling it a bug.
- A code comment is not a requirement.

## 2. Functional behavior and user journeys

**Key questions**

- Do primary and secondary flows work end-to-end?
- Are loading, empty, success, error, timeout, retry, and cancellation states represented?
- Can refresh, direct navigation, back/forward, or multiple tabs create inconsistent state?
- Are inputs normalized and validated at the correct boundary?
- Do buttons, links, keyboard actions, and form submission behave consistently?
- Are duplicate actions safe?

**Verification**

- Walk each critical journey in a real environment where possible, capturing each state transition.
- Test the same action through the UI, direct URL, and API where applicable.
- Interrupt the flow: refresh mid-action, go back after submit, open two tabs, lose network, retry.
- Compare client-side validation with server-side validation and with persisted data.

**Evidence to capture**

- Environment, account/role, steps, expected vs observed result.
- Screenshots or network traces for state inconsistencies.
- Whether the issue reproduces consistently or intermittently.

**False-positive traps**

- A missing test is a coverage gap, not proof of a defect.
- A spinner or optimistic UI is not proof of success.
- A 200 response does not prove the business operation completed.

## 3. Security and privacy

**Key questions**

- Are authentication, session lifecycle, account recovery, and logout behavior sound?
- Is authorization enforced at server/data boundaries, including object-level and tenant-level access?
- Are injection, XSS, CSRF, SSRF, path traversal, unsafe deserialization, and open redirects relevant and reachable?
- Are rate limits, brute-force controls, and abuse prevention present where needed?
- Are secrets, tokens, logs, error messages, source maps, and client bundles exposing information?
- Are file handling, content rendering, webhooks, CORS, headers, and dependencies configured safely?
- Is personal data minimized, consented, retained, deleted, exported, and shared appropriately?

**Verification**

- Trace every sensitive action from UI affordance to server enforcement to data access.
- Test with roles and objects the actor should not access, in an authorized environment.
- Inspect server handlers for authorization checks independent of UI.
- Review secret handling, bundle contents, logs, and error paths without printing values.
- Check headers/cookies/CORS on authorized endpoints; inspect dependency leads without assuming exploitability.
- Map personal data flows: collection, storage, processors, logging, export, deletion.

**Evidence to capture**

- Actor/role, request or code path, missing control, and resulting data/action.
- Redacted configuration or header output.
- For privacy: data type, purpose, recipient, retention, and consent state.

**False-positive traps**

- A vulnerability category is not a finding without a reachable path.
- Hidden UI is not access control, but it is also not proof of bypass.
- A dependency version alone does not prove exploitability.
- Scanner output needs reachability and context.
- Do not claim compliance or certification from a checklist.

## 4. Data integrity and lifecycle

**Key questions**

- Are validation, canonicalization, constraints, uniqueness, and referential integrity enforced?
- Are transactions, concurrency, race conditions, and idempotency handled?
- Can duplicate, orphan, or partially written records occur?
- Are migrations safe and rollback-compatible? Can old and new schemas coexist?
- Are retention, archival, deletion, export, backup, and restore defined and tested?
- Is ownership enforced across queries, exports, caches, and storage?
- Are timezone, precision, and historical consistency handled?

**Verification**

- Inspect schema constraints and the write paths that bypass them.
- Trace multi-step writes and identify what happens if one step fails.
- Test concurrent or repeated operations in a safe environment.
- Compare repository migrations with the live schema if access is available.
- Ask for restore evidence, not just backup configuration.
- Check deletion propagation to caches, search indexes, analytics, and object storage.

**Evidence to capture**

- Schema/constraint, write path, and the duplicate/orphan/partial state.
- Query results (redacted) or deterministic code paths.
- Migration version and deployment sequence.

**False-positive traps**

- A missing database constraint may be enforced transactionally in application code.
- Soft delete may be intentional; check the documented policy.
- Backup exists but restore untested is a coverage gap, not proof of data loss.

## 5. UX, usability, and trust

**Key questions**

- Is the value proposition and next action clear?
- Is navigation predictable and information findable?
- Are error messages actionable and privacy-safe?
- Are irreversible actions explained and recoverable where appropriate?
- Is there feedback after user actions?
- Do empty states guide users instead of dead-ending them?
- Are trust signals, pricing, terms, and expectations clear and consistent?
- Are there unnecessary steps, friction, confusing terminology, or dark patterns?

**Verification**

- Walk critical journeys as a first-time user and as a returning user.
- Check all states: empty, loading, partial, error, success, expired, no-permission.
- Compare wording across marketing, product, emails, and support.
- Test on narrow viewports and with keyboard-only navigation.
- Look for forced consent, hidden costs, confusing cancellation, or confirm-shaming.

**Evidence to capture**

- Screenshots or recordings of the friction.
- The exact copy and the user expectation it creates.
- Whether the issue blocks a task or only adds friction.

**False-positive traps**

- Subjective taste is not a usability defect. Tie concerns to user goals or evidence.
- Brand voice may be intentional.
- Accessibility issues belong primarily in domain 7; avoid double-reporting.

## 6. Performance and resource efficiency

**Key questions**

- How do rendering, hydration, interaction latency, and bundle weight behave?
- Are images, media, and fonts delivered efficiently?
- Are there network waterfalls, duplicate requests, or ineffective caching?
- Are database queries, pagination, and indexes appropriate?
- Are there memory leaks, long tasks, expensive computation, or unnecessary polling?
- How does the product behave on low-end devices and constrained networks?
- What are the infrastructure, API, storage, and third-party cost drivers?

**Verification**

- Measure where possible: field data, lab tools, browser traces, server timings.
- Compare against a baseline and state device/network conditions.
- Inspect bundle composition and third-party script cost.
- Review query plans for critical endpoints if database access is authorized.
- Check cache headers and CDN behavior rather than assuming.

**Evidence to capture**

- Metric, value, environment, device/network, and baseline.
- Trace or profile artifact location.
- Whether the issue is lab-only, field-observed, or source-inferred.

**False-positive traps**

- A slow pattern in source is not a measured regression.
- Lab results may not reflect real users.
- Third-party variance can dominate a single run; repeat before claiming.

## 7. Accessibility and compatibility

**Key questions**

- Is there semantic structure, labels, accessible names, and landmarks?
- Is keyboard navigation complete, with visible focus and correct order?
- Are dialogs, menus, carousels, and dynamic updates accessible?
- Is contrast sufficient, and does the layout work with zoom/reflow?
- Are errors identified and associated with their fields?
- Are dynamic state changes announced where needed?
- Are reduced motion, captions, and transcripts respected?
- Do browser/device differences break core tasks?

**Verification**

- Combine automated checks with manual keyboard and screen-reader inspection.
- Test at 200% zoom, narrow viewport, high contrast, and reduced motion.
- Check focus trapping/restoration in dialogs and menus.
- Use recognized standards (for example, WCAG) but do not claim full conformance without appropriate testing.

**Evidence to capture**

- Criterion, location, assistive technology/browser, and reproduction steps.
- Screenshot or recording where visual state matters.
- Whether the issue blocks a task or degrades experience.

**False-positive traps**

- An automated scan passing does not prove accessibility.
- Missing alt text may be correct for decorative images.
- Contrast tools can misread overlays and gradients; verify manually.

## 8. Content, SEO, and discoverability

**Key questions**

- Is content accurate, fresh, non-duplicated, and free of contradictions/placeholders?
- Are metadata, titles, descriptions, canonicals, robots directives, and sitemaps correct?
- Is structured data valid and eligible?
- Is content indexable and rendered for crawlers where intended?
- Are Open Graph/social previews correct?
- Are redirects, pagination, and internal links healthy?
- Are localization and fallbacks consistent?
- Are media, fonts, and icons properly licensed and attributed?

**Verification**

- Crawl a bounded set of pages; check status codes, canonicals, titles, and duplicates.
- Test with JavaScript disabled and with a crawler-like user agent where relevant.
- Validate structured data against the actual page content.
- Check `robots.txt`, sitemap completeness, and noindex on staging/preview.
- Review redirect chains and soft 404s.
- Check share previews for key pages.

**Evidence to capture**

- URL, status, rendered content, metadata, and expected behavior.
- Before/after if testing a fix.
- Whether the issue affects indexation, sharing, or only presentation.

**False-positive traps**

- Noindex may be intentional for private or duplicate pages.
- A missing sitemap entry does not always prevent indexing.
- Structured data eligibility depends on page type and provider rules.
- Content duplication may be intentional syndication.

## 9. Reliability and production operations

**Key questions**

- Are errors handled, timed out, retried, and surfaced appropriately?
- Are logs, metrics, traces, alerts, and health checks present for critical flows?
- Are background jobs, queues, schedules, and webhooks reliable and observable?
- Is backup/restore evidence available?
- Are deployment, migration, rollback, and environment separation safe?
- Are capacity, quotas, dependency outages, and graceful degradation handled?
- Are runbooks, ownership, admin recovery, and audit trails clear?

**Verification**

- Trace failure paths: provider down, slow response, partial success, retry exhaustion.
- Inspect job/queue configuration for idempotency, retries, dead letters, and ordering.
- Check whether critical failures produce alerts or only logs.
- Ask for restore drills, not just backup configuration.
- Review deployment order and version compatibility.

**Evidence to capture**

- Failure scenario, expected handling, observed handling.
- Log/alert/job evidence (redacted).
- Whether the gap is detection, recovery, or both.

**False-positive traps**

- A missing alert in the app may be covered by platform monitoring.
- A backup without a restore test is a coverage gap, not proof of loss.
- Retries may be intentional; check whether they are bounded and idempotent.

## 10. Architecture and maintainability

**Key questions**

- Are boundaries, cohesion, and coupling appropriate for the actual product?
- Is there a single source of truth for shared business rules and types?
- Are dependencies current, maintained, and license-compatible?
- Is the test strategy proportionate to risk?
- Are there complexity hotspots, dead code, or duplicated logic?
- Will the design survive incremental releases and schema evolution?
- Is any abstraction justified by actual variation?

**Verification**

- Map modules and dependencies; look for duplicated rules across layers.
- Check lockfiles, abandoned packages, version drift, and license constraints.
- Inspect test coverage around high-risk paths, not just aggregate percentages.
- Review migration and feature-flag strategy.

**Evidence to capture**

- Concrete duplication or coupling with impact on change safety.
- Dependency/version evidence.
- Test gaps tied to specific risks.

**False-positive traps**

- Architectural preference is not a defect.
- "Could be cleaner" is not actionable unless it creates a concrete risk.
- Aggregate coverage percentage can hide untested critical paths.

## 11. Analytics and measurement integrity

**Key questions**

- Are events defined around meaningful user actions?
- Are they duplicated, dropped, misattributed, or emitted at the wrong lifecycle stage?
- Do client/server events reconcile where necessary?
- Are consent and privacy rules respected?
- Are sensitive values excluded from event payloads?
- Are funnels and conversion definitions internally consistent?

**Verification**

- Inspect event definitions and firing points in code.
- Observe network events in a test environment; compare to expected lifecycle.
- Check route changes, retries, and duplicate submissions for repeat events.
- Reconcile purchase/signup/server-side events where possible.
- Check consent gating and PII in payloads.

**Evidence to capture**

- Event name, trigger point, payload (redacted), and observed duplication/missing state.
- Expected vs actual funnel step.

**False-positive traps**

- Ad blockers and privacy tools change measurement; do not overgeneralize from one browser.
- Sampling and attribution windows can explain discrepancies.
- Absence of analytics may be intentional.

## 12. Compliance and digital rights

**Key questions**

- Which jurisdiction, business context, data types, and obligations apply?
- Are required disclosures, privacy notices, terms, cookie/consent, marketing preferences, retention, and data-subject processes present?
- Are vendors and cross-border transfers disclosed as required?
- Are media, fonts, icons, and dependencies licensed for the intended use?
- Are age, accessibility, or sector-specific obligations relevant?

**Verification**

- Identify obligations from context, then compare observable behavior and documents.
- Check consent behavior (before/after choice, withdrawal, replay).
- Check deletion/export paths and retention claims.
- Review asset licenses where evidence is available.
- For Indonesian contexts, UU PDP may be relevant; route detailed legal analysis to qualified review. This skill reports observable gaps, not legal certification.

**Evidence to capture**

- The claimed policy, the observed behavior, and the gap.
- Jurisdiction/assumption and why it matters.
- Whether specialized review is required.

**False-positive traps**

- Do not give legal advice or certify compliance.
- A policy may be a draft or apply to another entity/jurisdiction.
- Missing cookie banner is not always a violation; context matters.

## 13. Product and business opportunities

**Key questions**

- Where is friction in onboarding, activation, conversion, or retention?
- What manual work or support load could be reduced?
- Are search, filtering, navigation, and content discovery effective?
- Are features discoverable and progressively disclosed?
- Is pricing, plan fit, and quota communication clear?
- Can operations be automated without adding risk?
- Are measurement and feedback loops useful?

**Verification**

- Use observed friction, support themes, analytics, or user research as evidence.
- Distinguish a hypothesis from a measured opportunity.
- Estimate effort and dependencies; do not promise conversion/revenue impact without data.

**Evidence to capture**

- The observed behavior or data supporting the opportunity.
- Expected benefit, confidence, effort, and dependencies.

**False-positive traps**

- A product opinion is not an evidence-based opportunity.
- Absence of a feature may be a deliberate scope decision.
- Do not imply measured business impact without measurement.
