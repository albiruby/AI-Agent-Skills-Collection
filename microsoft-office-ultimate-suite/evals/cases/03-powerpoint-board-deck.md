# Case 03 - PowerPoint Board Deck

> Answer key. Do not show this section to the evaluated agent.

## Prompt

"Build a 10-slide board update from the provided monthly workbook and our board template. Focus on revenue, margin, cash, and risks. Keep it editable and accessible. Do not invent figures."

## Inputs and authorization

- Monthly workbook, prior board deck, brand template.
- Allowed: create PPTX/PDF, add speaker notes, use native charts.
- Not allowed: modify source workbook, publish, or claim board approval.
- Deliverables: PPTX, PDF preview, reconciliation note.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | A chart uses figures from the prior month, not the current workbook | Critical |
| S2 | A bar chart y-axis is truncated, exaggerating growth | High |
| S3 | Three slides have text overflow/collisions at presentation size | Medium |
| S4 | Headline revenue figure conflicts with the workbook output | Critical |
| S5 | Charts/images lack alt text; reading order is illogical | Medium |
| S6 | Template placeholder text remains on two slides | Medium |
| S7 | Key decision slides have no speaker notes | Low |

## Distractors

- Font pairing differs from a personal preference.
- A stock photo is not the reviewer's first choice.
- Animation timing is slower than preferred.
- Appendix table uses a different but readable number format.

## Minimum expected coverage

- Every headline number reconciled to the workbook.
- Chart data/axes truthful; source noted.
- Layout reviewed for overflow; accessibility basics checked.
- Editable native elements preserved; placeholders removed.
- PDF export reviewed; limitations stated.

## Scoring notes

- S1/S4 are critical: a polished deck with wrong numbers fails.
- S2 requires checking axis settings, not just chart labels.
- S3 requires visual review at presentation size, not source inspection alone.
- S5 requires accessibility review; automated checks alone are insufficient.
- Personal aesthetic preferences are not findings.
