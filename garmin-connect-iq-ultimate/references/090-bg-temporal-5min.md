# 090-bg-temporal-5min: Background ServiceDelegate 5-Minute Temporal Scheduler

- **Domain Category**: Background
- **Primary Connect IQ API**: `Toybox.System.ServiceDelegate`
- **Sub-Skill ID**: `090-bg-temporal-5min`

## Overview

Schedule periodic background wakeups (`Background.registerForTemporalEvent`) obeying the 5-minute minimum interval rule.

## Production Monkey C Implementation Pattern

```monkeyc
(:background)
class SyncServiceDelegate extends System.ServiceDelegate {
    public function initialize() { ServiceDelegate.initialize(); }
    public function onTemporalEvent() as Void {
        Background.exit({"syncedAt" => Time.now().value()});
    }
}
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="Background"/>` and `(:background)` annotation on `AppBase`.
