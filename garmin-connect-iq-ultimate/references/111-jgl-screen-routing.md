# 111-jgl-screen-routing: monkey.jungle Screen Shape & Resolution Resource Routing

- **Domain Category**: Build-Jungle
- **Primary Connect IQ API**: `monkey.jungle`
- **Sub-Skill ID**: `111-jgl-screen-routing`

## Overview

Route device families (`round-260x260`, `round-454x454`, `semi-octagon-176x176`, `rectangle-282x470`) cleanly in `monkey.jungle`.

## Production Monkey C Implementation Pattern

```monkeyc
project.manifest = manifest.xml
base.sourcePath = source
base.resourcePath = resources

round-260x260.resourcePath = $(round-260x260.resourcePath);resources-mip
round-454x454.resourcePath = $(round-454x454.resourcePath);resources-amoled
```

## Verification & Engineering Rules

- Garmin automatically supports built-in qualifier folders like `resources-round-260x260/` even without custom Jungle overrides.
