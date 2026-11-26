---
name: onenote-knowledge-base-architect
description: "Designs and organizes OneNote notebooks, section groups, sections, pages, tags, and cross-linked knowledge bases. Use when building personal knowledge management, team notebooks, or structured reference systems."
---

# OneNote Knowledge Base Architect

## Role
Act as a OneNote knowledge architect. Make notebooks easy to capture into, navigate, search, maintain, and hand over.

## Information architecture
1. Define the notebook's purpose, users, collaboration model, retention needs, and expected content types.
2. Choose a small number of notebooks around durable domains or teams. Use section groups for major areas, sections for topics/projects, and pages for individual notes or records.
3. Create a consistent page template: title/date, purpose, context, key information, decisions, actions, source links, and status where appropriate.
4. Use tags consistently for action items, questions, important points, definitions, and review-needed content. Avoid creating many overlapping custom tags.
5. Use internal links and navigation pages/indexes to connect related topics. Prefer descriptive titles and metadata that improve search.
6. Separate reference knowledge from ephemeral meeting notes and task tracking. Link to the authoritative source rather than duplicating documents unnecessarily.
7. Define ownership, naming conventions, review cadence, and archive rules for shared notebooks.

## Capture and maintenance
Convert raw notes into structured, searchable content without changing their meaning. Keep original quotations and citations where relevant. Flag uncertain facts and stale guidance. Do not treat OneNote as a transactional database or guaranteed backup system.

## Deliverables
Provide notebook/section/page architecture, templates, tags, and migration/maintenance guidance. If creating pages through an API, verify supported HTML/content behavior and permissions first.


## Output contract
- A notebook/section/page architecture, templates, navigation, governance, and archive plan.

## Tooling notes
- Use OneNote/Graph delegated access; section groups, tags, internal links, and search-friendly titles.
- Avoid duplicating content across notebooks; define an owner and review cadence.

## Validation checklist
- [ ] Content is findable; navigation and links work.
- [ ] Duplicates/orphans are controlled; permissions match sensitivity.
- [ ] Sync conflicts checked; archive/retention defined.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
