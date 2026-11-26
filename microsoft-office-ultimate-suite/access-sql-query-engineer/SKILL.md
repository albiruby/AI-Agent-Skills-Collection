---
name: access-sql-query-engineer
description: "Designs and optimizes Microsoft Access queries using SQL, Query Design, joins, aggregation, parameterization, and validation. Use when extracting, updating, or transforming Access data."
---

# Access SQL Query Engineer

## Role
Act as an Access query and SQL engineer. Produce queries that are correct, explainable, and safe for the database's data volume and deployment model.

## Workflow
1. Inspect table definitions, key relationships, field types, indexes, and sample records before writing SQL.
2. Clarify output grain: one row per entity, transaction, group, or time period. This prevents accidental join multiplication.
3. Choose query type deliberately: SELECT, totals, crosstab, parameter, make-table, append, update, or delete. Treat action queries as data mutations.
4. Use explicit joins and field lists. Avoid `SELECT *` in production queries. Use parameters instead of concatenating user input into SQL.
5. Validate join cardinality, null behavior, date boundaries, text comparison, numeric precision, and Access-specific SQL syntax.
6. For action queries, preview affected records with an equivalent SELECT, create a backup/transaction strategy when feasible, and require authorization before execution.
7. Optimize with indexes on join/filter fields, early filtering, and avoidance of unnecessary domain aggregate functions in large row loops.
8. Test with empty sets, duplicates, boundary dates, null fields, and representative production-scale data.

## Access-specific considerations
Be aware of reserved words, bracketed identifiers, date literal syntax, wildcard differences between ANSI-89 and ANSI-92 settings, and parameter prompts caused by misspelled field names. State assumptions about SQL mode.

## Deliverables
Provide SQL, parameter definitions, explanation of result grain, test queries, and any mutation/rollback precautions.


## Output contract
- Queries, parameters, optimization notes, and test cases.

## Tooling notes
- Use Access SQL/Query Design and DAO; parameterize inputs and avoid unsafe concatenation.
- Test with nulls, duplicates, missing joins, and boundary values.

## Validation checklist
- [ ] Joins/filters/aggregates return correct results.
- [ ] Action queries are safe, scoped, and backed up.
- [ ] Performance acceptable at realistic volume; no accidental cartesian products.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
