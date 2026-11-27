# 034-df-alert-popups: Full-Screen DataFieldAlert Popups & Haptics

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.DataFieldAlert`
- **Sub-Skill ID**: `034-df-alert-popups`

## Overview

Display a full-screen modal alert overlay over any activity page when a critical threshold or nutrition timer triggers.

## Production Monkey C Implementation Pattern

```monkeyc
class FuelAlertView extends WatchUi.DataFieldAlert {
    public function initialize() { DataFieldAlert.initialize(); }
    public function onUpdate(dc as Dc) as Void {
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        dc.setColor(0x00E676, Graphics.COLOR_TRANSPARENT);
        dc.drawText(dc.getWidth()/2, dc.getHeight()/2, Graphics.FONT_LARGE,
            "TAKE 25g GEL NOW", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
// Trigger via: if (WatchUi has :DataFieldAlert) { WatchUi.showAlert(new FuelAlertView()); }
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="DataFieldAlert"/>` in `manifest.xml`.
