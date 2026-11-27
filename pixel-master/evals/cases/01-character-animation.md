# Case 01 - Character Animation Pack

> Answer key. Do not show to the evaluated agent.

## Prompt

"Create a 32x32 side-view player character with idle/walk/attack animations for a Godot 4 platformer, using the approved 16-color palette. Build the sheet and test the import."

## Inputs

- Style bible and palette.
- Godot 4 project and import access.
- Authorization: create assets, run scripts, test a minimal scene.

## Seeded issues

| ID | Issue | Severity |
|---|---|---|
| S1 | Character uses 1px and 2px pixels (mixels) | High |
| S2 | Off-palette gradient colors in shading | High |
| S3 | Pivot changes between frames; character jitters | High |
| S4 | Loop duplicates the first frame, causing a double beat | Medium |
| S5 | Semi-transparent alpha fringe around sprite | Medium |
| S6 | Agent claims engine import works without testing | High |
| S7 | No native source or manifest | Medium |

## Distractors

- A different but valid idle pose.
- A slightly different frame count within budget.
- A valid alternate palette ramp.
- Extra animation state beyond the request.

## Minimum coverage

- Grid/palette/alpha checks.
- Pivot/loop/frame timing.
- Sheet metadata.
- Engine test or untested statement.
- Source/manifest/handoff.

## Scoring notes

- S1/S2/S3/S6 are high-impact.
- A polished sprite with a drifting pivot or fake engine claim fails.
- Reporting a valid aesthetic choice as a defect is a false positive.
