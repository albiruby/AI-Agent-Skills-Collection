# Case 01 - Garmin Visual Pack

> Answer key. Do not show to the evaluated agent.

## Prompt

"Document this Garmin Connect IQ watch face, clean the simulator screenshots, and build a Garmin IQ Store cover, hero, and three feature screens. Use real captures. Do not invent devices or features."

## Inputs

- Monkey C repo with `manifest.xml`, `monkey.jungle`, sources.
- Raw simulator captures for 4 states.
- Brand palette/logo.
- Authorization: read repo, run image scripts, create docs/assets; no store submission.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | A raw simulator window (title/menu/status bar) is used as a final asset | High |
| S2 | Clean cutout has a white rectangular background / opaque corners | High |
| S3 | Round watch display is stretched into a square | High |
| S4 | Store asset filename says 1440x720 but file is another size | Medium |
| S5 | Copy claims a device not declared in `manifest.xml` | High |
| S6 | Screenshots show fake/empty data or debug overlays | Medium |
| S7 | No lossless masters under `store-assets/master/` | Low |
| S8 | Store compliance claimed without checking current requirements | Medium |

## Distractors

- A color preference in the hero.
- A different but valid font pairing.
- Extra feature screen beyond the minimum three.
- A missing optional architecture section.

## Minimum coverage

- Correct capture type (device cutout vs display-only).
- Clean transparency, no chrome, no halo, uniform scale.
- Store dimensions/masters.
- Claims match manifest/source.
- QA report states checked vs unverified.
- No store publication claim.

## Scoring notes

- S2/S3 are critical visual failures even if the banner looks polished.
- S5 is critical: unsupported device claims can fail review.
- Reporting a valid font/palette choice as a defect is a false positive.
