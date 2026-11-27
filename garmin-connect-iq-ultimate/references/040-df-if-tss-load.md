# 040-df-if-tss-load: Intensity Factor (IF) & Training Stress Score (TSS)

- **Domain Category**: DataField
- **Primary Connect IQ API**: `Activity.Info`
- **Sub-Skill ID**: `040-df-if-tss-load`

## Overview

Compute real-time Intensity Factor (`NP / FTP`) and cumulative Training Stress Score during cycling or running workouts.

## Production Monkey C Implementation Pattern

```monkeyc
public function calcTss(durationSec as Number, np as Number, ftp as Number) as Float {
    if (ftp <= 0 || durationSec <= 0) { return 0.0f; }
    var ifVal = np.toFloat() / ftp.toFloat();
    return ((durationSec.toFloat() * np.toFloat() * ifVal) / (ftp.toFloat() * 3600.0f)) * 100.0f;
}
```

## Verification & Engineering Rules

- Provide an app setting in `properties.xml` for user FTP (default `250W`) with validation guarding `ftp >= 50`.
