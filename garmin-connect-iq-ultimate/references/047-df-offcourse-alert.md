# 047-df-offcourse-alert: Course Navigation Off-Course Distance Monitor

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.offCourseDistance`
- **Sub-Skill ID**: `047-df-offcourse-alert`

## Overview

Monitor `info.offCourseDistance` (meters) during trail/course navigation and highlight the field in red when drift exceeds 30 meters.

## Production Monkey C Implementation Pattern

```monkeyc
var offDist = (info has :offCourseDistance && info.offCourseDistance != null)
    ? info.offCourseDistance : 0.0f;
if (offDist > 30.0f) {
    dc.setColor(0xFF1744, Graphics.COLOR_TRANSPARENT);
}
```

## Verification & Engineering Rules

- Pair with `info.distanceToNextPoint` and `info.elevationAtNextPoint` to build complete trail aid-station dashboards.
