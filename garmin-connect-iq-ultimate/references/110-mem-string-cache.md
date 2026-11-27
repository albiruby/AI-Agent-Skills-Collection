# 110-mem-string-cache: Dirty-Flag String Caching in 1Hz Render Loops

- **Domain Category**: Memory
- **Primary Connect IQ API**: `Toybox.Lang.String`
- **Sub-Skill ID**: `110-mem-string-cache`

## Overview

Format strings (`hour:min`, `hr bpm`) only when the underlying integer changes rather than on every `onUpdate(dc)` call.

## Production Monkey C Implementation Pattern

```monkeyc
private var _lastMin as Number = -1;
private var _cachedTimeStr as String = "00:00";

public function getTimeStr(hour as Number, min as Number) as String {
    if (min != _lastMin) {
        _lastMin = min;
        _cachedTimeStr = hour.format("%02d") + ":" + min.format("%02d");
    }
    return _cachedTimeStr;
}
```

## Verification & Engineering Rules

- Saves dozens of transient string allocations per minute.
