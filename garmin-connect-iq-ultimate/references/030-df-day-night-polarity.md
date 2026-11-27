# 030-df-day-night-polarity: Automatic Day/Night Background Color Polarity

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.DataField.getBackgroundColor`
- **Sub-Skill ID**: `030-df-day-night-polarity`

## Overview

Match the user's activity background setting (Black vs White) dynamically on every `onUpdate(dc)` pass.

## Production Monkey C Implementation Pattern

```monkeyc
var bg = getBackgroundColor();
var fg = (bg == Graphics.COLOR_BLACK) ? Graphics.COLOR_WHITE : Graphics.COLOR_BLACK;
var muted = (bg == Graphics.COLOR_BLACK) ? Graphics.COLOR_LT_GRAY : Graphics.COLOR_DK_GRAY;
dc.setColor(fg, bg);
dc.clear();
```

## Verification & Engineering Rules

- Always test both Black and White background themes in the simulator (`Data Fields -> Background Color`).
