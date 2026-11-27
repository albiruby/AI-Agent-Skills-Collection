# 018-wf-sunrise-sunset: Sunrise, Sunset & Golden Hour Calculation

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Toybox.Weather`
- **Sub-Skill ID**: `018-wf-sunrise-sunset`

## Overview

Retrieve accurate local sunrise and sunset `Time.Moment` values using `Weather.getSunrise()` and `Weather.getSunset()`.

## Production Monkey C Implementation Pattern

```monkeyc
private function getSunTimes() as [Time.Moment or Null, Time.Moment or Null] {
    if (!(Toybox has :Weather)) { return [null, null]; }
    var cond = Weather.getCurrentConditions();
    if (cond == null || cond.observationLocationPosition == null) {
        return [null, null];
    }
    var now = Time.now();
    var pos = cond.observationLocationPosition;
    return [Weather.getSunrise(pos, now), Weather.getSunset(pos, now)];
}
```

## Verification & Engineering Rules

- Format returned `Moment` objects with `Time.Gregorian.info(moment, Time.FORMAT_SHORT)`.
