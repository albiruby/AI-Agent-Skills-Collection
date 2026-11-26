# Operating Model

## 1. Purpose

The skill is an audit orchestrator, not a fixed checklist executor. It must discover the system, select relevant investigation paths, validate evidence, and communicate uncertainty.

## 2. Audit dimensions are independent

Do not conflate:

- **Technology stack:** languages, frameworks, libraries, data stores, hosting.
- **Architecture:** monolith, services, serverless, static, event-driven, hybrid, monorepo, and other structures.
- **Product profile:** e-commerce, SaaS, marketplace, portfolio, publishing, internal tool, and so on.
- **Capabilities:** authentication, payments, search, uploads, notifications, subscriptions, background jobs, analytics.
- **Environment:** local, test, staging, production, preview, offline/edge environment.

A project may have many values in every dimension. Identify them independently.

## 3. Scope before depth

Audit the requested scope first. Expand to adjacent areas only when needed to validate a finding, trace a dependency, or identify a material propagation risk. Do not silently turn a focused audit into an unrestricted penetration test or broad repository rewrite.

## 4. Risk-weighted effort

Spend more effort where failure has greater consequence or likelihood. Examples include authentication, access control, payment, personal data, destructive actions, availability, and business-critical workflows. A brochure site may need stronger content, accessibility, SEO, and form checks than database consistency checks.

## 5. Project context is a working model

Build a compact model of:

- Actors and roles.
- Primary user journeys.
- Business rules and invariants.
- Important data entities and ownership.
- State transitions.
- External dependencies.
- Trust boundaries.
- Operational recovery paths.

Mark assumptions and confidence. Update this model when new evidence contradicts it.

## 6. Audit loop

For each important area:

1. State the expected behavior or invariant (or mark it unknown).
2. Identify the implementation path and boundaries.
3. Identify realistic failure and abuse conditions.
4. Select a safe verification method available in the environment.
5. Collect evidence.
6. Classify the result.
7. Consider propagation and second-order effects.
8. Record limitations and next verification steps.

## 7. Avoid checklist theatre

A checklist item is not complete because it was read. Record whether it was inspected, statically reviewed, dynamically tested, or independently verified. Do not claim a test was performed unless it actually ran.

## 8. Useful audit heuristics

- Follow high-value data from input to storage, display, export, and deletion.
- Follow permission checks from UI affordance to server-side enforcement and data access.
- Follow asynchronous operations from enqueue to processing, retry, failure, and user notification.
- Follow a content or configuration change through cache, rendering, indexing, and rollback.
- Follow a deployment through migration, health checks, monitoring, and rollback.
- Look for mismatches between UI language, actual behavior, business policy, and stored state.
