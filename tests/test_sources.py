from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.sources import (
    CLASS_BEGIN,
    CLASS_END,
    STATUSES,
    TYPES,
    USE_ROLES,
    class_bibliography,
    class_block,
    class_files,
    load_support_map,
    part_of,
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


class SupportBibliographyTests(unittest.TestCase):
    """Además del paper, el libro: cada clase declara con qué se estudia."""

    @classmethod
    def setUpClass(cls):
        cls.registry = load_registry()
        cls.support = load_support_map(ROOT)
        cls.items = extract_items(ROOT)
        cls.biblio = class_bibliography(cls.registry, cls.support, cls.items)

    def test_every_part_declares_a_reference_work(self):
        partes = {part_of(p.relative_to(ROOT).as_posix()) for p in class_files(ROOT)}
        self.assertEqual(partes - set(self.support["parts"]), set())

    def test_reference_works_exist_and_carry_a_valid_isbn(self):
        por_id = {e["id"]: e for e in self.registry["entries"]}
        for parte, manuales in self.support["parts"].items():
            for manual in manuales:
                with self.subTest(parte=parte, obra=manual["id"]):
                    entry = por_id.get(manual["id"])
                    self.assertIsNotNone(entry)
                    self.assertEqual(entry["type"], "book")
                    self.assertTrue(isbn13_is_valid(entry.get("isbn13", "")))
                    self.assertTrue(manual.get("scope"))
                    self.assertTrue(manual.get("why"))

    def test_every_class_has_at_least_one_supporting_work(self):
        sin_obra = [path for path, datos in self.biblio.items() if not datos["obras"]]
        self.assertEqual(sin_obra, [])

    def test_the_block_in_each_class_matches_the_registry(self):
        for path in class_files(ROOT):
            rel = path.relative_to(ROOT).as_posix()
            with self.subTest(clase=rel):
                texto = path.read_text(encoding='utf-8')
                self.assertIn(CLASS_BEGIN, texto)
                corte = texto.index(CLASS_END) + len(CLASS_END)
                bloque = texto[texto.index(CLASS_BEGIN):corte]
                esperado = class_block(self.biblio[rel])
                self.assertEqual(bloque.splitlines(), esperado.splitlines())

    def test_the_block_never_writes_an_isbn_by_hand(self):
        """El ISBN que se muestra sale del registro, no del texto de la clase."""
        por_id = {e["id"]: e for e in self.registry["entries"]}
        isbns = {e["isbn13"] for e in por_id.values() if e.get("isbn13")}
        for datos in self.biblio.values():
            bloque = class_block(datos)
            for token in re.findall(r"97[89]\d{10}", bloque):
                self.assertIn(token, isbns)


class VerifierTests(unittest.TestCase):
    def test_repository_passes_the_source_verifier(self):
        result = verify(ROOT)
        self.assertEqual(result["problems"], [])
        self.assertTrue(result["ok"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
