#!/usr/bin/env python3
"""Arithmetic and checks for usability-test-analysis. Standard library only.

Five commands, each printing what it did and every choice it made:

  columns       list the columns of a results file, with sample values and a guessed type
  pseudonymise  replace participant names with P1, P2 ... and write a private key file
  ratings       count, distribution, median and mean for each rating question
  completion    adjusted-Wald interval for a task completion count
  quotes        check that every quote in a findings file appears verbatim in the data

The file is a CSV. Two layouts are read:

  wide  one row per participant, one column per question (the default)
  long  one row per participant per question, with a question column and an answer column

Run any command with --help for its options. See scripts/README.md.
"""
import argparse
import csv
import difflib
import json
import os
import re
import statistics
import sys
import unicodedata


# ---------------------------------------------------------------------------
# Loading


def read_csv(path):
    """Return (headers, rows). Rows are dicts. Tolerates a UTF-8 byte order mark."""
    if path.lower().endswith((".xlsx", ".xls")):
        sys.exit(
            f"{path} is a spreadsheet, not a CSV. Export it as CSV from the tool or from "
            "Excel, Numbers or Google Sheets (File, Download, CSV), then run this again."
        )
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def require(headers, *cols):
    missing = [c for c in cols if c and c not in headers]
    if missing:
        found = "\n  ".join(headers)
        sys.exit(f"Column not found: {', '.join(missing)}\nColumns in the file:\n  {found}")


def to_records(headers, rows, participant, layout, question_col=None, answer_col=None):
    """Normalise either layout to a list of (participant, question, answer) tuples."""
    require(headers, participant)
    records = []
    if layout == "long":
        require(headers, question_col, answer_col)
        for r in rows:
            records.append((r[participant].strip(), r[question_col].strip(), r[answer_col]))
    else:
        for r in rows:
            for h in headers:
                if h == participant:
                    continue
                records.append((r[participant].strip(), h, r.get(h) or ""))
    return records


def layout_args(p):
    p.add_argument("file", help="results CSV")
    p.add_argument("--participant", required=True, help="column holding the participant name or ID")
    p.add_argument("--layout", choices=["wide", "long"], default="wide",
                   help="wide: one row per participant (default). long: one row per answer")
    p.add_argument("--question-col", help="long layout: the column holding the question text")
    p.add_argument("--answer-col", help="long layout: the column holding the answer")


def check_layout(args):
    if args.layout == "long" and not (args.question_col and args.answer_col):
        sys.exit("The long layout needs --question-col and --answer-col.")


# ---------------------------------------------------------------------------
# columns


def guess_type(values):
    vals = [v.strip() for v in values if v and v.strip()]
    if not vals:
        return "empty"
    nums = []
    for v in vals:
        try:
            nums.append(float(v))
        except ValueError:
            break
    if len(nums) == len(vals):
        if all(n.is_integer() for n in nums) and min(nums) >= 0 and max(nums) <= 11:
            return f"rating? (values {int(min(nums))} to {int(max(nums))})"
        return "number (time? count?)"
    distinct = len(set(v.lower() for v in vals))
    avg_len = sum(len(v) for v in vals) / len(vals)
    if avg_len > 60:
        return "open text or transcript"
    if distinct <= max(3, len(vals) // 3):
        return f"category ({distinct} distinct values)"
    return "short text"


def cmd_columns(args):
    headers, rows = read_csv(args.file)
    print(f"{args.file}: {len(rows)} rows, {len(headers)} columns\n")
    for i, h in enumerate(headers, 1):
        col = [r.get(h) or "" for r in rows]
        sample = next((v for v in col if v.strip()), "")
        sample = sample.replace("\n", " ")
        if len(sample) > 70:
            sample = sample[:67] + "..."
        print(f"{i:>3}. {h}")
        print(f"     guess:  {guess_type(col)}")
        print(f"     sample: {sample!r}")
    print("\nThe guesses are a starting point only. Confirm the mapping with the user before analysing.")


# ---------------------------------------------------------------------------
# pseudonymise


def cmd_pseudonymise(args):
    headers, rows = read_csv(args.file)
    require(headers, args.participant)
    key = {}
    for r in rows:
        name = r[args.participant].strip()
        if name and name not in key:
            key[name] = f"P{len(key) + 1}"

    replaced = 0
    first_name_hits = []
    for r in rows:
        for h in headers:
            if h == args.participant:
                continue
            text = r.get(h) or ""
            # Longest first, so "Anna Lee" is replaced before "Ann" can match inside it.
            for name, pid in sorted(key.items(), key=lambda kv: -len(kv[0])):
                if name and name in text:
                    replaced += text.count(name)
                    text = text.replace(name, pid)
            r[h] = text
        r[args.participant] = key.get(r[args.participant].strip(), r[args.participant])

    for r in rows:
        for h in headers:
            if h == args.participant:
                continue
            for name, pid in key.items():
                first = name.split()[0] if name.split() else ""
                if len(first) > 2 and first != name and re.search(rf"\b{re.escape(first)}\b", r.get(h) or ""):
                    first_name_hits.append((r[args.participant], h, first))

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=headers)
        w.writeheader()
        w.writerows(rows)
    with open(args.key, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["participant_id", "original"])
        for name, pid in key.items():
            w.writerow([pid, name])

    print(f"{len(key)} participants renamed P1 to P{len(key)}, in order of first appearance.")
    print(f"{replaced} occurrence(s) of a full name replaced inside answers.")
    print(f"Pseudonymised file: {os.path.abspath(args.out)}")
    print(f"Key (keep private, never put it in the report): {os.path.abspath(args.key)}")
    if first_name_hits:
        print("\nFirst names that may still identify someone. Check these cells by hand:")
        for pid, col, first in first_name_hits:
            print(f"  {pid}, column {col!r}: {first!r}")
    print("\nNames of other people, places and employers inside answers are not touched.")


