# 080-app-button-vs-touch: 5-Button Tactile vs 2-Button Touchscreen Input Routing

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `System.DeviceSettings.isTouchScreen`
- **Sub-Skill ID**: `080-app-button-vs-touch`

## Overview

Check `System.getDeviceSettings().isTouchScreen` to provide on-screen touch affordances alongside physical button hints.

## Production Monkey C Implementation Pattern

```monkeyc
var isTouch = System.getDeviceSettings().isTouchScreen;
```

## Verification & Engineering Rules

- Even on touch-capable Fenix/Epix/Forerunner models, users often disable touch during rain or workouts—always support physical buttons.
