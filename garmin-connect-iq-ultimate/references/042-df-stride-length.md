# 042-df-stride-length: Running Cadence & Real-Time Stride Length Math

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.currentCadence`
- **Sub-Skill ID**: `042-df-stride-length`

## Overview

Derive instantaneous stride length in meters (`speedMetersPerMin / cadenceSpm`) from `currentSpeed` and `currentCadence`.

## Production Monkey C Implementation Pattern

```monkeyc
public function calcStrideLengthMeters(speedMps as Float, cadenceSpm as Number) as Float {
    if (cadenceSpm <= 0 || speedMps <= 0.1f) { return 0.0f; }
    return (speedMps * 60.0f) / cadenceSpm.toFloat();
}
```

## Verification & Engineering Rules

- Garmin reports running `currentCadence` in total steps per minute (both feet), whereas cycling cadence is revolutions per minute.
