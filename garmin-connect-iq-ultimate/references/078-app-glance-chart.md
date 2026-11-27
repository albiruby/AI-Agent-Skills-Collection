# 078-app-glance-chart: Glance Sparkline Mini-Chart & Cached Telemetry

- **Domain Category**: Glance
- **Primary Connect IQ API**: `WatchUi.GlanceView`
- **Sub-Skill ID**: `078-app-glance-chart`

## Overview

Draw a compact polyline sparkline inside `GlanceView.onUpdate(dc)` using `dc.getWidth()` and `dc.getHeight()`.

## Production Monkey C Implementation Pattern

```monkeyc
// Scale y-coordinates to [4 .. dc.getHeight() - 4] inside GlanceView.onUpdate(dc)
```

## Verification & Engineering Rules

- Never clear background to opaque black in `GlanceView` on AMOLED devices if using native system glance styling.
