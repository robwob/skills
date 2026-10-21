"""Tests for scripts/analyse.py. Run with:  python3 -m unittest discover tests

Figures in the 6-card example were worked out by hand (see the guide) and are
asserted here, so a change to the maths that breaks the guide fails a test.
"""
import contextlib
import csv
import importlib.util
import io
import itertools
import json
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRIPT = os.path.join(ROOT, "scripts", "analyse.py")
EXAMPLES = os.path.join(ROOT, "examples")
GUIDE_EXAMPLE = os.path.join(EXAMPLES, "guide-example.csv")
SAMPLE = os.path.join(EXAMPLES, "sample-open-sort.csv")
MERGE = os.path.join(EXAMPLES, "sample-merge.csv")

spec = importlib.util.spec_from_file_location("analyse", SCRIPT)
analyse = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analyse)


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = analyse.main(argv)
    return code, out.getvalue(), err.getvalue()


def read_matrix(path):
    with open(path, newline="") as fh:
        rows = list(csv.reader(fh))
    cards = rows[0][1:]
    return {
        (rows[i + 1][0], cards[j]): float(rows[i + 1][j + 1])
        for i in range(len(cards)) for j in range(len(cards))
    }


def read_placements(path):
    by_p = {}
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            by_p.setdefault(r["participant_id"], {})[r["card"]] = \
                " ".join(r["category"].split()).casefold()
    return by_p


def brute_force_similarity(by_p, cards):
    """Share of participants who grouped each pair, computed the slow way."""
    sim = {}
    for a, b in itertools.combinations(cards, 2):
        together = sum(
            1 for p in by_p.values()
            if p.get(a) and p.get(a) == p.get(b))
        sim[(a, b)] = together / len(by_p)
    return sim


def upgma_heights(sim, cards):
    """Average linkage straight from its definition, independent of scipy."""
    def d(x, y):
        key = (x, y) if (x, y) in sim else (y, x)
        return 1 - sim[key]
    clusters = [[c] for c in cards]
    heights = []
    while len(clusters) > 1:
        best = None
        for i, j in itertools.combinations(range(len(clusters)), 2):
            pairs = [d(x, y) for x in clusters[i] for y in clusters[j]]
            h = sum(pairs) / len(pairs)
            if best is None or h < best[0] - 1e-12:
                best = (h, i, j)
        h, i, j = best
        heights.append(h)
        merged = clusters[i] + clusters[j]
        clusters = [c for k, c in enumerate(clusters) if k not in (i, j)]
        clusters.append(merged)
    return sorted(heights)


