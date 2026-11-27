# 060-fit-255byte-budget: FIT 255-Byte Developer Data Budget Optimization

- **Domain Category**: FitContributor
- **Primary Connect IQ API**: `Toybox.FitContributor`
- **Sub-Skill ID**: `060-fit-255byte-budget`

## Overview

Keep total developer field bytes across all active DataFields below the 255-byte per-message hardware ceiling.

## Production Monkey C Implementation Pattern

```monkeyc
// Prefer compact integer types over floats or strings:
// DATA_TYPE_UINT8  = 1 byte (0..255)
// DATA_TYPE_SINT16 = 2 bytes (-32768..32767)
// DATA_TYPE_FLOAT  = 4 bytes
```

## Verification & Engineering Rules

- Use `DATA_TYPE_UINT8` or `DATA_TYPE_UINT16` with fixed-point scaling instead of `DATA_TYPE_STRING` whenever possible.
