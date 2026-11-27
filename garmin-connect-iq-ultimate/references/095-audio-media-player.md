# 095-audio-media-player: Media.ContentIterator & Playback Control Lifecycle

- **Domain Category**: AudioProvider
- **Primary Connect IQ API**: `Toybox.Media.ContentIterator`
- **Sub-Skill ID**: `095-audio-media-player`

## Overview

Supply track metadata, shuffle/repeat states, and skip hooks to the native Garmin Music Player via `Media.ContentIterator`.

## Production Monkey C Implementation Pattern

```monkeyc
// Return Media.ContentProfile with AlbumArt and PlaybackProfile from ContentDelegate
```

## Verification & Engineering Rules

- Inspect `Media.getCacheStatistics()` before downloading new audio files to verify available flash storage.
