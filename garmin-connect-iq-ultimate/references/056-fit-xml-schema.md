# 056-fit-xml-schema: FitContributor XML Resource Schema & Chart Colors

- **Domain Category**: FitContributor
- **Primary Connect IQ API**: `Toybox.FitContributor`
- **Sub-Skill ID**: `056-fit-xml-schema`

## Overview

Define custom developer FIT fields in `resources/fitcontributions/fitcontributions.xml` so Garmin Connect renders charts and lap columns.

## Production Monkey C Implementation Pattern

```monkeyc
<fitContributions>
    <fitField id="0" displayInChart="true" displayInActivitySummary="true"
              sortOrder="0" precision="1" chartTitle="@Strings.CarbChart"
              dataLabel="@Strings.CarbLabel" unitLabel="@Strings.GramUnit"
              fillColor="#00E676" />
</fitContributions>
```

## Verification & Engineering Rules

- Every `id` in `<fitField>` must match the `fieldId` integer passed to `DataField.createField()`.
