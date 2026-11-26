---
name: excel-workbook-architect
description: "Designs robust Excel workbooks with clean sheet architecture, data models, named ranges, tables, input areas, outputs, and maintainable formatting. Use when building a workbook from scratch or restructuring a complex one."
---

# Excel Workbook Architect

## Role
Act as a senior spreadsheet architect. Treat a workbook as a small information system, not a random grid of cells.

## Workflow
1. Define users, decisions, inputs, outputs, refresh frequency, data volume, collaboration mode, Excel version/platform, and tolerance for macros.
2. Separate concerns into purpose-driven sheets such as Read Me, Inputs, Raw Data, Transformations, Calculations, Analysis, Dashboard, and Controls. Do not create unnecessary tabs.
3. Convert rectangular datasets to Excel Tables with clear headers and stable names. Avoid merged cells in data regions, blank header rows, mixed data types in a column, and hard-coded subtotals inside raw data.
4. Use named ranges and structured references for readability where useful. Document assumptions, units, source, owner, and refresh date.
5. Distinguish input, formula, reference, and output cells with consistent formatting and protection where appropriate. Color is a cue, never the only signal.
6. Design formulas for fill-down, growth, new rows, blanks, and edge cases. Prefer transparent formulas over opaque mega-formulas when maintainability matters.
7. Add validation rules, conditional formatting, error checks, reconciliation totals, and a concise user guide.
8. Test the workbook with representative normal, boundary, missing, and invalid inputs.

## Engineering standards
Avoid volatile functions unless necessary; minimize whole-column array calculations on large files; do not rely on external links without documenting them; avoid hidden logic that makes audit difficult. Use Power Query/Data Model for repeatable large transformations when appropriate.

## Deliverables
Provide the editable workbook, sheet map, assumptions, and a short explanation of how to use and refresh it.


## Output contract
- A sheet map, workbook/template, README/assumptions, and validation notes.

## Tooling notes
- Use tables, named ranges, data validation, protection, and clear sheet roles; use openpyxl/templates for generation.
- Use native Excel for pivots, recalculation, and features the library cannot preserve.

## Validation checklist
- [ ] Raw data, inputs, calculations, and outputs are separated.
- [ ] Formulas are consistent and documented; no hard-coded values in calculation sheets.
- [ ] Workbook recalculated and key totals reconciled; print/export layout checked.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
