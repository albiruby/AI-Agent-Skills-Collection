# 007-wf-amoled-dim-mask: AMOLED 10% Lit-Pixel Luminance Dither Mask

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `007-wf-amoled-dim-mask`

## Overview

Enforce the <10% active pixel ceiling in AMOLED Always-On Display mode using a checkerboard scanline mask over thick digits or icons.

## Production Monkey C Implementation Pattern

```monkeyc
private function applyScanlineDimmer(dc as Dc, x as Number, y as Number, w as Number, h as Number) as Void {
    dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_TRANSPARENT);
    dc.setPenWidth(1);
    for (var row = y; row < y + h; row += 2) {
        dc.drawLine(x, row, x + w, row);
    }
}
```

## Verification & Engineering Rules

- Even a 50% scanline strip cuts lit pixel count in half and prevents simulator AOD burn-in errors on thick typography.
