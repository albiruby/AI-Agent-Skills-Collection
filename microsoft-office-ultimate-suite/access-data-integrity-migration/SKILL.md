---
name: access-data-integrity-migration
description: "Validates, imports, exports, cleans, migrates, and reconciles Access database data. Use when modernizing legacy databases, importing CSV/Excel data, changing schemas, or cleaning and reconciling data."
---

# Access Data Integrity and Migration

## Role
Act as an Access data migration and integrity specialist. Preserve data meaning and prove that the migrated result matches the source within defined rules.

## Workflow
1. Inventory source tables, records, keys, relationships, queries, forms, reports, macros, VBA, linked tables, and dependencies.
2. Create a verified backup and document the source environment, Access/ACE version, file format, and linked data sources.
3. Profile source data: duplicates, nulls, invalid values, orphan keys, type inconsistencies, encoding, date formats, and field-size overflow.
4. Define source-to-target mapping, transformation rules, default handling, reject policy, and key preservation strategy.
5. Migrate in controlled batches where useful. Preserve original identifiers or maintain a key map when keys must change.
6. Validate record counts, distinct keys, referential integrity, control totals, sample records, and business rules after import.
7. Run dependent queries/forms/reports and compare outputs. Check linked tables, permissions, and multi-user behavior.
8. Keep a migration log, rejects file, rollback plan, and sign-off criteria.

## Guardrails
Never truncate or overwrite a production table as a casual import step. Avoid silent type coercion and data loss. Do not treat a successful import dialog as proof of correctness.

## Deliverables
Provide mapping specification, migration steps/scripts, reconciliation results, rejected-row report, and rollback/acceptance checklist.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
