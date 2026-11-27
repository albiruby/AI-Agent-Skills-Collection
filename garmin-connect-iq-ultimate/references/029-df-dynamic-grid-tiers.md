# 029-df-dynamic-grid-tiers: Adaptive 4-Tier Layout Engine (1-Field to 8-Field)

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Graphics.Dc`
- **Sub-Skill ID**: `029-df-dynamic-grid-tiers`

## Overview

Classify the assigned pane dimensions `(dc.getWidth(), dc.getHeight())` into Full, Half, Wide Strip, or Quadrant mode.

## Production Monkey C Implementation Pattern

```monkeyc
enum LayoutTier { TIER_FULL, TIER_HALF, TIER_STRIP, TIER_COMPACT }
private var _tier as LayoutTier = TIER_COMPACT;

public function onLayout(dc as Dc) as Void {
    var w = dc.getWidth();
    var h = dc.getHeight();
    var sw = System.getDeviceSettings().screenWidth;
    var sh = System.getDeviceSettings().screenHeight;
    if (h >= (sh * 80) / 100) { _tier = TIER_FULL; }
    else if (h >= (sh * 42) / 100) { _tier = TIER_HALF; }
    else if (w >= (sw * 80) / 100) { _tier = TIER_STRIP; }
    else { _tier = TIER_COMPACT; }
}
```

## Verification & Engineering Rules

- Adjust font sizes and hide secondary sub-labels when `_tier == TIER_COMPACT`.
