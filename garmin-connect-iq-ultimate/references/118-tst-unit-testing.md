# 118-tst-unit-testing: Run-No-Evil (:test) Automated Unit Test Suite

- **Domain Category**: Testing
- **Primary Connect IQ API**: `Toybox.Test`
- **Sub-Skill ID**: `118-tst-unit-testing`

## Overview

Write automated unit tests for metabolic math, pace converters, and bit-packing using `(:test)` functions and `Test.assertEqualMessage`.

## Production Monkey C Implementation Pattern

```monkeyc
import Toybox.Test;
import Toybox.Lang;

(:test)
function testBitPackRoundTrip(logger as Test.Logger) as Boolean {
    var x = 215;
    var y = 180;
    var packed = ((x & 0x3FF) << 12) | (y & 0x3FF);
    Test.assertEqualMessage((packed >> 12) & 0x3FF, 215, "X coordinate mismatch");
    Test.assertEqualMessage(packed & 0x3FF, 180, "Y coordinate mismatch");
    return true;
}
```

## Verification & Engineering Rules

- Functions annotated with `(:test)` are automatically stripped from production release builds.
