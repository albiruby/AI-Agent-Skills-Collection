# 117-loc-i18n-strings: Multi-Language String Resources & Dynamic Formatting

- **Domain Category**: Localization
- **Primary Connect IQ API**: `WatchUi.loadResource`
- **Sub-Skill ID**: `117-loc-i18n-strings`

## Overview

Localize UI labels across English (`resources-eng/`), Indonesian (`resources-ind/`), and Japanese (`resources-jpn/`) with `Lang.format`.

## Production Monkey C Implementation Pattern

```monkeyc
var tpl = WatchUi.loadResource(Rez.Strings.FuelAlertFormat) as String;
var msg = Lang.format(tpl, [grams.format("%d")]);
```

## Verification & Engineering Rules

- Declare supported `<iq:language>` tags inside `manifest.xml`.
