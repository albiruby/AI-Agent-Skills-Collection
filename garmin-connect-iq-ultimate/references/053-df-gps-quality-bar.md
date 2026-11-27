# 053-df-gps-quality-bar: GPS Constellation Quality & Accuracy Indicator

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.currentLocationAccuracy`
- **Sub-Skill ID**: `053-df-gps-quality-bar`

## Overview

Map `info.currentLocationAccuracy` (`QUALITY_NOT_AVAILABLE` .. `QUALITY_GOOD`) into a 4-bar satellite signal widget.

## Production Monkey C Implementation Pattern

```monkeyc
var acc = (info has :currentLocationAccuracy && info.currentLocationAccuracy != null)
    ? info.currentLocationAccuracy : Position.QUALITY_NOT_AVAILABLE;
```

## Verification & Engineering Rules

- Render 4 green bars for `QUALITY_GOOD`, 3 amber bars for `QUALITY_USABLE`, and 1 red bar for `QUALITY_POOR`.
