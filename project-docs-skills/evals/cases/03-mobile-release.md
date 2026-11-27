# Case 03 - Mobile Release Pack

> Answer key. Do not show to the evaluated agent.

## Prompt

"Prepare App Store and Google Play screenshots, a README, permissions explanation, and release notes for this mobile app. Use real screenshots and clean status bars."

## Inputs

- Flutter/React Native repo, iOS/Android configs.
- Simulator/emulator access with test account.
- Brand assets.
- Authorization: capture, create docs/assets, no store submission.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | Status bar shows personal notifications or test banner | High |
| S2 | Screenshot stretched to a different aspect ratio | High |
| S3 | Store panel dimensions do not match the current placement | Medium |
| S4 | Permissions explanation omits a permission used by the app | High |
| S5 | Release notes list unmerged/planned work as released | High |
| S6 | Duplicate setup instructions in README and user guide disagree | Medium |
| S7 | No QA or unverified-store statement | Medium |

## Distractors

- A different device frame style.
- A valid alternative screenshot order.
- A missing optional FAQ.
- A minor caption wording preference.

## Minimum coverage

- Clean status bars and real app states.
- Correct device sizes/aspect ratios.
- Permissions match platform manifests.
- Release notes reflect released changes.
- One source of truth for setup.
- QA/unverified statement.

## Scoring notes

- S1/S2/S4/S5 are high-impact.
- A pretty screen with fake data or wrong permissions fails.
- Personal aesthetic preferences are not findings.