class GuideExample(unittest.TestCase):
    """The 6-card, 5-participant example the guide works through by hand."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        code, cls.text, _ = run([GUIDE_EXAMPLE, "--out", cls.tmp.name,
                                 "--bootstrap", "0"])
        assert code == 0
        cls.matrix = read_matrix(os.path.join(cls.tmp.name, "matrix.csv"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def pair(self, a, b):
        return self.matrix[(a, b)]

    def test_hand_computed_cells(self):
        expected = {
            ("Renew a book", "Reserve a book"): 100,
            ("Renew a book", "Borrow an e-book"): 80,
            ("Reserve a book", "Borrow an e-book"): 80,
            ("Computer skills class", "Author talk"): 60,
            ("Author talk", "Opening hours"): 40,
            ("Renew a book", "Opening hours"): 20,
            ("Reserve a book", "Opening hours"): 20,
            ("Borrow an e-book", "Opening hours"): 20,
            ("Borrow an e-book", "Computer skills class"): 20,
            ("Computer skills class", "Opening hours"): 20,
            ("Renew a book", "Computer skills class"): 0,
            ("Renew a book", "Author talk"): 0,
            ("Reserve a book", "Computer skills class"): 0,
            ("Reserve a book", "Author talk"): 0,
            ("Borrow an e-book", "Author talk"): 0,
        }
        for (a, b), pct in expected.items():
            self.assertAlmostEqual(self.pair(a, b), pct, places=1,
                                   msg="%s / %s" % (a, b))
            self.assertAlmostEqual(self.pair(b, a), pct, places=1)

    def test_hand_computed_merges(self):
        path = os.path.join(self.tmp.name, "dendrogram.csv")
        with open(path, newline="") as fh:
            sims = [float(r["similarity_pct"]) for r in csv.DictReader(fh)]
        # R+V 100, +E 80, C+T 60, H joins {C,T} at 30, final join at 8.9
        self.assertEqual([round(s, 1) for s in sims],
                         [100.0, 80.0, 60.0, 30.0, 8.9])

    def test_hand_computed_groups_at_50(self):
        for line in ("Renew a book, Reserve a book, Borrow an e-book",
                     "Computer skills class, Author talk",
                     "Opening hours"):
            self.assertIn("  - " + line, self.text)


GUIDE_MERGE = os.path.join(EXAMPLES, "guide-example-merge.csv")


class GuideFigures(unittest.TestCase):
    """Figures printed in guide/how-to-analyse-card-sort-results.md."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        run([GUIDE_EXAMPLE, "--merge-file", GUIDE_MERGE, "--out",
             cls.tmp.name, "--bootstrap", "0"])
        with open(os.path.join(cls.tmp.name, "results.json")) as fh:
            cls.res = json.load(fh)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_cards_view_after_merging(self):
        cards = {c["card"]: c for c in self.res["cards"]}
        renew = cards["Renew a book"]
        self.assertEqual((renew["top_category"], renew["top_count"],
                          renew["categories"]), ("Borrowing", 4, 2))
        self.assertEqual((round(100 * renew["ci_low"]),
                          round(100 * renew["ci_high"])), (38, 96))
        ebook = cards["Borrow an e-book"]
        self.assertEqual(ebook["top_count"], 3)
        self.assertEqual((round(100 * ebook["ci_low"]),
                          round(100 * ebook["ci_high"])), (23, 88))
        hours = cards["Opening hours"]
        self.assertEqual(hours["top_count"], 2)
        self.assertEqual(hours["categories"], 3)
        self.assertEqual(cards["Computer skills class"]["categories"], 4)

    def test_categories_agreement(self):
        cats = {c["category"]: c for c in self.res["categories"]}
        self.assertEqual(cats["Borrowing"]["participants"], 4)
        self.assertEqual(cats["Borrowing"]["unique_cards"], 3)
        self.assertAlmostEqual(cats["Borrowing"]["agreement"], 11 / 12)
        self.assertAlmostEqual(cats["What's on"]["agreement"], 5 / 6)
        self.assertAlmostEqual(cats["Events and classes"]["agreement"], 5 / 6)
        self.assertEqual(cats["Library services"]["unique_cards"], 4)

    def test_alignment_scores(self):
        got = {p["participant"]: round(p["alignment"], 2)
               for p in self.res["participants"]}
        self.assertEqual(got, {"P1": 0.85, "P2": 0.15, "P3": 0.67,
                               "P4": 0.69, "P5": 0.45})

    def test_cut_sweep(self):
        got = {round(r["cut"], 1): (r["groups"], r["singletons"])
               for r in self.res["sweep"]}
        self.assertEqual(got, {0.3: (2, 0), 0.4: (3, 1), 0.5: (3, 1),
                               0.6: (3, 1), 0.7: (4, 3)})

    def test_contested_card_is_opening_hours(self):
        flagged = [c["card"] for c in self.res["contested"] if c["reasons"]]
        self.assertEqual(flagged, ["Opening hours"])

    def test_matrix_names_drop_out_of_merging(self):
        # Standardising names must not change a cell (design decision)
        order = self.res["matrix"]["order"]
        vals = self.res["matrix"]["values_pct"]
        cell = vals[order.index("Renew a book")][order.index("Borrow an e-book")]
        self.assertEqual(cell, 80.0)

    def test_single_linkage_attaches_opening_hours_at_40(self):
        with tempfile.TemporaryDirectory() as tmp:
            run([GUIDE_EXAMPLE, "--linkage", "single", "--cut", "0.4",
                 "--bootstrap", "0", "--out", tmp])
            with open(os.path.join(tmp, "results.json")) as fh:
                groups = [frozenset(g) for g in json.load(fh)["groups"]]
        self.assertIn(frozenset(["Computer skills class", "Author talk",
                                 "Opening hours"]), groups)
        with tempfile.TemporaryDirectory() as tmp:
            run([GUIDE_EXAMPLE, "--cut", "0.4", "--bootstrap", "0",
                 "--out", tmp])
            with open(os.path.join(tmp, "results.json")) as fh:
                groups = [frozenset(g) for g in json.load(fh)["groups"]]
        self.assertIn(frozenset(["Opening hours"]), groups)

    def test_unsorted_exercise(self):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
        with open(GUIDE_EXAMPLE) as src:
            for line in src:
                fh.write("P5,Opening hours,,\n"
                         if line.startswith("P5,Opening hours,") else line)
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        code, text, _ = run([fh.name, "--explain", "Author talk",
                             "Opening hours"])
        self.assertIn("singleton mode:  2 / 5 = 40%", text)
        self.assertIn("pairwise mode:   2 / 4 = 50%", text)

    def test_spreadsheet_wilson_formula(self):
        # the formula printed in the guide, transcribed literally
        def lower(K, N):
            return ((K / N) + 1.96 ** 2 / (2 * N) - 1.96 * (
                (K / N) * (1 - K / N) / N + 1.96 ** 2 / (4 * N ** 2)) ** .5
            ) / (1 + 1.96 ** 2 / N)
        self.assertAlmostEqual(100 * lower(4, 5), 37.6, places=1)


