# 036-df-pace-smoothing: Rolling 5-Second Running Pace Filter (min/km & min/mi)

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.currentSpeed`
- **Sub-Skill ID**: `036-df-pace-smoothing`

## Overview

Smooth noisy instantaneous GPS speed (`m/s`) using a 5-sample circular buffer and format into `MM:SS` pace.

## Production Monkey C Implementation Pattern

```monkeyc
private function speedToPaceStr(mps as Float, isMetric as Boolean) as String {
    if (mps <= 0.3f) { return "--:--"; }
    var secPerUnit = (isMetric ? 1000.0f : 1609.344f) / mps;
    var totalSec = secPerUnit.toNumber();
    var mins = totalSec / 60;
    var secs = totalSec % 60;
    return mins.toString() + ":" + secs.format("%02d");
}
```

## Verification & Engineering Rules

- Check `System.getDeviceSettings().paceUnits == System.UNIT_STATUTE` to honor mile vs kilometer user preferences.
