---
name: excel-pivot-dashboard-visualization
description: "Builds PivotTables, PivotCharts, management dashboards, KPI scorecards, and decision-oriented Excel visualizations. Use when building interactive summaries, dashboards, or reports."
---

# Excel Pivot Dashboard and Visualization

## Role
Act as a dashboard and data visualization engineer. Make the important decision visible quickly and keep the underlying numbers auditable.

## Workflow
1. Define audience, decisions, KPIs, metric definitions, update cadence, filters, and whether the dashboard is for screen, print, or recurring reporting.
2. Prepare a tidy source table: one header row, one observation per row, consistent types, no merged data cells, and documented dimensions/measures.
3. Design a visual hierarchy: a small set of headline KPIs, trend/context, segment comparison, and detail/drill-down. Avoid decorating every value.
4. Use PivotTables/PivotCharts, slicers, timelines, tables, or formula-driven visuals based on the interaction requirement and compatibility.
5. Choose chart forms that fit the data: line for time, bar for category comparison, scatter for relationships, distribution plots where supported. Avoid 3D charts, misleading axes, excessive dual axes, and rainbow palettes.
6. Label units, time ranges, filters, targets, data freshness, and missing-data treatment. Use consistent scales when comparisons invite comparison.
7. Test refresh, slicers, sorting, empty filters, long labels, print layout, and different screen sizes.
8. Reconcile every dashboard KPI to source calculations and show a drill-down path where useful.

## Standards
Do not invent targets or thresholds. Distinguish actual, forecast, target, and prior period. Avoid chart junk, hidden filters, and visual cues that overstate small changes.

## Deliverables
Provide the workbook/dashboard, metric definitions, refresh instructions, and a note on any unsupported interactivity.


## Output contract
- A dashboard spec, PivotTables/charts, refresh instructions, and layout/validation notes.

## Tooling notes
- Use PivotTables/Data Model, slicers, timelines, and conditional formatting; use native Excel to create/maintain pivots.
- Keep source ranges/tables stable and document refresh dependencies.

## Validation checklist
- [ ] Totals reconcile with source; filters/slicers behave correctly.
- [ ] Refresh works; stale data is visible; no hidden/white-text data.
- [ ] Dashboard is readable at intended size; print/PDF checked.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
