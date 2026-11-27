# 004-wf-power-budget: WatchFaceDelegate 30ms Power Budget Guard

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `WatchUi.WatchFaceDelegate`
- **Sub-Skill ID**: `004-wf-power-budget`

## Overview

Catch `onPowerBudgetExceeded(powerInfo)` when `onPartialUpdate(dc)` averages over 30ms and gracefully disable 1Hz updates instead of crashing.

## Production Monkey C Implementation Pattern

```monkeyc
class SafeWatchFaceDelegate extends WatchUi.WatchFaceDelegate {
    private var _view as CoreWatchFaceView;

    public function initialize(view as CoreWatchFaceView) {
        WatchFaceDelegate.initialize();
        _view = view;
    }

    public function onPowerBudgetExceeded(powerInfo as WatchFacePowerInfo) as Void {
        System.println("Budget exceeded: " + powerInfo.executionTimeAverage);
        _view.disablePartialUpdates();
    }
}
```

## Verification & Engineering Rules

- Return `[view, new SafeWatchFaceDelegate(view)]` from `AppBase.getInitialView()`.
- Profile partial update timings in the Connect IQ Simulator using Watch Face Diagnostics.
