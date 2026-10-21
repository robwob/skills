"""Tests for scripts/render_report.py. Run with:  python3 -m unittest discover tests"""
import contextlib
import copy
import importlib.util
import io
import json
import os
import re
import struct
import tempfile
import unittest
import zlib
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAMPLES = os.path.join(ROOT, "examples")


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(ROOT, "scripts", filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


render_report = load("render_report", "render_report.py")
analyse = load("analyse", "analyse.py")

VOID = {"meta", "br", "img", "hr", "input", "link", "path", "line"}


class Balanced(HTMLParser):
    """Flags unclosed or stray tags, so a template slip fails a test."""

    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append("unexpected </%s> after %s" % (
                tag, self.stack[-3:]))
        else:
            self.stack.pop()


def balanced(page):
    p = Balanced()
    p.feed(page)
    return p.errors, p.stack


def run_analyse(argv):
    with contextlib.redirect_stdout(io.StringIO()):
        return analyse.main(argv)


def png_bytes():
    """A valid 2x2 PNG built by hand, so no image library is needed."""
    def chunk(kind, data):
        body = kind + data
        return (struct.pack(">I", len(data)) + body
                + struct.pack(">I", zlib.crc32(body) & 0xffffffff))
    raw = b"".join(b"\x00" + b"\x20\x40\x80" * 2 for _ in range(2))
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", 2, 2, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


class DataRoute(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        run_analyse([os.path.join(EXAMPLES, "sample-open-sort.csv"),
                     "--merge-file", os.path.join(EXAMPLES, "sample-merge.csv"),
                     "--exclude", "P19", "--bootstrap", "100",
                     "--out", cls.tmp.name])
        with open(os.path.join(cls.tmp.name, "results.json")) as fh:
            cls.results = json.load(fh)
        with open(os.path.join(EXAMPLES, "sample-findings.json")) as fh:
            cls.findings = json.load(fh)
        cls.page = render_report.render(cls.findings, cls.results)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_both_layers_and_key_sections(self):
        for needle in ("Layer 1", "Layer 2", 'id="summary"',
                       'id="structure"', 'id="contested"',
                       'id="recommendations"', 'id="limits"',
                       'id="settings"', 'id="matrix"', 'id="dendrogram"',
                       'id="stability"', "Confidence: High",
                       "Basis: computed from the data"):
            self.assertIn(needle, self.page)

    def test_html_is_balanced(self):
        self.assertEqual(balanced(self.page), ([], []))

    def test_self_contained(self):
        self.assertNotRegex(self.page, r"(src|href)=\"https?://")
        self.assertNotIn("<script", self.page)

    def test_heatmap_prints_every_number(self):
        n = len(self.results["matrix"]["values_pct"])
        block = self.page.split('id="matrix"')[1].split("</table>")[0]
        self.assertEqual(len(re.findall(r"<td[^>]*>(\d+)</td>", block)),
                         n * n)

    def test_dendrogram_has_every_card_and_a_text_version(self):
        svg = re.search(r'<svg class="dendro".*?</svg>', self.page,
                        re.S).group(0)
        for card in self.results["dendrogram"]["cards"]:
            self.assertIn(card.replace("'", "&#x27;"), svg)
        self.assertIn("cut 50%", svg)
        self.assertIn("Text version of the tree", self.page)

    def test_contested_card_comes_from_the_data_when_not_supplied(self):
        findings = copy.deepcopy(self.findings)
        del findings["proposed_structure"]
        findings["findings"] = []
        page = render_report.render(findings, self.results)
        self.assertIn("Book a study room", page.split('id="contested"')[1])

    def test_no_em_or_en_dashes_in_output(self):
        findings = copy.deepcopy(self.findings)
        findings["summary"][0] += " It worked \u2014 mostly. Ages 10\u201315."
        page = render_report.render(findings, self.results)
        self.assertNotIn("\u2014", page)
        self.assertNotIn("\u2013", page)
        self.assertIn("Ages 10 to 15", page)

    def test_html_in_text_is_escaped(self):
        findings = copy.deepcopy(self.findings)
        findings["summary"][0] = "<script>alert(1)</script>"
        page = render_report.render(findings, self.results)
        self.assertNotIn("<script>alert", page)
        self.assertIn("&lt;script&gt;", page)

    def test_default_limits_present_and_guide_is_named(self):
        self.assertIn("not a validated structure", self.page)
        self.assertIn("how-to-analyse-card-sort-results.md", self.page)


class Validation(unittest.TestCase):
    def base(self):
        with open(os.path.join(EXAMPLES, "sample-findings.json")) as fh:
            return json.load(fh)

    def test_bad_confidence_is_rejected(self):
        f = self.base()
        f["findings"][0]["confidence"] = "Very high"
        with self.assertRaises(render_report.ReportError):
            render_report.render(f, None)

    def test_bad_basis_is_rejected(self):
        f = self.base()
        f["recommendations"][0]["basis"] = "vibes"
        with self.assertRaises(render_report.ReportError):
            render_report.render(f, None)

    def test_missing_required_fields(self):
        f = self.base()
        del f["summary"]
        with self.assertRaises(render_report.ReportError):
            render_report.render(f, None)
        f = self.base()
        del f["study"]["route"]
        with self.assertRaises(render_report.ReportError):
            render_report.render(f, None)

    def test_cli_reports_errors_without_a_traceback(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code = render_report.main(["--findings", "/no/such.json",
                                       "--out", "/tmp/x.html"])
        self.assertEqual(code, 2)
        self.assertIn("Error", err.getvalue())


class ImageRoute(unittest.TestCase):
    def findings(self, shot_path):
        return {
            "title": "Image route example",
            "study": {"tool": "Playbook UX", "sort_type": "open",
                      "participants": 12, "cards": 3, "route": "image"},
            "summary": ["Two cards group together."],
            "transcribed": {
                "legend": "darker means more participants grouped the pair",
                "matrix": {"cards": ["A", "B", "C"],
                           "values_pct": [[100, 70, 10], [70, 100, 20],
                                          [10, 20, 100]]},
                "merges": [{"members": ["A", "B"], "value": "70%",
                            "meaning": "share who grouped them together"}],
            },
            "screenshots": [{"path": shot_path,
                             "alt": "Similarity matrix screenshot"}],
        }

    def temp(self, suffix, data):
        fh = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        fh.write(data)
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        return fh.name

    def test_screenshot_is_embedded_and_marked_lower_confidence(self):
        path = self.temp(".png", png_bytes())
        page = render_report.render(self.findings(path), None)
        self.assertIn("data:image/png;base64,", page)
        self.assertIn('alt="Similarity matrix screenshot"', page)
        self.assertIn("lower confidence", page)
        self.assertIn("transcription error", page)
        self.assertEqual(balanced(page), ([], []))

    def test_shading_estimates_are_marked_with_a_tilde(self):
        path = self.temp(".png", png_bytes())
        f = self.findings(path)
        f["transcribed"]["matrix"]["approximate"] = True
        page = render_report.render(f, None)
        self.assertIn(">~70<", page)
        self.assertIn("estimated from shading", page)
        f["transcribed"]["matrix"]["approximate"] = False
        page = render_report.render(f, None)
        self.assertNotIn(">~70<", page)
        self.assertIn(">70<", page)

    def test_missing_or_wrong_type_screenshot(self):
        with self.assertRaises(render_report.ReportError):
            render_report.render(self.findings("/no/such.png"), None)
        with self.assertRaises(render_report.ReportError):
            render_report.render(self.findings(self.temp(".bmp", b"x")),
                                 None)

    def test_oversize_screenshot_is_rejected(self):
        path = self.temp(".png", b"0" * (render_report.MAX_IMAGE_BYTES + 1))
        with self.assertRaises(render_report.ReportError):
            render_report.render(self.findings(path), None)


class ClosedRoute(unittest.TestCase):
    def test_closed_results_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_analyse([os.path.join(EXAMPLES, "sample-closed-sort.csv"),
                         "--sort-type", "closed", "--bootstrap", "100",
                         "--out", tmp])
            with open(os.path.join(tmp, "results.json")) as fh:
                results = json.load(fh)
        findings = {
            "title": "Closed sort example",
            "study": {"tool": "Generic CSV", "sort_type": "closed",
                      "participants": 30, "cards": 12, "route": "data"},
            "summary": ["Most cards have a clear home."],
        }
        page = render_report.render(findings, results)
        self.assertIn("Runner-up", page)
        self.assertIn("Book a study room", page.split('id="contested"')[1])
        self.assertNotIn('id="matrix"', page)
        self.assertNotIn('id="dendrogram"', page)
        self.assertEqual(balanced(page), ([], []))


if __name__ == "__main__":
    unittest.main()
