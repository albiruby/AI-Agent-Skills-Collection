# 037-df-gap-minetti: Grade Adjusted Pace (GAP) Minetti Cost Model

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info`
- **Sub-Skill ID**: `037-df-gap-minetti`

## Overview

Compute Grade Adjusted Pace by scaling horizontal speed with Minetti's polynomial metabolic cost of running on uphill/downhill gradients.

## Production Monkey C Implementation Pattern

```monkeyc
private function calcGapFactor(gradeRatio as Float) as Float {
    var g = (gradeRatio < -0.30f) ? -0.30f : ((gradeRatio > 0.30f) ? 0.30f : gradeRatio);
    // Minetti cost relative to flat running (3.6 J/kg/m)
    var cost = 155.4f*g*g*g*g*g - 30.4f*g*g*g*g - 43.3f*g*g*g + 46.3f*g*g + 19.5f*g + 3.6f;
    return cost / 3.6f;
}
```

## Verification & Engineering Rules

- Smooth altitude delta over at least 15 meters of horizontal distance before calculating `gradeRatio = dAlt / dDist`.
