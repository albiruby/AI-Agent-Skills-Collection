# Case 02 - Tileset and Engine

> Answer key. Do not show to the evaluated agent.

## Prompt

"Build a 16x16 grass/dirt/water tileset with transitions for a Godot 4 top-down game, and verify it in a test map."

## Inputs

- Style bible/palette.
- Tile size and terrain list.
- Godot project and import access.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | Visible seams/gaps between tiles at integer scale | High |
| S2 | Missing inner-corner/transition combinations | High |
| S3 | Texture filter left on Linear | High |
| S4 | Compression/mipmaps cause bleeding/artifacts | Medium |
| S5 | Collision does not match water/cliff visuals | Medium |
| S6 | No test map; integration claimed untested | High |
| S7 | Palette/value hierarchy makes characters disappear on grass | Medium |

## Distractors

- A different but complete autotile convention (3x3 vs blob).
- Additional decoration variants.
- A different valid tile size outside the requested spec.

## Minimum coverage

- Complete transition set for the chosen convention.
- Seam/bleeding test.
- Engine settings and runtime test.
- Collision alignment.
- Palette/value check with a character.

## Scoring notes

- S1/S2/S3/S6 are high-impact.
- A pretty tile sheet that fails in-engine is not done.
- Do not penalize a valid alternate autotile convention if the spec allows it.
