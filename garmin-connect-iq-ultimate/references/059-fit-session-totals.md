# 059-fit-session-totals: MESG_TYPE_SESSION Overall Activity Summary Stats

- **Domain Category**: FitContributor
- **Primary Connect IQ API**: `FitContributor.MESG_TYPE_SESSION`
- **Sub-Skill ID**: `059-fit-session-totals`

## Overview

Record overall workout summary statistics (`MESG_TYPE_SESSION`) displayed in the Garmin Connect activity summary panel.

## Production Monkey C Implementation Pattern

```monkeyc
_sessionField = createField("total_carbs", 2, FitContributor.DATA_TYPE_UINT16, {
    :mesgType => FitContributor.MESG_TYPE_SESSION,
    :units => "g"
});
```

## Verification & Engineering Rules

- Update `_sessionField.setData(totalGrams)` whenever the cumulative total changes so it is persisted even if the activity ends abruptly.
