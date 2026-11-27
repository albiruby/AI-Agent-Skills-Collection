# 054-df-edge-wide-panels: Edge 540/840/1040/1050 Rectangular Cycling Panels

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `054-df-edge-wide-panels`

## Overview

Optimize rectangular grid layouts for Garmin Edge cycling computers (`246x322`, `282x470`, `480x800`) with 1-px divider lines.

## Production Monkey C Implementation Pattern

```monkeyc
public function drawEdgeGrid(dc as Dc, w as Number, h as Number) as Void {
    dc.setPenWidth(1);
    dc.setColor(Graphics.COLOR_DK_GRAY, Graphics.COLOR_TRANSPARENT);
    dc.drawLine(0, h / 2, w, h / 2);
    dc.drawLine(w / 2, 0, w / 2, h);
}
```

## Verification & Engineering Rules

- Edge cycling computers have zero bezel curvature (`getObscurityFlags() == 0`), allowing full edge-to-edge corner utilization.
