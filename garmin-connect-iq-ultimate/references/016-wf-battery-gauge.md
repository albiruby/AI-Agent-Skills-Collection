# 016-wf-battery-gauge: Battery Percentage & Remaining Days Estimation

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `System.Stats`
- **Sub-Skill ID**: `016-wf-battery-gauge`

## Overview

Read `System.getSystemStats().battery` and `batteryInDays` (CIQ 3.3+) with color-coded low-battery warnings.

## Production Monkey C Implementation Pattern

```monkeyc
var stats = System.getSystemStats();
var pct = stats.battery.toNumber();
var days = (stats has :batteryInDays && stats.batteryInDays != null)
    ? stats.batteryInDays.format("%.0f") + "d"
    : pct.toString() + "%";
```

## Verification & Engineering Rules

- Highlight battery below 20% in amber (`0xFFB300`) and below 10% in red (`0xFF1744`).
