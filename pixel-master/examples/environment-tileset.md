# Example: Environment and Tileset

## Brief

A 16x16 top-down grass/forest tileset with cliffs, water, paths, props, parallax, and a playable test map in Godot 4.

## 1. Lock the spec

- Native viewport: 320x180 (4x to 720p, 6x to 1080p).
- Tile size: 16x16; character cell 16x24.
- Projection: top-down 3/4.
- Palette: 24 colors; light top-left.
- Terrain: grass, dirt path, water, cliff, forest edge.
- Autotile: 3x3 minimal set + inner corners; expand to blob/47 if needed.

Use `../templates/tileset-spec.md`.

## 2. Terrain plan

| Terrain | Tiles | Transitions | Collision |
|---|---|---|---|
| grass | base + variants | dirt/path/water/forest | walkable |
| dirt path | straight/corner/T/cross | grass | walkable |
| water | center/shore/corner | grass/cliff | blocked |
| cliff | top/edge/corner | grass/water | blocked/one-way |
| forest edge | edge/corner | grass | blocked |

- Define the neighbor bitmask and priority.
- Add 1-2 px atlas extrusion.
- Keep repetition controlled with variants and decals.

## 3. Production

1. Draw the 3x3 minimal set first; test every adjacency.
2. Add corners, ends, single tiles, and inner corners.
3. Add props (rocks, bushes, signs) and ensure value separation from characters.
4. Build 2-3 parallax layers with compressed contrast.
5. Assemble a test map with tight corridors, open areas, and terrain transitions.

## 4. Engine integration

- Godot 4 TileSet: terrain sets, physics layers, custom data for hazards.
- Nearest filtering, no compression/mipmaps, integer scaling, pixel snap.
- Test camera pan, diagonal movement, and all terrain seams.

## 5. QA

- [ ] No seams/gaps at 1x and integer zoom.
- [ ] All transition combinations exist.
- [ ] Collision matches visuals.
- [ ] Characters read against every terrain.
- [ ] Props do not look like interactive tiles unless intended.
- [ ] Parallax values compressed.
- [ ] Engine import and test map verified.

## 6. Handoff

Deliver atlas, tile metadata/TSX or engine resource, collision notes, test map, manifest, and QA report.
