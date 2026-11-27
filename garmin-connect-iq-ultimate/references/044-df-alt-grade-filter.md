# 044-df-alt-grade-filter: Barometric Altitude & Road Gradient (%) Kalman Filter

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.altitude`
- **Sub-Skill ID**: `044-df-alt-grade-filter`

## Overview

Compute smooth road slope percentage (`100 * deltaAltitude / deltaDistance`) using a distance-gated ring buffer.

## Production Monkey C Implementation Pattern

```monkeyc
private var _lastDist as Float = 0.0f;
private var _lastAlt as Float = 0.0f;
private var _gradePct as Float = 0.0f;

public function updateGrade(dist as Float, alt as Float) as Float {
    var dDist = dist - _lastDist;
    if (dDist >= 12.0f) {
        _gradePct = ((alt - _lastAlt) / dDist) * 100.0f;
        _lastDist = dist;
        _lastAlt = alt;
    }
    return _gradePct;
}
```

## Verification & Engineering Rules

- Never update gradient when horizontal distance delta is under 10 meters, or GPS jitter will cause wild slope spikes.
