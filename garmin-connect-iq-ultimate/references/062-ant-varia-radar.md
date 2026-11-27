# 062-ant-varia-radar: AntPlus.BikeRadar Approaching Vehicle Threat Tracker

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.AntPlus.BikeRadar`
- **Sub-Skill ID**: `062-ant-varia-radar`

## Overview

Read Varia Rearview Radar vehicle targets (up to 8 simultaneous approaching vehicles with range in meters and closing speed in m/s).

## Production Monkey C Implementation Pattern

```monkeyc
class RadarHandler extends AntPlus.BikeRadarListener {
    public function initialize() { BikeRadarListener.initialize(); }
    public function onBikeRadarUpdate(targets as Array<AntPlus.RadarTarget>) as Void {
        for (var i = 0; i < targets.size(); i++) {
            if (targets[i].threat != AntPlus.THREAT_LEVEL_NONE) {
                var rangeM = targets[i].range;
                var speedMps = targets[i].speed;
            }
        }
    }
}
```

## Verification & Engineering Rules

- Highlight `THREAT_LEVEL_FAST_APPROACHING` in crimson (`0xFF1744`) for fast-closing vehicles.
