"""Tests for scripts/check.py. Run from the skill folder with:  python3 -m unittest discover tests"""
import contextlib
import csv
import importlib.util
import io
import json
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SAMPLE = os.path.join(ROOT, "examples", "sample-results.csv")

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
        code, _ = run("pseudonymise", SAMPLE, "--participant", "Participant",
                      "--out", self.path("anon.csv"), "--key", self.path("key.csv"))
        self.assertEqual(code, 0)
        return self.path("anon.csv")


class Ratings(Base):
    def test_sample_task_one(self):
        code, out = run("ratings", self.anon(), "--participant", "Participant",
                        "--question", "3", "--scale", "1-7", "--json", self.path("r.json"))
        self.assertEqual(code, 0, out)
        with open(self.path("r.json")) as fh:
            q = json.load(fh)["questions"][0]
        self.assertEqual(q["n"], 6)
        self.assertEqual(q["distribution"]["7"], 3)
        self.assertEqual(q["median"], 6.5)
        self.assertEqual(q["mean"], 6.33)

    def test_blank_and_out_of_scale_are_not_counted(self):
        f = self.write("r.csv", "id,Q\nP1,5\nP2,\nP3,9\nP4,3.5\nP5,1\n")
        code, out = run("ratings", f, "--participant", "id", "--question", "Q",
                        "--scale", "1-5", "--json", self.path("r.json"))
        self.assertEqual(code, 0, out)
        with open(self.path("r.json")) as fh:
            q = json.load(fh)["questions"][0]
        self.assertEqual(q["n"], 2)
        self.assertEqual(q["blank"], ["P2"])
        self.assertEqual([p for p, _ in q["invalid"]], ["P3", "P4"])
        self.assertEqual(q["mean"], 3.0)

    def test_long_layout(self):
        f = self.write("l.csv", "who,question,answer\nP1,Ease,4\nP2,Ease,2\nP1,Why,slow\n")
        code, out = run("ratings", f, "--participant", "who", "--layout", "long",
                        "--question-col", "question", "--answer-col", "answer",
                        "--question", "Ease", "--scale", "1-5")
        self.assertEqual(code, 0, out)
        self.assertIn("Mean: 3.0 / 5", out)

    def test_unknown_question_lists_the_real_ones(self):
        code, out = run("ratings", SAMPLE, "--participant", "Participant",
                        "--question", "Nope", "--scale", "1-7")
        self.assertNotEqual(code, 0)
        self.assertIn("Device", out)

    def test_xlsx_is_refused_with_instructions(self):
        code, out = run("columns", "results.xlsx")
        self.assertNotEqual(code, 0)
        self.assertIn("CSV", out)


class Completion(Base):
    def test_matches_sauros_worked_example(self):
        # MeasuringU, 10 Things To Know About Completion Rates: 1 of 5 gives about 2% to 64%.
        lo, hi = check.adjusted_wald(1, 5)
        self.assertAlmostEqual(lo, 0.02, delta=0.01)
        self.assertAlmostEqual(hi, 0.64, delta=0.01)

    def test_lewis_and_sauro_seven_of_ten(self):
        lo, hi = check.adjusted_wald(7, 10)
        self.assertAlmostEqual(lo, 0.392, delta=0.002)
        self.assertAlmostEqual(hi, 0.897, delta=0.002)

    def test_all_succeeded_is_not_one_hundred_percent(self):
        code, out = run("completion", "6", "6")
        self.assertEqual(code, 0)
        self.assertIn("56% to 100%", out)


class Pseudonymise(Base):
    def test_names_replaced_in_answers_and_key_written(self):
        f = self.write("p.csv", "Name,Notes\nAnna Lee,Anna Lee said hi\nAnn Ho,Ann was quiet\n")
        code, out = run("pseudonymise", f, "--participant", "Name",
                        "--out", self.path("o.csv"), "--key", self.path("k.csv"))
        self.assertEqual(code, 0, out)
        with open(self.path("o.csv"), newline="") as fh:
            rows = list(csv.DictReader(fh))
        self.assertEqual(rows[0]["Name"], "P1")
        self.assertEqual(rows[0]["Notes"], "P1 said hi")
        # First name alone is flagged, not silently replaced.
        self.assertIn("'Ann'", out)
        with open(self.path("k.csv"), newline="") as fh:
            self.assertEqual(list(csv.reader(fh))[1], ["P1", "Anna Lee"])


class Quotes(Base):
    def check(self, quotes):
        qf = self.write("q.json", json.dumps(quotes))
        return run("quotes", self.anon(), "--participant", "Participant", "--quotes", qf)

    def test_verbatim_with_typographic_quotes_and_ellipsis(self):
        code, out = self.check([
            {"quote": "I gave up and said I’d ring them.", "participant": "P4"},
            {"quote": "I looked for an edit button ... changed it there", "participant": "P1"},
        ])
        self.assertEqual(code, 0, out)
        self.assertIn("2 of 2", out)

    def test_paraphrase_fails(self):
        code, out = self.check([{"quote": "The arrows are too small", "participant": "P5"}])
        self.assertEqual(code, 1)
        self.assertIn("NOT FOUND", out)

    def test_wrong_participant_is_named(self):
        code, out = self.check([{"quote": "I thought I'd have to start over", "participant": "P1"}])
        self.assertEqual(code, 1)
        self.assertIn("found under P2", out)

    def test_ellipsis_pieces_must_be_in_order(self):
        code, out = self.check([{"quote": "changed it there ... I looked for an edit button",
                                 "participant": "P1"}])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
