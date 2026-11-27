# 101-bio-body-battery: SensorHistory Body Battery & All-Day Stress Streams

- **Domain Category**: Biometrics
- **Primary Connect IQ API**: `Toybox.SensorHistory`
- **Sub-Skill ID**: `101-bio-body-battery`

## Overview

Read Garmin Body Battery (`0..100`) and Stress (`0..100`) from `Toybox.SensorHistory` with capability guards.

## Production Monkey C Implementation Pattern

```monkeyc
private function getLatestBodyBattery() as Number or Null {
    if ((Toybox has :SensorHistory) && (SensorHistory has :getBodyBatteryHistory)) {
        var iter = SensorHistory.getBodyBatteryHistory({:period => 1, :order => SensorHistory.ORDER_NEWEST_FIRST});
        var sample = iter.next();
        if (sample != null && sample.data != null) {
            return sample.data.toNumber();
        }
    }
    return null;
}
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="SensorHistory"/>` in `manifest.xml`.
