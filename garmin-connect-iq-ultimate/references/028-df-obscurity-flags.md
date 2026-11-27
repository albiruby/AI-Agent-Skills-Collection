# 028-df-obscurity-flags: Round Bezel Obscurity Bitmask Detection

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.DataField.getObscurityFlags`
- **Sub-Skill ID**: `028-df-obscurity-flags`

## Overview

Read `getObscurityFlags()` inside `onLayout(dc)` to detect whether the field touches the top, bottom, left, or right curved bezel.

## Production Monkey C Implementation Pattern

```monkeyc
private var _obscurity as Number = 0;

public function onLayout(dc as Dc) as Void {
    _obscurity = getObscurityFlags();
    var isTopCurved = (_obscurity & OBSCURE_TOP) != 0;
    var isBotCurved = (_obscurity & OBSCURE_BOTTOM) != 0;
}
```

## Verification & Engineering Rules

- `getObscurityFlags()` can only be called inside `onLayout(dc)` or `onUpdate(dc)`; calling it in `initialize()` or `compute(info)` throws an error.
