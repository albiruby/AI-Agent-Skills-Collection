# 013-wf-bitmap-fonts: Custom BMFont (.fnt + .png) Glyph Filtering

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `WatchUi.FontResource`
- **Sub-Skill ID**: `013-wf-bitmap-fonts`

## Overview

Configure custom bitmap fonts in `resources/fonts/fonts.xml` with strict character filtering (`filter="0123456789:APM"`) to minimize RAM usage.

## Production Monkey C Implementation Pattern

```monkeyc
<!-- resources/fonts/fonts.xml -->
<fonts>
    <font id="HudDigitsFont" filename="hud_digits.fnt" antialias="true" filter="0123456789:.-%" />
</fonts>
```

## Verification & Engineering Rules

- Always specify `filter` on large display fonts so unused alphabet glyphs are stripped at compile time.
