# 017-wf-solar-intensity: Solar Charging Intensity Ring (Solar Watches)

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `System.Stats.solarIntensity`
- **Sub-Skill ID**: `017-wf-solar-intensity`

## Overview

Read `stats.solarIntensity` on Fenix Solar, Instinct Solar, and Forerunner 955 Solar models (`0..100` scale).

## Production Monkey C Implementation Pattern

```monkeyc
var stats = System.getSystemStats();
if (stats has :solarIntensity && stats.solarIntensity != null && stats.solarIntensity >= 0) {
    var solarPct = stats.solarIntensity; // 0 to 100
    drawSolarGauge(dc, solarPct);
}
```

## Verification & Engineering Rules

- `solarIntensity` returns `null` or a negative value on non-solar devices or when solar charging is inactive.
