# 008-wf-buffered-bitmap: CIQ 4.0+ Graphics Pool BufferedBitmap Caching

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.BufferedBitmapReference`
- **Sub-Skill ID**: `008-wf-buffered-bitmap`

## Overview

Allocate offscreen background layers in the system Graphics Pool (`createBufferedBitmap`) on CIQ 4.0+ with automatic fallback for CIQ 3.x.

## Production Monkey C Implementation Pattern

```monkeyc
private var _bgBuffer as Graphics.BufferedBitmap or Null = null;

private function allocBuffer(w as Number, h as Number) as Void {
    var opts = {:width => w, :height => h};
    if (Graphics has :createBufferedBitmap) {
        var ref = Graphics.createBufferedBitmap(opts);
        _bgBuffer = ref.get() as Graphics.BufferedBitmap;
    } else {
        _bgBuffer = new Graphics.BufferedBitmap(opts);
    }
}
```

## Verification & Engineering Rules

- Draw static dials, tick marks, and HUD frames once into `_bgBuffer`, then blit with `dc.drawBitmap(0, 0, _bgBuffer)` in `onUpdate(dc)`.
