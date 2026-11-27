# 021-wf-ble-notif-icons: Bluetooth Connection & Notification Count Badge

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `System.DeviceSettings`
- **Sub-Skill ID**: `021-wf-ble-notif-icons`

## Overview

Query `phoneConnected` and `notificationCount` from `System.getDeviceSettings()` to display connectivity and unread badge icons.

## Production Monkey C Implementation Pattern

```monkeyc
var dev = System.getDeviceSettings();
var connected = dev.phoneConnected;
var notifCount = (dev has :notificationCount) ? dev.notificationCount : 0;
```

## Verification & Engineering Rules

- Only render the notification counter badge when `notifCount > 0` to keep the watch face clean.
