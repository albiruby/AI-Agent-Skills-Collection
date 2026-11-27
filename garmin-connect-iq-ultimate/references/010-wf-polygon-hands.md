# 010-wf-polygon-hands: 2D Rotation Matrix Vector Polygon Watch Hands

- **Domain Category**: WatchFace
- **Primary Connect IQ API**: `Graphics.Dc.fillPolygon`
- **Sub-Skill ID**: `010-wf-polygon-hands`

## Overview

Render razor-sharp analog hour, minute, and second hands at any angle using a 2D rotation matrix over normalized vertex arrays.

## Production Monkey C Implementation Pattern

```monkeyc
private function drawRotatedHand(dc as Dc, cx as Number, cy as Number, angleRad as Float, coords as Array< Array<Float> >) as Void {
    var sin = Math.sin(angleRad);
    var cos = Math.cos(angleRad);
    var poly = new Array< Array<Numeric> >[coords.size()];
    for (var i = 0; i < coords.size(); i++) {
        var px = coords[i][0];
        var py = coords[i][1];
        poly[i] = [
            cx + (px * cos - py * sin),
            cy + (px * sin + py * cos)
        ];
    }
    dc.fillPolygon(poly);
}
```

## Verification & Engineering Rules

- Pre-allocate the output polygon array as a member variable to avoid allocating a new array every second.
