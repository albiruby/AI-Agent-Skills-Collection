# Tileset and Autotile Guide

## 1. Lock the grid

- Tile size: commonly 16x16 or 32x32; must match the engine and world scale.
- One logical pixel scale across tiles, props, characters, and UI on the same plane.
- Define the native viewport and integer display scale before drawing.
- Keep a 1-2 px extrusion/gutter around atlas tiles to prevent bleeding.

## 2. Terrain set design

Start with a **3x3 minimal terrain set**:

```text
corner | edge | corner
edge   | fill | edge
corner | edge | corner
```

Then expand to inner corners, outer corners, single tiles, ends, and transitions. For a full blob/47-tile set, define the neighbor bitmask explicitly.

## 3. Bitmask conventions

Document which neighbors count as "same terrain":

- 4-neighbor (N/E/S/W) for simple autotiles.
- 8-neighbor for corners/diagonals.
- Separate layers for ground, walls, cliffs, water, and decoration.
- Define precedence when two terrains meet (grass over dirt, water over sand).
- Keep a lookup table from bitmask to tile index; never guess in code.

## 4. Seams and repetition

- Test tile edges against every adjacent tile, including diagonals.
- Avoid obvious repeating motifs every 2-3 tiles; use variants and decals.
- Do not bake lighting direction inconsistently across tiles.
- Ensure transparent gaps do not reveal background incorrectly.
- Add transition tiles for grass-to-dirt, water-to-shore, path-to-grass, etc.

## 5. Collision and gameplay

- Separate visual tiles from collision shapes where possible.
- Define one-way platforms, slopes, ladders, and hazards explicitly.
- Keep collision aligned to the grid; document exceptions.
- Test character width/height against doorways and corners.
- Avoid collision meshes that depend on decoration variants.

## 6. Animated tiles

- Keep identical canvas and pivot across frames.
- Define frame durations in ms and loop behavior.
- Avoid animated tiles that shimmer or distract in large quantities.
- Test performance when many animated tiles are visible.

## 7. Atlas layout

- Group related terrain sets; avoid splitting a set across pages.
- Add extrusion/gutter; keep pivots consistent.
- Use deterministic names: `terrain_grass_16x16.png`, `terrain_water_autotile_32x32.png`.
- Include a metadata JSON/TSX/TMX or engine-native tile set when possible.
- Record tile size, grid, bitmask, and collision layers in the manifest.

## 8. QA

- [ ] Tile size and pixel scale match the project.
- [ ] No seams, gaps, or bleeding at 1x and integer zoom.
- [ ] All required transitions/corners exist.
- [ ] Repetition is controlled with variants.
- [ ] Collision aligns with visuals.
- [ ] Animated tiles loop cleanly.
- [ ] Engine import and test scene verified.
