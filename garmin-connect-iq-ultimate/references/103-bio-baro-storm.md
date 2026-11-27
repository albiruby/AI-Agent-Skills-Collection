# 103-bio-baro-storm: 3-Hour Barometric Pressure Delta & Storm Alert Arrow

- **Domain Category**: Biometrics
- **Primary Connect IQ API**: `SensorHistory.getPressureHistory`
- **Sub-Skill ID**: `103-bio-baro-storm`

## Overview

Calculate the 3-hour sea-level barometric pressure delta (in hPa) to render a falling/steady/rising weather trend arrow.

## Production Monkey C Implementation Pattern

```monkeyc
// Convert Pascals to hPa: var hPa = sample.data / 100.0f;
// Delta <= -2.0 hPa over 3 hours indicates a rapidly approaching low-pressure front.
```

## Verification & Engineering Rules

- Filter out spikes when the user changes elevation rapidly during mountain activities.
