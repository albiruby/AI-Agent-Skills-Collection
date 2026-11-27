# 099-ui-palette-lock: 3-Tone Cel-Shaded Hex Palette Lock for MIP & AMOLED

- **Domain Category**: UI-Theme
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `099-ui-palette-lock`

## Overview

Define explicit `<palette>` color locks on bitmaps and vector themes so 64-color MIP and 65K-color AMOLED screens match cleanly.

## Production Monkey C Implementation Pattern

```monkeyc
<bitmap id="TileSet" filename="tiles.png" dithering="none">
    <palette disableTransparency="false">
        <color>1E1410</color>
        <color>C68652</color>
        <color>F4EBD0</color>
        <color>9E2A2B</color>
        <color>5C3A21</color>
    </palette>
</bitmap>
```

## Verification & Engineering Rules

- On 64-color MIP displays, test palettes against the 6-bit RGB (`00, 55, AA, FF` per channel) hardware color cube.
