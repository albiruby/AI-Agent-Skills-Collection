# 026-df-simple-vs-custom: SimpleDataField vs Full Custom DataField Selection

- **Domain Category**: DataField
- **Primary Connect IQ API**: `WatchUi.SimpleDataField`
- **Sub-Skill ID**: `026-df-simple-vs-custom`

## Overview

Implement lightweight single-metric fields using `SimpleDataField` (<16KB RAM) or full custom-drawn dashboards using `DataField`.

## Production Monkey C Implementation Pattern

```monkeyc
class FastSimpleField extends WatchUi.SimpleDataField {
    public function initialize() {
        SimpleDataField.initialize();
        label = "CARB g/h";
    }

    public function compute(info as Activity.Info) as Numeric or Duration or String or Null {
        if (info has :energyExpenditure && info.energyExpenditure != null) {
            return (info.energyExpenditure * 60.0f * 0.18f).format("%.0f");
        }
        return "--";
    }
}
```

## Verification & Engineering Rules

- `SimpleDataField` automatically adapts fonts across 1-to-8 field layouts without writing any `onUpdate(dc)` code.