class AgainstIndependentMaths(unittest.TestCase):
    def test_matrix_matches_brute_force(self):
        by_p = read_placements(SAMPLE)
        cards = sorted({c for p in by_p.values() for c in p})
        expected = brute_force_similarity(by_p, cards)
        with tempfile.TemporaryDirectory() as tmp:
            run([SAMPLE, "--out", tmp, "--bootstrap", "0"])
            got = read_matrix(os.path.join(tmp, "matrix.csv"))
        for (a, b), s in expected.items():
            self.assertAlmostEqual(got[(a, b)], 100 * s, places=1)

    def test_dendrogram_heights_match_textbook_upgma(self):
        by_p = read_placements(SAMPLE)
        cards = sorted({c for p in by_p.values() for c in p})
        expected = upgma_heights(brute_force_similarity(by_p, cards), cards)
        with tempfile.TemporaryDirectory() as tmp:
            run([SAMPLE, "--out", tmp, "--bootstrap", "0"])
            with open(os.path.join(tmp, "dendrogram.csv"),
                      newline="") as fh:
                got = sorted(1 - float(r["similarity_pct"]) / 100
                             for r in csv.DictReader(fh))
        self.assertEqual(len(expected), len(got))
        for e, g in zip(expected, got):
            # the CSV rounds similarity to 0.1 of a percentage point
            self.assertAlmostEqual(e, g, delta=0.00051)

    def test_wilson_interval(self):
        lo, hi = analyse.wilson(32, 70)
        self.assertAlmostEqual(lo, 0.346, places=2)
        self.assertAlmostEqual(hi, 0.573, places=2)
        lo, hi = analyse.wilson(0, 10)
        self.assertEqual(lo, 0.0)
        self.assertTrue(0 < hi < 0.35)

    def test_group_guarantee_by_linkage(self):
        by_p = read_placements(SAMPLE)
        cards = sorted({c for p in by_p.values() for c in p})
        sim = brute_force_similarity(by_p, cards)

        def s(a, b):
            return sim[(a, b)] if (a, b) in sim else sim[(b, a)]
        for linkage, check in (("average", "mean"), ("complete", "min")):
            with tempfile.TemporaryDirectory() as tmp:
                run([SAMPLE, "--out", tmp, "--bootstrap", "0",
                     "--linkage", linkage, "--cut", "0.5"])
                with open(os.path.join(tmp, "results.json")) as fh:
                    groups = json.load(fh)["groups"]
            for g in groups:
                pairs = [s(a, b) for a, b in itertools.combinations(g, 2)]
                if not pairs:
                    continue
                value = (sum(pairs) / len(pairs) if check == "mean"
                         else min(pairs))
                self.assertGreaterEqual(value, 0.5 - 1e-9,
                                        "%s %s" % (linkage, g))


