# 027-df-compute-vs-onupdate: Separation of 1Hz compute(info) vs Visible onUpdate(dc)

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.DataField`
- **Sub-Skill ID**: `027-df-compute-vs-onupdate`

## Overview

Execute all telemetry accumulation, timers, and FIT file recording in `compute(info)` so state stays accurate even when the user scrolls to another data screen.

## Production Monkey C Implementation Pattern

```monkeyc
private var _cumSec as Number = 0;
private var _displayStr as String = "--";

public function compute(info as Activity.Info) as Void {
    _cumSec++;
    if (info has :currentHeartRate && info.currentHeartRate != null) {
        _displayStr = info.currentHeartRate.toString();
    }
}

public function onUpdate(dc as Dc) as Void {
    // Only executes when this data page is on screen
    dc.drawText(dc.getWidth() / 2, dc.getHeight() / 2, Graphics.FONT_NUMBER_MEDIUM,
        _displayStr, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
}
```

## Verification & Engineering Rules

- Never put cumulative counters or `FitContributor.setData()` inside `onUpdate(dc)`, because `onUpdate(dc)` pauses whenever the user views the map or another data page.
