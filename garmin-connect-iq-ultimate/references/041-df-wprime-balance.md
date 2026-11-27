# 041-df-wprime-balance: Skiba W'bal Anaerobic Work Capacity Differential Model

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.currentPower`
- **Sub-Skill ID**: `041-df-wprime-balance`

## Overview

Track real-time anaerobic work capacity depletion (`W'bal` in kJ) above Critical Power (CP) and exponential reconstitution below CP.

## Production Monkey C Implementation Pattern

```monkeyc
private var _wBalJoules as Float = 20000.0f; // 20 kJ W'

public function stepWbal(watts as Number, cp as Number, wPrimeMax as Float) as Float {
    if (watts > cp) {
        _wBalJoules -= (watts - cp).toFloat();
        if (_wBalJoules < 0.0f) { _wBalJoules = 0.0f; }
    } else {
        var dcp = cp - watts;
        var tau = 546.0f * Math.exp(-0.01f * dcp.toFloat()) + 316.0f;
        _wBalJoules += (wPrimeMax - _wBalJoules) / tau;
    }
    return _wBalJoules;
}
```

## Verification & Engineering Rules

- Render `W'bal` as a percentage bar that turns crimson when anaerobic reserve drops below 25%.
