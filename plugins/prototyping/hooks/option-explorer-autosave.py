#!/usr/bin/env python3
"""Safety net for option-explorer prototypes.

PreToolUse hook on Edit|Write|MultiEdit. If the file about to be edited is part
of an option-explorer prototype (the prototype's HTML, carrying
<meta name="generator" content="option-explorer">, or a shell, design or screen
file whose first comment names option-explorer) and is not a frozen copy inside
explorations/, copy it as it is now into explorations/.autosave/ beside the
prototype, unless the newest snapshot of that file is already identical.

Snapshots are named after the file's path from the prototype folder, e.g.
prototype__screens__home-20261111-160501.js. They are not record entries: the
option-explorer skill writes the record, this only guarantees no iteration is
ever lost. Always exits 0 and prints nothing, so it can never block an edit.
"""
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime

MARKER = b"option-explorer"
EXTS = (".html", ".js", ".css")


def project_root(path):
    """The nearest folder above the file that holds an explorations/ folder."""
    d = os.path.dirname(path)
    for _ in range(4):
        if os.path.isdir(os.path.join(d, "explorations")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    path = (data.get("tool_input") or {}).get("file_path") or ""
    if not path.endswith(EXTS) or not os.path.isfile(path):
        return
    if "explorations" in os.path.normpath(path).split(os.sep):
        return
    with open(path, "rb") as fh:
        body = fh.read()
    if MARKER not in body[:4096]:
        return
    root = project_root(path)
    if not root:
        return
    folder = os.path.join(root, "explorations", ".autosave")
    os.makedirs(folder, exist_ok=True)
    rel = os.path.relpath(path, root)
    stem, ext = os.path.splitext(rel.replace(os.sep, "__"))
    digest = hashlib.sha256(body).hexdigest()
    existing = sorted(f for f in os.listdir(folder) if f.startswith(stem + "-") and f.endswith(ext))
    if existing:
        with open(os.path.join(folder, existing[-1]), "rb") as fh:
            if hashlib.sha256(fh.read()).hexdigest() == digest:
                return
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copyfile(path, os.path.join(folder, f"{stem}-{stamp}{ext}"))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
