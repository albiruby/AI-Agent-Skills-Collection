# 043-df-vertical-speed-vam: Vertical Ascent Speed (VAM m/h & ft/h)

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.verticalSpeed`
- **Sub-Skill ID**: `043-df-vertical-speed-vam`

## Overview

Convert `info.verticalSpeed` (`m/s`) into climbing VAM (Velocita Ascensionale Media in `m/h`) for mountain running and cycling.

## Production Monkey C Implementation Pattern

```monkeyc
var vamMetersPerHour = 0;
if (info has :verticalSpeed && info.verticalSpeed != null) {
    vamMetersPerHour = (info.verticalSpeed * 3600.0f).toNumber();
}
```

## Verification & Engineering Rules

- Apply a 10-second rolling average to `verticalSpeed` to eliminate barometric altimeter step noise.
