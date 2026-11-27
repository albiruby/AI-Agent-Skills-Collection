# 077-app-glance-heap: (:glance) Annotation & 32KB Glance Heap Isolation

- **Domain Category**: Glance
- **Primary Connect IQ API**: `WatchUi.GlanceView`
- **Sub-Skill ID**: `077-app-glance-heap`

## Overview

Isolate widget glance code using `(:glance)` annotations so full-app views and assets are excluded from the restricted Glance heap.

## Production Monkey C Implementation Pattern

```monkeyc
(:glance)
class CompactGlanceView extends WatchUi.GlanceView {
    public function initialize() { GlanceView.initialize(); }
    public function onUpdate(dc as Dc) as Void {
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(0, dc.getHeight() / 2, Graphics.FONT_SMALL, "BIO-FEEDER: READY",
            Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}
```

## Verification & Engineering Rules

- Annotate `AppBase.getGlanceView()` and any helper functions it calls with `(:glance)`.
