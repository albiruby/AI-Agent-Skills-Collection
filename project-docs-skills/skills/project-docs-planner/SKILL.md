---
name: project-docs-planner
description: "Designs the smallest maintainable documentation system for a project: audience map, document set, source-of-truth boundaries, navigation, ownership, visual documentation plan, and file tree. Use when creating or reorganizing a docs folder, deciding which documents a project actually needs, or planning a full documentation and visual asset package."
---

# Project Docs Planner

## Mission

Design a documentation architecture that serves real readers without creating empty boilerplate. A smaller set of accurate, linked documents beats a large folder of placeholders.

## When to use

- The user asks for a documentation plan, docs structure, or "what docs should this project have?".
- The repository has documentation but no clear source of truth, navigation, or ownership.
- A full docs-and-visuals package needs a deliverable list before writing.
- A README has become an oversized dumping ground.

Do not use this skill to write the documents; it produces the architecture and plan. Use `project-tech-docs-author` for execution.

## Workflow

### 1. Map audiences to jobs

| Audience | They need to | Primary document |
|---|---|---|
| End users | Understand value, install, use, recover | README, user guide, FAQ |
| Developers | Set up, build, test, extend | Developer guide, architecture |
| Maintainers | Debug, release, operate, recover | Architecture, deployment, runbooks |
| Integrators | Call APIs, use SDKs, handle errors | API/SDK reference, examples |
| Operators | Deploy, monitor, back up, restore | Deployment, operations, troubleshooting |
| Reviewers/store visitors | Understand features and trust the product | README, store listing, clean previews |

Do not create a separate document for every audience if one concise guide serves them. Name the primary audience for each document.

### 2. Select the minimum document set

| Document | Create when | Must answer |
|---|---|---|
| `README.md` | Always | What is it, who is it for, how do I start, where is deeper detail? |
| `docs/ARCHITECTURE.md` | Non-trivial system or contributors | What are the components, flows, boundaries, trade-offs? |
| `docs/API.md` / SDK reference | Public or internal interface | How do I call it, what types/errors/limits exist? |
| `docs/CLI_REFERENCE.md` | CLI tool | What commands/flags/exit codes exist? |
| `docs/USER_GUIDE.md` | Multi-step user workflows | How do I accomplish real tasks? |
| `docs/DEPLOYMENT.md` | Deployed service/app | How is it built, configured, released, rolled back? |
| `docs/TROUBLESHOOTING.md` | Recurring failures | What does this symptom mean, what is safe to try? |
| `docs/SECURITY.md` | Sensitive data/permissions | How are secrets, access, reporting handled? |
| `CONTRIBUTING.md` | External contributors | How do I propose, test, and submit changes? |
| `CHANGELOG.md` | Released software | What changed, when, and what must users do? |
| ADRs (`docs/adr/`) | Consequential decisions | What was decided, why, and what trade-offs? |

These are options. Omit documents that have no verified content or real reader.

### 3. Define every document

For each file, record:

- Path and title.
- Audience and job.
- Questions it must answer.
- Verified sources.
- What it must not duplicate.
- Links to authoritative related documents.
- Owner/update trigger, if known.
- Acceptance criteria.

### 4. Build the source-of-truth map

| Fact/topic | Authoritative location | Linked from |
|---|---|---|
| Install/run commands | README or developer guide | All other docs |
| Architecture | `docs/ARCHITECTURE.md` | README, contributor guide |
| API contract | `docs/API.md` or generated reference | README, SDK docs |
| Config options | `docs/CONFIGURATION.md` or API ref | Deployment, troubleshooting |
| Release history | `CHANGELOG.md` | README, release notes |
| Store dimensions | `../../references/store-asset-specs.md` + official source | Asset manifest |

Do not copy long sections; link instead. If duplication is unavoidable, name the controlling source.

### 5. Design navigation

- README is the entry point: one-line value proposition, hero visual, quick start, links.
- Use a short docs index when there are more than 4-5 documents.
- Keep paths stable and lowercase; match the project's existing convention.
- Ensure links work on the target platform (GitHub, GitLab, docs site, package registry).
- Avoid orphan documents: every doc should be reachable from README or the docs index.

### 6. Plan visual documentation

For each visual, specify:

- Purpose: explain, prove, sell, or guide.
- Capture source and screen/state.
- Output type: raw evidence, clean device, display-only, viewport card, mockup, store composition, diagram.
- Destination and dimensions.
- Editable source requirement.
- Privacy/redaction needs.

Use `../../templates/screenshot-shotlist-template.md`.

### 7. Avoid over-documentation

- No empty "Roadmap", "Contributing", "FAQ", or "License" sections without real content.
- No duplicate setup instructions in three files.
- No architecture diagram that restates the folder tree.
- No store pack for an internal prototype.
- No separate file for a topic that fits one section.

### 8. Output contract

Produce:

- Documentation tree with one-line purpose per file.
- Deliverable matrix: file, audience, source, status (create/update/keep/omit).
- Source-of-truth map.
- Navigation plan.
- Visual shot list.
- Dependencies and open questions.
- Recommended execution order.

Use `../../templates/docs-plan-template.md`.

## Validation checklist

- [ ] Every proposed document has a named audience and real content source.
- [ ] No mandatory-looking placeholders or unused folders.
- [ ] Each fact has one authoritative location.
- [ ] Navigation reaches every document.
- [ ] Visual assets specify type, destination, dimensions, and source.
- [ ] The plan matches project maturity and distribution channel.
- [ ] Ownership/update triggers are stated where facts change often.

## Handoff

- Pass the document specs to `project-tech-docs-author`.
- Pass the shot list to `visual-asset-capture`.
- Pass dimensions and destinations to `store-preview-asset-builder`.
- Return the plan to `project-docs-skills` for sequencing.
