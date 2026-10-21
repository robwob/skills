#!/usr/bin/env python3
"""Convert a wide card sort grid into the one-row-per-placement shape.

Wide input: one row per card, one column per participant, each cell holding
the name of the group that participant put the card in (blank if unsorted).
This is the layout the guide uses for spreadsheet work:

    Card,P1,P2,P3
    Renew a book,Borrowing,Loans,Books

Long output, which analyse.py reads:

    participant_id,card,category,order

Uses only the standard library.
"""
from __future__ import annotations

import argparse
import csv
import sys


class ConvertError(Exception):
    pass


def convert(rows, card_col):
    headers = rows[0]
    if card_col is None:
        card_idx = 0
    elif card_col in headers:
        card_idx = headers.index(card_col)
    else:
        raise ConvertError("Column '%s' not found. Columns: %s." % (
            card_col, ", ".join(headers)))
    participants = [(i, h.strip()) for i, h in enumerate(headers)
                    if i != card_idx]
    if not participants:
        raise ConvertError("No participant columns found next to the card "
                           "column.")
    empty = [i for i, h in participants if not h]
    if empty:
        raise ConvertError("Participant column %d has no header." % (
            empty[0] + 1))
    names = [h for _, h in participants]
    if len(set(names)) != len(names):
        raise ConvertError("Participant column headers must be unique.")

    out, seen = [], set()
    for line_no, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        card = " ".join((row[card_idx] if card_idx < len(row) else "").split())
        if not card:
            raise ConvertError("Line %d has no card name." % line_no)
        if card in seen:
            raise ConvertError("The card '%s' appears twice." % card)
        seen.add(card)
        for i, name in participants:
            cat = " ".join((row[i] if i < len(row) else "").split())
            out.append([name, card, cat, ""])
    if not out:
        raise ConvertError("No data rows found.")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("input", help="wide CSV, one row per card")
    ap.add_argument("--out", required=True, help="long CSV to write")
    ap.add_argument("--card-col", help="name of the card column (default: "
                    "the first column)")
    args = ap.parse_args(argv)
    try:
        with open(args.input, newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.reader(fh))
        if not rows:
            raise ConvertError("The file is empty.")
        long_rows = convert(rows, args.card_col)
    except FileNotFoundError:
        sys.stderr.write("Error: File not found: %s\n" % args.input)
        return 2
    except UnicodeDecodeError:
        sys.stderr.write("Error: Could not read %s as UTF-8. Re-save it as "
                         "CSV UTF-8.\n" % args.input)
        return 2
    except ConvertError as exc:
        sys.stderr.write("Error: %s\n" % exc)
        return 2
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["participant_id", "card", "category", "order"])
        w.writerows(long_rows)
    print("Wrote %d placements to %s" % (len(long_rows), args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
