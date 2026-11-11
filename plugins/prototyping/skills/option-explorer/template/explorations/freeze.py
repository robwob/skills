#!/usr/bin/env python3
"""Freeze the prototype as it is now into the explorations record.

    python3 explorations/freeze.py --screen home --option B --title "B2: shorter list"
    python3 explorations/freeze.py --check

Copies the prototype into explorations/<screen>/NN-<slug>.html and appends an
entry to records.js. The previous latest entry for the same screen and option
is marked "replaced" (unless it was already rejected or replaced). why, aim and
outcome start as TODO and are written afterwards from the conversation.

--check reports whether the prototype differs from the newest frozen copy,
i.e. whether there is an iteration nobody has recorded yet. Exit 0 if up to
date, 1 if not.

The prototype is found automatically: the one .html file beside explorations/
that carries <meta name="generator" content="option-explorer">. Pass
--prototype if there is more than one.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
RECORDS = os.path.join(HERE, "records.js")
MARKER = b'content="option-explorer"'
PREFIX = "window.EXPLORATIONS = "
HEADER = '// Written by freeze.py. Everything after the "=" is JSON, so keep it valid JSON.\n'


def load():
    text = open(RECORDS, encoding="utf-8").read()
    body = text[text.index(PREFIX) + len(PREFIX):].strip()
    return json.loads(body.rstrip(";"))


def save(data):
    with open(RECORDS, "w", encoding="utf-8") as fh:
        fh.write(HEADER + PREFIX + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")


def find_prototype(given):
    if given:
        path = os.path.abspath(given)
        if not os.path.isfile(path):
            sys.exit(f"No prototype at {path}")
        return path
    found = []
    for name in sorted(os.listdir(PARENT)):
        path = os.path.join(PARENT, name)
        if name.endswith(".html") and os.path.isfile(path):
            with open(path, "rb") as fh:
                if MARKER in fh.read(4096):
                    found.append(path)
    if len(found) != 1:
        sys.exit(f"Expected one option-explorer prototype beside explorations/, found {len(found)}. Pass --prototype.")
    return found[0]


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48] or "iteration"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--screen", help="screen key, as in SCREENS (e.g. home)")
    ap.add_argument("--screen-name", help="display name for a screen the record has not seen yet")
    ap.add_argument("--option", help="option key, as in that screen's options (e.g. B)")
    ap.add_argument("--title", help='short title, e.g. "B2: shorter list"')
    ap.add_argument("--status", default="exploring", choices=["exploring", "chosen", "rejected", "replaced"])
    ap.add_argument("--rebuilt", action="store_true", help="the copy was reconstructed, not saved at the time")
    ap.add_argument("--prototype", help="path to the prototype, if it cannot be found automatically")
    ap.add_argument("--check", action="store_true", help="report whether there is an unrecorded iteration")
    a = ap.parse_args()

    proto = find_prototype(a.prototype)
    data = load()
    records = data.setdefault("records", [])

    if a.check:
        if not records:
            print("Nothing frozen yet: freeze the current state first.")
            sys.exit(1)
        newest = os.path.join(HERE, records[-1]["file"])
        if os.path.isfile(newest) and sha(newest) == sha(proto):
            print("Up to date: the prototype matches the newest frozen copy.")
            sys.exit(0)
        print(f"Unrecorded changes: the prototype differs from the newest frozen copy ({records[-1]['id']}).")
        sys.exit(1)

    if not (a.screen and a.option and a.title):
        ap.error("--screen, --option and --title are required unless --check")

    folder = os.path.join(HERE, a.screen)
    os.makedirs(folder, exist_ok=True)
    n = len([f for f in os.listdir(folder) if f.endswith(".html")]) + 1
    rel = f"{a.screen}/{n:02d}-{slug(a.title)}.html"
    shutil.copyfile(proto, os.path.join(HERE, rel))

    data["prototype"] = os.path.basename(proto)
    screens = data.setdefault("screens", {})
    if a.screen not in screens:
        screens[a.screen] = {"name": a.screen_name or a.screen.replace("-", " ").title()}

    for r in reversed(records):
        if r["screen"] == a.screen and r["option"] == a.option:
            if r["status"] in ("exploring", "chosen"):
                r["status"] = "replaced"
                if not r.get("outcome") or str(r["outcome"]).startswith("TODO"):
                    r["outcome"] = f"Replaced by {a.title}."
            break

    rid = f"{a.screen}-{n:02d}"
    today = date.today()
    records.append({
        "id": rid, "screen": a.screen, "option": a.option, "title": a.title,
        "date": f"{today.day} {today.strftime('%b %Y')}", "status": a.status, "file": rel,
        "why": "TODO", "aim": "TODO", "outcome": "TODO", "quotes": [],
        **({"rebuilt": True} if a.rebuilt else {}),
    })
    save(data)
    print(f"Frozen {rid}: explorations/{rel}")


if __name__ == "__main__":
    main()
