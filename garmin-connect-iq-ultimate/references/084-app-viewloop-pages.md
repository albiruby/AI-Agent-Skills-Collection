# 084-app-viewloop-pages: Multi-Page Vertical Carousel & Bezel Page Dots

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `WatchUi.ViewLoop`
- **Sub-Skill ID**: `084-app-viewloop-pages`

## Overview

Implement multi-page app carousels using `WatchUi.ViewLoop` (CIQ 3.4+) or custom bezel page indicator dots.

## Production Monkey C Implementation Pattern

```monkeyc
// Use WatchUi.ViewLoop with a ViewLoopFactory to get nativeGarmin page-indicator bezel animations
```

## Verification & Engineering Rules

- Fall back to manual `WatchUi.switchToView()` when `WatchUi has :ViewLoop` is false.
