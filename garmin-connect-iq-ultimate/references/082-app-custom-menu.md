# 082-app-custom-menu: WatchUi.CustomMenu & CustomMenuItem Owner-Drawn Lists

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `WatchUi.CustomMenu`
- **Sub-Skill ID**: `082-app-custom-menu`

## Overview

Render custom colored inventory cards, ECG status rows, or workout interval tables using `WatchUi.CustomMenu`.

## Production Monkey C Implementation Pattern

```monkeyc
class CodecRowItem extends WatchUi.CustomMenuItem {
    private var _label as String;
    public function initialize(id as Symbol, label as String) {
        CustomMenuItem.initialize(id, {});
        _label = label;
    }
    public function draw(dc as Dc) as Void {
        dc.setColor(0x00E676, Graphics.COLOR_BLACK);
        dc.drawText(12, dc.getHeight()/2, Graphics.FONT_SMALL, _label,
            Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
```

## Verification & Engineering Rules

- Each `CustomMenuItem` receives its own localized `Dc` clipped to the item's height.
