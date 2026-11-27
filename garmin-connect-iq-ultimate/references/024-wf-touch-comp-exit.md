# 024-wf-touch-comp-exit: Touch-Hold Complication Exit-To-Native-Widget

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Toybox.Complications.exitTo`
- **Sub-Skill ID**: `024-wf-touch-comp-exit`

## Overview

Launch native Garmin glances/widgets (Heart Rate, Weather, Steps, Body Battery) when the user taps and holds a watch face complication.

## Production Monkey C Implementation Pattern

```monkeyc
class InteractiveFaceDelegate extends WatchUi.WatchFaceDelegate {
    public function initialize() { WatchFaceDelegate.initialize(); }

    public function onPress(clickEvent as WatchUi.ClickEvent) as Boolean {
        if (Toybox has :Complications) {
            var coords = clickEvent.getCoordinates();
            if (coords[1] > 180) {
                Complications.exitTo(new Complications.Id(Complications.COMPLICATION_TYPE_HEART_RATE));
                return true;
            }
        }
        return false;
    }
}
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="ComplicationSubscriber"/>` in `manifest.xml` and CIQ 4.2+.
