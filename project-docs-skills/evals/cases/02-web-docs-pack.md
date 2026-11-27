# Case 02 - Web Documentation Pack

> Answer key. Do not show to the evaluated agent.

## Prompt

"Write a production-grade README and architecture doc for this web app, plus a GitHub social card and OG image from real screenshots. Verify commands and features."

## Inputs

- Next.js repo with package.json, routes, env example, tests.
- Staging URL and test account.
- Brand colors/logo.
- Authorization: read repo, run tests, browser capture, create docs/assets; no deploy.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | README documents a command that does not exist in package.json | High |
| S2 | Feature claim contradicts the code/feature flag | High |
| S3 | Relative image/link path is broken or wrong casing | Medium |
| S4 | Placeholder text remains in docs | Medium |
| S5 | Screenshot contains browser chrome or cookie banner | Medium |
| S6 | OG image dimensions do not match filename/spec | Medium |
| S7 | No alt text on key screenshots | Low |
| S8 | Deployment doc invents env vars | High |

## Distractors

- A missing optional roadmap section.
- A different valid hero layout.
- A minor tone preference.
- Extra architecture detail.

## Minimum coverage

- Commands and env vars verified.
- Architecture matches real modules.
- Clean screenshots and correct social dimensions.
- Links/placeholders checked.
- Unverified deployment/store items labeled.
- No secrets or customer data.

## Scoring notes

- S1/S2/S8 are critical/high accuracy failures.
- A polished OG card with wrong dimensions is still a failure.
- Reporting optional sections as missing is not a critical finding.
