"""Tests for scripts/check.py. Run from the skill folder with:  python3 -m unittest discover tests"""
import contextlib
import csv
import glob
import importlib.util
import io
import json
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EX = os.path.join(ROOT, "examples")
INTERVIEWS = sorted(glob.glob(os.path.join(EX, "interviews", "*.csv")))

spec = importlib.util.spec_from_file_location("check", os.path.join(ROOT, "scripts", "check.py"))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def run(*argv):
    out = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(out):
        try:
            check.main(list(argv))
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 1
            if isinstance(e.code, str):
                out.write(e.code)
    return code, out.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def path(self, name):
        return os.path.join(self.tmp.name, name)

    def write(self, name, text):
        with open(self.path(name), "w", newline="", encoding="utf-8") as fh:
            fh.write(text)
        return self.path(name)

    def anon(self):
        code, out = run("pseudonymise", *INTERVIEWS, "--speaker", "Speaker", "--text", "Text",
                        "--start", "Start", "--end", "End", "--interviewer", "Jordan Ellis",
                        "--out", self.path("anon.csv"), "--key", self.path("key.csv"))
        self.assertEqual(code, 0, out)
        return self.path("anon.csv")


class Timestamps(unittest.TestCase):
    def test_formats(self):
        self.assertEqual(check.to_seconds("00:01:02"), 62)
        self.assertEqual(check.to_seconds("1:02:03"), 3723)
        self.assertEqual(check.to_seconds("01:02"), 62)
        self.assertAlmostEqual(check.to_seconds("00:01:02,500"), 62.5)
        self.assertAlmostEqual(check.to_seconds("00:01:02.25"), 62.25)
        self.assertEqual(check.to_seconds("62.5"), 62.5)
        self.assertIsNone(check.to_seconds(""))
        self.assertIsNone(check.to_seconds("soon"))


class Pseudonymise(Base):
    def test_examples_become_six_participants(self):
        anon = self.anon()
        with open(anon, newline="") as fh:
            rows = list(csv.DictReader(fh))
        pids = {r["participant"] for r in rows if r["role"] == "participant"}
        self.assertEqual(pids, {f"P{i}" for i in range(1, 7)})
        self.assertTrue(all(r["participant"] == "" for r in rows if r["role"] == "interviewer"))
        with open(self.path("key.csv"), newline="") as fh:
            key = list(csv.reader(fh))
        self.assertEqual(key[1], ["P1", "interview-01", "Priya Shah"])

    def test_same_label_in_two_interviews_is_two_people(self):
        a = self.write("a.csv", "who,said\nMod,Hi\nParticipant,Hello\n")
        b = self.write("b.csv", "who,said\nMod,Hi\nParticipant,Hey\n")
        code, out = run("pseudonymise", a, b, "--speaker", "who", "--text", "said",
                        "--interviewer", "Mod", "--out", self.path("o.csv"), "--key", self.path("k.csv"))
        self.assertEqual(code, 0, out)
        self.assertIn("P2: interview 'b'", out)
        self.assertIn("labelled by role", out)

    def test_names_replaced_and_first_names_flagged(self):
        f = self.write("n.csv", "iv,who,t\n1,Sam Lee,Hi\n1,Anna Lee,Sam Lee asked me. Anna is me.\n")
        code, out = run("pseudonymise", f, "--speaker", "who", "--text", "t", "--interview", "iv",
                        "--interviewer", "Sam Lee", "--out", self.path("o.csv"), "--key", self.path("k.csv"))
        self.assertEqual(code, 0, out)
        with open(self.path("o.csv"), newline="") as fh:
            rows = list(csv.DictReader(fh))
        self.assertEqual(rows[1]["text"], "[Interviewer] asked me. Anna is me.")
        self.assertIn("'Anna'", out)

    def test_unknown_interviewer_lists_speakers(self):
        code, out = run("pseudonymise", INTERVIEWS[0], "--speaker", "Speaker", "--text", "Text",
                        "--interviewer", "Nobody", "--out", self.path("o.csv"), "--key", self.path("k.csv"))
        self.assertNotEqual(code, 0)
        self.assertIn("Priya Shah", out)

    def test_xlsx_is_refused_with_instructions(self):
        code, out = run("columns", "transcript.xlsx")
        self.assertNotEqual(code, 0)
        self.assertIn("CSV", out)


