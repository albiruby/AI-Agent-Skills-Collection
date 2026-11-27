# 081-app-menu2-controls: WatchUi.Menu2 Native Toggle, Icon & Sublabel Menus

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `WatchUi.Menu2`
- **Sub-Skill ID**: `081-app-menu2-controls`

## Overview

Construct hardware-accelerated native settings and action menus using `Menu2`, `MenuItem`, and `ToggleMenuItem`.

## Production Monkey C Implementation Pattern

```monkeyc
var menu = new WatchUi.Menu2({:title => "Bio-Feeder Setup"});
menu.addItem(new WatchUi.MenuItem("Carb Target", "75 g/h", :carbTarget, null));
menu.addItem(new WatchUi.ToggleMenuItem("Vibe Alerts", {:enabled => "ON", :disabled => "OFF"}, :vibe, true, null));
WatchUi.pushView(menu, new SetupMenuDelegate(), WatchUi.SLIDE_UP);
```

## Verification & Engineering Rules

- Use `item.setSubLabel(newValueStr)` inside `Menu2InputDelegate.onSelect(item)` to update the menu row dynamically.
