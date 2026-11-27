# 035-df-hr-zone-colors: UserProfile Heart Rate Zone Lookup & Color Coding

- **Domain Category**: DataField
- **Primary Connect IQ API**: `UserProfile.getHeartRateZones`
- **Sub-Skill ID**: `035-df-hr-zone-colors`

## Overview

Fetch the athlete's actual 5-zone heart rate thresholds from `UserProfile.getHeartRateZones()` and map current HR to official Garmin zone colors.

## Production Monkey C Implementation Pattern

```monkeyc
private var _zones as Array<Number> or Null = null;

public function initZones() as Void {
    var sport = UserProfile.getCurrentSport();
    _zones = UserProfile.getHeartRateZones(sport);
}

public function getZoneColor(hr as Number) as Number {
    if (_zones == null || _zones.size() < 6) { return Graphics.COLOR_WHITE; }
    if (hr < _zones[1]) { return Graphics.COLOR_LT_GRAY; } // Z1
    if (hr < _zones[2]) { return 0x00AAFF; } // Z2 Blue
    if (hr < _zones[3]) { return 0x00E676; } // Z3 Green
    if (hr < _zones[4]) { return 0xFF8800; } // Z4 Orange
    return 0xFF1744; // Z5 Red
}
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="UserProfile"/>` in `manifest.xml`.
