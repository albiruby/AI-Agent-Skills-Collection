# 096-ui-ecg-bio-monitor: Resident Evil Bio-Monitor ECG Waveform Renderer

- **Domain Category**: UI-Theme
- **Primary Connect IQ API**: `Graphics.Dc.drawLine`
- **Sub-Skill ID**: `096-ui-ecg-bio-monitor`

## Overview

Render an authentic survival-horror inventory ECG monitor (`FINE`, `CAUTION`, `DANGER`) synced to live Heart Rate BPM.

## Production Monkey C Implementation Pattern

```monkeyc
// Normalized P-Q-R-S-T lookup table (16 steps per beat):
private var _ecgLut as Array<Number> = [0, 0, -3, 2, -18, 24, -8, 0, 0, 4, 6, 3, 0, 0, 0, 0];

private function drawEcgTrace(dc as Dc, x0 as Number, yMid as Number, width as Number, color as Number) as Void {
    dc.setColor(color, Graphics.COLOR_TRANSPARENT);
    dc.setPenWidth(2);
    var prevX = x0;
    var prevY = yMid;
    for (var i = 0; i < 32; i++) {
        var curX = x0 + (i * width) / 32;
        var curY = yMid + _ecgLut[i % 16];
        dc.drawLine(prevX, prevY, curX, curY);
        prevX = curX;
        prevY = curY;
    }
}
```

## Verification & Engineering Rules

- Color map: `<100 bpm` = `#00E676` (FINE), `100..135 bpm` = `#FFB300` (CAUTION), `136..160 bpm` = `#FF6D00` (CAUTION), `>160 bpm` = `#FF1744` (DANGER).
