# 071-ble-gatt-char-read: BLE GATT Characteristic Read & ByteArray Decoding

- **Domain Category**: BLE
- **Primary Connect IQ API**: `BluetoothLowEnergy.Characteristic`
- **Sub-Skill ID**: `071-ble-gatt-char-read`

## Overview

Decode binary IEEE-11073 floats and signed/unsigned integers from `ByteArray` payloads in `onCharacteristicRead()`.

## Production Monkey C Implementation Pattern

```monkeyc
public function onCharacteristicRead(char as BluetoothLowEnergy.Characteristic, status as BluetoothLowEnergy.Status, value as ByteArray) as Void {
    if (status == BluetoothLowEnergy.STATUS_SUCCESS && value.size() >= 2) {
        var uint16Val = value.decodeNumber(Lang.NUMBER_FORMAT_UINT16, {:offset => 0, :endianness => Lang.ENDIAN_LITTLE});
    }
}
```

## Verification & Engineering Rules

- Always verify `value.size()` before calling `decodeNumber()` to prevent out-of-bounds exceptions.
