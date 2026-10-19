---
name: game-asset-sheet-spec
description: Defines generation-safe specs for game and app assets from image models - sprite sheet geometry (square cells, frame count, baselines, gutters), tile and atlas grids, icon sizes, UI nine-slice frames, VFX frames, key-color backgrounds and directional views. Use when generating sprite sheets, tilesets, pixel art, icons, UI kits or VFX for games, or when frames overlap, touch, change scale or get cropped. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Game Asset Sheet Spec

## Purpose
Image models do not honor pixel math, so the spec describes geometry in relative terms the model can follow, then fixes the rest in post.

## Sprite sheet geometry (single animation, single direction)
- Landscape canvas (16:9 recommended). **One horizontal row** of N frames, chronological left to right.
- Each frame sits in a **square cell**; cell side = canvas width / N. Center the row vertically; flat key color above and below.
- Character occupies at most 65% of cell width and about 80% of cell height; at least 15% empty space on each side. Frames never touch, overlap or get cropped.
- Same scale, camera and proportions in every frame; **head-top and feet baseline fixed**; body bob at most 1 px.
- No labels, numbers, grid lines, borders, duplicate rows, extra poses.
- Final cleaned size per cell is set in the manifest (e.g. 32x32, 64x64) and reached by post-processing, not by prompting pixel counts.

## Frame counts (defaults)
Idle 4, walk 6, run 6, attack 4-6, hurt 2-3, death 5-6. Use the same counts for every character of the same class.

## Directions
Down = front, up = back, left/right = true side profile. Never mix views in one sheet. If the design is symmetric, generate right-facing and mirror for left.

## Tiles and atlases
- Ground tiles 16x16 (or project size), orthogonal, seamless on all four edges, no outline, no baked shadow.
- Atlas on a strict grid with equal spacing; one tile per cell; nothing overlapping; clear gaps between props.
- Test seamlessness by tiling a 3x3 grid in post.

## Props, items, UI, VFX
| Type | Spec |
|---|---|
| Props/buildings | Same camera as characters; 1 px outline; base on a clear ground-contact line; no cast shadow |
| Items/icons | One centered object, bold silhouette, readable at 16-24 px, no slot frame |
| UI frames | Nine-slice friendly; centers empty; no text; consistent border and corner radius language |
| VFX | Compact bold shapes, hard pixel clusters, limited accent colors, no soft glow; frames on key color |
| Backgrounds / key art | Full frame edge to edge, no key color, foreground/midground/background layers |

## Background rule
Use a flat uniform key color (default #FF00FF), edge to edge, no vignette, gradient or floor. The key color must never appear inside the artwork.

## Pixel art specifics
Request crisp square pixels, no anti-aliasing, no blur, limited palette. Expect the model to produce "pixel-looking" art at a larger resolution; downscale with nearest-neighbor and snap to the palette in post.

## Process
1. Pick the engine-agnostic spec above; adjust frame counts and sizes to the manifest.
2. Insert the geometry text into the format section of each sheet prompt (`master-prompt-builder`).
3. After generation, run the sheet checklist in `consistency-qa-reviewer`.
4. Slice and normalize via `asset-postprocess-handoff`.

## Pitfalls
- Asking for 8 frames in a narrow strip; use more cells only on a wider canvas or split the animation.
- Requesting exact pixel dimensions from the model.
- Letting two animations share one sheet.

## Gemini notes
- Request one sheet per generation. When the model or surface offers a higher output size, choose it for sheets so small frames keep detail, then downscale in post.
- Gemini can handle layout instructions but not exact pixel math; keep geometry in relative terms and fix sizes in post.
