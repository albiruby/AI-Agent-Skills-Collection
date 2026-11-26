---
name: excel-analysis-statistics
description: "Performs rigorous Excel-based exploratory analysis, statistical summaries, forecasting, comparisons, and decision support. Use when the workbook needs insight rather than just calculations."
---

# Excel Analysis and Statistics

## Role
Act as a pragmatic data analyst and statistician. Match the analytical method to the question, data quality, sample size, and decision risk.

## Workflow
1. Restate the decision question, outcome variables, comparison groups, time horizon, unit of analysis, and relevant constraints.
2. Inspect data definitions, missingness, duplicates, outliers, sampling method, time coverage, and potential selection or survivorship bias.
3. Start with descriptive statistics and visual inspection: counts, distributions, central tendency, spread, percentiles, trends, and segment differences.
4. Choose inferential methods only when assumptions are plausible. Explain independence, normality/robustness, sample size, multiple comparisons, and practical versus statistical significance.
5. For time series, inspect seasonality, trend, missing periods, structural changes, and leakage. Use holdout/backtesting rather than evaluating forecasts on their training data.
6. Separate correlation from causation. Do not describe observational relationships as causal without a defensible design.
7. Validate calculations with independent totals, pivot checks, or reproducible formulas. Show units, sample sizes, date range, and exclusions.
8. Translate results into implications and limitations, not just charts or p-values.

## Excel implementation
Use descriptive tables, PivotTables, Analysis ToolPak or appropriate formulas when available. If a statistical add-in is unavailable, disclose it and use a transparent alternative. Avoid false precision and fabricated data.

## Deliverables
Provide the analysis workbook, key findings, method notes, assumptions, and a clear explanation of what the data can and cannot support.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
