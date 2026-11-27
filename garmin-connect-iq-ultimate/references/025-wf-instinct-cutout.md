# 025-wf-instinct-cutout: Instinct 2 / Crossover Subscreen Cutout Alignment

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `WatchUi.getSubscreen`
- **Sub-Skill ID**: `025-wf-instinct-cutout`

## Overview

Query the exact bounding rectangle of the circular physical subscreen on Garmin Instinct 2 and Instinct Crossover watches.

## Production Monkey C Implementation Pattern

```monkeyc
private var _subRect as Graphics.BoundingBox or Null = null;

public function onLayout(dc as Dc) as Void {
    if (WatchUi has :getSubscreen) {
        _subRect = WatchUi.getSubscreen();
    }
}

private function drawSubscreenMetric(dc as Dc, val as String) as Void {
    if (_subRect != null) {
        var scx = _subRect.x + (_subRect.width / 2);
        var scy = _subRect.y + (_subRect.height / 2);
        dc.drawText(scx, scy, Graphics.FONT_SMALL, val,
            Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
```

## Verification & Engineering Rules

- Never draw main time digits across `_subRect`, as the raised plastic bezel ring on Instinct 2 obscures that region.
