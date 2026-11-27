# 057-fit-record-stream: MESG_TYPE_RECORD 1Hz Time-Series FIT Stream

- **Domain Category**: FitContributor
- **Primary Connect IQ API**: `FitContributor.MESG_TYPE_RECORD`
- **Sub-Skill ID**: `057-fit-record-stream`

## Overview

Write per-second telemetry into the activity `.fit` file stream using `FitContributor.MESG_TYPE_RECORD`.

## Production Monkey C Implementation Pattern

```monkeyc
_recordField = createField("carb_rate", 0, FitContributor.DATA_TYPE_FLOAT, {
    :mesgType => FitContributor.MESG_TYPE_RECORD,
    :units => "g/h"
});
// Inside compute(info):
_recordField.setData(currentRateFloat);
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="FitContributor"/>` in `manifest.xml`.
