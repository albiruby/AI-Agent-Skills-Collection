# 104-wth-forecast-api: Toybox.Weather Current Conditions & Hourly Sparkline

- **Domain Category**: Weather
- **Primary Connect IQ API**: `Toybox.Weather`
- **Sub-Skill ID**: `104-wth-forecast-api`

## Overview

Read `Weather.getCurrentConditions()` and `Weather.getHourlyForecast()` with temperature unit conversion (`C` vs `F`).

## Production Monkey C Implementation Pattern

```monkeyc
private function formatTemp(celsius as Numeric) as String {
    if (System.getDeviceSettings().temperatureUnits == System.UNIT_STATUTE) {
        return ((celsius.toFloat() * 9.0f / 5.0f) + 32.0f).format("%.0f") + "F";
    }
    return celsius.format("%.0f") + "C";
}
```

## Verification & Engineering Rules

- `Weather.getCurrentConditions().temperature` is always returned in degrees Celsius regardless of user settings.
