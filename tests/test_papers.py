
from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.papers import (
    FICHA_SECTIONS,
    NOTEBOOK_SECTIONS,
    find_paper,
    load_papers,
    load_sources,
    papers,
    sha256_of,
    validate_papers,
)
from ai_evolution.papers_lab import PAPER_RUNNERS, run_paper_lab

NOTEBOOKS = ROOT / "notebooks" / "papers"


class CatalogTests(unittest.TestCase):
    def test_catalog_is_valid_json_with_16_papers(self):
        data = load_papers()
        self.assertEqual(len(data["papers"]), 16)
        self.assertEqual(data["ruta_minima"], [item["id"] for item in data["papers"]])

    def test_sources_yaml_parses(self):
        sources = load_sources()
        for key in ("repositorios_de_preprints", "conferencias", "revisiones_abiertas", "buscadores_e_indices"):
            self.assertIn(key, sources)

    def test_unique_ids_dirs_and_labs(self):
        items = papers()
        self.assertEqual(len({item.id for item in items}), len(items))
        self.assertEqual(len({item.dir for item in items}), len(items))
        for item in items:
            self.assertIn(item.lab, PAPER_RUNNERS)

    def test_find_paper_accepts_several_forms(self):
        self.assertEqual(find_paper("P08").id, "P08")
        self.assertEqual(find_paper(8).id, "P08")
        self.assertEqual(find_paper("Attention Is All You Need").id, "P08")
        with self.assertRaises(KeyError):
            find_paper("P99")

    def test_chronological_order(self):
        years = [item.year for item in papers()]
        self.assertEqual(years, sorted(years))

    def test_every_primary_source_has_url(self):
        for item in load_papers()["papers"]:
            self.assertTrue(item["fuentes_primarias"], item["id"])
            for source in item["fuentes_primarias"]:
                self.assertTrue(source["url"].startswith("http"), item["id"])


