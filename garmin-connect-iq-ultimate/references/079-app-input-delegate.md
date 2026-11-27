# 079-app-input-delegate: Cross-Device BehaviorDelegate Semantic Navigation

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `WatchUi.BehaviorDelegate`
- **Sub-Skill ID**: `079-app-input-delegate`

## Overview

Map `onSelect()`, `onBack()`, `onNextPage()`, `onPreviousPage()`, and `onMenu()` so one delegate works across all Garmin watches.

## Production Monkey C Implementation Pattern

```monkeyc
class UniversalDelegate extends WatchUi.BehaviorDelegate {
    public function initialize() { BehaviorDelegate.initialize(); }
    public function onSelect() as Boolean { return true; }
    public function onNextPage() as Boolean { return true; }
    public function onPreviousPage() as Boolean { return true; }
    public function onBack() as Boolean { return false; } // false lets system pop view
}
```

## Verification & Engineering Rules

- Always prefer `BehaviorDelegate` over raw `KEY_UP` / `KEY_DOWN` checks.
