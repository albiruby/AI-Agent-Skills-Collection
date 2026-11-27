# 031-df-timer-callbacks: Activity Timer Start, Pause, Resume, Stop & Reset Hooks

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.DataField`
- **Sub-Skill ID**: `031-df-timer-callbacks`

## Overview

Track whether the workout timer is actively running (`TIMER_STATE_ON`) vs paused or stopped.

## Production Monkey C Implementation Pattern

```monkeyc
private var _isRunning as Boolean = false;

public function onTimerStart() as Void { _isRunning = true; }
public function onTimerResume() as Void { _isRunning = true; }
public function onTimerPause() as Void { _isRunning = false; }
public function onTimerStop() as Void { _isRunning = false; }
public function onTimerReset() as Void {
    _isRunning = false;
    resetSessionMetrics();
}
```

## Verification & Engineering Rules

- Also check `info.timerState == Activity.TIMER_STATE_ON` inside `compute(info)` in case the DataField was added mid-activity.
