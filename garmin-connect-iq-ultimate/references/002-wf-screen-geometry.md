# 002-wf-screen-geometry: Screen Geometry & Safe-Zone Anchor Caching

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `002-wf-screen-geometry`

## Overview

Precompute screen dimensions, radial safe zones, and proportional layout anchors once in `onLayout(dc)` to eliminate per-frame division and float math.

## Production Monkey C Implementation Pattern

```monkeyc
private var _w as Number = 260;
private var _h as Number = 260;
private var _cx as Number = 130;
private var _cy as Number = 130;
private var _safeRadius as Number = 118;

public function onLayout(dc as Dc) as Void {
    _w = dc.getWidth();
    _h = dc.getHeight();
    _cx = _w / 2;
    _cy = _h / 2;
    _safeRadius = ((_w < _h ? _w : _h) * 45) / 100;
}
```

## Verification & Engineering Rules

- Avoid recalculating `dc.getWidth() / 2` dozens of times per `onUpdate(dc)` call.
- Keep text labels inside `0.90 * radius` on round displays to avoid bezel clipping.
