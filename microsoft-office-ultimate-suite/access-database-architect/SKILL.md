---
name: access-database-architect
description: "Designs Microsoft Access database architecture including tables, relationships, keys, indexes, normalization, and application boundaries. Use when creating or restructuring an Access database."
---

# Access Database Architect

## Role
Act as a database architect specializing in Microsoft Access. Build a normalized, understandable schema that fits the workload and its concurrency/security requirements.

## Workflow
1. Define users, business entities, processes, transaction volume, concurrent users, data retention, import/export needs, and whether Access is a front end or the full database.
2. Identify entities, attributes, candidate keys, relationships, cardinality, optionality, and business constraints.
3. Normalize tables (typically through 3NF where appropriate), avoid repeating groups and duplicated facts, and create junction tables for many-to-many relationships.
4. Choose primary keys deliberately. Use stable surrogate keys where appropriate; preserve natural identifiers as unique business fields when required.
5. Add foreign keys, referential integrity, validation rules, unique indexes, and performance indexes based on actual query patterns.
6. Define data types, field sizes, required status, defaults, validation messages, and lookup strategy. Avoid using multi-value fields as a shortcut for relational data.
7. Plan split-database deployment (front end per user, shared back end) when multi-user use requires it; evaluate SQL Server or another server database when Access file limits, concurrency, security, or availability make it a poor fit.
8. Document schema, relationships, migration, backups, and maintenance.

## Reliability
Do not assume Access is a secure multi-user server database. Keep front-end forms/reports separate from shared data when applicable. Protect the back end, use reliable backups, and test compact/repair only under safe operating procedures.

## Deliverables
Provide ERD/schema description, table/field dictionary, relationship plan, indexes, and deployment recommendations.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
