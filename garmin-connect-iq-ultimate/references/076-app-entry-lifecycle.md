# 076-app-entry-lifecycle: AppBase Lifecycle: onStart, getInitialView & onStop

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `Application.AppBase`
- **Sub-Skill ID**: `076-app-entry-lifecycle`

## Overview

Structure `AppBase` entry points cleanly across foreground launches, glance previews, and background wakeups.

## Production Monkey C Implementation Pattern

```monkeyc
class MasterApp extends Application.AppBase {
    public function initialize() { AppBase.initialize(); }
    public function onStart(state as Dictionary?) as Void {}
    public function onStop(state as Dictionary?) as Void {}
    public function getInitialView() as [Views] or [Views, InputDelegates] {
        var view = new MainView();
        return [view, new MainDelegate(view)];
    }
}
```

## Verification & Engineering Rules

- Keep `onStart()` fast; defer heavy asset loading to `View.onLayout(dc)` or `View.onShow()`.
