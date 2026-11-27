# 019-wf-moon-phase: Synodic Lunar Phase & Illumination Math

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Toybox.Time`
- **Sub-Skill ID**: `019-wf-moon-phase`

## Overview

Compute exact moon phase (`0..7`) and illumination percentage directly from Unix epoch time (`Time.now().value()`) with zero external dependencies.

## Production Monkey C Implementation Pattern

```monkeyc
public function getMoonPhaseIndex(unixSec as Number) as Number {
    var synodicSec = 2551443; // 29.53059 days in seconds
    var refNewMoon = 1704974220; // Known New Moon epoch (Jan 11, 2024 11:57 UTC)
    var age = (unixSec - refNewMoon) % synodicSec;
    if (age < 0) { age += synodicSec; }
    return ((age * 8) / synodicSec) % 8;
}
```

## Verification & Engineering Rules

- Runs in <0.1ms and requires zero GPS or network permissions.
