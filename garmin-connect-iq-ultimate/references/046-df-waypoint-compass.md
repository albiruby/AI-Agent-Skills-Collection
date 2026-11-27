# 046-df-waypoint-compass: Next Waypoint Distance, Bearing & Relative Arrow

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.bearing`
- **Sub-Skill ID**: `046-df-waypoint-compass`

## Overview

Compute relative turn angle (`bearing - track`) to draw a directional pointer arrow toward the next course waypoint.

## Production Monkey C Implementation Pattern

```monkeyc
if (info has :bearing && info.bearing != null && info has :track && info.track != null) {
    var relAngleRad = info.bearing - info.track;
    drawCompassArrow(dc, _cx, _cy, relAngleRad);
}
```

## Verification & Engineering Rules

- `info.bearing` and `info.track` are reported in radians (`-PI` to `+PI`).
