# 032-df-lap-accumulator: Lap Button Event & Per-Lap Metric Snapshot

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.DataField.onTimerLap`
- **Sub-Skill ID**: `032-df-lap-accumulator`

## Overview

Capture per-lap averages and totals in `onTimerLap()` before resetting lap-specific accumulators.

## Production Monkey C Implementation Pattern

```monkeyc
private var _lapPowerSum as Number = 0;
private var _lapSamples as Number = 0;
private var _lastLapAvgPower as Number = 0;

public function onTimerLap() as Void {
    if (_lapSamples > 0) {
        _lastLapAvgPower = _lapPowerSum / _lapSamples;
    }
    _lapPowerSum = 0;
    _lapSamples = 0;
}
```

## Verification & Engineering Rules

- If writing a `MESG_TYPE_LAP` FitContributor field, update it with `setData()` continuously during the lap so the latest value is ready when the lap closes.
