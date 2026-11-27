---
name: pixel-art-spritesheet-atlas-architect
description: "Specialist in sprite sheet layouts, texture atlas packing, frame indexing, pivot/origin alignment, cell padding/extrusion, naming conventions, and structured engine metadata (JSON/XML/Aseprite hash/array). Use when assembling animations or tiles into production sprite sheets and atlases."
---
# Pixel Art Spritesheet & Atlas Architect

Structure, pack, pad, and index pixel art animations, tilesets, and UI elements into clean, engine-ready sprite sheets and texture atlases with exact metadata and zero bleed or alignment jitter.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Packing individual PNG frames into horizontal strips, uniform grids, or tightly packed texture atlases.
- Generating standardized JSON/XML metadata (frame rects, durations in ms, animation tag ranges, pivot/origin points, 9-slice coordinates).
- Adding cell padding or 1-2 px edge extrusion to prevent texture bleeding in game engines.
- Establishing deterministic file and animation tag naming conventions.

## Core Architecture Standards

1. **Layout Selection**:
   - **Uniform Grid / Row-per-State Sheet**: Best for human readability, simple engines (RPG Maker, GameMaker, Godot `AnimatedSprite2D` grid), and predictable frame indexing (`row = state`, `col = frame`).
   - **Tightly Packed Atlas (Trimmed Rects)**: Best for memory efficiency and large character/boss sheets; requires JSON metadata preserving `spriteSourceSize` and `sourceSize` so trimmed frames never shift pivot.
2. **Padding & Edge Extrusion**:
   - **Sprites**: Add at least `1-2 px` transparent padding between cells so adjacent frames never bleed into each other under subpixel camera movement.
   - **Tilesets**: Add `1 px` edge extrusion (repeating border pixels outward into a 2 px gutter) to eliminate 1-pixel transparent seam cracks between tiles in GPU renderers.
3. **Power-of-Two (POT) Awareness**: Keep atlas dimensions within target GPU limits (e.g., `512x512`, `1024x1024`, `2048x2048` max for mobile/web) while avoiding excessive wasted empty space.
4. **Canonical Pivot & Origin**: Store explicit pivot coordinates `(px, py)` in pixels or normalized `[0.0, 1.0]` per asset class:
   - Characters / Grounded Props: Bottom-center (`x = width/2`, `y = foot_baseline`).
   - Projectiles / VFX / Icons: Geometric center (`0.5, 0.5`).
   - Tiles / UI Panels: Top-left (`0, 0`).
5. **Deterministic Naming Convention**: `<category>_<entity>_<variant>_<state>_<dir>_<frame:02d>.png` (e.g., `chr_hero_knight_walk_right_01.png`) and atlas JSON tags matching exact engine animation state names.

## Workflow Steps

1. **Inventory Input Frames**: Verify all input frames share consistent pixel density, lossless RGBA PNG format, and verified naming.
2. **Lock Packing Mode & Padding**: Choose uniform grid vs. trimmed rect packing, cell dimensions, gutter/extrusion width, and max sheet size.
3. **Pack & Generate Metadata**: Execute packing via Python (`Pillow`) or CLI (`aseprite --sheet`, `libresprite`, or atlas packer) and emit lossless PNG + JSON metadata (`frames`, `meta.frameTags`, `meta.slices`, `meta.pivots`).
4. **Validate Alignment & Zero Bleed**: Render a verification contact sheet or GIF playback reconstructed directly from the generated atlas + JSON metadata to prove zero jitter, clipping, or wrong frame order.

## Gotchas

- Never trim transparent borders from animation frames without writing exact `spriteSourceSize` offsets into metadata - otherwise every frame snaps to top-left and jitters wildly.
- Never mix assets that require different texture wrap modes (e.g., repeating parallax backgrounds with clamped character sprites) inside the same packed atlas.

## Extended scope

- Choose between fixed-cell sheets, tightly packed atlases, strips, separate frames, and layered exports.
- Define frame order, tag/clip naming, trim behavior, padding, extrusion, pivot/origin, and bounding box.
- Prevent bleeding, accidental frame overlap, alpha fringe, and incorrect sampling.
- Generate or validate JSON/CSV metadata where supported by the target pipeline.
- Plan atlas grouping by update frequency, material, resolution, and platform constraints.
- Keep source files and exported artifacts linked with deterministic naming and reproducible settings.
- Verify animation durations, tags, directions, and dimensions after export.

## Deliverables

- Spritesheet/atlas image(s)
- Metadata files and naming map
- Pivot and animation clip manifest
- Export settings and validation report

## Quality gates

- Metadata accurately points to the intended frames.
- No texture bleeding or unintended alpha borders.
- Atlas size and grouping meet platform constraints.
- Source assets remain editable and traceable.

## Collaboration and handoff

Coordinate with: `pixel-art-sprite-animator`, `pixel-art-tileset-level-artist`, `pixel-art-prop-item-artist`, `pixel-art-editor-operator`, `pixel-art-game-engine-integration`, `pixel-art-production-delivery-manager`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
