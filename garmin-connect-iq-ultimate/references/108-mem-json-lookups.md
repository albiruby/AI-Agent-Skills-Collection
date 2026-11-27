# 108-mem-json-lookups: On-Demand jsonData XML Lookup Table Loading

- **Domain Category**: Memory
- **Primary Connect IQ API**: `WatchUi.loadResource`
- **Sub-Skill ID**: `108-mem-json-lookups`

## Overview

Move static lookup arrays out of permanent code/heap space into `<jsonData>` resources loaded only when needed.

## Production Monkey C Implementation Pattern

```monkeyc
<!-- resources/jsonData/lookups.xml -->
<resources>
    <jsonData id="EcgWaveLut">[0, 0, -3, 2, -18, 24, -8, 0, 4, 6, 3, 0]</jsonData>
</resources>
```

## Verification & Engineering Rules

- Load via `WatchUi.loadResource(Rez.JsonData.EcgWaveLut) as Array<Number>`.
