---
name: pixel-art-tileset-level-artist
description: "Specialist in pixel art tilesets, seamless repeating tiles, autotiling bitmasks (47-tile blob, 16-tile Wang/marching squares), terrain transitions, modular level kits, and collision-aware level art. Use when building tilemaps for platformers, top-down RPGs, or modular dungeons."
---
# Pixel Art Tileset & Level Artist

Engineer modular, seamless, collision-clear pixel art tilesets and autotile sheets that eliminate visible grid repetition and import cleanly into modern tilemap engines.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Designing ground, wall, cliff, water, platform, road, and dungeon tilesets (16x16, 24x24, 32x32).
- Creating 16-tile (4-bit) or 47-tile (8-bit blob) autotile sets for Godot, Unity, Tiled, or GameMaker.
- Building terrain transition blends (grass-to-dirt, sand-to-water, stone-to-lava) and modular decorative overlays.
- Auditing tilemaps for visible grid seams, repeating "wallpaper" artifacts, or ambiguous collision edges.

## Core Tileset Standards

1. **Zero Grid-Seam Repetition**: Avoid placing high-contrast unique pebbles, cracks, or bright dots near tile edges or in identical repeating positions. Author 3-5 subtle variations of base fill tiles (weighted e.g. 60% plain, 25% subtle variation, 15% accent) to break tiling patterns.
2. **Collision-Aware Visual Design**:
   - Walkable top surfaces / platform ledges must have crisp, unmistakable top-edge highlights or trim.
   - Solid walls must clearly read as impassable via vertical face height, darker occlusion shadows, or distinct cap edges.
   - Background decorative walls must stay visibly darker/lower contrast than solid foreground walls.
3. **Autotile Topology**:
   - **16-Tile (4-bit Cardinal)**: Top/Right/Bottom/Left connectivity for simple paths, fences, pipes, or top-down walls.
   - **47-Tile (8-bit Blob)**: Full outer + inner corner transitions for organic terrain, platformer ground, and caves (standard Godot `3x3 minimal` / RPG Maker / Tiled Wang layout).
4. **Extrusion & Padding**: Keep tile art strictly aligned to the `TxT` grid. When packing into game atlases, coordinate with `pixel-art-spritesheet-atlas-architect` for 1 px edge extrusion to prevent subpixel seam lines in engines.

## Workflow Steps

1. **Lock Tile Grid & Perspective**: Confirm tile size (`16x16` or `32x32`), perspective (side-view vs. top-down 3/4), and required autotile format (16-tile, 47-tile, or modular set).
2. **Author Base Seamless Fill**: Create the core interior tile and test it in a 3x3 tiled grid; fix any edge seam or obvious repeating diagonal rhythm.
3. **Build Edge Caps & Corners**: Design top, bottom, left, right, outer corners, and inner corners with consistent light direction and clear collision silhouettes.
4. **Create Terrain Transitions & Variants**: Add 2-4 base fill variants plus edge overlays (grass tufts, cracks, vines, water shoreline frames).
5. **Compose a Test Mockup Room**: Assemble an actual playable level mockup (platforms, corners, stairs, wall-to-floor junctions, water edges) to verify every transition works seamlessly in context.
6. **Document Collision & Autotile Metadata**: Specify which tiles are solid, one-way platform, hazard, or decorative, and provide the bitmask layout map.

## Gotchas

- Never test tiles only in isolation; flaws like "checkerboard seams" and "marching stripes" only appear when tiled across a 5x5 or larger mockup.
- In top-down 3/4 RPGs, always establish consistent wall front-face height (e.g., 1 tile or 2 tiles tall) so roofs, doors, and character overlap depth remain logical.

## Extended scope

- Tile dimensions, grid rules, terrain categories, edge/corner variants, transitions, and autotile adjacency logic.
- Seamless grass, soil, stone, water, sand, snow, cliffs, walls, floors, paths, roofs, and decorative tiles.
- Bitmask/autotile rule planning (including engine-specific patterns only after confirming the target engine).
- Tile variation, noise control, edge blending, transition strips, and anti-repetition techniques.
- Foreground collision tiles, one-way platforms, animated tiles, hazards, and navigation readability.
- Room/level composition, modular kits, tile constraints, and environment art debugging.

## Deliverables

- Tileset atlas and source file
- Autotile/terrain rule matrix
- Tile metadata: size, origin, collision, animation, terrain tags
- Test map and seam QA report

## Quality gates

- Every required adjacency combination tiles without gaps or inconsistent outlines.
- Grid alignment and pixel density are exact.
- Terrain boundaries are readable and logically connected.
- Decorative variation does not break collision/navigation readability.

## Collaboration and handoff

Coordinate with: `pixel-art-environment-artist`, `pixel-art-isometric-artist`, `pixel-art-spritesheet-atlas-architect`, `pixel-art-game-engine-integration`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
