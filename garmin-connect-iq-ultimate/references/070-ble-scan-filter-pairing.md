# 070-ble-scan-filter-pairing: BLE Peripheral Scan Iterator & RSSI Filtering

- **Domain Category**: BLE
- **Primary Connect IQ API**: `BluetoothLowEnergy.BleDelegate`
- **Sub-Skill ID**: `070-ble-scan-filter-pairing`

## Overview

Iterate through `ScanResults` in `onScanResults()`, filter by advertised service UUID and RSSI threshold, and pair with `pairDevice()`.

## Production Monkey C Implementation Pattern

```monkeyc
public function onScanResults(scanResults as BluetoothLowEnergy.Iterator) as Void {
    for (var res = scanResults.next() as BluetoothLowEnergy.ScanResult; res != null; res = scanResults.next()) {
        if (res.getRssi() > -80) {
            BluetoothLowEnergy.setScanState(BluetoothLowEnergy.SCAN_STATE_OFF);
            BluetoothLowEnergy.pairDevice(res);
            break;
        }
    }
}
```

## Verification & Engineering Rules

- Always stop scanning (`SCAN_STATE_OFF`) as soon as a target device is matched to save battery.
