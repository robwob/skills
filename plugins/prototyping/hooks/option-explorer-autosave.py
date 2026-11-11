#!/usr/bin/env python3
"""Safety net for option-explorer prototypes.

PreToolUse hook on Edit|Write|MultiEdit. If the file about to be edited is an
option-explorer prototype (it carries <meta name="generator" content="option-explorer">)
and is not itself a frozen copy inside explorations/, copy it as it is now into
explorations/.autosave/<name>-<timestamp>.html beside it, unless the newest
snapshot is already identical.

These snapshots are not record entries. The option-explorer skill writes the
record; this only guarantees no iteration is ever lost. Always exits 0 and
prints nothing, so it can never block an edit.
"""
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime

MARKER = b'content="option-explorer"'


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    path = (data.get("tool_input") or {}).get("file_path") or ""
    if not path.endswith(".html") or not os.path.isfile(path):
        return
    parts = os.path.normpath(path).split(os.sep)
    if "explorations" in parts:
        return
    with open(path, "rb") as fh:
        body = fh.read()
    if MARKER not in body[:4096]:
        return
    folder = os.path.join(os.path.dirname(path), "explorations", ".autosave")
    os.makedirs(folder, exist_ok=True)
    stem = os.path.splitext(os.path.basename(path))[0]
    digest = hashlib.sha256(body).hexdigest()
    existing = sorted(f for f in os.listdir(folder) if f.startswith(stem + "-") and f.endswith(".html"))
    if existing:
        with open(os.path.join(folder, existing[-1]), "rb") as fh:
            if hashlib.sha256(fh.read()).hexdigest() == digest:
                return
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copyfile(path, os.path.join(folder, f"{stem}-{stamp}.html"))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
