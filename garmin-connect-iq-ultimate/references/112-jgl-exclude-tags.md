# 112-jgl-exclude-tags: Compile-Time excludeAnnotations (:amoled vs :mip)

- **Domain Category**: Build-Jungle
- **Primary Connect IQ API**: `monkey.jungle`
- **Sub-Skill ID**: `112-jgl-exclude-tags`

## Overview

Strip unused code paths at compile time using `(:amoled)` and `(:mip)` annotations paired with `excludeAnnotations`.

## Production Monkey C Implementation Pattern

```monkeyc
# Inside monkey.jungle:
fenix7.excludeAnnotations = amoled
epix2.excludeAnnotations = mip
```

## Verification & Engineering Rules

- Excluded functions consume zero bytes in the compiled `.prg` binary, saving precious code space on 32KB DataFields.
