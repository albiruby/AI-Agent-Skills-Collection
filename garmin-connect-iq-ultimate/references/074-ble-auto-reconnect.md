# 074-ble-auto-reconnect: BLE Disconnection Recovery & Unpair Cleanup

- **Domain Category**: BLE
- **Primary Connect IQ API**: `BluetoothLowEnergy.BleDelegate`
- **Sub-Skill ID**: `074-ble-auto-reconnect`

## Overview

Detect peripheral dropouts in `onConnectedStateChanged(device, state)` and trigger clean reconnection or scan fallback.

## Production Monkey C Implementation Pattern

```monkeyc
public function onConnectedStateChanged(device as BluetoothLowEnergy.Device, state as BluetoothLowEnergy.ConnectionState) as Void {
    if (state == BluetoothLowEnergy.CONNECTION_STATE_DISCONNECTED) {
        _device = null;
        BluetoothLowEnergy.setScanState(BluetoothLowEnergy.SCAN_STATE_SCANNING);
    }
}
```

## Verification & Engineering Rules

- Call `BluetoothLowEnergy.unpairDevice(_device)` in `onStop()` when the app exits.