# ---------------------------------------------------------------------------
# ratings


def parse_scale(text):
    m = re.fullmatch(r"\s*(-?\d+)\s*(?:-|to|\.\.)\s*(-?\d+)\s*", text or "")
    if not m:
        sys.exit(f"--scale must look like 1-7, got {text!r}")
    lo, hi = int(m.group(1)), int(m.group(2))
    if lo >= hi:
        sys.exit("--scale minimum must be below its maximum")
    return lo, hi


def summarise(values, lo, hi):
    counts = {p: 0 for p in range(lo, hi + 1)}
    for v in values:
        counts[v] += 1
    n = len(values)
    out = {"n": n, "distribution": counts}
    if n:
        out["median"] = statistics.median(values)
        out["mean"] = round(sum(values) / n, 2)
        out["min"] = min(values)
        out["max"] = max(values)
    return out


def cmd_ratings(args):
    check_layout(args)
    headers, rows = read_csv(args.file)
    lo, hi = parse_scale(args.scale)
    records = to_records(headers, rows, args.participant, args.layout, args.question_col, args.answer_col)
    # In the wide layout a question can be given by its number from the `columns` listing.
    questions = []
    for q in args.question:
        if args.layout == "wide" and q.isdigit() and 1 <= int(q) <= len(headers):
            questions.append(headers[int(q) - 1])
        else:
            questions.append(q)
    known = {q for _, q, _ in records}
    unknown = [q for q in questions if q not in known]
    if unknown:
        sys.exit("Question not found: " + "; ".join(unknown) + "\nQuestions in the data:\n  "
                 + "\n  ".join(sorted(known)))

    result = {"scale": [lo, hi], "questions": []}
    for q in questions:
        values, by_participant, blank, invalid = [], {}, [], []
        for pid, qq, ans in records:
            if qq != q:
                continue
            a = (ans or "").strip()
            if not a:
                blank.append(pid)
                continue
            try:
                v = float(a)
            except ValueError:
                invalid.append((pid, a))
                continue
            if not v.is_integer() or not lo <= v <= hi:
                invalid.append((pid, a))
                continue
            values.append(int(v))
            by_participant[pid] = int(v)
        s = summarise(values, lo, hi)
        s.update({"question": q, "by_participant": by_participant,
                  "blank": blank, "invalid": invalid})
        result["questions"].append(s)

    for s in result["questions"]:
        print(f"\n{s['question']}")
        print(f"  Answered: {s['n']}" + (f", blank: {len(s['blank'])} ({', '.join(s['blank'])})" if s["blank"] else ""))
        if s["invalid"]:
            print("  Not counted, outside the scale or not a whole number: "
                  + ", ".join(f"{p}={a!r}" for p, a in s["invalid"]))
        if not s["n"]:
            continue
        dist = ", ".join(f"{k}: {v}" for k, v in s["distribution"].items() if v)
        print(f"  Distribution: {dist}")
        print(f"  Median: {s['median']}   Mean: {s['mean']} / {hi}   Range: {s['min']} to {s['max']}")
        print("  By participant: " + ", ".join(f"{p}={v}" for p, v in s["by_participant"].items()))
        working = " + ".join(str(v) for v in s["by_participant"].values())
        print(f"  Working: ({working}) / {s['n']} = {s['mean']}")

    print("\nThe mean is printed for comparison with published benchmarks only. Lead with the "
          "distribution: at small numbers one participant moves the mean a long way.")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print(f"Written: {os.path.abspath(args.json)}")


# ---------------------------------------------------------------------------
# completion


def adjusted_wald(x, n, z=1.96):
    """Adjusted-Wald interval (Agresti and Coull), as Sauro and Lewis recommend for small n."""
    n_adj = n + z * z
    p_adj = (x + z * z / 2) / n_adj
    half = z * (p_adj * (1 - p_adj) / n_adj) ** 0.5
    return max(0.0, p_adj - half), min(1.0, p_adj + half)


