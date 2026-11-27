# 115-stg-disk-storage: Application.Storage Key-Value Disk Persistence

- **Domain Category**: Storage
- **Primary Connect IQ API**: `Toybox.Application.Storage`
- **Sub-Skill ID**: `115-stg-disk-storage`

## Overview

Persist structured user data, cached API payloads, and workout state across app restarts using `Application.Storage`.

## Production Monkey C Implementation Pattern

```monkeyc
Application.Storage.setValue("lastCarbTarget", 80);
var target = Application.Storage.getValue("lastCarbTarget") as Number or Null;
if (target == null) { target = 60; }
```

## Verification & Engineering Rules

- `Application.Storage` writes directly to flash storage without loading the entire store into RAM (up to 128KB per app).
