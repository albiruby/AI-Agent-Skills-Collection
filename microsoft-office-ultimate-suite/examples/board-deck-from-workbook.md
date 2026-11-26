# Worked Example: Board Deck from a Workbook

## Scenario

The CFO asks: "Turn this monthly workbook into a 10-slide board update. Focus on revenue, margin, cash, and risks. Keep it editable in our template."

## 1. Intake

- Audience: board members; limited time; decision is to note performance and approve the revised forecast.
- Source: `FY26_Monthly_Model_v7.xlsx`, plus the prior board deck template.
- Deliverable: editable PPTX, PDF preview, speaker notes.
- Constraints: brand template, 16:9, 10 slides plus appendix, no fabricated data.
- Authorization: read workbook; create new files; do not modify the source workbook.

## 2. Inspect before generating

- Confirm the workbook sheets: `Inputs`, `Actuals`, `Calc`, `Checks`, `Output`.
- Verify the reporting period, currency, units, and version date.
- Recalculate key totals independently; check `Checks` sheet and reconciliation.
- Identify the authoritative figures for revenue, gross margin, cash, forecast, and risk notes.
- Check whether the workbook has stale cached values; open/recalculate if tools allow.
- Flag any missing or conflicting figures before designing slides.

## 3. Narrative

1. Title: FY26 month-end: revenue on plan, margin pressure in Q3.
2. Headline metrics: revenue, gross margin, cash, runway.
3. Revenue vs plan: trend and variance drivers.
4. Margin bridge: price, mix, cost.
5. Cash and runway: actual vs forecast.
6. Forecast change: what changed and why.
7. Risks and mitigations.
8. Decisions requested.
9. Appendix: assumptions and definitions.
10. Appendix: detailed tables.

## 4. Build the deck

- Use the board template's layouts and theme; do not flatten to images.
- For each slide, write the takeaway title first, then choose one dominant visual.
- Rebuild charts from the workbook's output table, not screenshots where native charts are feasible.
- Keep axes truthful, label units/currency, and show the time period.
- Put detailed tables in the appendix; keep main slides readable at distance.
- Add speaker notes with the "so what" and source references.
- Add alt text to charts/images and check reading order.

## 5. Validation

- Reconcile every headline number to the workbook; record the comparison.
- Reopen the PPTX; check placeholders, fonts, text overflow, chart data, and notes.
- Review in slide sorter and presentation mode; export to PDF.
- Check accessibility: alt text, reading order, contrast, color-only meaning.
- Confirm the source workbook was not modified.

## 6. Handoff

- Deliver `FY26_Board_Update_v1.pptx` and PDF preview.
- State: figures reconciled to model v7; checks performed; what could not be verified (for example, native font availability on the board portal).
- List assumptions, open questions, and the owner for final approval.

## 7. What commonly goes wrong

- Copying stale workbook values instead of recalculating.
- Screenshot charts that cannot be edited or traced to data.
- Too many numbers per slide; no clear takeaway.
- Inconsistent formatting after pasting between decks.
- Forgetting speaker notes and source references.
- Claiming the deck is "board-ready" without a visual or accessibility review.
