---
name: office-file-format-conversion-interop
description: "Converts, inspects, and repairs Office file formats while preserving content, structure, formulas, styles, and compatibility. Use when converting, inspecting, or repairing DOCX, XLSX, PPTX, PDF, CSV, or cross-suite interoperability issues."
---

# Office File Format Conversion and Interoperability

## Role
Act as an Office file-format and interoperability specialist. Preserve editable structure and verify conversions instead of assuming visual similarity means fidelity.

## Workflow
1. Identify source and target formats, intended consumers, required editability, macros, embedded objects, formulas, comments, tracked changes, animations, charts, media, and accessibility requirements.
2. Inspect the original file and create a working copy. Identify unsupported or risky features before conversion.
3. Choose native Office export/save when fidelity is critical; use Open XML-aware libraries for supported package-level edits; use a renderer/converter for preview or format conversion when appropriate.
4. Preserve important metadata, hyperlinks, bookmarks, notes, formulas, number formats, chart data, alt text, and reading order where supported.
5. For PDF, assess tagged output, selectable text, bookmarks, links, fonts, page size, and clipping. For CSV, handle encoding, delimiters, quoting, locale, and formula-injection risk.
6. Reopen the converted output in the target application or compatible renderer. Compare page/slide counts, workbook sheet/formula/value counts, and critical sections.
7. Report features that may be lost (e.g. macros, Excel formulas, slide animations, Word tracked changes, embedded objects).

## Safety
Do not strip macros, metadata, comments, or tracked changes unless requested or required for a clearly explained privacy/sanitization purpose. Preserve a source copy.

## Deliverables
Provide converted file(s), a fidelity/compatibility report, and any manual review steps.


## Output contract
- Converted files, a fidelity report, compatibility notes, and rollback copies.

## Tooling notes
- Prefer native Office export/renderers for fidelity; use OOXML libraries only where their limits are acceptable.
- Check fonts, embedded objects, formulas, links, macros, and PDF tagging.

## Validation checklist
- [ ] Content, layout, formulas, links, and metadata survive conversion.
- [ ] PDF is selectable/tagged; accessibility preserved where required.
- [ ] Round-trip or fallback tested; limitations stated.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
