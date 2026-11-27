# 114-cpl-has-guards: Runtime 'has' Symbol & API Level Compatibility Guards

- **Domain Category**: Compiler
- **Primary Connect IQ API**: `Toybox.Lang`
- **Sub-Skill ID**: `114-cpl-has-guards`

## Overview

Support CIQ 3.2 through CIQ 5.0+ in a single codebase by guarding newer APIs with `has` checks.

## Production Monkey C Implementation Pattern

```monkeyc
if ((Toybox has :Complications) && (Complications has :getComplications)) {
    // Safe on CIQ 4.2+ devices
}
```

## Verification & Engineering Rules

- Always guard `Weather`, `Complications`, `SensorHistory`, `setAntiAlias`, and `createBufferedBitmap` with `has`.