class StatsAndPrompts(Base):
    def test_stats_runs(self):
        code, out = run("stats", self.anon())
        self.assertEqual(code, 0, out)
        self.assertIn("interview-01", out)

    def test_interviewer_dominating_is_flagged(self):
        f = self.write("t.csv", "who,said\nMod,One two three four five six seven eight\nP,Yes\n")
        run("pseudonymise", f, "--speaker", "who", "--text", "said", "--interviewer", "Mod",
            "--out", self.path("o.csv"), "--key", self.path("k.csv"))
        code, out = run("stats", self.path("o.csv"))
        self.assertIn("spoke more words than the participant", out)

    def test_prompts_finds_hypothetical_and_leading(self):
        code, out = run("prompts", self.anon())
        self.assertEqual(code, 0, out)
        self.assertIn("[leading] interview 'interview-02'", out)
        self.assertIn("[hypothetical] interview 'interview-01'", out)
        self.assertNotIn("Tell me about", out)


class Quotes(Base):
    def check(self, quotes):
        qf = self.write("q.json", json.dumps(quotes))
        return run("quotes", self.anon(), "--quotes", qf)

    def test_sample_quotes_pass(self):
        code, out = run("quotes", self.anon(), "--quotes", os.path.join(EX, "sample-quotes.json"))
        self.assertEqual(code, 0, out)

    def test_typographic_marks_and_ellipsis(self):
        code, out = self.check([
            {"quote": "I hadn’t sent a reading since the summer ... I just forgot.", "participant": "P1"},
        ])
        self.assertEqual(code, 0, out)

    def test_interviewer_words_are_caught(self):
        code, out = self.check([{"quote": "That must have been frustrating, right?", "participant": "P2"}])
        self.assertEqual(code, 1)
        self.assertIn("INTERVIEWER'S WORDS", out)

    def test_wrong_participant_is_named(self):
        code, out = self.check([{"quote": "I take a photo of the meter first, every time", "participant": "P1"}])
        self.assertEqual(code, 1)
        self.assertIn("found under P5", out)

    def test_wrong_timestamp_is_caught(self):
        code, out = self.check([{"quote": "I take a photo of the meter first, every time",
                                 "participant": "P5", "at": "00:03:01"}])
        self.assertEqual(code, 1)
        self.assertIn("TIMESTAMP WRONG (found at 00:01:03)", out)

    def test_paraphrase_fails_with_closest_text(self):
        code, out = self.check([{"quote": "The bill was almost double what I thought", "participant": "P1"}])
        self.assertEqual(code, 1)
        self.assertIn("NOT FOUND", out)
        self.assertIn("Closest text", out)


class Tally(Base):
    def test_sample_coding(self):
        code, out = run("tally", os.path.join(EX, "sample-coding.csv"), "--transcripts", self.anon(),
                        "--segments", os.path.join(EX, "sample-segments.csv"), "--json", self.path("t.json"))
        self.assertEqual(code, 0, out)
        with open(self.path("t.json")) as fh:
            themes = {t["theme"]: t for t in json.load(fh)["themes"]}
        est = themes["Estimated bills arrive as a surprise"]
        self.assertEqual(est["for_count"], 4)
        self.assertEqual(est["against"], ["P6"])
        self.assertEqual(est["suggested"]["coherence"], "minor")
        # P1 is coded twice for the reminder theme and counts once.
        rem = themes["Reading reminders arrive when people cannot act"]
        self.assertEqual(rem["for_count"], 4)
        self.assertEqual(rem["strongest_evidence"], {"occasion": 3, "general": 1})
        hyp = themes["Would use a photo reading feature"]
        self.assertEqual(hyp["suggested"]["evidence"], "serious")

    def test_bad_rows_are_reported(self):
        f = self.write("c.csv", "participant,at,theme,evidence,stance\n"
                                "P9,00:01:00,T,occasion,for\n"
                                "P1,00:09:59,T,occasion,for\n"
                                "P1,00:01:13,T,gossip,for\n")
        code, out = run("tally", f, "--transcripts", self.anon())
        self.assertEqual(code, 1)
        self.assertIn("'P9' is not in the transcripts", out)
        self.assertIn("no turn by P1 at 00:09:59", out)
        self.assertIn("'gossip'", out)

    def test_needs_a_total(self):
        f = self.write("c.csv", "participant,theme,evidence,stance\nP1,T,occasion,for\n")
        code, out = run("tally", f)
        self.assertNotEqual(code, 0)
        self.assertIn("--participants", out)


