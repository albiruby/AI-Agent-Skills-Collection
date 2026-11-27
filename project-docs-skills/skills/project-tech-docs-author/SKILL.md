---
name: project-tech-docs-author
description: "Writes and maintains grounded technical documentation for software projects: README, architecture, API/SDK/CLI references, user and developer guides, configuration, deployment, troubleshooting, security notes, and changelogs. Use when a user asks to write, rewrite, standardize, or update project documentation, add diagrams, or turn a codebase into a clear docs set without inventing features or commands."
---

# Project Tech Docs Author

## Mission

Produce documentation that a real reader can act on, derived from repository evidence. Every command, path, flag, endpoint, configuration key, supported target, and compatibility claim must be verified.

## When to use

- Creating or rewriting `README.md` or a docs folder.
- Documenting architecture, data flow, APIs, SDKs, CLI flags, configuration, deployment, or troubleshooting.
- Turning a codebase into a professional documentation package.
- Updating docs after a release or structural change.

## Evidence workflow

1. **Read before writing.** Inspect manifests, entry points, routes, schemas, migrations, tests, CI, env examples, and existing docs.
2. **Build a fact sheet.** Feature → evidence → status (implemented/partial/planned/deprecated/unverified).
3. **Reuse terminology.** Match the project's names for modules, commands, and concepts.
4. **Write for a reader and a job.** One document should answer one class of questions.
5. **Verify every example.** Run or trace commands when tools allow; otherwise label them unverified.
6. **Cross-check links and claims.** No stale paths, duplicated truths, or unsupported statements.

## Document patterns

### README

Keep it scannable, typically 80-200 lines:

1. Title and one-sentence value proposition.
2. Clean hero visual or screenshot (if it helps).
3. Status and supported platforms (verified).
4. Key features as concrete capabilities.
5. Prerequisites.
6. Quick start: exact install/run commands.
7. Basic usage example.
8. Project structure (short).
9. Links to deep docs.
10. License and attribution (only if verified).

Avoid generic boilerplate, fake badges, and unverified performance claims.

### Architecture

- System context and responsibilities.
- Component/module boundaries.
- Critical data/control flows.
- Persistence, integrations, auth boundaries.
- Key trade-offs and constraints.
- Current vs proposed architecture.
- Mermaid diagram only when it clarifies relationships; see `../../references/mermaid-diagram-guide.md`.

### API / SDK reference

- Authentication and authorization.
- Endpoints/methods, parameters, types, constraints.
- Request/response examples that match the code.
- Errors, status codes, retries, idempotency.
- Pagination, rate limits, versioning.
- SDK installation, imports, and compatibility.

### CLI reference

- Installation and invocation.
- Commands, flags, defaults, environment variables.
- Examples with expected output.
- Exit codes and error behavior.
- Destructive commands and safety notes.

### User guide

Organize by user goals. For each task: prerequisites, steps, expected result, failure recovery. Use real UI labels and screenshots only when genuine.

### Configuration

- Actual options, types, defaults, valid ranges, scope.
- Secret handling and placeholder examples.
- Environment-specific differences.
- Validation and reload behavior.

### Deployment / operations

- Build and release steps.
- Required settings and permissions.
- Health checks, migrations, rollback, recovery.
- Monitoring, logging, and known operational limits.
- Only document what is verified.

### Troubleshooting

- Symptom → likely cause → safe diagnostic → fix → prevention.
- Separate confirmed causes from possibilities.
- Never recommend destructive fixes without warnings.

### Changelog / release notes

- Keep a Changelog categories: Added, Changed, Deprecated, Removed, Fixed, Security.
- User-facing release notes: New, Improved, Fixed.
- Do not list planned or unmerged work as released.

## Grounding and status labels

Use precise language:

- **Implemented:** confirmed in code/tests/observed behavior.
- **Partially implemented:** some behavior exists but constraints remain.
- **Planned:** intended, not available.
- **Deprecated:** present but no longer recommended.
- **Unverified:** evidence is insufficient.

A dependency, config entry, or UI label alone does not prove a feature works.

## Visuals in documentation

- Embed only clean, chrome-free screenshots.
- Use relative paths with exact casing.
- Add meaningful alt text.
- Keep diagrams editable (Mermaid source) where possible.
- Do not use AI-generated UI as evidence of the real app.
- Keep image dimensions reasonable for repository rendering.

## Templates

Use the pack templates as starting points, then remove anything that is not true for the project:

- `../../templates/README-template.md`
- `../../templates/ARCHITECTURE-template.md`
- `../../templates/API-template.md`
- `../../templates/USER-GUIDE-template.md`
- `../../templates/DEPLOYMENT-template.md`
- `../../templates/TROUBLESHOOTING-template.md`
- `../../templates/CHANGELOG-template.md`
- `../../templates/CONTRIBUTING-template.md`
- `../../templates/ADR-template.md`

## Output contract

- Create/revise the requested documents at the requested paths.
- Report source evidence used, files changed, and facts still unverified.
- Do not create unrelated docs without a clear need.
- Preserve valid existing content and conventions.

## Validation checklist

- [ ] Every command/path/flag exists in the project or is labeled unverified.
- [ ] Every feature claim has evidence and a maturity label.
- [ ] No leftover placeholders, TODOs, or lorem ipsum.
- [ ] Relative links and image paths resolve with exact casing.
- [ ] Terminology and examples are consistent across documents.
- [ ] No secrets, private URLs, or personal data.
- [ ] README remains scannable; deep detail is linked.
- [ ] Diagrams render and match the implementation.
- [ ] Changelog reflects released changes only.

## Handoff

- Pass the docs tree and remaining gaps to `docs-release-packager`.
- Pass visual requests to `visual-asset-capture` and `store-preview-asset-builder`.
- Pass the finished set to `docs-visual-qa-auditor`.
