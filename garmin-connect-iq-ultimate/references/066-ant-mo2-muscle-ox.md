# 066-ant-mo2-muscle-ox: Custom ANT+ GenericChannel Muscle Oxygen (MO2 / SmO2)

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.Ant.GenericChannel`
- **Sub-Skill ID**: `066-ant-mo2-muscle-ox`

## Overview

Pair directly with Moxy / Humon ANT+ Muscle Oxygen sensors (Device Type `31`, Period `8192`, RF `57`) via `Ant.GenericChannel`.

## Production Monkey C Implementation Pattern

```monkeyc
var chanAssign = new Ant.ChannelAssignment(Ant.CHANNEL_TYPE_RX_NOT_TX, Ant.NETWORK_PLUS);
var devCfg = new Ant.DeviceConfig({
    :deviceNumber => 0, // Wildcard search
    :deviceType => 31,  // ANT+ Muscle Oxygen
    :transmissionType => 0,
    :messagePeriod => 8192,
    :radioFrequency => 57
});
```

## Verification & Engineering Rules

- Always call `GenericChannel.release()` in `onStop()` so the hardware ANT channel is freed.
