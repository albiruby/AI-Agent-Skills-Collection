# 061-ant-bikepower-listener: Native AntPlus.BikePower Torque, Cadence & Balance

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.AntPlus.BikePower`
- **Sub-Skill ID**: `061-ant-bikepower-listener`

## Overview

Subscribe to native `AntPlus.BikePowerListener` callbacks for pedal smoothness, torque effectiveness, and left/right balance.

## Production Monkey C Implementation Pattern

```monkeyc
class PowerSensorListener extends AntPlus.BikePowerListener {
    public function initialize() { BikePowerListener.initialize(); }
    public function onCalculatedPowerUpdate(data as AntPlus.CalculatedPower) as Void {
        var watts = data.power;
    }
    public function onPedalPowerBalanceUpdate(data as AntPlus.PedalPowerBalance) as Void {
        var rightPct = data.pedalPowerPercent;
    }
}
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="Ant"/>` in `manifest.xml`.