class Confidence(Base):
    def assess(self, data):
        f = self.write("a.json", json.dumps(data))
        return run("confidence", f, "--json", self.path("o.json"))

    def finding(self, fid, **concerns):
        f = {"id": fid, "title": fid}
        for c in check.COMPONENTS:
            f[c] = {"concern": concerns.get(c, "none"), "why": "because"}
        return f

    def test_rule(self):
        cases = [
            ({}, "High"),
            ({"adequacy": "minor"}, "High"),
            ({"adequacy": "minor", "coherence": "minor", "relevance": "minor"}, "Medium"),
            ({"coherence": "moderate"}, "Medium"),
            ({"coherence": "moderate", "evidence": "moderate"}, "Low"),
            ({"evidence": "serious"}, "Low"),
        ]
        for concerns, want in cases:
            level, _ = check.finding_level([concerns.get(c, "none") for c in check.COMPONENTS])
            self.assertEqual(level, want, concerns)

    def test_sample_assessments(self):
        code, out = run("confidence", os.path.join(EX, "sample-assessments.json"), "--json", self.path("o.json"))
        self.assertEqual(code, 0, out)
        with open(self.path("o.json")) as fh:
            res = json.load(fh)
        lv = {x["id"]: x["level"] for k in res for x in res[k]}
        self.assertEqual(lv, {"F1": "High", "F2": "Medium", "F3": "High",
                              "O1": "Medium", "O2": "High", "R1": "Medium", "R2": "High"})

    def test_recommendation_capped_at_medium(self):
        code, out = self.assess({
            "findings": [self.finding("F1")],
            "opportunities": [{"id": "O1", "from": ["F1"]}],
            "recommendations": [{"id": "R1", "from": ["O1"]}],
        })
        self.assertEqual(code, 0, out)
        self.assertIn("capped at Medium", out)

    def test_override_lowers_only_and_needs_a_reason(self):
        code, out = self.assess({"findings": [dict(self.finding("F1", coherence="moderate"), override="High",
                                                   override_why="sure")]})
        self.assertEqual(code, 1)
        self.assertIn("can only lower", out)
        code, out = self.assess({"findings": [dict(self.finding("F1"), override="Low")]})
        self.assertEqual(code, 1)
        self.assertIn("needs override_why", out)
        code, out = self.assess({"findings": [dict(self.finding("F1"), override="Low", override_why="one recording was lost")]})
        self.assertEqual(code, 0, out)
        self.assertIn("lowered to Low by judgement", out)

    def test_missing_why_and_unknown_source(self):
        f = self.finding("F1", adequacy="minor")
        f["adequacy"]["why"] = ""
        code, out = self.assess({"findings": [f], "opportunities": [{"id": "O1", "from": ["F7"]}],
                                 "recommendations": [{"id": "R1", "from": []}]})
        self.assertEqual(code, 1)
        self.assertIn("F1: adequacy has a minor concern and no why", out)
        self.assertIn("O1: 'from' names F7", out)
        self.assertIn("R1: 'from' is empty", out)

    def test_designer_only_recommendation(self):
        code, out = self.assess({"recommendations": [{"id": "R1", "title": "Mine", "designer_only": True}]})
        self.assertEqual(code, 0, out)
        self.assertIn("Not assessed", out)


if __name__ == "__main__":
    unittest.main()
