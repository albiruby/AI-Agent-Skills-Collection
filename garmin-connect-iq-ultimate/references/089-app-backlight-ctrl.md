# 089-app-backlight-ctrl: Programmatic Backlight Flash & Timeout Control

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `Toybox.Attention.backlight`
- **Sub-Skill ID**: `089-app-backlight-ctrl`

## Overview

Activate the display backlight during night alerts using `Attention.backlight(true)` guarded against battery-saver exceptions.

## Production Monkey C Implementation Pattern

```monkeyc
if (Attention has :backlight) {
    try {
        Attention.backlight(true);
    } catch (ex) {}
}
```

## Verification & Engineering Rules

- Wrap `Attention.backlight()` in `try/catch` because it can throw `BacklightOnTooLongException` if called repeatedly.
