# 097-ui-tactical-hud: Tactical Codec Corner Reticles & Scanline Frame

- **Domain Category**: UI-Theme
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `097-ui-tactical-hud`

## Overview

Draw military/codec corner brackets, degree tick rings, and CRT scanlines into a cached `BufferedBitmap` layer.

## Production Monkey C Implementation Pattern

```monkeyc
private function drawCornerBracket(dc as Dc, x as Number, y as Number, dx as Number, dy as Number, len as Number) as Void {
    dc.drawLine(x, y, x + dx * len, y);
    dc.drawLine(x, y, x, y + dy * len);
}
```

## Verification & Engineering Rules

- Render all static HUD frames once into a 4-color `BufferedBitmap` so frame render time stays under 2ms.
