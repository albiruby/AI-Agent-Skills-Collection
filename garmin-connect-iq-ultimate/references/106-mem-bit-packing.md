# 106-mem-bit-packing: 32-Bit Integer Coordinate & Color Bit-Packing

- **Domain Category**: Memory
- **Primary Connect IQ API**: `Toybox.Lang.Number`
- **Sub-Skill ID**: `106-mem-bit-packing`

## Overview

Pack `(x, y, width, height)` or `(x, y, color)` tuples into a single 32-bit `Number` to cut array memory by 75%.

## Production Monkey C Implementation Pattern

```monkeyc
// Pack x (10 bits), y (10 bits), val (12 bits):
var packed = ((x & 0x3FF) << 22) | ((y & 0x3FF) << 12) | (val & 0xFFF);
var ux = (packed >> 22) & 0x3FF;
var uy = (packed >> 12) & 0x3FF;
var uval = packed & 0xFFF;
```

## Verification & Engineering Rules

- Ideal for storing lookup tables, polygon coordinates, and waveform histories.