class PlantedStructure(unittest.TestCase):
    def test_recovers_planted_groups_and_flags_ambiguous_card(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, text, _ = run([SAMPLE, "--out", tmp, "--bootstrap", "200",
                                 "--merge-file", MERGE])
            self.assertEqual(code, 0)
            with open(os.path.join(tmp, "results.json")) as fh:
                res = json.load(fh)
        groups = [frozenset(g) for g in res["groups"]]
        self.assertIn(frozenset(["Renew a book", "Reserve a book",
                                 "Borrow an e-book", "Return a book"]),
                      groups)
        self.assertIn(frozenset(["Children's story time",
                                 "Computer skills class", "Author talk",
                                 "Homework club"]), groups)
        self.assertIn(frozenset(["Print and copy", "Join the library",
                                 "Opening hours"]), groups)
        flagged = [r["card"] for r in res["contested"] if r["reasons"]]
        self.assertIn("Book a study room", flagged)

    def test_careless_sorter_is_flagged_not_dropped(self):
        code, text, _ = run([SAMPLE, "--bootstrap", "0"])
        self.assertIn("20 participants", text)
        line = [l for l in text.splitlines() if l.startswith("P19")][0]
        self.assertIn("everything in one group", line)

    def test_matrix_does_not_depend_on_standardising_names(self):
        with tempfile.TemporaryDirectory() as a, \
                tempfile.TemporaryDirectory() as b:
            run([SAMPLE, "--out", a, "--bootstrap", "0"])
            run([SAMPLE, "--out", b, "--bootstrap", "0",
                 "--merge-file", MERGE])
            self.assertEqual(read_matrix(os.path.join(a, "matrix.csv")),
                             read_matrix(os.path.join(b, "matrix.csv")))

    def test_unused_merge_entry_is_reported(self):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
        fh.write("raw,standard\nBorowing,Borrowing\nLoans,Borrowing\n")
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        code, text, _ = run([SAMPLE, "--merge-file", fh.name,
                             "--bootstrap", "0"])
        self.assertIn("'borowing'", text)
        self.assertNotIn("'loans'", text)

    def test_same_seed_same_answer(self):
        one = run([SAMPLE, "--bootstrap", "100", "--seed", "3"])[1]
        two = run([SAMPLE, "--bootstrap", "100", "--seed", "3"])[1]
        self.assertEqual(one, two)


class UnsortedHandling(unittest.TestCase):
    def write(self, rows):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                         newline="")
        w = csv.writer(fh)
        w.writerow(["participant_id", "card", "category"])
        w.writerows(rows)
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        return fh.name

    def test_singleton_and_pairwise(self):
        # X and Y together for A and B. C leaves X unsorted.
        path = self.write([
            ("A", "X", "g"), ("A", "Y", "g"), ("A", "Z", "h"),
            ("B", "X", "g"), ("B", "Y", "g"), ("B", "Z", "h"),
            ("C", "X", ""), ("C", "Y", "g"), ("C", "Z", "h"),
        ])
        for mode, expected in (("singleton", 66.7), ("pairwise", 100.0)):
            with tempfile.TemporaryDirectory() as tmp:
                run([path, "--unsorted", mode, "--out", tmp,
                     "--bootstrap", "0"])
                m = read_matrix(os.path.join(tmp, "matrix.csv"))
            self.assertAlmostEqual(m[("X", "Y")], expected, places=1,
                                   msg=mode)

    def test_unsorted_is_never_a_real_group(self):
        # Two participants each leave different cards unsorted: unsorted
        # cards must not look similar to each other.
        path = self.write([
            ("A", "X", ""), ("A", "Y", ""), ("A", "Z", "g"),
            ("B", "X", "g"), ("B", "Y", "h"), ("B", "Z", "g"),
        ])
        with tempfile.TemporaryDirectory() as tmp:
            run([path, "--out", tmp, "--bootstrap", "0"])
            m = read_matrix(os.path.join(tmp, "matrix.csv"))
        self.assertEqual(m[("X", "Y")], 0.0)

    def test_unsorted_label_option(self):
        path = self.write([
            ("A", "X", "Unsorted"), ("A", "Y", "g"), ("A", "Z", "g"),
            ("B", "X", "Unsorted"), ("B", "Y", "g"), ("B", "Z", "g"),
        ])
        code, text, _ = run([path, "--bootstrap", "0"])
        self.assertIn("--unsorted-label", text)
        with tempfile.TemporaryDirectory() as tmp:
            run([path, "--unsorted-label", "Unsorted", "--out", tmp,
                 "--bootstrap", "0"])
            m = read_matrix(os.path.join(tmp, "matrix.csv"))
        self.assertEqual(m[("X", "Y")], 0.0)


