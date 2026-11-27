# 067-ant-core-body-temp: Custom ANT+ GenericChannel CORE Body Temperature

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.Ant.GenericChannel`
- **Sub-Skill ID**: `067-ant-core-body-temp`

## Overview

Decode Data Page `0x01` from CORE Body Temperature sensors (Device Type `123`, Period `16384`, RF `57`) for core and skin temp.

## Production Monkey C Implementation Pattern

```monkeyc
// Parse 8-byte payload in onMessage(msg as Ant.Message):
var payload = msg.getPayload();
if (msg.messageId == Ant.MSG_ID_BROADCAST_DATA && payload[0] == 0x01) {
    var coreRaw = (payload[7] << 8) | payload[6];
    var coreTempC = coreRaw.toFloat() / 100.0f;
}
```

## Verification & Engineering Rules

- Store paired `deviceNumber` in `Application.Storage` so subsequent sessions reconnect immediately without wildcard search.
