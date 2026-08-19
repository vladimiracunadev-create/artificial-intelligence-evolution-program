from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.sources import (
    STATUSES,
    TYPES,
    USE_ROLES,
    book_locator,
    doi_is_wellformed,
    extract_items,
    isbn13_is_valid,
    load_registry,
    normalize_url_key,
    normalize_work_key,
    paper_locator,
    registry_keys,
    registry_stats,
    used_keys,
    verify,
)


class LocatorTests(unittest.TestCase):
    def test_isbn13_check_digit(self):
        self.assertTrue(isbn13_is_valid("9780134610993"))  # AIMA, 4.ª ed.
        self.assertTrue(isbn13_is_valid("978-0-262-03561-3"))  # Deep Learning
        self.assertFalse(isbn13_is_valid("9780134610994"))  # dígito de control roto
        self.assertFalse(isbn13_is_valid("0134610997"))  # ISBN-10
        self.assertFalse(isbn13_is_valid(""))
        self.assertFalse(isbn13_is_valid("1230134610993"))  # prefijo inválido

    def test_doi_shape(self):
        self.assertTrue(doi_is_wellformed("10.1093/mind/LIX.236.433"))
        self.assertTrue(doi_is_wellformed("10.48550/arXiv.1706.03762"))
        self.assertFalse(doi_is_wellformed("https://doi.org/10.1093/mind"))
        self.assertFalse(doi_is_wellformed("mind/LIX.236.433"))

    def test_canonical_forms(self):
        self.assertEqual(
            book_locator("9780262035613"), "https://openlibrary.org/isbn/9780262035613"
        )
        self.assertEqual(
            paper_locator("10.1145/3442188.3445922"),
            "https://doi.org/10.1145/3442188.3445922",
        )


class NormalizationTests(unittest.TestCase):
    def test_url_key_is_stable(self):
        variants = [
            "https://www.nist.gov/itl/ai-risk-management-framework",
            "http://nist.gov/itl/ai-risk-management-framework/",
            "https://nist.gov/itl/ai-risk-management-framework?utm=x#seccion",
        ]
        keys = {normalize_url_key(url) for url in variants}
        self.assertEqual(keys, {"nist.gov/itl/ai-risk-management-framework"})

    def test_work_key_is_stable(self):
        self.assertEqual(
            normalize_work_key("  Deep  Learning. "), normalize_work_key("deep learning")
        )


class ExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = extract_items(ROOT)

    def test_every_class_has_references(self):
        classes = {item.class_path for item in self.items}
        self.assertEqual(len(classes), 183)

    def test_every_citation_declares_its_use(self):
        sin_uso = [f"{i.class_path}:{i.line_no}" for i in self.items if not i.declares_use]
        self.assertEqual(sin_uso, [])

    def test_use_roles_cover_every_type(self):
        self.assertEqual(set(USE_ROLES), set(TYPES))


class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = load_registry()
        cls.items = extract_items(ROOT)

    def test_registry_includes_the_papers_catalog_by_reference(self):
        registries = {inc["registry"] for inc in self.registry["includes"]}
        self.assertIn("papers/catalog/papers.json", registries)

    def test_entry_shape(self):
        for entry in self.registry["entries"]:
            self.assertIn(entry["type"], TYPES, entry["id"])
            self.assertIn(entry["status"], STATUSES, entry["id"])
            self.assertTrue(entry["used_in"], entry["id"])
            if entry["status"] == "pendiente":
                self.assertTrue(entry.get("pending_reason"), entry["id"])

    def test_verified_entries_carry_a_resolvable_locator(self):
        for entry in self.registry["entries"]:
            if entry["status"] != "verificada":
                continue
            if entry["type"] == "book":
                self.assertTrue(isbn13_is_valid(entry.get("isbn13", "")), entry["id"])
                self.assertEqual(entry["locator"], book_locator(entry["isbn13"]), entry["id"])
            elif entry["type"] == "paper":
                self.assertTrue(doi_is_wellformed(entry.get("doi", "")), entry["id"])
                self.assertEqual(entry["locator"], paper_locator(entry["doi"]), entry["id"])
            else:
                self.assertTrue(entry["locator"].startswith("https://"), entry["id"])
                self.assertTrue(entry.get("accessed"), entry["id"])

    def test_coverage_is_complete(self):
        url_uses, work_uses = used_keys(self.items)
        covered_urls, covered_works = registry_keys(self.registry)
        self.assertEqual([k for k in url_uses if k not in covered_urls], [])
        self.assertEqual([k for k in work_uses if k not in covered_works], [])
        self.assertEqual(registry_stats(self.registry, self.items)["coverage_pct"], 100.0)

    def test_nothing_invented_without_a_locator(self):
        """Sin localizador resoluble, la entrada es pendiente. No hay término medio."""
        for entry in self.registry["entries"]:
            if entry["status"] == "verificada":
                self.assertTrue(entry.get("locator"), entry["id"])


class VerifierTests(unittest.TestCase):
    def test_repository_passes_the_source_verifier(self):
        result = verify(ROOT)
        self.assertEqual(result["problems"], [])
        self.assertTrue(result["ok"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
