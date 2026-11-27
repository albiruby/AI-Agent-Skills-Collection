# 073-ble-write-queue: Sequential BLE GATT Operation Queue State Machine

- **Domain Category**: BLE
- **Primary Connect IQ API**: `BluetoothLowEnergy.BleDelegate`
- **Sub-Skill ID**: `073-ble-write-queue`

## Overview

Queue multiple BLE reads, writes, and CCCD subscriptions sequentially so Garmin's single-flight BLE stack never drops requests.

## Production Monkey C Implementation Pattern

```monkeyc
// Pop the next queued GATT operation inside onCharacteristicWrite / onDescriptorWrite
```

## Verification & Engineering Rules

- Issuing two `requestWrite()` calls in the same tick without waiting for the callback causes `Ble` write failures on physical watches.
