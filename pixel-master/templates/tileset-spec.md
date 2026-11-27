# Tileset Specification

## Grid

- Tile size:
- Atlas dimensions:
- Native viewport:
- Pixel scale:
- Projection:

## Terrain sets

| Set | Tiles | Bitmask | Transitions | Collision |
|---|---:|---|---|---|
| grass | | 4/8-neighbor | dirt/path/water | solid |
| water | | | shore | blocked |
| cliff | | | top/edge | one-way |

## Layout

```text
<atlas layout / rows / columns / padding / extrusion>
```

## Bitmask

- Neighbor convention: N/E/S/W or 8-way
- Bit order:
- Lookup table:
- Priority when terrains overlap:

## Collision

- Visual/collision separation:
- One-way platforms:
- Slopes/ladders/hazards:
- Character clearance:

## Animated tiles

| Tile | Frames | Duration (ms) | Loop | Notes |
|---|---:|---:|---|---|
| | | | | |

## QA

- [ ] All corners/edges/transitions exist
- [ ] No seams or bleeding at integer scale
- [ ] Repetition controlled
- [ ] Collision matches visuals
- [ ] Animated tiles loop
- [ ] Engine import tested
