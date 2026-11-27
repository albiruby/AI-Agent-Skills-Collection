# 014-wf-radial-arc-gauges: Segmented Radial Arc Gauges & Angle Mapping

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc.drawArc`
- **Sub-Skill ID**: `014-wf-radial-arc-gauges`

## Overview

Convert normalized ratios (`0.0 .. 1.0`) into Garmin `drawArc` degree coordinates (`0` = 3 o'clock, `90` = 12 o'clock).

## Production Monkey C Implementation Pattern

```monkeyc
private function drawProgressArc(dc as Dc, cx as Number, cy as Number, r as Number, ratio as Float, color as Number) as Void {
    var clamped = (ratio < 0.0f) ? 0.0f : ((ratio > 1.0f) ? 1.0f : ratio);
    var sweep = (clamped * 240.0f).toNumber();
    if (sweep <= 0) { return; }
    var startDeg = 210;
    var endDeg = (startDeg - sweep + 360) % 360;
    dc.setPenWidth(6);
    dc.setColor(color, Graphics.COLOR_TRANSPARENT);
    dc.drawArc(cx, cy, r, Graphics.ARC_CLOCKWISE, startDeg, endDeg);
}
```

## Verification & Engineering Rules

- Guard `startDeg == endDeg` before calling `dc.drawArc()`, because Garmin draws a full 360-degree circle when start and end angles are equal.
