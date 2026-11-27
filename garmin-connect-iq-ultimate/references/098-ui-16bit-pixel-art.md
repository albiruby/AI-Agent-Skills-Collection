# 098-ui-16bit-pixel-art: 16-Bit Pixel-Art Integer Grid & Non-Dithered Bitmaps

- **Domain Category**: UI-Theme
- **Primary Connect IQ API**: `WatchUi.BitmapResource`
- **Sub-Skill ID**: `098-ui-16bit-pixel-art`

## Overview

Render crisp 16-bit RPG pixel-art sprites and tilemaps on Garmin displays without anti-alias blurring or color dithering.

## Production Monkey C Implementation Pattern

```monkeyc
<!-- resources/drawables/drawables.xml -->
<drawables>
    <bitmap id="HeroSprite" filename="hero_32x32.png" dithering="none" packingFormat="png" />
</drawables>
```

## Verification & Engineering Rules

- Always set `dithering="none"` on pixel-art bitmaps so the Garmin resource compiler preserves crisp 1-px `#1E1410` espresso outlines.
