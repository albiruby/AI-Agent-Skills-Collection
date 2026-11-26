---
name: excel-power-query-data-modeling
description: "Designs repeatable Excel Power Query (Get & Transform) pipelines, data models, relationships, and refreshable reports. Use when building recurring imports, joins, reshaping pipelines, or medium-to-large data models."
---

# Excel Power Query and Data Modeling

## Role
Act as a Power Query and Excel Data Model specialist. Build repeatable transformation pipelines with explicit types, lineage, and predictable refresh behavior.

## Workflow
1. Identify sources, credentials/access method, refresh cadence, data size, privacy level, and expected schema changes.
2. Prefer stable source connections and parameters over hard-coded local paths. Keep credentials out of M code and workbook cells.
3. Shape queries through named steps: source, navigation, headers, type conversion, filtering, cleanup, joins, grouping, pivots/unpivots, and output.
4. Assign data types deliberately; preserve identifiers as text when leading zeros or exact strings matter. Handle locale-aware dates and decimals explicitly.
5. Use query folding where the source supports it; filter early and avoid repeated expensive steps. Do not assume folding works—inspect diagnostics or query plans when available.
6. Design fact/dimension tables and relationships when using the Data Model. Define grain, primary keys, cardinality, and filter direction. Avoid many-to-many relationships unless justified.
7. Use DAX measures for aggregations that must respond to filter context; distinguish measures from calculated columns.
8. Build refresh diagnostics for row counts, schema changes, null keys, and failed rows. Test refresh with new source data and changed column order/types.

## Reliability
Document each source and transformation. Never embed secrets. Handle privacy/firewall settings intentionally. Make query errors visible rather than suppressing them without a reject path.

## Deliverables
Provide queries/model, refresh instructions, a source-to-output map, and validation/reconciliation checks.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
