"""Declara, en cada clase, el uso que esa clase hace de cada fuente que cita.

No reescribe el contenido de las clases: solo añade al final de la cita, cuando
falta, la función que esa fuente cumple en la clase, tomada de un vocabulario
controlado y derivada del tipo de la entrada en `sources/bibliography.json`.

El vocabulario es mecánico a propósito. Un motivo redactado fuente a fuente
habría que inventarlo, y este repositorio no inventa aparato crítico: las citas
que ya traen su propia explicación se dejan intactas.

    python scripts/annotate_class_sources.py           # anota
    python scripts/annotate_class_sources.py --check   # falla si falta alguna
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.sources import (  # noqa: E402
    REF_HEADING,
    USE_ROLES,
    load_registry,
    normalize_url_key,
    normalize_work_key,
    RefItem,
    extract_urls,
    WORK_RE,
    class_files,
    reference_block,
)


def type_index(registry: dict) -> tuple[dict[str, str], dict[str, str]]:
    urls: dict[str, str] = {}
    works: dict[str, str] = {}
    for entry in registry["entries"]:
        for key in entry.get("url_keys", []):
            urls.setdefault(normalize_url_key(key), entry["type"])
        for key in entry.get("aliases", []):
            works.setdefault(normalize_work_key(key), entry["type"])
    return urls, works


def role_for(item: RefItem, urls: dict[str, str], works: dict[str, str]) -> str:
    for key in item.url_keys:
        if key in urls:
            return USE_ROLES[urls[key]]
    for key in item.work_keys:
        if key in works:
            return USE_ROLES[works[key]]
    return USE_ROLES["reference"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    urls, works = type_index(load_registry())
    touched = 0
    missing: list[str] = []

    for path in class_files(ROOT):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        block = reference_block(text)
        if block is None:
            continue
        lines = text.splitlines(keepends=True)
        heading = next(i for i, l in enumerate(lines) if l.startswith(REF_HEADING))
        changed = False
        for index in range(heading + 1, len(lines)):
            line = lines[index].strip()
            if line.startswith("## ") or line.startswith("<!-- papers:inicio -->"):
                break
            if not line.startswith("- "):
                continue
            body = line[2:].strip()
            item = RefItem(
                class_path=rel,
                line_no=index + 1,
                text=body,
                urls=extract_urls(body),
                works=WORK_RE.findall(body),
            )
            if item.declares_use:
                continue
            if args.check:
                missing.append(f"{rel}:{item.line_no}")
                continue
            role = role_for(item, urls, works)
            lines[index] = f"- {body} — uso: {role}\n"
            changed = True
            touched += 1
        if changed:
            path.write_text("".join(lines), encoding="utf-8")

    if args.check:
        if missing:
            print(f"{len(missing)} fuentes sin declarar el uso; la primera: {missing[0]}")
            return 1
        print("Todas las fuentes citadas declaran su uso.")
        return 0
    print(f"{touched} citas anotadas con el uso que la clase hace de la fuente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
