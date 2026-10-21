"""Tests for scripts/to_long.py. Run with:  python3 -m unittest discover tests"""
import contextlib
import csv
import importlib.util
import io
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAMPLES = os.path.join(ROOT, "examples")


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(ROOT, "scripts", filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


to_long = load("to_long", "to_long.py")
analyse = load("analyse", "analyse.py")

WIDE = """Card,P1,P2,P3
Renew a book,Borrowing,Loans,Books
Reserve a book,Borrowing,Loans,Books
Author talk,Events,Events,
"""


class ToLong(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def write(self, name, text):
        path = os.path.join(self.tmp.name, name)
        with open(path, "w", newline="", encoding="utf-8") as fh:
            fh.write(text)
        return path

    def run_main(self, argv):
        err = io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(err):
            code = to_long.main(argv)
        return code, err.getvalue()

    def read(self, path):
        with open(path, newline="", encoding="utf-8") as fh:
            return list(csv.DictReader(fh))

    def test_converts_one_row_per_placement(self):
        src = self.write("wide.csv", WIDE)
        out = os.path.join(self.tmp.name, "long.csv")
        code, _ = self.run_main([src, "--out", out])
        self.assertEqual(code, 0)
        rows = self.read(out)
        self.assertEqual(len(rows), 9)
        self.assertEqual(
            [r for r in rows if r["participant_id"] == "P2"
             and r["card"] == "Renew a book"][0]["category"], "Loans")

    def test_blank_cell_stays_blank_meaning_unsorted(self):
        src = self.write("wide.csv", WIDE)
        out = os.path.join(self.tmp.name, "long.csv")
        self.run_main([src, "--out", out])
        row = [r for r in self.read(out) if r["participant_id"] == "P3"
               and r["card"] == "Author talk"][0]
        self.assertEqual(row["category"], "")

    def test_round_trip_through_the_analysis(self):
        src = self.write("wide.csv", WIDE)
        out = os.path.join(self.tmp.name, "long.csv")
        self.run_main([src, "--out", out])
        outdir = os.path.join(self.tmp.name, "a")
        with contextlib.redirect_stdout(io.StringIO()):
            code = analyse.main([out, "--bootstrap", "0", "--out", outdir])
        self.assertEqual(code, 0)
        with open(os.path.join(outdir, "matrix.csv"), newline="") as fh:
            rows = list(csv.reader(fh))
        cards = rows[0][1:]
        cell = rows[1 + cards.index("Renew a book")][
            1 + cards.index("Reserve a book")]
        self.assertEqual(float(cell), 100.0)

    def test_guide_layout_matches_the_guide_example(self):
        # the worked example, written wide, must give the same matrix
        wide = self.write("guide-wide.csv", (
            "Card,P1,P2,P3,P4,P5\n"
            "Renew a book,Borrowing,Loans,Books,Borrowing,Library services\n"
            "Reserve a book,Borrowing,Loans,Books,Borrowing,Library services\n"
            "Borrow an e-book,Borrowing,Digital,Books,Borrowing,Library services\n"
            "Computer skills class,Events,Digital,What's on,Learning,Events and classes\n"
            "Author talk,Events,Events,What's on,What's on,Events and classes\n"
            "Opening hours,Info,Info,What's on,What's on,Library services\n"))
        out = os.path.join(self.tmp.name, "long.csv")
        self.run_main([wide, "--out", out])
        results = []
        for source in (out, os.path.join(EXAMPLES, "guide-example.csv")):
            d = tempfile.mkdtemp(dir=self.tmp.name)
            with contextlib.redirect_stdout(io.StringIO()):
                analyse.main([source, "--bootstrap", "0", "--out", d])
            with open(os.path.join(d, "matrix.csv")) as fh:
                results.append(fh.read())
        self.assertEqual(results[0], results[1])

    def test_errors(self):
        for text, fragment in (
            ("Card,P1\nA,x\nA,y\n", "appears twice"),
            ("Card,P1,P1\nA,x,y\n", "unique"),
            ("Card\nA\n", "No participant columns"),
            ("Card,P1\n,x\n", "no card name"),
        ):
            src = self.write("bad.csv", text)
            code, err = self.run_main([src, "--out",
                                       os.path.join(self.tmp.name, "o.csv")])
            self.assertEqual(code, 2, text)
            self.assertIn(fragment, err)
        code, err = self.run_main(["/no/such.csv", "--out", "/tmp/o.csv"])
        self.assertEqual(code, 2)
        self.assertIn("File not found", err)

    def test_named_card_column(self):
        src = self.write("wide.csv", "P1,Item,P2\nx,A,y\n")
        out = os.path.join(self.tmp.name, "long.csv")
        code, _ = self.run_main([src, "--out", out, "--card-col", "Item"])
        self.assertEqual(code, 0)
        self.assertEqual({r["card"] for r in self.read(out)}, {"A"})


if __name__ == "__main__":
    unittest.main()
