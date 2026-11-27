# 107-mem-byte-buffers: Compact ByteArray ([]b) Binary Telemetry Buffers

- **Domain Category**: Memory
- **Primary Connect IQ API**: `Toybox.Lang.ByteArray`
- **Sub-Skill ID**: `107-mem-byte-buffers`

## Overview

Store 120-sample histories in a raw `ByteArray` (`new [240]b`) using 2 bytes per `UINT16` sample instead of `Array<Number>`.

## Production Monkey C Implementation Pattern

```monkeyc
private var _buf as ByteArray = new [120]b;

public function setSample(idx as Number, val as Number) as Void {
    _buf.encodeNumber(val, Lang.NUMBER_FORMAT_UINT16, {:offset => idx * 2});
}

public function getSample(idx as Number) as Number {
    return _buf.decodeNumber(Lang.NUMBER_FORMAT_UINT16, {:offset => idx * 2}) as Number;
}
```

## Verification & Engineering Rules

- Reduces a 60-sample buffer from ~1KB (`Array<Number>`) down to ~136 bytes (`ByteArray`).
