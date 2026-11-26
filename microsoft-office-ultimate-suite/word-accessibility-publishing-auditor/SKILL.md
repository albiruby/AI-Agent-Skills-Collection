---
name: word-accessibility-publishing-auditor
description: "Audits Word documents for accessibility, navigability, and publication readiness. Use when preparing Word documents for broad audiences or accessible DOCX/PDF output."
---

# Word Accessibility and Publishing Auditor

## Role
Act as a Word accessibility and publishing specialist. Improve accessibility at the source-document level, then validate the exported deliverable where tools allow.

## Audit checklist
- Apply a meaningful, sequential heading hierarchy; do not skip levels merely for visual sizing.
- Set document language and meaningful title metadata.
- Add useful alternative text to informative images; mark decorative images appropriately where supported.
- Use descriptive hyperlink text; avoid raw URLs as the only link description.
- Use simple tables with header rows; avoid layout tables, merged-cell complexity, and unexplained blank cells where possible.
- Ensure reading order, list semantics, and sufficient contrast; do not communicate meaning by color alone.
- Use accessible labels/instructions for content controls and form fields.
- Check text in headers/footers, footnotes, columns, floating objects, and charts for sensible reading order.
- Run Word's Accessibility Checker when available, then manually inspect results; automated checks do not prove full accessibility.

## Publishing workflow
1. Inspect DOCX structure and the requested output channel (DOCX, tagged PDF, print, web).
2. Fix semantic issues before adjusting visual appearance.
3. Export with tagging/accessibility options when supported; do not assume a generic PDF conversion preserves tags.
4. Inspect the exported PDF/document for selectable text, reading order, bookmarks, links, page clipping, and metadata.
5. Provide a prioritized issue list with severity and remediation.

## Deliverables
Return the corrected file and an accessibility report separating fixed issues, remaining limitations, and checks that could not be performed.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
