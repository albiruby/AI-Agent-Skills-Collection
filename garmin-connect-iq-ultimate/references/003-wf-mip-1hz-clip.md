# 003-wf-mip-1hz-clip: MIP 1Hz Partial Update & Clipping Region

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `WatchUi.WatchFace.onPartialUpdate`
- **Sub-Skill ID**: `003-wf-mip-1hz-clip`

## Overview

Update seconds or live heart rate at 1Hz on transflective MIP displays during sleep mode while staying strictly below the 30ms execution time limit.

## Production Monkey C Implementation Pattern

```monkeyc
public function onPartialUpdate(dc as Dc) as Void {
    var secStr = System.getClockTime().sec.format("%02d");
    var x = _cx - 18;
    var y = _cy + 24;
    var w = 36;
    var h = 22;

    dc.setClip(x, y, w, h);
    dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
    dc.fillRectangle(x, y, w, h);
    dc.setColor(0x00E676, Graphics.COLOR_TRANSPARENT);
    dc.drawText(_cx, y + 11, Graphics.FONT_TINY, secStr,
        Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
}
```

## Verification & Engineering Rules

- Always call `dc.clearClip()` at the start of `onUpdate(dc)` so full-screen redraws are not trapped inside the last 1Hz clip box.
- Keep clip area as small as possible (under 40x30 px).
