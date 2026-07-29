
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
CURRICULUM_PATH = REPO_ROOT / "curriculum.yaml"


@dataclass(frozen=True)
class Lesson:
    id: str
    number: int
    title: str
    part_id: str
    part_title: str
    path: str
    lab_kind: str
    level: str
    estimated_hours: int
    keywords: tuple[str, ...]


@lru_cache(maxsize=1)
def load_curriculum() -> dict[str, Any]:
    return yaml.safe_load(CURRICULUM_PATH.read_text(encoding="utf-8"))


def lessons() -> list[Lesson]:
    result = []
    for part in load_curriculum()["parts"]:
        for item in part["lessons"]:
            result.append(
                Lesson(
                    id=str(item["id"]),
                    number=int(item["number"]),
                    title=item["title"],
                    part_id=str(part["id"]),
                    part_title=part["title"],
                    path=item["path"],
                    lab_kind=item["lab_kind"],
                    level=part["level"],
                    estimated_hours=int(item["estimated_hours"]),
                    keywords=tuple(item["keywords"]),
                )
            )
    return result


def find_lesson(identifier: str | int) -> Lesson:
    text = str(identifier).strip()
    for item in lessons():
        if item.id == text.zfill(3) or item.path.endswith(text) or text.lower() in item.title.lower():
            return item
    raise KeyError(f"clase no encontrada: {identifier}")
