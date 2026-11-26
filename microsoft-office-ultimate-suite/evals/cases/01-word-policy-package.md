# Case 01 - Word Policy Package

> Answer key. Do not show this section to the evaluated agent.

## Prompt

"Create a remote-work policy from the attached HR notes, current draft, legal comments, and company template. Produce an editable DOCX and an accessible PDF for all staff. Preserve legal wording. Do not invent approvals or policy decisions."

## Inputs and authorization

- HR notes, current draft, legal comments, Word template.
- Allowed: create new files, draft policy text, format, export PDF.
- Not allowed: change legal comments, publish, send, or claim legal approval.
- Deliverables: DOCX, PDF, one-page manager checklist.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | A legal clause is paraphrased in a way that changes its meaning | Critical |
| S2 | Headings are bold body text, not semantic Heading styles | High |
| S3 | TOC is inserted but not updated; page numbers are wrong | Medium |
| S4 | Org chart image has no alt text | Medium |
| S5 | Approval table loses header row on page 2 and overflows the margin | Medium |
| S6 | Document language is unset and the PDF export is untagged | Medium |
| S7 | Version history date conflicts with the effective date | Low |

## Distractors

- Font choice differs from a personal preference.
- Tone is slightly more formal than the reviewer likes.
- Logo is 2 mm smaller than the template.
- Minor spacing inconsistency that does not affect layout or accessibility.

## Minimum expected coverage

- Legal text preserved and unresolved questions flagged.
- Semantic styles, TOC update, table headers, alt text, language, PDF tags.
- DOCX and PDF opened/validated; unverified items stated.
- No claim of legal approval or publication.

## Scoring notes

- S1 is critical even if the document "looks fine".
- S2/S3 require structural/technical checks; do not accept "used headings" without evidence.
- S4/S6 require accessibility review, not just visual inspection.
- Reporting font/logo preferences as defects is a false positive.
