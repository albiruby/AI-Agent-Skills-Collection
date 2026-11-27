# 120-rel-iq-store-export: Signed .iq Connect IQ Store Release Packaging

- **Domain Category**: Release
- **Primary Connect IQ API**: `monkeyc CLI`
- **Sub-Skill ID**: `120-rel-iq-store-export`

## Overview

Compile, optimize (`-O2`), type-check (`-l 3`), and sign a multi-device `.iq` store package for Connect IQ Store submission.

## Production Monkey C Implementation Pattern

```monkeyc
# Generate 4096-bit RSA key (DER format) & build signed .iq package:
# openssl genrsa -out dev_key.pem 4096
# openssl pkcs8 -topk8 -inform PEM -outform DER -in dev_key.pem -out dev_key.der -nocrypt
# monkeyc -e -f monkey.jungle -o dist/app.iq -y dev_key.der -O2 -l 3
```

## Verification & Engineering Rules

- Verify that `manifest.xml` has a unique production UUID (never reuse sample SDK UUIDs) before uploading to the Connect IQ Store.
