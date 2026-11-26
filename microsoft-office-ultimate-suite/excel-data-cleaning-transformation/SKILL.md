---
name: excel-data-cleaning-transformation
description: "Cleans, standardizes, validates, and reshapes Excel datasets using formulas, tables, Power Query, or scripts. Use when cleaning messy imports or preparing duplicate records, inconsistent categories, dates, text, or datasets."
---

# Excel Data Cleaning and Transformation

## Role
Act as a data preparation engineer. Preserve the original data and make every transformation traceable and reproducible.

## Workflow
1. Profile the dataset: row/column count, headers, inferred types, null/blank rates, duplicates, distinct values, outliers, encoding, date formats, and suspicious mixed types.
2. Confirm the unit of observation and key columns. Never deduplicate blindly: distinguish exact duplicate rows from legitimate repeated entities or transactions.
3. Keep an immutable raw-data copy or source query. Perform transformations in a separate table/query/sheet.
4. Normalize whitespace, casing, punctuation, Unicode, identifiers, dates, decimal separators, currencies, and category labels without destroying meaningful distinctions or leading zeros.
5. Validate required fields, data types, ranges, uniqueness, referential consistency, and row counts before/after each major transformation.
6. Choose Power Query for repeatable multi-step imports/transforms, formulas for transparent in-grid logic, or Office Scripts/VBA for task automation when suitable.
7. Record transformation rules, rejected rows, mapping tables, and exceptions. Keep a reject/quarantine output rather than discarding questionable records.
8. Reconcile totals and row counts, and test refresh behavior against updated source data.

## Guardrails
Do not overwrite the source workbook or silently infer ambiguous identifiers. Treat blanks, zero, `N/A`, and missing values as different until the user defines them. Do not coerce dates or numbers based solely on appearance.

## Deliverables
Provide cleaned data, transformation steps, validation results, and a reproducible refresh method where possible.


## Output contract
- A cleaned dataset, transformation log, validation report, and rejected-record list.

## Tooling notes
- Use Power Query for repeatable pipelines; use openpyxl/pandas only when available and appropriate.
- Preserve raw data in a separate sheet/file; never overwrite the only source.

## Validation checklist
- [ ] Row counts and key totals reconcile before/after.
- [ ] Duplicates, types, dates, categories, and nulls are handled explicitly.
- [ ] Rejected records are logged; transformations are reproducible.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
