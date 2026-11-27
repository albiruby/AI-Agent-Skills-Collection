# 092-bg-phone-comm-sync: Companion Smartphone App Mailbox & PhoneAppMessage

- **Domain Category**: Background
- **Primary Connect IQ API**: `Toybox.Communications`
- **Sub-Skill ID**: `092-bg-phone-comm-sync`

## Overview

Exchange direct dictionary payloads with a companion Android/iOS Connect IQ Mobile SDK app via `registerForPhoneAppMessages()`.

## Production Monkey C Implementation Pattern

```monkeyc
Communications.registerForPhoneAppMessages(method(:onPhoneMsg));
// Send to phone:
Communications.transmit({"cmd" => "ACK"}, null, new CommListener());
```

## Verification & Engineering Rules

- Always pass a `Communications.ConnectionListener` subclass to `Communications.transmit()`.
