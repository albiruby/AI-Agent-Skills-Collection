# 075-sensor-25hz-accel: High-Frequency 25Hz Raw Accelerometer DataListener

- **Domain Category**: Sensor
- **Primary Connect IQ API**: `Toybox.Sensor.registerSensorDataListener`
- **Sub-Skill ID**: `075-sensor-25hz-accel`

## Overview

Stream 25Hz tri-axial accelerometer (`x`, `y`, `z` in milli-G) and beat-to-beat R-R intervals for rep counting or HRV analysis.

## Production Monkey C Implementation Pattern

```monkeyc
var opts = {
    :period => 1,
    :accelerometer => {:enabled => true, :sampleRate => 25}
};
Sensor.registerSensorDataListener(method(:onAccelData), opts);
```

## Verification & Engineering Rules

- Only available in Device Apps (`watch-app`); unregister in `onStop()` via `Sensor.unregisterSensorDataListener()`.
