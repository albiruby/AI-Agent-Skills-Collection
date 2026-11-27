# 069-ble-uuid-registry: BluetoothLowEnergy Custom GATT Profile Registration

- **Domain Category**: BLE
- **Primary Connect IQ API**: `Toybox.BluetoothLowEnergy`
- **Sub-Skill ID**: `069-ble-uuid-registry`

## Overview

Register up to 3 custom BLE GATT service and characteristic UUID definitions (`BluetoothLowEnergy.registerProfile`).

## Production Monkey C Implementation Pattern

```monkeyc
var profileDef = {
    :uuid => BluetoothLowEnergy.stringToUuid("0000180D-0000-1000-8000-00805F9B34FB"),
    :characteristics => [{
        :uuid => BluetoothLowEnergy.stringToUuid("00002A37-0000-1000-8000-00805F9B34FB"),
        :descriptors => [BluetoothLowEnergy.cccdUuid()]
    }]
};
BluetoothLowEnergy.registerProfile(profileDef);
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="BluetoothLowEnergy"/>` in `manifest.xml`.
