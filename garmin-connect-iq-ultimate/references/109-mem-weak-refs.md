# 109-mem-weak-refs: WeakReference Safe Caching & Circular Reference Prevention

- **Domain Category**: Memory
- **Primary Connect IQ API**: `Toybox.Lang.WeakReference`
- **Sub-Skill ID**: `109-mem-weak-refs`

## Overview

Prevent reference-counted memory leaks between `View` and `Delegate` or `Timer` callbacks using `obj.weak()`.

## Production Monkey C Implementation Pattern

```monkeyc
// Monkey C uses reference counting (not mark-and-sweep GC!).
// Circular references (A -> B and B -> A) will NEVER be freed unless broken or stored as WeakReference:
private var _weakView as WeakReference;
public function initialize(view as MainView) {
    _weakView = view.weak();
}
```

## Verification & Engineering Rules

- This is the #1 cause of hidden memory leaks in Monkey C: always break parent-child cycles in `onHide()` or use `.weak()`.
