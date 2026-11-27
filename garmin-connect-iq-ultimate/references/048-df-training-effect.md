# 048-df-training-effect: Dual Aerobic & Anaerobic Training Effect Bars

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.trainingEffect`
- **Sub-Skill ID**: `048-df-training-effect`

## Overview

Read `info.trainingEffect` and `info.anaerobicTrainingEffect` (`0.0 .. 5.0` scale) to render side-by-side physiological load bars.

## Production Monkey C Implementation Pattern

```monkeyc
var aero = (info has :trainingEffect && info.trainingEffect != null) ? info.trainingEffect : 0.0f;
var anaero = (info has :anaerobicTrainingEffect && info.anaerobicTrainingEffect != null) ? info.anaerobicTrainingEffect : 0.0f;
```

## Verification & Engineering Rules

- Color-code `>= 4.0` as Overreaching/High Impact so athletes can see when an interval block hits its physiological target.