class ContractTests(unittest.TestCase):
    def test_repository_contract(self):
        result = validate_papers(strict=True)
        self.assertTrue(result["ok"], result["errors"][:10])
        self.assertEqual(result["papers"], 16)
        self.assertEqual(result["notebooks"], 24)
        self.assertEqual(result["notebooks_transformer"], 8)

    def test_every_ficha_has_the_18_sections_in_order(self):
        for item in papers():
            with self.subTest(paper=item.id):
                text = (ROOT / item.ficha_path).read_text(encoding="utf-8")
                found = [line[3:].strip() for line in text.splitlines() if line.startswith("## ")]
                self.assertEqual([s for s in found if s in FICHA_SECTIONS], list(FICHA_SECTIONS))

    def test_every_notebook_has_the_17_moments_in_order(self):
        for path in sorted(NOTEBOOKS.glob("*.ipynb")):
            with self.subTest(notebook=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(payload["nbformat"], 4)
                found = [
                    line[3:].strip()
                    for cell in payload["cells"]
                    if cell["cell_type"] == "markdown"
                    for line in "".join(cell["source"]).splitlines()
                    if line.startswith("## ")
                ]
                self.assertEqual([s for s in found if s in NOTEBOOK_SECTIONS], list(NOTEBOOK_SECTIONS))

    def test_derived_artefacts_exist(self):
        for item in papers():
            with self.subTest(paper=item.id):
                for rel in (item.notebook_path, item.assessment_path,
                            f"instructor/papers/{item.dir}.md", f"student/papers/{item.dir}.md"):
                    self.assertTrue((ROOT / rel).is_file(), rel)

    def test_no_absolute_paths_in_notebooks(self):
        for path in sorted(NOTEBOOKS.glob("*.ipynb")):
            text = path.read_text(encoding="utf-8")
            with self.subTest(notebook=path.name):
                self.assertNotIn("C:\\\\", text)
                self.assertNotIn("/home/", text)
                self.assertNotIn("/Users/", text)

    def test_manifest_hashes_are_current(self):
        manifest = json.loads((ROOT / "papers" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["papers"], 16)
        self.assertEqual(manifest["notebooks"], 24)
        for entry in manifest["files"]:
            target = ROOT / entry["path"]
            with self.subTest(file=entry["path"]):
                self.assertTrue(target.exists())
                self.assertEqual(sha256_of(target), entry["sha256"])


class PaperLabTests(unittest.TestCase):
    def test_every_runner_returns_the_contract(self):
        for index, kind in enumerate(sorted(PAPER_RUNNERS), start=1):
            with self.subTest(kind=kind):
                result = run_paper_lab(kind, seed=index)
                self.assertEqual(result["kind"], kind)
                self.assertEqual(result["seed"], index)
                self.assertTrue(result["result"])
                self.assertGreaterEqual(len(result["evidence"]), 2)
                self.assertGreaterEqual(len(result["limitations"]), 2)

    def test_runners_are_deterministic(self):
        for kind in sorted(PAPER_RUNNERS):
            with self.subTest(kind=kind):
                self.assertEqual(run_paper_lab(kind, seed=3), run_paper_lab(kind, seed=3))

    def test_unknown_runner_raises(self):
        with self.assertRaises(KeyError):
            run_paper_lab("no-existe")

    def test_perceptron_separates_and_but_not_xor(self):
        result = run_paper_lab("perceptron", seed=1)["result"]
        self.assertTrue(result["separable"]["AND"])
        self.assertFalse(result["separable"]["XOR"])

    def test_backprop_gradient_check(self):
        result = run_paper_lab("backprop", seed=7)["result"]
        self.assertLess(result["grad_check"]["abs_diff"], 1e-5)
        self.assertLess(result["loss_history"][-1]["loss"], result["loss_history"][0]["loss"])

    def test_attention_weights_sum_to_one_and_mask_the_future(self):
        result = run_paper_lab("transformer", seed=5)["result"]
        for i, row in enumerate(result["mascara_causal"]):
            # la salida está redondeada a 3 decimales: se compara con tolerancia
            self.assertAlmostEqual(sum(row), 1.0, delta=0.002)
            self.assertEqual(sum(row[i + 1:]), 0.0)

    def test_scaling_keeps_attention_entropy_higher(self):
        entropies = run_paper_lab("transformer", seed=5)["result"]["entropia_media"]
        self.assertGreater(entropies["con_escala_sqrt_dk"], entropies["sin_escala"])

    def test_bahdanau_learns_the_alignment(self):
        for seed in (1, 7, 42):
            with self.subTest(seed=seed):
                result = run_paper_lab("bahdanau", seed=seed)["result"]
                self.assertEqual(result["aciertos_de_alineacion"], "4/4")
                for row in result["alignment"]:
                    self.assertAlmostEqual(row["suma_alpha"], 1.0, places=2)

    def test_word2vec_analogy_is_stable_across_seeds(self):
        for seed in (1, 7, 42):
            with self.subTest(seed=seed):
                top = run_paper_lab("word2vec", seed=seed)["result"]["analogy_rey_menos_hombre_mas_mujer"]
                self.assertEqual(top[0]["word"], "reina")

    def test_rag_ranks_the_right_document_first(self):
        result = run_paper_lab("rag", seed=2)["result"]
        self.assertEqual(result["ranking"][0]["doc"], "d4")

    def test_agentic_escalates_instead_of_answering(self):
        result = run_paper_lab("agentic", seed=2)["result"]
        self.assertTrue(result["escalado_a_humano"])
        self.assertLessEqual(result["consumido"]["pasos"], result["presupuesto"]["pasos"])


class NotebookExecutionTests(unittest.TestCase):
    """Smoke test: cada celda de código de cada notebook se ejecuta sin excepción."""

    def test_all_notebook_code_cells_run(self):
        for path in sorted(NOTEBOOKS.glob("*.ipynb")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            namespace: dict[str, object] = {"__name__": "__main__"}
            with self.subTest(notebook=path.name):
                buffer = io.StringIO()
                with redirect_stdout(buffer):
                    for cell in payload["cells"]:
                        if cell["cell_type"] == "code":
                            exec("".join(cell["source"]), namespace)  # noqa: S102
                self.assertTrue(buffer.getvalue().strip(), f"{path.name} no imprimió nada")


if __name__ == "__main__":
    unittest.main()
