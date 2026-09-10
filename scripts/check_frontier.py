#!/usr/bin/env python3
"""Valida que la frontera tenga fuente, versión y fecha de revisión vigentes."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
FRONTIER = ROOT / "frontier" / "current-topics.yaml"
ALLOWED_MATURITY = {"standard", "current", "emerging"}


def validate(max_age_days: int = 120) -> list[str]:
    payload = yaml.safe_load(FRONTIER.read_text(encoding="utf-8"))
    errors: list[str] = []
    ids: set[str] = set()
    today = date.today()
    for topic in payload.get("topics", []):
        topic_id = topic.get("id")
        if not topic_id or topic_id in ids:
            errors.append(f"id ausente o duplicado: {topic_id!r}")
        ids.add(topic_id)
        if topic.get("maturity") not in ALLOWED_MATURITY:
            errors.append(f"{topic_id}: maturity inválida")
        if not str(topic.get("source", "")).startswith("https://"):
            errors.append(f"{topic_id}: falta fuente https")
        try:
            reviewed = date.fromisoformat(str(topic["reviewed"]))
        except (KeyError, ValueError):
            errors.append(f"{topic_id}: reviewed inválido")
            continue
        age = (today - reviewed).days
        if age < 0:
            errors.append(f"{topic_id}: fecha de revisión futura")
        if topic.get("maturity") in {"standard", "current"} and age > max_age_days:
            errors.append(f"{topic_id}: revisión vencida ({age} días > {max_age_days})")
        if topic.get("maturity") == "standard" and not topic.get("spec_version"):
            errors.append(f"{topic_id}: un estándar debe fijar spec_version")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-age-days", type=int, default=120)
    args = parser.parse_args()
    errors = validate(args.max_age_days)
    if errors:
        raise SystemExit("Frontera desactualizada:\n- " + "\n- ".join(errors))
    print(f"OK: frontera vigente ({len(yaml.safe_load(FRONTIER.read_text(encoding='utf-8'))['topics'])} temas)")


if __name__ == "__main__":
    main()
