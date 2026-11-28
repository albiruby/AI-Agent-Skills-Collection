# Case 02 — Responsive Dashboard & Accessibility

## Fixture

A fictional analytics dashboard with:

- A KPI grid using fixed `320px` columns; page overflows to 412px at 375px.
- A 980px data table with no scroll wrapper.
- An “Invite member” modal with a visual overlay but no focus trap.
- A revenue chart with three series distinguished only by hue.
- A profile form error rendered as text but not associated with the input.
- KPI skeleton height 72px vs final 116px (CLS 0.18).
- Source access and Playwright are available.

## Prompt

> Audit the dashboard, reports, and settings at 320/375/768/1440. Fix the responsive breakages and the accessibility issues you can verify. Show me evidence that the fixes hold.

## Expected behavior

1. Map routes, states, and viewports; record coverage.
2. Reproduce mobile overflow with exact scrollWidth and offending selector.
3. Wrap the table in its own scroll region, not the page.
4. Treat the modal focus escape as a functional accessibility defect.
5. Add non-color encoding + legend/table alternative to the chart.
6. Associate the form error and move focus on submit.
7. Fix skeleton geometry; measure CLS before/after in the same lab conditions.
8. Re-test 320/375/768 and keyboard paths; state field-data limitations.

## Evidence required

- Overflow: `scrollWidth`, viewport, offender, computed grid columns.
- Table: page scrollWidth before/after; scroller region.
- Modal: Tab path before/after; Escape/restore.
- Chart: grayscale screenshot or description; legend/table.
- Form: `aria-invalid`/`aria-describedby`; announcement.
- CLS: before/after values and conditions.

## Scoring focus

| Criterion | Must show |
|---|---|
| Severity | Overflow and focus escape as P0/P1, not P2 |
| Root cause | Grid wrapper, table scroller, dialog behavior, encoding |
| Verification | 320/375/768 + keyboard + CLS lab |
| Coverage honesty | Field CLS pending; admin blocked |

## Failure modes

- Hiding overflow with `overflow-x: hidden` on `body`.
- Shrinking table text to 10px instead of adding a scroller.
- Adding `aria-modal` but no focus trap.
- “Add a legend” without a non-color encoding.
- Claiming AA conformance from an automated scan.
- Claiming field CLS improved from a single lab run.
