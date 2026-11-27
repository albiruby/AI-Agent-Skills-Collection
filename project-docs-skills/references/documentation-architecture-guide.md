# Documentation Architecture Guide

Use this guide to choose the smallest documentation system that serves the project's real audiences. It is a planning reference, not a mandatory file list.

## 1. Audience map

| Audience | Core job | Primary entry | Depth |
|---|---|---|---|
| Visitor / evaluator | Understand value and trust | README | Short |
| End user | Install, use, recover | README → user guide | Task-oriented |
| Developer / contributor | Set up, build, test, extend | README → developer guide | Practical |
| Maintainer / operator | Deploy, monitor, recover, upgrade | Architecture, deployment, runbooks | Operational |
| Integrator | Call APIs/SDKs correctly | API reference, examples | Precise |
| Store reviewer / buyer | Understand features and see product | Store listing, clean previews | Visual + claims |

A single document may serve multiple audiences, but each document should have one primary job.

## 2. Maturity → documentation depth

| Maturity | Recommended set |
|---|---|
| Prototype / spike | README, run instructions, known limitations, sample data notes |
| Internal tool | README, setup, architecture, troubleshooting, ownership |
| Maintained open source | README, contributing, architecture, testing, changelog, license |
| Public API/SDK | README, API reference, examples, versioning, compatibility, errors |
| Production service | README, architecture, deployment, operations, security, runbooks, changelog |
| Store-bound app | Above + user guide, clean screenshots, store listing, release notes, privacy/permissions |

Do not create documents for maturity levels the project has not reached.

## 3. Document contracts

For each document, define:

- **Path/title:** stable, predictable.
- **Audience/job:** one sentence.
- **Questions it answers:** 3-7 concrete questions.
- **Authoritative sources:** code paths, schemas, configs, tests.
- **Must not duplicate:** facts owned elsewhere.
- **Links:** where the reader goes next.
- **Update trigger:** release, API change, config change, incident.
- **Acceptance:** what makes it complete and correct.

## 4. Source-of-truth map

Assign each recurring fact to one owner:

| Fact | Owner | Linked from |
|---|---|---|
| Install/run commands | README or developer guide | Everything |
| Architecture | Architecture doc | README, contributor guide |
| API contract | API reference / generated spec | README, SDK docs |
| Config keys | Configuration reference | Deployment, troubleshooting |
| Release history | Changelog | README, release notes |
| Store dimensions | Platform requirements record | Asset manifest, QA |
| Visual asset inventory | Asset manifest | README, QA, handoff |

Link instead of copying. If duplication is necessary, state which copy controls updates.

## 5. Navigation rules

- README is the front door: value, hero visual, quick start, docs links.
- Add a docs index when there are more than 4-5 documents.
- Keep paths lowercase and stable; avoid renaming without redirects.
- Every document should be reachable from README or the index.
- Use relative links for repository docs; test on the actual host.
- Do not rely on headings alone for navigation in long documents.

## 6. Visual documentation plan

Decide per visual:

- Purpose: prove, explain, guide, sell.
- Source: real capture, diagram, screenshot, editable design.
- Output type: raw evidence, clean device, display-only, viewport card, mockup, store composition, diagram.
- Destination and dimensions.
- Alt text/description.
- Privacy/redaction.
- Editable source needed?

Do not turn every screenshot into a marketing composition. Keep clean evidence assets separate.

## 7. Content anti-patterns

- A README that is a second architecture document.
- Empty sections for "Contributing", "Roadmap", "FAQ", or "License".
- Commands copied from a blog and never checked.
- Three documents repeating the same setup steps.
- A diagram that only restates the folder tree.
- Store copy that promises planned features.
- Screenshots with simulator chrome or fake data.
- Documentation for an internal prototype dressed as a commercial launch.

## 8. Execution order

1. Context and evidence.
2. Audience and document set.
3. Source-of-truth map.
4. Draft README and critical docs.
5. Capture/clean visuals.
6. Deep references and diagrams.
7. QA and package.

## 9. Review gates

- **Scope gate:** every document has a real reader and source.
- **Accuracy gate:** commands/claims evidence-linked.
- **Navigation gate:** no orphans; links resolve.
- **Visual gate:** clean assets, correct crop type, readable at destination.
- **Compliance gate:** store requirements checked or marked unverified.
- **Handoff gate:** manifest, limitations, and next actions stated.
