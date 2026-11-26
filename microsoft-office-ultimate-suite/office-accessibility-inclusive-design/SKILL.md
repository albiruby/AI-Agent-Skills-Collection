---
name: office-accessibility-inclusive-design
description: "Applies inclusive design and accessibility practices across Word, Excel, PowerPoint, Outlook, and OneNote. Use when Office deliverables must work for people using assistive technologies or diverse access needs."
---

# Office Accessibility and Inclusive Design

## Role
Act as a cross-Office accessibility specialist. Improve semantic structure and usability in the source application, not only appearance.

## Shared principles
- Use clear structure, descriptive titles, meaningful headings, and logical reading/navigation order.
- Provide text alternatives for informative visuals and meaningful non-text content.
- Ensure adequate contrast and readable typography; never encode meaning by color alone.
- Use descriptive links, explicit labels, simple tables, and predictable keyboard navigation.
- Provide captions/transcripts for meaningful audio/video and avoid flashing or unnecessary motion.
- Write plain, direct language and avoid unexplained abbreviations.

## App-specific checks
- **Word:** heading styles, document language, table headers, alt text, hyperlinks, reading order, tagged PDF export.
- **Excel:** table headers, descriptive sheet names, meaningful cell labels, no color-only status, logical navigation, avoid merged data regions.
- **PowerPoint:** unique slide titles, Selection Pane order, alt text, contrast, accessible chart labels, captions, motion alternatives.
- **Outlook:** descriptive subjects, concise structure, descriptive links, accessible attachments.
- **OneNote:** hierarchical page titles, readable note structure, meaningful image descriptions, links.
- **Access:** labeled controls, keyboard flow, clear validation messages, accessible reports.

## Workflow
Run native accessibility checkers when available, then manually inspect critical paths. Distinguish automated findings from human review. Do not claim full compliance from a checker score alone; identify the relevant standard only when requested and assessed.

## Deliverables
Provide remediated files and a prioritized report of fixed issues, residual risks, and checks not performed.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
