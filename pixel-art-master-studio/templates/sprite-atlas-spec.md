# Sprite Atlas Specification

## Atlas

- Name/version:
- Dimensions:
- Cell size:
- Padding/extrusion:
- Max texture size:
- Packing rule:

## Frames

| Asset | State | Direction | Frames | Cell | Pivot | Durations (ms) | Tags |
|---|---|---|---:|---|---:|---|---|
| | | | | | | | |

## Layout

```text
<rows/columns/frame order or link to atlas image>
```

## Metadata

- Format: JSON / XML / engine-native
- Frame tags:
- Durations:
- Pivot/origin:
- Events (hitbox, VFX, sound):

## Engine import

- Engine/version:
- Filter/compression:
- Scale/PPU:
- Animation controller:
- Collision/physics:
- Sorting layer:

## QA

- [ ] Every frame present and correctly ordered
- [ ] Pivot/baseline consistent
- [ ] No bleeding or clipping
- [ ] Metadata matches frames
- [ ] Engine playback tested
- [ ] Lossless masters/sources retained
