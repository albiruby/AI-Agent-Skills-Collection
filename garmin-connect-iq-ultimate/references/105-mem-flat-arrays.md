# 105-mem-flat-arrays: Zero-Dictionary Flat Enum Array Architecture

- **Domain Category**: Memory
- **Primary Connect IQ API**: `Toybox.Lang.Array`
- **Sub-Skill ID**: `105-mem-flat-arrays`

## Overview

Save 2KB to 8KB of heap RAM in DataFields and Glances by replacing `Dictionary` objects with `enum`-indexed flat arrays.

## Production Monkey C Implementation Pattern

```monkeyc
enum {
    STAT_HR = 0,
    STAT_PWR = 1,
    STAT_CAD = 2,
    STAT_COUNT = 3
}
private var _metrics as Array<Number> = new Array<Number>[STAT_COUNT];
```

## Verification & Engineering Rules

- Every Monkey C `Dictionary` costs ~150+ bytes of hash-table overhead even when empty.
