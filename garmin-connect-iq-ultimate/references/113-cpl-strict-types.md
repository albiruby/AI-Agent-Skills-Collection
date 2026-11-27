# 113-cpl-strict-types: Monkey C Strict Type Checking (--typecheck 3) Patterns

- **Domain Category**: Compiler
- **Primary Connect IQ API**: `Toybox.Lang`
- **Sub-Skill ID**: `113-cpl-strict-types`

## Overview

Satisfy Garmin's strictest compiler level (`-l 3`) using union types (`Number or Null`), narrow casts (`as Number`), and typed containers (`Array<Number>`).

## Production Monkey C Implementation Pattern

```monkeyc
private var _samples as Array<Float> = new Array<Float>[10];
private var _activeHr as Number or Null = null;

public function processHr(val as Number or Null) as Number {
    if (val != null) {
        return val * 2; // Compiler narrows val to Number automatically inside if-block
    }
    return 0;
}
```

## Verification & Engineering Rules

- Copy member variables into a local `var localHr = _activeHr;` before null-checking so `-l 3` knows the value cannot mutate mid-function.
