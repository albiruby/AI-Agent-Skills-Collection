# Palette Specification

- Name/version:
- Paradigm:
- Color budget:
- Source/inspiration (license):

## Palette table

| Index | Hex | Role | Ramp/material | Notes |
|---:|---|---|---|---|
| 0 | #000000 | outline | universal | |
| 1 | #1a1c2c | shadow | cloth | |
| 2 | #5d275d | mid | cloth | |
| 3 | #b13e53 | highlight | cloth | |
| 4 | #ef7d57 | accent | skin | |

## Ramps

```text
skin:    [1, 2, 3]
cloth:   [1, 4]
metal:   [0, 1, 4]
VFX:     [3, 4] + alpha
```

## Rules

- Light direction:
- Hue shift:
- Saturation/value policy:
- Dithering:
- AA/outline:
- Forbidden colors:
- Grayscale check:

## Usage

- Characters:
- Environments:
- UI:
- VFX:
- Backgrounds/parallax:

## Validation

- [ ] Unique colors ≤ budget
- [ ] Palette compliance checked
- [ ] Value hierarchy works in grayscale
- [ ] Materials remain distinct
- [ ] Palette recorded in manifest/style bible
