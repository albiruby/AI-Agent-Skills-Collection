# 011-wf-antialias-draw: Hardware Anti-Aliasing for Vectors & Arcs

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc.setAntiAlias`
- **Sub-Skill ID**: `011-wf-antialias-draw`

## Overview

Enable hardware anti-aliasing on supported CIQ 3.2+ devices before drawing polygons, lines, and radial arcs.

## Production Monkey C Implementation Pattern

```monkeyc
if (dc has :setAntiAlias) {
    dc.setAntiAlias(true);
}
dc.setPenWidth(3);
dc.drawArc(_cx, _cy, _safeRadius, Graphics.ARC_CLOCKWISE, 90, 270);
```

## Verification & Engineering Rules

- Disable anti-aliasing when rendering crisp 1-px pixel-art outlines or monochrome Instinct displays.
