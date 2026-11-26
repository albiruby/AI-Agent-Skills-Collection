---
name: website-blindspot-auditor
description: "Universally audit websites and web applications for overlooked bugs, edge cases, security and privacy risks, business and requirement gaps, cross-layer failures, operational weaknesses, and improvement opportunities. Adapts its audit to the detected technology stack, architecture, capabilities, and product use case, with optional stack adapters, mode runbooks, and an evaluation harness. Use when asked to audit, inspect, review, stress-test, pre-mortem, or find blind spots in a website or web application."
---

# Website Blind-Spot Auditor

## Mission

Act as an adaptive, evidence-driven auditor for websites and web applications. Find meaningful issues and opportunities that conventional code review, happy-path testing, or a fixed checklist may miss.

**Do not audit every project in the same way.** First understand the product and system, then select relevant audit domains and methods. Technology is evidence about implementation, not a substitute for understanding the product.

Core equation:

**Universal method + project context + capability-based selection + technology-aware verification + honest evidence = useful audit.**

## What this skill is — and is not

This skill is a **discovery-first audit orchestrator**. It is strongest when the request is open-ended: "find what we missed", "stress-test this", "what could break", "audit this properly". It adapts its scope to the product, then follows data, permissions, money, content, and failure paths across layers.

It is not:

- A replacement for a narrowly requested code change. If the user asks for a fix, audit only enough to guide the fix, and respect the requested scope.
- A generic checklist that must be exhausted. Irrelevant domains are marked Not Applicable with a reason.
- A penetration test or a compliance certification. It can identify security/privacy gaps, but it does not authorize intrusive testing or certify legal compliance.

## Relationship to structured audit packs

When the collection also contains a structured pre-launch audit pack such as `production-readiness-audit-skills`:

- Use **this skill** for adaptive discovery, adversarial thinking, cross-layer failure hunting, second-order effects, and finding what fixed checklists miss.
- Use the **structured pack** for a repeatable, domain-by-domain pre-launch gate with a defined verdict, scoring, and remediation workflow.
- Running both is valid in sequence: use this skill to discover and challenge, then route verified gaps into the structured pack for formal closure. Do not load both blindly and duplicate the same checks; state which role each one is playing.

## When to use

Use this skill when the user asks to audit, review, inspect, assess, test, harden, troubleshoot, pre-mortem, or discover hidden risks/opportunities in a website, web application, API-backed frontend, CMS-driven site, storefront, SaaS product, or a related web system.

Use it especially when the request is ambiguous about depth or when the user suspects that conventional review or testing has missed something.

## Operating modes

Infer the mode from the request. Ask only when the choice materially changes safety, scope, or effort.

- **Deep Audit (default):** Broad, risk-weighted review of the project and relevant system boundaries.
- **Focused Audit:** Deeply inspect a specified feature, route, component, service, integration, or concern, including its dependencies and adjacent failure paths.
- **Blind-Spot Hunt:** Prioritize neglected assumptions, untested surfaces, unusual-but-realistic scenarios, cross-layer interactions, second-order effects, and non-obvious opportunities. Hypothesis-driven and time-boxed.
- **Re-audit / Verification:** Compare the current system against a prior report or remediation claims. Classify each item as fixed, partially fixed, regressed, unchanged, or unverifiable, and check for new risk introduced by the fix.

Mode changes prioritization and minimum coverage, not the standards for evidence or safety. Runbooks for each mode are in `references/13-mode-runbooks.md`.

## Non-negotiable principles

1. **Context before checklist.** Identify what the product does, who uses it, what matters, and how it is built before selecting tests.
2. **Stack-agnostic core.** Never assume a specific framework, language, database, CMS, cloud, or package manager.
3. **Capability-led selection.** Audit capabilities that exist or are strongly indicated; mark irrelevant domains Not Applicable rather than forcing them.
4. **Unknown-stack resilience.** If a technology is unfamiliar or unsupported, use observable behavior, standard protocols, architecture clues, and generic verification. State what could not be verified.
5. **Evidence over volume.** Never invent findings, inflate severity, or report generic best practices as confirmed defects.
6. **Follow data and state.** Trace meaningful user actions and data across frontend, backend, persistence, integrations, background work, and operations when those layers exist.
7. **Challenge the implementation.** The code may be inconsistent with the real requirement. Do not treat current behavior as proof of intended behavior.
8. **Read-only by default.** Do not modify files, data, configuration, dependencies, or production systems unless the user explicitly authorizes the specific change or test.
9. **Be transparent.** Distinguish inspected, executed, verified, inferred, inaccessible, and untested areas.
10. **No false assurance.** "No issue found" is not proof that a system is secure, correct, compliant, or reliable.

## Workflow

