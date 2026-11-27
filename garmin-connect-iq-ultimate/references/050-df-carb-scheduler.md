# 050-df-carb-scheduler: Glycogen Depletion & Carbohydrate Intake Codec

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info`
- **Sub-Skill ID**: `050-df-carb-scheduler`

## Overview

Model intensity-adjusted carbohydrate oxidation (`g/min`) across HR zones and trigger periodic gel refueling countdowns.

## Production Monkey C Implementation Pattern

```monkeyc
public function calcCarbGramsPerMin(kcalPerMin as Float, hrRatio as Float) as Float {
    // Higher %HRMax shifts substrate oxidation from fat toward glycogen
    var choFraction = (hrRatio < 0.65f) ? 0.40f : ((hrRatio < 0.80f) ? 0.68f : 0.88f);
    return (kcalPerMin * choFraction) / 4.0f; // 4 kcal per gram of carbohydrate
}
```

## Verification & Engineering Rules

- Track net glycogen balance (`consumedGrams - burnedGrams`) to prevent bonking in marathons and ultras.
