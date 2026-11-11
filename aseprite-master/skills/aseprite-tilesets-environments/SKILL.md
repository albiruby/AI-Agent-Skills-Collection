---
name: aseprite-tilesets-environments
description: Creates pixel-art environment tiles, autotile-compatible sets, props, terrain, backgrounds, and modular scene assets in Aseprite. Use when the user needs tileset tiles, autotile edge and corner transitions, terrain pieces, props, or modular background sections for a game map.
---

# Tilesets and Environments

## Before drawing
Confirm tile dimensions, grid, perspective, terrain types, adjacency rules, collision needs, and target engine. Do not assume a tile size or autotile convention.

## Tile workflow
1. Set canvas and grid to verified dimensions.
2. Define terrain palette ramps and light direction.
3. Create representative base tiles.
4. Build edges, corners, transitions, inner corners, and variants required by the target ruleset.
5. Test adjacency visually in a mock map if possible.
6. Check seams at tile boundaries.
7. Add decorative props as separate tiles or layers where useful.
8. Export with the exact sheet layout and metadata expected by the engine.

## Environment consistency
- Maintain consistent perspective and scale.
- Keep walkable surfaces readable.
- Avoid high-contrast details that falsely resemble collision boundaries.
- Use restrained variation to prevent obvious repetition.
- Ensure shadows and highlights agree between neighboring tiles.
- Keep decorative overlays separate if the pipeline supports it.

## Acceptance criteria
- Every required tile type is present.
- Grid alignment is exact.
- No unintended gaps or edge seams.
- Repeated tiles do not produce obvious accidental patterns.
- Collision-relevant shapes are distinguishable or documented.
- Export layout matches the receiving engine's import rules.
