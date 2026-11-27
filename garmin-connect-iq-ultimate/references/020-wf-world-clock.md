# 020-wf-world-clock: Dual Timezone & UTC Offset World Clock

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `System.ClockTime`
- **Sub-Skill ID**: `020-wf-world-clock`

## Overview

Calculate UTC time and secondary timezone offsets using `System.getClockTime().timeZoneOffset` and `Time.Moment` arithmetic.

## Production Monkey C Implementation Pattern

```monkeyc
var clock = System.getClockTime();
var utcNow = Time.now().add(new Time.Duration(-clock.timeZoneOffset));
var targetOffsetSec = 9 * 3600; // e.g. JST (UTC+9)
var targetMoment = utcNow.add(new Time.Duration(targetOffsetSec));
var targetInfo = Time.Gregorian.utcInfo(targetMoment, Time.FORMAT_SHORT);
```

## Verification & Engineering Rules

- Use `Gregorian.utcInfo()` after manually applying `timeZoneOffset` so local DST rules are not double-applied.
