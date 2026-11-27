---
name: project-context-analyzer
description: "Inspects a software project and builds a reliable factual foundation for documentation and visual production: purpose, stack, platforms, architecture, feature maturity, audiences, existing docs, assets, workflows, gaps, and available tools. Use when documenting an unfamiliar project, before capturing screenshots, or when existing documentation may be stale or incomplete."
---

# Project Context Analyzer

## Mission

Act as a project analyst. Establish what is true about the project before anyone writes documentation or produces a screenshot. Your output is a compact evidence model, not a generic audit report.

## When to use

- Before a README, architecture guide, user guide, API reference, or release pack.
- Before capturing or cleaning screenshots when the project type, target device, or intended state is unclear.
- When docs exist but may be outdated, contradictory, or disconnected from the code.
- When selecting the documentation set, visual outputs, and store requirements.

## Evidence rules

1. Prefer source code, configuration, tests, schemas, CI, and observed behavior over existing prose.
2. Do not treat a UI label, TODO, branch name, mock, or issue as proof that a feature is implemented.
3. Record where each material fact came from (path, symbol, test, screenshot, or authoritative external source).
4. Label inference and uncertainty explicitly.
5. Never reveal secret values, tokens, personal data, or private endpoints.
6. Do not modify the project during analysis.
7. Stop expanding scope when the requested task is already well-founded.

## Inspection checklist

### 1. Identity and purpose

- Project name, one-sentence purpose, problem solved.
- Product boundaries: what it does and explicitly does not do.
- Current maturity: prototype, alpha, beta, production, maintenance, archived.

### 2. Type and targets

- Archetype: wearable/embedded, web/SaaS, mobile, desktop, CLI, API/SDK/library, game, data/ML tool, other.
- Target platforms, devices, browsers, OS versions, runtimes, or store channels.
- Distribution model: open source, internal, commercial store, package registry, self-hosted.

### 3. Stack and architecture

- Languages, frameworks, runtimes, package managers, build tools.
- Entry points, major modules, boundaries, persistence, external services.
- Diagram-worthy flows: request → auth → business logic → persistence → async → UI.
- Configuration and environment variables; verify names and defaults.

### 4. Execution workflows

- Install, build, run, test, lint, type-check, package, deploy, and release commands.
- CI/CD and release automation.
- Prerequisites and known environment constraints.

### 5. Features and maturity

Create a matrix:

| Feature/capability | Evidence | Status | Audience | Notes |
|---|---|---|---|---|
| | | Implemented / Partial / Planned / Deprecated / Unverified | | |

Only include features supported by code, tests, config, or observed behavior. Mark planned work as planned.

### 6. Documentation inventory

- Existing README, docs, API references, changelog, comments, diagrams.
- Stale commands, broken links, duplicate sources of truth, missing audiences.
- Documentation that is accurate but poorly structured.

### 7. Visual asset inventory

- Raw screenshots, simulator captures, device frames, logos, icons, brand colors, fonts.
- Existing clean assets, store graphics, OG images, diagrams.
- Licensing/provenance concerns.
- Asset naming and folder conventions.

### 8. Tool and capability probe

Record what is actually available:

| Capability | Available? | Limits |
|---|---|---|
| Read repository/files | | |
| Write files | | |
| Run shell/scripts | | |
| Control simulator/emulator | | |
| Browser automation | | |
| Inspect images visually | | |
| Process images (crop/alpha/compose) | | |
| Render diagrams | | |
| Access official platform requirements | | |
| Create archives | | |

A missing capability is a limitation, not a reason to invent output.

### 9. Risks and contradictions

- Code vs docs, UI vs server behavior, manifest vs claims.
- Unsupported devices or platforms implied by marketing.
- Sensitive data visible in screenshots or sample configs.
- Missing licensing or asset provenance.

## Output contract

Return a concise context report:

1. Project summary and audience.
2. Archetype, stack, targets, distribution.
3. Architecture and critical flows.
4. Verified feature/maturity matrix.
5. Documentation and asset inventory.
6. Gaps relevant to the request.
7. Capability probe and missing tools.
8. Assumptions, contradictions, and blockers.
9. Recommended next actions and which specialist skill to load.

## Validation checklist

- [ ] Claims are evidence-linked, not inferred from labels.
- [ ] Implemented/planned/deprecated status is explicit.
- [ ] Target platforms and distribution channel are verified.
- [ ] Existing docs/assets were checked for reuse and conflicts.
- [ ] Tool capabilities and limits are recorded.
- [ ] No secrets or personal data are included.
- [ ] The report is scoped to the user's request, not an exhaustive audit.

## Handoff

If the task is documentation, pass the feature matrix and source-of-truth map to `project-docs-planner`.
If the task is visual, pass the target device/platform, existing assets, and capability limits to `visual-asset-capture`.
If the task is a full pack, return control to `project-docs-skills`.
