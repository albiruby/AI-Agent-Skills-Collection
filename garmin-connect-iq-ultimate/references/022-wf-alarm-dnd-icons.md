# 022-wf-alarm-dnd-icons: Alarm Count & Do Not Disturb Status Indicators

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `System.DeviceSettings`
- **Sub-Skill ID**: `022-wf-alarm-dnd-icons`

## Overview

Check `alarmCount` and `doNotDisturb` on `System.getDeviceSettings()` to render status bar icons.

## Production Monkey C Implementation Pattern

```monkeyc
var dev = System.getDeviceSettings();
var hasAlarms = (dev.alarmCount > 0);
var isDnd = (dev has :doNotDisturb) ? dev.doNotDisturb : false;
```

## Verification & Engineering Rules

- Check `dev has :doNotDisturb` before reading because older CIQ API levels do not expose DND state.
