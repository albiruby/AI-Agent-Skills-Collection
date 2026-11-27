# 086-app-save-discard: Safe Workout Pause, Save & Discard Confirmation Flow

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `Toybox.ActivityRecording.Session`
- **Sub-Skill ID**: `086-app-save-discard`

## Overview

Intercept the Back/Stop button while a session is recording so the user never loses a workout accidentally.

## Production Monkey C Implementation Pattern

```monkeyc
// When session.isRecording() is true, call session.stop() and push a Resume / Save / Discard Menu2
```

## Verification & Engineering Rules

- Always wait for `session.save()` or `session.discard()` before calling `WatchUi.popView()` to exit the app.
