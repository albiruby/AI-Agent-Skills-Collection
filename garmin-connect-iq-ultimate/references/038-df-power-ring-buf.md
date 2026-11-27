# 038-df-power-ring-buf: 3s, 10s & 30s Cycling/Running Power Ring Buffer

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.currentPower`
- **Sub-Skill ID**: `038-df-power-ring-buf`

## Overview

Maintain zero-allocation O(1) sliding window sums for 3-second, 10-second, and 30-second average power.

## Production Monkey C Implementation Pattern

```monkeyc
private var _pwrRing as Array<Number> = new Array<Number>[30];
private var _ringIdx as Number = 0;
private var _ringCount as Number = 0;

public function pushPower(watts as Number) as Void {
    _pwrRing[_ringIdx] = watts;
    _ringIdx = (_ringIdx + 1) % 30;
    if (_ringCount < 30) { _ringCount++; }
}
```

## Verification & Engineering Rules

- Initialize all 30 slots to `0` in `initialize()` so no `null` elements exist in `_pwrRing`.
