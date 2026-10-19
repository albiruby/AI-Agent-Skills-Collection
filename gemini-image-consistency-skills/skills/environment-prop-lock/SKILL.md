---
name: environment-prop-lock
description: Locks recurring locations, architecture, props, materials, scale and time-of-day so scenes, tiles, backgrounds and objects match one world. Use when generating settings, level backgrounds, tilesets, interiors, buildings, items or any non-character asset that must look like it belongs with the rest, or when the user says "same location", "consistent props", "environment kit". Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Environment & Prop Lock

## Purpose
Fix the visual rules of places and objects the same way character cards fix people.

## Location card
| Field | Content |
|---|---|
| Name and function | e.g. village square, where meetings happen |
| Layout | Zones and landmarks, entrances, paths |
| Architecture vocabulary | Roof, walls, windows, doors, decoration repeated everywhere |
| Materials | Max 5 materials with palette colors |
| Vegetation / ground | Species or type, ground texture |
| Lighting | Time of day, light direction, color |
| Scale anchor | A human figure height or tile size that fixes scale |
| Density | Sparse, medium, cluttered; number of props per area |
| Variants | Day/night, season, damaged/intact |

## Prop library
For each prop: name, silhouette in 5 words, material, size relative to the anchor character, 1-2 identifying details, states (closed/open, full/empty).

## Modular kit approach (recommended)
Instead of generating whole scenes first, generate **modules**: ground tiles, walls, roofs, trees, rocks, props. Assemble scenes from the kit. This gives much better consistency and reuse.

## Process
1. List locations and the 10-20 most important props from the brief.
2. Write location and prop cards; reuse the theme motifs and materials.
3. Define the **scale anchor** and repeat it in prompts ("a villager would reach the door handle").
4. Generate one hero image per location as its anchor, then derive variants by editing.
5. Check seam rules for tiles (see `game-asset-sheet-spec`).

## Output
Location cards, prop table, and a one-line Environment Lock for prompts:
`ENVIRONMENT: <name> - <architecture>, <materials>, <ground>, <light>, <scale anchor>.`

## Pitfalls
- Fully different architecture per scene. Reuse the same 3-4 shapes.
- Props that float or have no ground contact. State "base rests on the ground".
- Scenes with too many unique objects; the model will invent extras.

## Gemini notes
- Generate one hero image per location and attach it as the reference for variants (time of day, season). Generate modules (tiles, props) as separate requests, then assemble in an editor.
