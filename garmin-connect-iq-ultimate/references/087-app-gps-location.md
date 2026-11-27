# 087-app-gps-location: Multi-Band GNSS / GPS Continuous Location Subscription

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `Toybox.Position`
- **Sub-Skill ID**: `087-app-gps-location`

## Overview

Enable continuous GNSS/GPS positioning in a Device App using `Position.enableLocationEvents()` with constellation configuration.

## Production Monkey C Implementation Pattern

```monkeyc
Position.enableLocationEvents(Position.LOCATION_CONTINUOUS, method(:onPosition));
// Disable in onStop():
Position.enableLocationEvents(Position.LOCATION_DISABLE, null);
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="Positioning"/>` in `manifest.xml`. Always disable GPS in `onStop()`.
