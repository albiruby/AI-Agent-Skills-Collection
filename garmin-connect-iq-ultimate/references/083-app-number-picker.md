# 083-app-number-picker: WatchUi.Picker Numeric & Custom Wheel Selectors

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `WatchUi.Picker`
- **Sub-Skill ID**: `083-app-number-picker`

## Overview

Build native rotary/scroll value pickers for selecting numbers (e.g., FTP, target carbs, timer intervals).

## Production Monkey C Implementation Pattern

```monkeyc
// Subclass WatchUi.PickerFactory to supply getDrawable(index, isSelected) and getValue(index)
```

## Verification & Engineering Rules

- Pop the Picker view inside `PickerDelegate.onAccept(values)` after saving `values[0]`.
