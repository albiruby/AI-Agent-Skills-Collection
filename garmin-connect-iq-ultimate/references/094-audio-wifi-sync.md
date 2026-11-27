# 094-audio-wifi-sync: AudioContentProviderApp SyncDelegate & Playlist Download

- **Domain Category**: AudioProvider
- **Primary Connect IQ API**: `Toybox.Media.AudioContentProviderApp`
- **Sub-Skill ID**: `094-audio-wifi-sync`

## Overview

Download offline `.mp3` / `.m4a` tracks over Wi-Fi into Garmin's encrypted media storage using `Communications.SyncDelegate`.

## Production Monkey C Implementation Pattern

```monkeyc
// Use HTTP_RESPONSE_CONTENT_TYPE_AUDIO to download directly into a Media.ContentRef
```

## Verification & Engineering Rules

- Only available on Garmin Music watches (`fr265`, `fr965`, `fenix7`, `epix2`, `venu3`).
