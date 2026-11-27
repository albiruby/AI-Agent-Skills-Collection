# 049-df-kcal-burn-rate: Real-Time Caloric Burn Rate (kcal/h & kcal/km)

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.energyExpenditure`
- **Sub-Skill ID**: `049-df-kcal-burn-rate`

## Overview

Convert `info.energyExpenditure` (`kcal/min`) into hourly burn rate (`kcal/h`) and cumulative `info.calories`.

## Production Monkey C Implementation Pattern

```monkeyc
var kcalPerHour = 0;
if (info has :energyExpenditure && info.energyExpenditure != null) {
    kcalPerHour = (info.energyExpenditure * 60.0f).toNumber();
}
```

## Verification & Engineering Rules

- Fall back to `info.calories * 3600000 / info.timerTime` if `energyExpenditure` returns `null`.