Follow this workflow in order. Scale depth to project size, risk, available time, and user scope. Do not block on missing documentation; reconstruct context from available evidence and record assumptions.

Track the audit in `templates/audit-plan.md` as you move through steps 1–5. Use `templates/intake-and-scope.md` when the request needs a formal scope/authorization record.

### 1. Establish scope, authorization, and success criteria

- Identify the target: repository, site, route, feature, environment, or supplied artifact.
- Determine whether the target is local, test, staging, preview, or production.
- Treat the default permission as read-only and non-destructive.
- Record allowed actions, forbidden actions, test-data rules, and stop conditions.
- Do not probe external systems, authenticated accounts, production data, or third parties unless the user has authorized that scope.
- If access or authorization is unclear for an action that could affect a live system, do not perform that action. Continue with safe static analysis and report the limitation.
- Clarify what "done" means for this request: discovery, decision support, a full report, or verification of prior findings.

Use `references/14-intake-and-scoping.md` for the intake question bank and ambiguity handling.

### 2. Reconstruct project context

Inspect available evidence such as repository structure, manifests, lockfiles, route definitions, configuration, schemas, tests, documentation, deployment files, and representative implementation paths.

Determine, with confidence labels where needed:

- Product purpose and likely user groups.
- Project type(s) and business model(s).
- Languages, frameworks, runtimes, and build tools.
- Frontend, backend, API, database, CMS, storage, authentication, hosting, and integrations.
- Core capabilities and critical user journeys.
- Trust boundaries, sensitive data, and important business invariants.
- Available test, browser, runtime, log, and deployment access.

Never print secret values. If secrets are found, report the location and exposure risk without reproducing the value.

### 3. Map architecture and critical flows

Build a lightweight map of relevant components and their interactions. Trace the most important flows end-to-end, for example: user action → UI state → request/action → authorization → business logic → persistence → asynchronous side effect → user-visible result.

Do not assume every layer exists. A static site may have no database or backend; a server-rendered app may not have a separate API; a headless CMS may act as the content source. Map what is actually present.

Use `references/07-cross-layer-analysis.md` to identify boundaries worth tracing.

### 4. Select applicable audit domains and adapters

Use the adaptive rules in `references/03-adaptive-selection.md` and the domain briefs in `references/04-audit-domains.md`.

Always consider the universal baseline. Activate conditional profiles and technology-specific guidance only when supported by project evidence. For each domain, record one status:

- Applicable — relevant to this project.
- Not Applicable — clearly outside project scope.
- Unknown — insufficient evidence to decide.

Do not equate Unknown with Not Applicable.

When a supported stack is detected, load the matching adapter from `adapters/` (index in `adapters/README.md`). Adapters sharpen verification; they do not replace the universal audit. If no adapter exists, follow the unknown-technology path in `references/03-adaptive-selection.md`.

### 5. Establish baseline and probe capabilities

Use available, appropriate checks such as existing tests, build, type checking, linting, static analysis, dependency inspection, browser inspection, logs, or runtime checks. Discover the project's actual scripts and conventions first. Do not install tools or change project state without permission.

Record baseline failures separately from newly discovered findings. A pre-existing failing test may be a finding, but explain why it matters and avoid attributing its cause without evidence.

Record what you can actually execute: shell, browser automation, test runner, database read access, logs, deployment metadata. Missing capability is a coverage limitation, not a reason to overclaim or give up.

`references/15-check-command-cookbook.md` lists safe, read-only checks by capability and stack. Use only the checks that fit the environment and authorization.

### 6. Investigate and challenge assumptions

Use the blind-spot methods in `references/06-blindspot-methods.md`, the scenario library in `references/08-edge-case-library.md`, and the cross-layer method in `references/07-cross-layer-analysis.md`.

Prioritize:

- Critical user journeys and business invariants.
- Authentication, authorization, sensitive data, and trust boundaries.
- Money, inventory, booking, identity, publication, or other irreversible/high-impact transitions when present.
- Partial failures, retries, duplicate submissions, stale state, concurrency, and recovery.
- Interfaces between components and external dependencies.
- Untested or weakly observed areas.
- Future change risks and second-order consequences.

Ask "what else could fail?" after discovering a significant issue. Explore adjacent components when the evidence indicates a shared root cause or propagation path. Test one hypothesis at a time and record what each probe actually demonstrated.

### 7. Verify and classify findings

Follow `references/09-evidence-and-prioritization.md`.

Classify each result as one of:

- **Verified Finding** — directly demonstrated or conclusively established by strong evidence.
- **Potential Risk** — credible concern that needs additional verification.
- **Coverage Gap** — important area not adequately inspected or tested.
- **Improvement Opportunity** — worthwhile enhancement, not necessarily a defect.
- **Not Applicable** — irrelevant to the project's actual capabilities or scope.

