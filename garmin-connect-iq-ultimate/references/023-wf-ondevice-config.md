# 023-wf-ondevice-config: On-Device WatchFace Customize Menu (getSettingsView)

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Application.AppBase.getSettingsView`
- **Sub-Skill ID**: `023-wf-ondevice-config`

## Overview

Allow users to configure watch face colors, hands, and data slots directly from the watch's native 'Customize' menu without a phone.

## Production Monkey C Implementation Pattern

```monkeyc
public function getSettingsView() as [Views] or [Views, InputDelegates] or Null {
    var menu = new WatchUi.Menu2({:title => "Customize HUD"});
    menu.addItem(new WatchUi.ToggleMenuItem("ECG Grid", "Show scanlines", :grid, true, null));
    return [menu, new WatchFaceSettingsDelegate()];
}
```

## Verification & Engineering Rules

- Persist changes via `Application.Properties.setValue()` or `Application.Storage.setValue()` inside `Menu2InputDelegate.onSelect()`.
