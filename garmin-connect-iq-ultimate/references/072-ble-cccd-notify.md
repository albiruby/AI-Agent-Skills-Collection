# 072-ble-cccd-notify: BLE CCCD Notification & Indication Subscription

- **Domain Category**: BLE
- **Primary Connect IQ API**: `BluetoothLowEnergy.Descriptor`
- **Sub-Skill ID**: `072-ble-cccd-notify`

## Overview

Enable live BLE characteristic notifications by writing `[0x01, 0x00]b` to the Client Characteristic Configuration Descriptor (`cccdUuid()`).

## Production Monkey C Implementation Pattern

```monkeyc
var cccd = characteristic.getDescriptor(BluetoothLowEnergy.cccdUuid());
if (cccd != null) {
    cccd.requestWrite([0x01, 0x00]b);
}
```

## Verification & Engineering Rules

- Wait for `onDescriptorWrite(descriptor, status)` before issuing the next GATT operation.
