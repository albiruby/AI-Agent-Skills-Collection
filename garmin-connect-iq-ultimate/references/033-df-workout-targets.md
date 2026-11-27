# 033-df-workout-targets: Structured Workout Step & Target Range Inspector

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.getCurrentWorkoutStep`
- **Sub-Skill ID**: `033-df-workout-targets`

## Overview

Read active interval targets (`step.targetType`, `targetValueLow`, `targetValueHigh`) during structured Garmin workouts.

## Production Monkey C Implementation Pattern

```monkeyc
if (Activity has :getCurrentWorkoutStep) {
    var stepInfo = Activity.getCurrentWorkoutStep();
    if (stepInfo != null && stepInfo.step instanceof Activity.WorkoutStep) {
        var step = stepInfo.step as Activity.WorkoutStep;
        var low = step.targetValueLow;
        var high = step.targetValueHigh;
    }
}
```

## Verification & Engineering Rules

- Check `if (stepInfo.step instanceof Activity.WorkoutIntervalStep)` when handling repeat blocks.
