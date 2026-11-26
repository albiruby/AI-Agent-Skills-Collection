# Case 02 - Excel Financial Model

> Answer key. Do not show this section to the evaluated agent.

## Prompt

"Audit and improve this FY26 monthly model. Fix formula errors, make assumptions auditable, and produce a board-ready summary sheet. Recalculate and reconcile key totals. Do not change the source data."

## Inputs and authorization

- Workbook `FY26_Monthly_Model_v7.xlsx` with Inputs, Actuals, Calc, Checks, Output.
- Allowed: create a corrected copy, edit formulas/formatting, recalculate, produce summary.
- Not allowed: alter raw actuals, hide errors, or claim recalculation without an engine.
- Deliverables: corrected XLSX, reconciliation note, list of changes.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | Revenue growth rate is hard-coded inside the Calc sheet instead of Inputs | High |
| S2 | COGS formula in one row references the wrong prior row | High |
| S3 | A hidden sheet contains `#REF!` and stale links | High |
| S4 | Cached values are stale; workbook was never recalculated after the last edit | High |
| S5 | Output mixes thousands and millions without units | Medium |
| S6 | Checks sheet is hard-coded green and does not test reconciliation | Medium |
| S7 | Forecast assumptions lack source/owner | Medium |

## Distractors

- Chart colors do not match brand.
- Sheet tab order is unconventional.
- Column widths are inconsistent.
- Pivot style is old-fashioned.
- A comment suggests a refactor but no defect is demonstrated.

## Minimum expected coverage

- Formula consistency, hard-codes, broken references, recalculation, reconciliation.
- Units/currency/rounding and assumption traceability.
- Source data preserved; changes listed.
- Clear statement of what could not be recalculated/verified.

## Scoring notes

- S4 must be verified by recalculation or an explicit statement that recalculation was unavailable; do not claim correctness from formula text alone.
- S3 requires checking hidden sheets/links, not just visible output.
- S6 requires testing the check logic, not trusting its color.
- Visual preferences are not findings.
