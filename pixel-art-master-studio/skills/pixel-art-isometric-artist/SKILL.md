---
name: pixel-art-isometric-artist
description: "Specialist in isometric pixel art using crisp 2:1 pixel projection, orthographic grids, isometric buildings, terrain blocks, props, depth sorting, and perspective consistency. Use when creating isometric strategy, tactics, city-builder, or RPG pixel art assets."
---
# Pixel Art Isometric Artist

Construct clean, geometrically accurate 2:1 isometric pixel art tiles, buildings, props, and scenes with consistent projection angles, lighting planes, and reliable depth sorting.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Designing isometric ground tiles, slopes, water, roads, and elevation blocks.
- Creating isometric architecture, interiors, vehicles, furniture, and modular city/tactics kits.
- Establishing isometric tile dimensions, anchor points, and painter's-algorithm / Y-sort depth rules.

## Isometric Pixel Geometry Rules

1. **True Pixel-Art 2:1 Projection**: Use strict 2-pixels-horizontal by 1-pixel-vertical diagonal lines (approx. 26.565 deg) rather than mathematical 30-degree isometric lines (which produce ugly irregular jaggies in pixel art).
2. **Standard Tile Diamond Dimensions**: Choose even-width diamonds that tessellate cleanly without gaps:
   - Common sizes: `32x16`, `48x24`, `64x32`, `96x48`, `128x64` (top diamond face).
   - Verify whether corners use a 2-pixel flat tip (classic crisp tessellation) or 1-pixel pointed tip, and enforce that exact corner rule across every tile in the project.
3. **Three-Plane Lighting Model**: An isometric cube has 3 visible faces that must hold distinct values for instant 3D readability:
   - **Top Face**: Brightest value (direct overhead/key light).
   - **Left Face** (or Right, locked in Style Bible): Midtone value.
   - **Opposite Side Face**: Darkest shadow value.
4. **Vertical Axis & Modular Height**: All vertical lines are strictly 90-degree vertical columns. Lock a standard elevation step height (e.g., `16 px` or `24 px` per floor/cliff level) so stacked blocks, stairs, and roofs align seamlessly.
5. **Depth Sorting & Footprint Anchoring**: Define every multi-tile building or prop by its integer tile footprint (e.g., `1x1`, `2x1`, `2x2`) and place its sorting pivot at the bottom-most diamond vertex (or tile-center baseline) for clean Y-sorting / isometric Z-ordering.

## Workflow Steps

1. **Lock Isometric Grid Spec**: Define diamond `WxH` (e.g., `64x32`), corner pixel style (2 px flat vs. 1 px point), and vertical step unit.
2. **Construct Wireframe Bounding Box**: Draw the 2:1 isometric bounding prism first for every building, terrain block, or prop to guarantee perspective alignment.
3. **Block Three-Plane Values**: Fill Top, Left, and Right planes with distinct ramp values before adding windows, roofs, or surface texture.
4. **Align Surface Details to 2:1 Axes**: Roof shingles, windows, doors, cracks, and cast shadows must strictly follow the left 2:1 axis, right 2:1 axis, or vertical axis.
5. **Tessellation & Overlap Verification**: Place the asset inside a 3x3 isometric test grid with neighboring tiles and a character sprite to verify zero gaps, zero Z-fighting, and consistent scale.

## Gotchas

- Mixing 2:1 pixel lines with arbitrary 3:1 or 1:1 diagonals on the same building immediately breaks the isometric illusion.
- Never forget seamless edge alignment on isometric diamonds: a 1-pixel error on the diamond border creates visible black or white grid lines across the entire map.

## Extended scope

- Define projection conventions and grid axes; distinguish true isometric, dimetric, and stylized oblique views.
- Apply consistent slope ratios and vertical edges appropriate to the project rather than assuming one universal 2:1 rule.
- Design buildings, roads, terrain, vegetation, furniture, vehicles, and small props in shared projection.
- Plan tile footprints, elevation, occlusion, sorting layers, and object pivots.
- Compose isometric scenes with readable paths, height changes, and visual landmarks.
- Create modular isometric tiles and transition pieces without perspective drift.

## Deliverables

- Projection/grid specification
- Isometric sprite or modular asset set
- Tile footprint, elevation, pivot, and sorting guidance
- Calibration/test scene

## Quality gates

- All assets share the approved projection; no accidental perspective mixing.
- Grid slopes and vertical edges are consistent.
- Object footprint and occlusion work in the intended engine.
- Small details do not distort the perceived volume.

## Collaboration and handoff

Coordinate with: `pixel-art-environment-artist`, `pixel-art-tileset-level-artist`, `pixel-art-prop-item-artist`, `pixel-art-game-engine-integration`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
