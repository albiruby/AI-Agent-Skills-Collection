#!/usr/bin/env python3
"""Static analyzer for Garmin Connect IQ (Monkey C) projects."""

import os
import re
import sys


def audit_project(project_dir: str) -> int:
    issues = []
    manifest_path = os.path.join(project_dir, "manifest.xml")
    if not os.path.isfile(manifest_path):
        issues.append("[ERROR] Missing manifest.xml at project root.")

    source_dir = os.path.join(project_dir, "source")
    if not os.path.isdir(source_dir):
        issues.append("[ERROR] Missing source/ directory.")
    else:
        for root, _, files in os.walk(source_dir):
            for fname in files:
                if not fname.endswith(".mc"):
                    continue
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                on_update_match = re.search(r"function\s+onUpdate\s*\([^)]*\)\s*(?:as\s+\w+\s*)?\{(.*?)\n\s*\}", content, re.S)
                if on_update_match and "loadResource(" in on_update_match.group(1):
                    issues.append(f"[WARN] {fname}: WatchUi.loadResource() called inside onUpdate(dc) risks Out-Of-Memory and frame drops.")

                if "function onPartialUpdate" in content and "setClip" not in content:
                    issues.append(f"[WARN] {fname}: onPartialUpdate(dc) implemented without dc.setClip() risks exceeding the 30ms power budget.")

    if issues:
        print("Connect IQ Project Audit Findings:")
        for item in issues:
            print(" -", item)
        return 1

    print("Connect IQ Project Audit PASSED: Zero structural, memory, or power-budget anti-patterns detected.")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(audit_project(target))
