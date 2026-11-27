# 116-stg-gcm-settings: Garmin Connect Mobile App Settings & onSettingsChanged

- **Domain Category**: Storage
- **Primary Connect IQ API**: `Toybox.Application.Properties`
- **Sub-Skill ID**: `116-stg-gcm-settings`

## Overview

Define user-configurable settings in `resources/settings/settings.xml` and reload them live in `AppBase.onSettingsChanged()`.

## Production Monkey C Implementation Pattern

```monkeyc
public function onSettingsChanged() as Void {
    _view.reloadUserPreferences();
    WatchUi.requestUpdate();
}
```

## Verification & Engineering Rules

- Always wrap `Application.Properties.getValue(key)` in a helper that validates type and returns a safe default if corrupted.
