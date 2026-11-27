# 055-df-touch-page-cycle: Interactive Touch-Tap View Mode Cycling in DataFields

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.InputDelegate`
- **Sub-Skill ID**: `055-df-touch-page-cycle`

## Overview

Allow touchscreen watch and Edge users to tap a DataField pane during an activity to cycle between primary and secondary pages.

## Production Monkey C Implementation Pattern

```monkeyc
// On CIQ 3.2+ devices supporting DataField input delegates:
class PageCycleDelegate extends WatchUi.InputDelegate {
    private var _view as CustomDashboardField;
    public function initialize(v as CustomDashboardField) {
        InputDelegate.initialize();
        _view = v;
    }
    public function onTap(evt as WatchUi.ClickEvent) as Boolean {
        _view.nextSubPage();
        return true;
    }
}
```

## Verification & Engineering Rules

- Always provide an automatic rotation fallback timer (e.g., every 8 seconds) for non-touch 5-button watches.
