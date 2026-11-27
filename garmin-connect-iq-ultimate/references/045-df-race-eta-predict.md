# 045-df-race-eta-predict: Finish Time Predictor & Target Distance ETA

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.elapsedDistance`
- **Sub-Skill ID**: `045-df-race-eta-predict`

## Overview

Project finish time and ETA for target race distances (5K, 10K, Half Marathon, Marathon, 100K Ultra) by blending overall average speed with current rolling speed.

## Production Monkey C Implementation Pattern

```monkeyc
public function predictRemainingSec(targetMeters as Float, elapsedMeters as Float, blendedMps as Float) as Number {
    var rem = targetMeters - elapsedMeters;
    if (rem <= 0.0f || blendedMps <= 0.2f) { return 0; }
    return (rem / blendedMps).toNumber();
}
```

## Verification & Engineering Rules

- Weight `blendedMps = 0.7 * avgSpeed + 0.3 * rolling30sSpeed` for realistic race pacing projections.
