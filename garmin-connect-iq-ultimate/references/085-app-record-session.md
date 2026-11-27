# 085-app-record-session: Standalone ActivityRecording Session & Sport Profiles

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `Toybox.ActivityRecording`
- **Sub-Skill ID**: `085-app-record-session`

## Overview

Record full standalone workouts to Garmin Connect from a Device App using `ActivityRecording.createSession()`.

## Production Monkey C Implementation Pattern

```monkeyc
_session = ActivityRecording.createSession({
    :name => "Bio-Feeder Run",
    :sport => Activity.SPORT_RUNNING,
    :subSport => Activity.SUB_SPORT_TRAIL
});
_session.start();
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="Fit"/>` in `manifest.xml`.
