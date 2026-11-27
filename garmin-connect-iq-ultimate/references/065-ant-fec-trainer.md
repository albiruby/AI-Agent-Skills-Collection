# 065-ant-fec-trainer: AntPlus.FitnessEquipment Smart Trainer ERG Control

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.AntPlus.FitnessEquipment`
- **Sub-Skill ID**: `065-ant-fec-trainer`

## Overview

Control ANT+ FE-C smart indoor trainers in target power (ERG), slope simulation, or resistance mode.

## Production Monkey C Implementation Pattern

```monkeyc
// Use FitnessEquipment.controlEquipment(AntPlus.TRAINER_TARGET_POWER, targetWatts)
```

## Verification & Engineering Rules

- Only available in Device Apps (`watch-app`) and DataFields with ANT permission.
