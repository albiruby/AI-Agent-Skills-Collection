# 063-ant-run-dynamics: AntPlus.RunningDynamics GCT, Vertical Oscillation & Ratio

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.AntPlus.RunningDynamics`
- **Sub-Skill ID**: `063-ant-run-dynamics`

## Overview

Capture Ground Contact Time (`ms`), GCT Balance (`%`), Vertical Oscillation (`mm`), and Vertical Ratio (`%`) from HRM-Pro/Run pods.

## Production Monkey C Implementation Pattern

```monkeyc
class RunDynListener extends AntPlus.RunningDynamicsListener {
    public function initialize() { RunningDynamicsListener.initialize(); }
    public function onRunningDynamicsUpdate(data as AntPlus.RunningDynamicsData) as Void {
        var gctMs = data.groundContactTime;
        var vertOscMm = data.verticalOscillation;
    }
}
```

## Verification & Engineering Rules

- Guard each property on `RunningDynamicsData` against `null` during walk breaks.
