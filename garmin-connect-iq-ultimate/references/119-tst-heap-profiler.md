# 119-tst-heap-profiler: System.getSystemStats() Live Heap & Peak Memory Profiler

- **Domain Category**: Testing
- **Primary Connect IQ API**: `System.Stats`
- **Sub-Skill ID**: `119-tst-heap-profiler`

## Overview

Monitor `usedMemory`, `freeMemory`, and `totalMemory` at runtime to verify at least 15% free headroom before release.

## Production Monkey C Implementation Pattern

```monkeyc
var stats = System.getSystemStats();
System.println(Lang.format("Heap: $1$ / $2$ bytes (Free: $3$)", [
    stats.usedMemory, stats.totalMemory, stats.freeMemory
]));
```

## Verification & Engineering Rules

- Always test peak memory while opening `Menu2` settings or receiving a background `onBackgroundData` payload.
