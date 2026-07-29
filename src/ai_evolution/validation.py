
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from .catalog import REPO_ROOT, load_curriculum
from .labs import RUNNERS


REQUIRED_LESSON_FILES = {
    "README.md",
    "theory.md",
    "assessment.md",
    "lesson.yaml",
    "lab.py",
    "notebook.ipynb",
    "notebook_student.ipynb",
    "notebook_solution.ipynb",
}


def validate_repository(*, strict: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    curriculum = load_curriculum()
    lessons = [lesson for part in curriculum["parts"] for lesson in part["lessons"]]

    ids = [str(item["id"]) for item in lessons]
    if len(ids) != len(set(ids)):
        errors.append("IDs de clases duplicados")
    if len(curriculum["parts"]) != 15:
        errors.append(f"se esperaban 15 partes y hay {len(curriculum['parts'])}")
    if len(lessons) != 180:
        errors.append(f"se esperaban 180 clases y hay {len(lessons)}")

    for item in lessons:
        folder = REPO_ROOT / item["path"]
        if not folder.is_dir():
            errors.append(f"falta carpeta: {item['path']}")
            continue
        present = {path.name for path in folder.iterdir() if path.is_file()}
        missing = REQUIRED_LESSON_FILES - present
        if missing:
            errors.append(f"{item['id']}: faltan {sorted(missing)}")
        if item["lab_kind"] not in RUNNERS:
            errors.append(f"{item['id']}: lab_kind desconocido {item['lab_kind']}")
        manifest = yaml.safe_load((folder / "lesson.yaml").read_text(encoding="utf-8"))
        if str(manifest["id"]) != str(item["id"]):
            errors.append(f"{item['id']}: lesson.yaml desalineado")
        for notebook_name in ("notebook.ipynb", "notebook_student.ipynb", "notebook_solution.ipynb"):
            path = folder / notebook_name
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError) as exc:
                errors.append(f"{item['id']}/{notebook_name}: {exc}")
                continue
            if payload.get("nbformat") != 4 or not payload.get("cells"):
                errors.append(f"{item['id']}/{notebook_name}: contrato notebook inválido")

    if strict:
        for path in REPO_ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            if "TODO AUTOR" in text or "LOREM IPSUM" in text.upper():
                errors.append(f"placeholder editorial en {path.relative_to(REPO_ROOT)}")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                clean = target.split("#", 1)[0].strip()
                if not clean or clean.startswith(("http://", "https://", "mailto:", "oai-")):
                    continue
                if not (path.parent / clean).resolve().exists():
                    errors.append(
                        f"enlace interno roto en {path.relative_to(REPO_ROOT)}: {target}"
                    )
        if warnings:
            errors.extend(warnings)

    return {
        "ok": not errors,
        "parts": len(curriculum["parts"]),
        "lessons": len(lessons),
        "notebooks": len(lessons) * 3,
        "errors": errors,
        "warnings": warnings,
    }
