# 015-wf-goal-progress-bars: Steps, Calories & Active Minutes Goal Bars

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `ActivityMonitor.Info`
- **Sub-Skill ID**: `015-wf-goal-progress-bars`

## Overview

Query `ActivityMonitor.getInfo()` safely to render daily step goal progress, floors climbed, and active minutes.

## Production Monkey C Implementation Pattern

```monkeyc
var info = ActivityMonitor.getInfo();
var steps = (info.steps != null) ? info.steps : 0;
var goal = (info.stepGoal != null && info.stepGoal > 0) ? info.stepGoal : 10000;
var ratio = steps.toFloat() / goal.toFloat();
```

## Verification & Engineering Rules

- Always guard `info.stepGoal > 0` before division to prevent divide-by-zero crashes on unconfigured profiles.
