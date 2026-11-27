# 093-bg-comp-publisher: Background Custom Complication Publisher (CIQ 4.2+)

- **Domain Category**: Background
- **Primary Connect IQ API**: `Toybox.Complications.updateComplication`
- **Sub-Skill ID**: `093-bg-comp-publisher`

## Overview

Publish live app metrics from your background service so third-party and native watch faces can display them.

## Production Monkey C Implementation Pattern

```monkeyc
if (Toybox has :Complications) {
    Complications.updateComplication(0, {
        :value => "85g",
        :shortLabel => "CARB"
    });
}
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="ComplicationPublisher"/>` and `<iq:complications>` in `manifest.xml`.