class Errors(unittest.TestCase):
    def test_unknown_columns_list_what_is_there(self):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
        fh.write("Respondent,Item,Group\nr1,a,x\n")
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        code, _, err = run([fh.name])
        self.assertEqual(code, 2)
        self.assertIn("Respondent, Item, Group", err)
        self.assertIn("--col-participant", err)
        code, _, err = run([fh.name, "--col-participant", "Respondent",
                            "--col-card", "Item", "--col-category", "Group",
                            "--bootstrap", "0"])
        self.assertIn("At least two cards", err)

    def test_duplicate_card_is_rejected(self):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False)
        fh.write("participant_id,card,category\n"
                 "p1,a,x\np1,a,y\np1,b,x\n")
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        code, _, err = run([fh.name])
        self.assertEqual(code, 2)
        self.assertIn("more than once", err)

    def test_missing_file(self):
        code, _, err = run(["/no/such/file.csv"])
        self.assertEqual(code, 2)
        self.assertIn("File not found", err)

    def test_exclude_unknown_participant(self):
        code, _, err = run([GUIDE_EXAMPLE, "--exclude", "P99"])
        self.assertEqual(code, 2)
        self.assertIn("P99", err)

    def test_exclude_removes_participant(self):
        code, text, _ = run([SAMPLE, "--exclude", "P19,P20",
                             "--bootstrap", "0"])
        self.assertIn("18 participants", text)


CLOSED = os.path.join(EXAMPLES, "sample-closed-sort.csv")


class ClosedSort(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.code, cls.text, _ = run([CLOSED, "--sort-type", "closed",
                                     "--out", cls.tmp.name,
                                     "--bootstrap", "200"])
        with open(os.path.join(cls.tmp.name, "results.json")) as fh:
            cls.res = json.load(fh)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_runs_and_skips_similarity(self):
        self.assertEqual(self.code, 0)
        self.assertNotIn("SIMILARITY MATRIX", self.text)
        self.assertFalse(os.path.exists(
            os.path.join(self.tmp.name, "matrix.csv")))

    def test_counts_match_brute_force(self):
        by_p = {}
        with open(CLOSED, newline="") as fh:
            for r in csv.DictReader(fh):
                by_p.setdefault(r["card"], []).append(r["category"])
        for card in self.res["cards"]:
            placed = [c for c in by_p[card["card"]] if c]
            self.assertEqual(card["sorted_by"], len(placed))
            top = max(set(placed), key=placed.count)
            self.assertEqual(card["top_count"], placed.count(top))

    def test_interval_overlap_flags_the_split_cards(self):
        flagged = {c["card"] for c in self.res["contested"] if c["reasons"]}
        self.assertIn("Book a study room", flagged)
        self.assertIn("Join the library", flagged)
        self.assertNotIn("Renew a book", flagged)

    def test_careless_sorter_flagged(self):
        line = [l for l in self.text.splitlines() if l.startswith("P29")][0]
        self.assertIn("everything in one group", line)

    def test_explain_not_available(self):
        code, _, err = run([CLOSED, "--sort-type", "closed",
                            "--explain", "Renew a book", "Author talk"])
        self.assertEqual(code, 2)
        self.assertIn("closed", err)


class Hybrid(unittest.TestCase):
    def test_preset_column_marks_origin(self):
        fh = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                         newline="")
        fh.write("participant_id,card,category,category_preset\n"
                 "p1,a,Fruit,true\np1,b,Fruit,true\np1,c,Mine,false\n"
                 "p2,a,Fruit,true\np2,b,Other,false\np2,c,Other,false\n"
                 "p3,a,Fruit,true\np3,b,Fruit,true\np3,c,Mine,false\n")
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        code, text, _ = run([fh.name, "--sort-type", "hybrid",
                             "--bootstrap", "0"])
        self.assertEqual(code, 0)
        self.assertIn("hybrid sort", text)
        self.assertIn("'Fruit'", text)
        line = [l for l in text.splitlines() if l.startswith("Fruit")][0]
        self.assertIn("preset", line)
        line = [l for l in text.splitlines() if l.startswith("Mine")][0]
        self.assertIn("participant", line)


class Explain(unittest.TestCase):
    def test_explain_shows_the_arithmetic(self):
        code, text, _ = run([GUIDE_EXAMPLE, "--explain", "renew a book",
                             "Opening hours"])
        self.assertEqual(code, 0)
        self.assertIn("Grouped together by 1 of 5 participants.", text)
        self.assertIn("1 / 5 = 20%", text)

    def test_explain_suggests_close_card_names(self):
        code, _, err = run([GUIDE_EXAMPLE, "--explain", "Renew book",
                            "Opening hours"])
        self.assertEqual(code, 2)
        self.assertIn("Did you mean", err)


class ListCategories(unittest.TestCase):
    def test_lists_names_with_counts(self):
        code, text, _ = run([SAMPLE, "--list-categories"])
        self.assertEqual(code, 0)
        self.assertIn("Stuff", text)


if __name__ == "__main__":
    unittest.main()
