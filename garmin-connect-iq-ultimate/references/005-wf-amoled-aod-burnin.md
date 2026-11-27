# 005-wf-amoled-aod-burnin: AMOLED Burn-In Protection Detection

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `System.DeviceSettings`
- **Sub-Skill ID**: `005-wf-amoled-aod-burnin`

## Overview

Detect `requiresBurnInProtection` at runtime to switch AMOLED devices (Epix, Fenix 8, Forerunner 265/965, Venu 3) into a compliant Always-On Display (AOD) mode.

## Production Monkey C Implementation Pattern

```monkeyc
private var _requiresBurnIn as Boolean = false;

public function initialize() {
    WatchFace.initialize();
    var settings = System.getDeviceSettings();
    if (settings has :requiresBurnInProtection) {
        _requiresBurnIn = settings.requiresBurnInProtection;
    }
}
```

## Verification & Engineering Rules

- Never run 1Hz updates on devices where `requiresBurnInProtection` is `true`.
- Test Sleep Mode in the simulator for Epix Gen 2 or Forerunner 965 to trigger the burn-in checker.
