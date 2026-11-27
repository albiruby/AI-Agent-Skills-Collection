# 058-fit-lap-columns: MESG_TYPE_LAP Custom Lap Table Columns

- **Domain Category**: FitContributor
- **Primary Connect IQ API**: `FitContributor.MESG_TYPE_LAP`
- **Sub-Skill ID**: `058-fit-lap-columns`

## Overview

Add custom developer columns to the Splits/Laps table in Garmin Connect Mobile and Web.

## Production Monkey C Implementation Pattern

```monkeyc
_lapField = createField("lap_carbs", 1, FitContributor.DATA_TYPE_UINT16, {
    :mesgType => FitContributor.MESG_TYPE_LAP,
    :units => "g"
});
```

## Verification & Engineering Rules

- Call `_lapField.setData(currentLapValue)` continuously inside `compute(info)` and reset your counter inside `onTimerLap()`.
