
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.catalog import find_lesson, lessons, load_curriculum
from ai_evolution.labs import RUNNERS, run_lab
from ai_evolution.validation import validate_repository


class CurriculumTests(unittest.TestCase):
    def test_counts(self):
        curriculum = load_curriculum()
        self.assertEqual(len(curriculum["parts"]), 15)
        self.assertEqual(len(lessons()), 183)

    def test_unique_ids_and_paths(self):
        all_lessons = lessons()
        self.assertEqual(len({item.id for item in all_lessons}), len(all_lessons))
        self.assertEqual(len({item.path for item in all_lessons}), len(all_lessons))

    def test_find_lesson(self):
        self.assertEqual(find_lesson("1").id, "001")
        self.assertEqual(find_lesson("agentes racionales").id, "004")

    def test_repository_contract(self):
        result = validate_repository(strict=True)
        self.assertTrue(result["ok"], result["errors"][:10])
        self.assertEqual(result["notebooks"], 549)


class LabTests(unittest.TestCase):
    def test_every_runner_contract(self):
        for index, kind in enumerate(sorted(RUNNERS), start=1):
            with self.subTest(kind=kind):
                result = run_lab(kind, seed=index)
                self.assertEqual(result["kind"], kind)
                self.assertEqual(result["seed"], index)
                self.assertTrue(result["evidence"])
                self.assertTrue(result["limitations"])

    def test_deterministic_where_expected(self):
        self.assertEqual(run_lab("search", seed=1), run_lab("search", seed=1))
        self.assertEqual(run_lab("agent", seed=7), run_lab("agent", seed=7))

    def test_notebooks_are_json(self):
        first = lessons()[0]
        folder = ROOT / first.path
        for name in ("notebook.ipynb", "notebook_student.ipynb", "notebook_solution.ipynb"):
            payload = json.loads((folder / name).read_text(encoding="utf-8"))
            self.assertEqual(payload["nbformat"], 4)
            self.assertGreaterEqual(len(payload["cells"]), 4)


class VersionCoherenceTests(unittest.TestCase):
    """La versión se declara en cinco sitios: o coinciden todos, o el repo miente.

    Ya ocurrió dos veces: en 0.2.1 (`curriculum.yaml` y `__version__` arrastraban
    0.1.0) y en 0.4.x (`__version__` y la app Android se quedaron en 0.3.0
    mientras `pyproject` iba por 0.4.2). Esta prueba lo convierte en un fallo de
    CI en lugar de en un hallazgo casual.
    """

    def canonical(self) -> str:
        for line in (ROOT / "pyproject.toml").read_text(encoding="utf-8").splitlines():
            if line.startswith("version = "):
                return line.split('"')[1]
        self.fail("pyproject.toml no declara version")

    def test_all_manifests_declare_the_same_version(self):
        esperada = self.canonical()
        declarada = {
            "src/ai_evolution/__init__.py": re.search(
                r'__version__\s*=\s*"([^"]+)"',
                (ROOT / "src" / "ai_evolution" / "__init__.py").read_text(encoding="utf-8"),
            ).group(1),
            "curriculum.yaml": str(yaml.safe_load((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))["version"]),
            "apps/android/package.json": json.loads(
                (ROOT / "apps" / "android" / "package.json").read_text(encoding="utf-8")
            )["version"],
        }
        for fuente, valor in declarada.items():
            with self.subTest(fuente=fuente):
                self.assertEqual(valor, esperada)

    def test_readme_badge_matches(self):
        esperada = self.canonical()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"version-{esperada}-", readme)

    def test_changelog_documents_the_current_version(self):
        esperada = self.canonical()
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn(f"## {esperada} — ", changelog)


if __name__ == "__main__":
    unittest.main()
