# 039-df-normalized-power: Coggan Normalized Power (NP) 4th-Power Engine

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info.currentPower`
- **Sub-Skill ID**: `039-df-normalized-power`

## Overview

Calculate real-time Normalized Power using a 30-second rolling average raised to the 4th power, averaged over active time, and fourth-rooted.

## Production Monkey C Implementation Pattern

```monkeyc
private var _sumPwr4 as Double = 0.0d;
private var _npSamples as Number = 0;

public function updateNp(rolling30sWatts as Float) as Number {
    var p2 = rolling30sWatts.toDouble() * rolling30sWatts.toDouble();
    _sumPwr4 += (p2 * p2);
    _npSamples++;
    return Math.pow(_sumPwr4 / _npSamples.toDouble(), 0.25d).toNumber();
}
```

## Verification & Engineering Rules

- Use 64-bit `Double` (`0.0d`) for `_sumPwr4` because `watts^4` summed over a multi-hour ride overflows 32-bit `Float` precision.
