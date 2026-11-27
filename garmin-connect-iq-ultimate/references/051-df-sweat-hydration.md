# 051-df-sweat-hydration: Sweat Rate & Sodium Electrolyte Depletion Model

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info`
- **Sub-Skill ID**: `051-df-sweat-hydration`

## Overview

Estimate cumulative fluid loss (`mL`) and sodium loss (`mg`) based on workout duration, intensity, and ambient temperature.

## Production Monkey C Implementation Pattern

```monkeyc
public function calcSweatMlPerHour(baseMlHr as Number, tempC as Float, intensityRatio as Float) as Number {
    var tempFactor = (tempC > 20.0f) ? (1.0f + (tempC - 20.0f) * 0.035f) : 1.0f;
    return (baseMlHr.toFloat() * tempFactor * intensityRatio).toNumber();
}
```

## Verification & Engineering Rules

- Let the athlete configure their baseline sweat rate (`500..2000 mL/h`) and sweat sodium concentration (`500..1500 mg/L`) in settings.