A code pattern can establish a likely defect if its behavior is unambiguous, but do not claim runtime impact that has not been observed. Separate severity from confidence.

Deduplicate symptoms sharing one root cause. Keep separate findings when their impact, remediation, or root cause materially differs.

When the user needs structured output or a downstream workflow, emit findings using `templates/findings.schema.json`. Keep prose evidence human-readable; the schema is for exchange, not a substitute for explanation.

### 8. Prioritize and report

Use `templates/audit-report.md`, `templates/exec-summary.md`, and `templates/coverage-matrix.md`. Lead with the most consequential verified findings, then important potential risks, coverage gaps, and opportunities.

For every actionable finding, provide location, evidence, impact, confidence, reproduction/verification steps, and a practical recommendation. Identify assumptions and limitations. Provide a remediation order that considers dependencies and regression risk. Use `templates/remediation-plan.md` when the output needs to drive execution.

### 9. Close with honest coverage and a definition of done

Score coverage using `references/16-coverage-and-completion.md` and attach the coverage matrix. State what was inspected, what was actually executed, what was verified, what was inferred, and what could not be accessed. Never say "fully secure," "bug-free," or "complete" based on a bounded audit.

If a prior report exists, use `templates/re-audit.md` and report status per item: fixed, partially fixed, regressed, unchanged, or unverifiable.

## Adapters

Load only adapters supported by evidence. See `adapters/README.md` for detection signals and selection guidance.

| Adapter | Use when |
|---|---|
| `adapters/nextjs-vercel.md` | Next.js App Router/Pages Router, server actions, RSC, ISR/caching, Vercel deployment |
| `adapters/wordpress.md` | WordPress/WooCommerce, themes/plugins, REST API, roles/capabilities, wp-cron |
| `adapters/ecommerce-and-payments.md` | Storefront, cart/checkout, inventory, payments, webhooks, refunds, subscriptions |
| `adapters/supabase-postgres.md` | Supabase auth/storage/RLS/edge functions or direct PostgreSQL access |
| `adapters/static-spa.md` | Static/CDN-hosted sites, client-side routers, SPAs, service workers |
| `adapters/ai-enabled-product.md` | LLM features, RAG, tool calling, model providers, AI-assisted workflows |

## Adaptive references

Load only the reference material relevant to the current project and task:

- Audit planning and principles: `references/01-operating-model.md`
- Reconnaissance, context, and evidence inventory: `references/02-reconnaissance-and-context.md`
- Stack, project, and capability selection: `references/03-adaptive-selection.md`
- Domain briefs: questions, verification, evidence, false-positive traps: `references/04-audit-domains.md`
- Business/product profiles and highest-yield blind spots: `references/05-project-profiles.md`
- Non-obvious reasoning techniques: `references/06-blindspot-methods.md`
- Interaction and end-to-end failure analysis: `references/07-cross-layer-analysis.md`
- Scenario catalogue: `references/08-edge-case-library.md`
- Evidence, confidence, severity, prioritization: `references/09-evidence-and-prioritization.md`
- Authorization, privacy, operational safety: `references/10-safety-and-scope.md`
- Technology adapter format and authoring rules: `references/11-adapter-authoring.md`
- Skill validation and evaluation harness: `references/12-validation.md`
- Mode runbooks and stop conditions: `references/13-mode-runbooks.md`
- Intake question bank and scope contract: `references/14-intake-and-scoping.md`
- Safe read-only check cookbook by stack/capability: `references/15-check-command-cookbook.md`
- Coverage scoring and definition of done: `references/16-coverage-and-completion.md`
- Worked examples: `examples/README.md`
- Evaluation cases and scorecard: `evals/README.md`

## Output contract

Unless the user requests another format, produce:

1. Executive summary and audit scope (see `templates/exec-summary.md`).
2. Detected project context and assumptions.
3. Prioritized findings (verified first), with severity, confidence, evidence, and verification steps.
4. Blind-spot discoveries and second-order risks.
5. Improvement opportunities.
6. Coverage matrix, coverage score, and audit limitations.
7. Recommended remediation sequence, with acceptance criteria.

Keep the main report concise enough to act on. Put detailed evidence and reproduction steps under each finding. If no verified findings are found, say so explicitly and highlight important unverified risks and coverage gaps rather than manufacturing issues.

## Definition of done (summary)

An audit is done for this skill when:

- Scope, authorization, and exclusions are explicit.
- Applicable domains and adapters are recorded with reasons; Unknown is not treated as Not Applicable.
- Every critical journey has been traced to the extent access allows.
- Findings are classified, deduplicated, and evidence-linked.
- Coverage and limitations are scored and visible.
- The report does not imply stronger assurance than the evidence supports.

Full criteria by mode: `references/16-coverage-and-completion.md`.
