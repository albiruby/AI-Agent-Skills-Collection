# 091-bg-json-webrequest: Background HTTPS JSON WebRequest & Bearer Auth

- **Domain Category**: Background
- **Primary Connect IQ API**: `Toybox.Communications.makeWebRequest`
- **Sub-Skill ID**: `091-bg-json-webrequest`

## Overview

Execute HTTPS REST requests in foreground or background processes and handle HTTP status codes and JSON parsing.

## Production Monkey C Implementation Pattern

```monkeyc
var opts = {
    :method => Communications.HTTP_REQUEST_METHOD_GET,
    :headers => {"Authorization" => "Bearer " + token},
    :responseType => Communications.HTTP_RESPONSE_CONTENT_TYPE_JSON
};
Communications.makeWebRequest(url, null, opts, method(:onWebResponse));
```

## Verification & Engineering Rules

- Requires `<iq:uses-permission id="Communications"/>` and an active Garmin Connect Mobile Bluetooth or Wi-Fi connection.
