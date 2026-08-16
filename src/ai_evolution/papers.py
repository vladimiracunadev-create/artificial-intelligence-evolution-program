"""Catálogo y contrato de calidad del eje `papers/`.

El eje convierte cada paper fundacional en una experiencia reproducible:

    problema histórico → propuesta → intuición → matemática mínima →
    implementación → experimento → interpretación → limitaciones → siguiente hito

Este módulo es la única fuente de verdad del *contrato*: qué secciones debe tener
una ficha, qué secciones debe tener un notebook y qué debe cumplir `papers.json`.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from .catalog import REPO_ROOT
from .papers_lab import PAPER_RUNNERS


PAPERS_DIR = REPO_ROOT / "papers"
CATALOG_PATH = PAPERS_DIR / "catalog" / "papers.json"
SOURCES_PATH = PAPERS_DIR / "catalog" / "sources.yaml"
MANIFEST_PATH = PAPERS_DIR / "manifest.json"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks" / "papers"

#: Contrato de ficha pedagógica: 18 secciones obligatorias, en este orden.
FICHA_SECTIONS: tuple[str, ...] = (
    "1. Identificación",
    "2. Problema anterior",
    "3. Propuesta",
    "4. Intuición sin fórmulas",
    "5. Matemática mínima",
    "6. Arquitectura o flujo",
    "7. Qué observar en el paper original",
    "8. Evidencia y resultados",
    "9. Impacto",
    "10. Limitaciones",
    "11. Errores comunes",
    "12. Relación con trabajos anteriores",
    "13. Relación con trabajos posteriores",
    "14. Notebook asociado",
    "15. Actividades Bloom",
    "16. Autoevaluación",
    "17. Respuestas esperadas",
    "18. Fuentes primarias",
)

#: Contrato de notebook: 17 momentos obligatorios, en este orden.
NOTEBOOK_SECTIONS: tuple[str, ...] = (
    "1. Título y paper",
    "2. Objetivos",
    "3. Prerrequisitos",
    "4. Intuición",
    "5. Concepto mínimo",
    "6. Código explicado",
    "7. Predicción antes de ejecutar",
    "8. Experimento controlado",
    "9. Salida interpretable",
    "10. Comentario pedagógico",
    "11. Error o anti-patrón deliberado",
    "12. Corrección",
    "13. Desafío guiado",
    "14. Desafío autónomo",
    "15. Evidencia de aprendizaje",
    "16. Cierre",
    "17. Conexión con el siguiente hito",
)

REQUIRED_PAPER_FIELDS: tuple[str, ...] = (
    "id", "dir", "slug", "title", "title_es", "authors", "year", "venue", "venue_type",
    "acceso", "level", "lab", "hito", "problema", "propuesta", "keywords",
    "anteriores", "posteriores", "clases_del_programa", "fuentes_primarias", "consultado",
)

VALID_LEVELS = ("L0", "L1", "L2", "L3", "L4", "L5")


@dataclass(frozen=True)
class Paper:
    id: str
    dir: str
    slug: str
    title: str
    title_es: str
    authors: tuple[str, ...]
    year: int
    venue: str
    level: str
    lab: str
    hito: str
    keywords: tuple[str, ...]

    @property
    def ficha_path(self) -> str:
        return f"papers/foundational/{self.dir}/README.md"

    @property
    def notebook_path(self) -> str:
        return f"notebooks/papers/{self.dir}.ipynb"

    @property
    def assessment_path(self) -> str:
        return f"assessments/papers/{self.dir}.md"


@lru_cache(maxsize=1)
def load_papers() -> dict[str, Any]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def load_sources() -> dict[str, Any]:
    return yaml.safe_load(SOURCES_PATH.read_text(encoding="utf-8"))


def papers() -> list[Paper]:
    return [
        Paper(
            id=item["id"],
            dir=item["dir"],
            slug=item["slug"],
            title=item["title"],
            title_es=item["title_es"],
            authors=tuple(item["authors"]),
            year=int(item["year"]),
            venue=item["venue"],
            level=item["level"],
            lab=item["lab"],
            hito=item["hito"],
            keywords=tuple(item["keywords"]),
        )
        for item in load_papers()["papers"]
    ]


def find_paper(identifier: str | int) -> Paper:
    text = str(identifier).strip().lower()
    for item in papers():
        if text in (item.id.lower(), item.dir.lower(), item.slug.lower()):
            return item
        if text.isdigit() and item.id.lower() == f"p{int(text):02d}":
            return item
        if text in item.title.lower() or text in item.title_es.lower():
            return item
    raise KeyError(f"paper no encontrado: {identifier}")


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _markdown_sections(text: str) -> list[str]:
    return [line[3:].strip() for line in text.splitlines() if line.startswith("## ")]


def _notebook_sections(payload: dict[str, Any]) -> list[str]:
    found = []
    for cell in payload.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in "".join(cell.get("source", [])).splitlines():
            if line.startswith("## "):
                found.append(line[3:].strip())
    return found


def _check_contract(found: list[str], expected: tuple[str, ...], label: str, errors: list[str]) -> None:
    ordered = [item for item in found if item in expected]
    if ordered != list(expected):
        missing = [item for item in expected if item not in found]
        if missing:
            errors.append(f"{label}: faltan secciones {missing}")
        else:
            errors.append(f"{label}: las secciones están fuera del orden del contrato")


def validate_papers(*, strict: bool = False) -> dict[str, Any]:
    """Verifica el contrato completo del eje `papers/`."""
    errors: list[str] = []
    if not CATALOG_PATH.exists():
        return {"ok": False, "papers": 0, "notebooks": 0, "errors": ["falta papers/catalog/papers.json"]}

    data = load_papers()
    items = data["papers"]
    ids = [item["id"] for item in items]
    if len(ids) != len(set(ids)):
        errors.append("IDs de papers duplicados")
    if ids != data["ruta_minima"]:
        errors.append("`ruta_minima` no coincide con el orden de `papers`")

    try:
        load_sources()
    except yaml.YAMLError as exc:                                  # pragma: no cover - defensivo
        errors.append(f"sources.yaml inválido: {exc}")

    notebooks = 0
    for item in items:
        pid = item["id"]
        missing_fields = [field for field in REQUIRED_PAPER_FIELDS if field not in item]
        if missing_fields:
            errors.append(f"{pid}: faltan campos {missing_fields}")
            continue
        if item["level"] not in VALID_LEVELS:
            errors.append(f"{pid}: nivel desconocido {item['level']}")
        if item["lab"] not in PAPER_RUNNERS:
            errors.append(f"{pid}: motor desconocido {item['lab']}")
        if not item["fuentes_primarias"]:
            errors.append(f"{pid}: sin fuente primaria registrada")
        for source in item["fuentes_primarias"]:
            if not source.get("url", "").startswith("http"):
                errors.append(f"{pid}: fuente primaria sin URL válida")

        ficha = REPO_ROOT / "papers" / "foundational" / item["dir"] / "README.md"
        if not ficha.exists():
            errors.append(f"{pid}: falta la ficha {ficha.relative_to(REPO_ROOT).as_posix()}")
        else:
            _check_contract(_markdown_sections(ficha.read_text(encoding="utf-8")),
                            FICHA_SECTIONS, f"{pid} ficha", errors)

        notebook = NOTEBOOKS_DIR / f"{item['dir']}.ipynb"
        if not notebook.exists():
            errors.append(f"{pid}: falta el notebook {notebook.relative_to(REPO_ROOT).as_posix()}")
        else:
            notebooks += 1
            try:
                payload = json.loads(notebook.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{pid}/notebook: JSON inválido ({exc})")
                payload = {}
            if payload.get("nbformat") != 4 or not payload.get("cells"):
                errors.append(f"{pid}/notebook: contrato nbformat inválido")
            else:
                _check_contract(_notebook_sections(payload), NOTEBOOK_SECTIONS, f"{pid} notebook", errors)

        for lesson_path in item["clases_del_programa"]:
            if not (REPO_ROOT / lesson_path).is_dir():
                errors.append(f"{pid}: clase enlazada inexistente {lesson_path}")

    extra_notebooks = sorted(
        path.name for path in NOTEBOOKS_DIR.glob("T*.ipynb")
    ) if NOTEBOOKS_DIR.exists() else []
    for name in extra_notebooks:
        payload = json.loads((NOTEBOOKS_DIR / name).read_text(encoding="utf-8"))
        if payload.get("nbformat") != 4 or not payload.get("cells"):
            errors.append(f"notebooks/papers/{name}: contrato nbformat inválido")
        else:
            _check_contract(_notebook_sections(payload), NOTEBOOK_SECTIONS, f"{name}", errors)

    if strict and MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        for entry in manifest["files"]:
            target = REPO_ROOT / entry["path"]
            if not target.exists():
                errors.append(f"manifest: falta {entry['path']}")
            elif sha256_of(target) != entry["sha256"]:
                errors.append(f"manifest: SHA-256 desactualizado en {entry['path']}")

    return {
        "ok": not errors,
        "papers": len(items),
        "notebooks": notebooks + len(extra_notebooks),
        "notebooks_transformer": len(extra_notebooks),
        "errors": errors,
    }
