# 009-wf-palette-compress: Indexed Palette Compression for Offscreen Buffers

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.BufferedBitmap`
- **Sub-Skill ID**: `009-wf-palette-compress`

## Overview

Restrict `BufferedBitmap` color palettes to 4 or 16 colors so offscreen buffers consume 2-bpp or 4-bpp instead of full 8/16-bpp memory.

## Production Monkey C Implementation Pattern

```monkeyc
var opts = {
    :width => dc.getWidth(),
    :height => dc.getHeight(),
    :palette => [
        Graphics.COLOR_BLACK,
        0x004D25,
        0x00E676,
        Graphics.COLOR_WHITE
    ]
};
```

## Verification & Engineering Rules

- Every color drawn into a paletted `BufferedBitmap` must exist in `:palette`, or the graphics engine will snap to the nearest color.
