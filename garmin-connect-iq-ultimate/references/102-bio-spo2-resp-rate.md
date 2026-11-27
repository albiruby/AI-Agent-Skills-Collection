# 102-bio-spo2-resp-rate: Pulse Ox SpO2 & Respiration Rate Biometric Readers

- **Domain Category**: Biometrics
- **Primary Connect IQ API**: `Toybox.SensorHistory`
- **Sub-Skill ID**: `102-bio-spo2-resp-rate`

## Overview

Fetch blood oxygen saturation (`getOxygenSaturationHistory`) and breaths-per-minute (`ActivityMonitor.getInfo().respirationRate`).

## Production Monkey C Implementation Pattern

```monkeyc
var info = ActivityMonitor.getInfo();
var brpm = (info has :respirationRate && info.respirationRate != null) ? info.respirationRate : null;
```

## Verification & Engineering Rules

- Always display `--` when SpO2 or respiration samples are stale or `null`.
