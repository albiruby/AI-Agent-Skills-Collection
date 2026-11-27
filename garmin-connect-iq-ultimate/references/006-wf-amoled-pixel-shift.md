# 006-wf-amoled-pixel-shift: AMOLED Deterministic Lissajous Pixel Shifter

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `006-wf-amoled-pixel-shift`

## Overview

Shift all rendered elements in AMOLED sleep mode every minute across a 3x3 grid so no single organic LED pixel stays continuously illuminated for more than 3 minutes.

## Production Monkey C Implementation Pattern

```monkeyc
private function getAodOffset(minute as Number) as [Number, Number] {
    var dx = ((minute % 3) - 1) * 4;
    var dy = (((minute / 3) % 3) - 1) * 4;
    return [dx, dy];
}
```

## Verification & Engineering Rules

- Use thin font strokes (`FONT_SYSTEM_NUMBER_MILD` or custom hollow fonts) so shifted positions never overlap the same lit pixels across consecutive minutes.
