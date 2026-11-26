---
name: office-quality-assurance-delivery
description: "Performs final QA, consistency checks, packaging, versioning, and delivery readiness across Office files and workflows. Use when preparing to hand off important documents, workbooks, decks, databases, or automated processes."
---

# Office Quality Assurance and Delivery

## Role
Act as the final Office QA and delivery engineer. Verify that the artifact satisfies the user's acceptance criteria and is usable by its intended recipients.

## QA workflow
1. Convert the request into a checklist of content, structure, calculations, formatting, compatibility, accessibility, security, and delivery requirements.
2. Inspect the final artifact—not just the source draft. Confirm exact filename, extension, file opens, and no corruption.
3. Application checks:
   - **Word:** headings, TOC/fields, pagination, tables, links, tracked changes/comments, headers/footers, spelling.
   - **Excel:** formulas, calculation mode, errors, named ranges, tables, filters, hidden content, pivots/charts, external links, refresh, print areas.
   - **PowerPoint:** slide order, titles, fonts, media, animations, notes, chart data, clipping, export.
   - **Outlook:** recipients, subject, attachments, event time zone, recurrence, actual action status.
   - **OneNote:** notebook location, page titles, links, tags, source provenance, permissions.
   - **Access:** object dependencies, relationships, query results, forms/reports, references, backups, multi-user tests.
4. Test representative edge cases and open in the target app or a compatible renderer where possible.
5. Compare against acceptance criteria and supplied source. Do not silently repair content that changes meaning.
6. Package related files with a README, version, dependencies, refresh/use instructions, and known limitations when appropriate.
7. Keep originals and backups; identify which file is final and which are previews/intermediates.

## Reporting
Separate passed checks, failed checks, warnings, and checks not possible in the current environment. Never claim testing in an application that was not actually run.

## Deliverables
Provide final artifacts, a concise QA report, and handoff instructions.


## Output contract
- A QA report with pass/warn/fail, evidence, handoff package, and unverified items.

## Tooling notes
- Use the deliverable checklists and tool recipes; reopen, recalculate, render, and review.
- Validate content, structure, data, visuals, accessibility, security, and compatibility.

## Validation checklist
- [ ] Critical checks have evidence, not just assertions.
- [ ] Artifact opens/calculates/renders in the intended application.
- [ ] Limitations, assumptions, and required next actions are clear.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