def cmd_completion(args):
    x, n = args.successes, args.n
    if not 0 <= x <= n or n < 1:
        sys.exit("Successes must be between 0 and n, and n at least 1.")
    lo, hi = adjusted_wald(x, n)
    print(f"{x} of {n} completed.")
    print(f"95% adjusted-Wald interval for the completion rate: {lo:.0%} to {hi:.0%}.")
    print("Report the count and this range together, never the point percentage on its own.")


# ---------------------------------------------------------------------------
# quotes


QUOTE_MAP = {
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"', "\u2032": "'", "\u2033": '"',
    "\u2013": "-", "\u2014": "-", "\u2026": "...", "\u00a0": " ",
}


def norm(text):
    """Normalise only what does not change meaning: typographic quotes, dashes, spacing, case."""
    text = unicodedata.normalize("NFKC", text or "")
    for a, b in QUOTE_MAP.items():
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip().lower()


def split_ellipsis(quote):
    """A quote with '...' is checked as fragments that must appear in order."""
    return [f.strip() for f in re.split(r"\.\.\.|\[\.\.\.\]", norm(quote)) if f.strip()]


def find_in_order(fragments, text):
    pos = 0
    for f in fragments:
        i = text.find(f, pos)
        if i < 0:
            return False
        pos = i + len(f)
    return True


def closest(quote, texts):
    q = norm(quote)
    best, best_ratio = None, 0.0
    for pid, text in texts:
        t = norm(text)
        if not t:
            continue
        sm = difflib.SequenceMatcher(None, q, t, autojunk=False)
        m = sm.find_longest_match(0, len(q), 0, len(t))
        start = max(0, m.b - m.a)
        window = t[start:start + len(q) + 20]
        r = difflib.SequenceMatcher(None, q, window).ratio()
        if r > best_ratio:
            best, best_ratio = (pid, window), r
    return best, best_ratio


def cmd_quotes(args):
    check_layout(args)
    headers, rows = read_csv(args.file)
    records = to_records(headers, rows, args.participant, args.layout, args.question_col, args.answer_col)
    by_pid = {}
    for pid, _, ans in records:
        by_pid.setdefault(pid, []).append(ans or "")
    texts = [(pid, "\n".join(a)) for pid, a in by_pid.items()]

    with open(args.quotes, encoding="utf-8") as fh:
        quotes = json.load(fh)
    if isinstance(quotes, dict):
        quotes = quotes.get("quotes", [])

    failures = 0
    for i, item in enumerate(quotes, 1):
        quote, pid = item.get("quote", ""), str(item.get("participant", "")).strip()
        frags = split_ellipsis(quote)
        own = norm("\n".join(by_pid.get(pid, [])))
        if pid and pid not in by_pid:
            status = "PARTICIPANT NOT IN DATA"
        elif frags and find_in_order(frags, own):
            status = "VERBATIM"
        else:
            others = [p for p, t in texts if p != pid and frags and find_in_order(frags, norm(t))]
            status = f"WRONG PARTICIPANT (found under {', '.join(others)})" if others else "NOT FOUND"
        ok = status == "VERBATIM"
        failures += not ok
        print(f"{i:>3}. [{status}] {pid}: \"{quote}\"")
        if not ok and status == "NOT FOUND":
            match, ratio = closest(quote, texts)
            if match and ratio >= 0.5:
                print(f"     Closest text ({match[0]}, {ratio:.0%} similar): \"{match[1]}\"")
            print("     Replace it with the participant's exact words, or remove it.")

    print(f"\n{len(quotes) - failures} of {len(quotes)} quotes verbatim.")
    print("Checked ignoring case, spacing and typographic quote marks. '...' marks a cut, and the "
          "pieces must appear in order. Nothing else is forgiven.")
    if failures:
        sys.exit(1)


# ---------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("columns", help="list columns with a guessed type")
    p.add_argument("file")
    p.set_defaults(func=cmd_columns)

    p = sub.add_parser("pseudonymise", help="replace participant names with P1, P2 ...")
    p.add_argument("file")
    p.add_argument("--participant", required=True)
    p.add_argument("--out", required=True, help="pseudonymised CSV to write")
    p.add_argument("--key", required=True, help="private key CSV to write")
    p.set_defaults(func=cmd_pseudonymise)

    p = sub.add_parser("ratings", help="summarise rating questions")
    layout_args(p)
    p.add_argument("--question", action="append", required=True,
                   help="a rating question, exactly as it appears in the data, or (wide layout) "
                        "its column number from `columns`. Repeat for each")
    p.add_argument("--scale", required=True, help="the scale, for example 1-5 or 1-7")
    p.add_argument("--json", help="also write the results to this JSON file")
    p.set_defaults(func=cmd_ratings)

    p = sub.add_parser("completion", help="interval for a task completion rate")
    p.add_argument("successes", type=int)
    p.add_argument("n", type=int)
    p.set_defaults(func=cmd_completion)

    p = sub.add_parser("quotes", help="check quotes are verbatim")
    layout_args(p)
    p.add_argument("--quotes", required=True,
                   help='JSON list of {"quote": ..., "participant": ...}')
    p.set_defaults(func=cmd_quotes)

    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
