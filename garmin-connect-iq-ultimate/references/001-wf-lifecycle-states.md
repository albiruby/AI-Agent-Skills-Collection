# 001-wf-lifecycle-states: WatchFace Lifecycle & Power State Machine

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `WatchUi.WatchFace`
- **Sub-Skill ID**: `001-wf-lifecycle-states`

## Overview

Manage `initialize()`, `onLayout(dc)`, `onShow()`, `onUpdate(dc)`, `onPartialUpdate(dc)`, `onEnterSleep()`, `onExitSleep()`, and `onHide()` without leaking resources.

## Production Monkey C Implementation Pattern

```monkeyc
class CoreWatchFaceView extends WatchUi.WatchFace {
    private var _isAwake as Boolean = true;
    private var _font as WatchUi.FontResource or Null = null;

    public function initialize() {
        WatchFace.initialize();
    }

    public function onShow() as Void {
        _font = WatchUi.loadResource(Rez.Fonts.PrimaryFont) as WatchUi.FontResource;
    }

    public function onHide() as Void {
        _font = null; // Free heap when WatchFace is not visible
    }

    public function onEnterSleep() as Void {
        _isAwake = false;
        WatchUi.requestUpdate();
    }

    public function onExitSleep() as Void {
        _isAwake = true;
        WatchUi.requestUpdate();
    }
}
```

## Verification & Engineering Rules

- Never call `WatchUi.loadResource()` inside `onUpdate(dc)`.
- Always set heavy references to `null` in `onHide()` on tight-memory MIP devices.
