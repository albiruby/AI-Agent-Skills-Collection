# 052-df-cardiac-drift: Cardiac Drift & Thermal Strain Index

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info`
- **Sub-Skill ID**: `052-df-cardiac-drift`

## Overview

Calculate Aerobic Decoupling (`Pa:Hr` or `Pw:Hr` drift %) between the first half and second half of an endurance session.

## Production Monkey C Implementation Pattern

```monkeyc
public function calcDecouplingPct(efFirstHalf as Float, efSecondHalf as Float) as Float {
    if (efFirstHalf <= 0.0f) { return 0.0f; }
    return ((efFirstHalf - efSecondHalf) / efFirstHalf) * 100.0f;
}
```

## Verification & Engineering Rules

- Decoupling above 5.0% signals significant thermal strain, dehydration, or aerobic fatigue.
