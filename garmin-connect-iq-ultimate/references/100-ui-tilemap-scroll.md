# 100-ui-tilemap-scroll: 3/4 Top-Down Orthographic Tilemap Viewport Scroller

- **Domain Category**: UI-Theme
- **Primary Connect IQ API**: `Graphics.Dc.drawBitmap2`
- **Sub-Skill ID**: `100-ui-tilemap-scroll`

## Overview

Render a scrolling 16x16 or 32x32 tilemap background driven by daily step progress (e.g., transitioning from village to forest).

## Production Monkey C Implementation Pattern

```monkeyc
// Map step ratio (0.0 .. 1.0) to camera X offset across the tilemap array
```

## Verification & Engineering Rules

- Blit only the visible tiles intersecting the watch viewport (`dc.getWidth() x dc.getHeight()`).
