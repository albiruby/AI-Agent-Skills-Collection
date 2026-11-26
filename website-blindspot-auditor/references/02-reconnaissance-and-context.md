# Reconnaissance and Context Reconstruction

## 1. Inspect, do not assume

Use whichever read-only repository and project-inspection tools are available. Start with a bounded overview rather than recursively dumping the entire repository.

Useful evidence sources include:

- Top-level directory structure and workspace/monorepo manifests.
- Package, dependency, runtime, and lock files.
- Build, lint, test, type-check, and task-runner configuration.
- Routing and page definitions.
- Representative UI components and server-side handlers.
- API specifications, schemas, ORM models, and migrations.
- Authentication, authorization, and middleware configuration.
- CMS schemas, content models, and preview configuration.
- Storage, queue, scheduled-job, webhook, and integration code.
- Infrastructure-as-code, deployment, CI/CD, and environment examples.
- Existing tests, documentation, issue notes, and architecture diagrams.

Avoid spending time on generated output, vendored dependencies, large binary assets, caches, and build artefacts unless they are directly relevant.

## 2. Detect project context

Record the best-supported answers to:

| Question | Evidence to seek |
|---|---|
| What does the product do? | README, UI copy, routes, domain model, docs |
| Who uses it? | Roles, flows, copy, access rules, product docs |
| What are critical journeys? | Routes, forms, actions, tests, analytics events |
| What data matters? | Schemas, models, validation, storage flows |
| What can go wrong materially? | Business invariants, destructive actions, trust boundaries |
| What is external? | API clients, SDKs, webhooks, integrations, infrastructure |
| What can be tested? | Scripts, test config, runtime, browser, credentials, logs |

Do not infer sensitive business rules solely from UI labels. Seek corroborating evidence.

## 3. Confidence labels

- **Confirmed:** directly supported by explicit configuration, code, schema, documentation, or observed behavior.
- **Probable:** supported by multiple consistent signals but not conclusively established.
- **Unknown:** evidence is absent, ambiguous, inaccessible, or contradictory.

Record conflicts rather than silently choosing one source.

## 4. Reconstruct user journeys

For each important journey, identify:

- Entry point and preconditions.
- User identity and permission context.
- Inputs and validation.
- State changes and persistence.
- External calls or asynchronous effects.
- Success, failure, retry, and cancellation paths.
- User-visible confirmation and recovery options.

A journey can be simple (open page → read content) or complex (sign up → verify → subscribe → pay → provision → notify).

## 5. Reconstruct business invariants

Examples of invariants, only when applicable:

- One account must not read another account's private records.
- A payment must not be captured twice for one intended purchase.
- A confirmed booking must not exceed available capacity.
- An unpublished document must not appear in public views.
- A cancelled entitlement must not continue granting paid access beyond policy.
- A deleted account's data must follow the stated deletion/retention policy.

When the actual rule is unknown, report the ambiguity as a requirement gap rather than inventing the rule.

## 6. Monorepos and multi-application projects

Identify workspace boundaries and shared packages. Map each independently deployable app or service, then inspect shared authentication, UI, types, schemas, utilities, and configuration for systemic risk. Do not assume a repository equals one deployable website.
