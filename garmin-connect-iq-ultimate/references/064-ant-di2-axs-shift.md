# 064-ant-di2-axs-shift: AntPlus.Shifting Electronic Drivetrain Gear & Battery

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.AntPlus.Shifting`
- **Sub-Skill ID**: `064-ant-di2-axs-shift`

## Overview

Read front/rear derailleur gear numbers, gear ratios, and shifter battery status (Shimano Di2 / SRAM AXS).

## Production Monkey C Implementation Pattern

```monkeyc
// Read current front and rear gear index from AntPlus.Shifting
```

## Verification & Engineering Rules

- Check `getBatteryStatus()` to alert the rider when derailleur or shifter coin-cell batteries hit Low/Critical.
