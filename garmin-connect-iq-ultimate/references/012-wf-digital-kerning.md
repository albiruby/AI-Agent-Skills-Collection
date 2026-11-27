# 012-wf-digital-kerning: Tabular Monospace Digital Time Kerning

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc.getTextDimensions`
- **Sub-Skill ID**: `012-wf-digital-kerning`

## Overview

Render digital hours and minutes at fixed horizontal offsets so proportional system fonts never jitter when digits change from `11` to `08`.

## Production Monkey C Implementation Pattern

```monkeyc
private function drawFixedDigits(dc as Dc, cx as Number, cy as Number, text as String, font as FontDefinition, stepX as Number) as Void {
    var chars = text.toCharArray();
    var startX = cx - ((chars.size() - 1) * stepX) / 2;
    for (var i = 0; i < chars.size(); i++) {
        dc.drawText(startX + (i * stepX), cy, font, chars[i].toString(),
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
```

## Verification & Engineering Rules

- Measure the widest glyph `'8'` once in `onLayout(dc)` via `dc.getTextWidthInPixels("8", font)` to set `stepX`.
