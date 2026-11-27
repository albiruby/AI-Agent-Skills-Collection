# 068-ant-burst-tx-msg: ANT+ Acknowledged & Burst Data Transmission

- **Domain Category**: ANT+
- **Primary Connect IQ API**: `Toybox.Ant.GenericChannel`
- **Sub-Skill ID**: `068-ant-burst-tx-msg`

## Overview

Send acknowledged configuration commands (`sendAcknowledge(data)`) to external ANT+ sensors upon receiving `MSG_ID_BROADCAST_DATA`.

## Production Monkey C Implementation Pattern

```monkeyc
var cmd = new [8];
cmd[0] = 0x46; // Request Data Page
GenericChannel.sendAcknowledge(cmd);
```

## Verification & Engineering Rules

- Only transmit `sendAcknowledge()` immediately after receiving a broadcast message from the master sensor to avoid RF collisions.
