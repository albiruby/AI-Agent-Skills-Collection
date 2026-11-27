# 088-app-vibe-tone-alert: Tactile VibeProfile Sequences & Codec Audio Tones

- **Domain Category**: DeviceApp
- **Primary Connect IQ API**: `Toybox.Attention`
- **Sub-Skill ID**: `088-app-vibe-tone-alert`

## Overview

Trigger custom multi-pulse vibration rhythms (`Attention.VibeProfile`) and alert tones (`Attention.playTone`).

## Production Monkey C Implementation Pattern

```monkeyc
if (Attention has :vibrate) {
    Attention.vibrate([
        new Attention.VibeProfile(100, 180),
        new Attention.VibeProfile(0, 90),
        new Attention.VibeProfile(100, 320)
    ]);
}
if (Attention has :playTone) {
    Attention.playTone(Attention.TONE_INTERVAL_ALERT);
}
```

## Verification & Engineering Rules

- Check `Attention has :playTone` because several vivoactive/Venu models have vibration motors but no piezo buzzer.
