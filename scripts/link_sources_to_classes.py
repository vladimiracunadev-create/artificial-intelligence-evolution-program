"""Bibliografía de apoyo en cada clase: además del paper, el libro que lo desarrolla.

El bloque de papers responde **de dónde salió** el mecanismo. Este responde
**con qué se estudia**: la obra que desarrolla el contenido de la clase con el
espacio que una clase no tiene.

Cada clase muestra los libros que ya cita —con el capítulo, cuando la cita lo
indica— y, si su parte tiene obra de referencia en
`sources/support_map.json`, también esa. Todo sale del registro: aquí no se
escribe ni un ISBN ni un título a mano.

El bloque va entre marcadores, así que la operación es idempotente.

Uso::

    python scripts/link_sources_to_classes.py            # inserta o actualiza
    python scripts/link_sources_to_classes.py --check    # falla si está desfasado
    python scripts/link_sources_to_classes.py --remove   # retira los bloques
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.sources import (  # noqa: E402
    CLASS_BEGIN,
    CLASS_END,
    class_bibliography,
    class_block,
    class_files,
    extract_items,
    load_registry,
    load_support_map,
)

ANCLA = "\n---\n\n## ⬅️ Clase anterior"


def aplicar(texto: str, bloque: str) -> str:
    """Inserta o reemplaza el bloque, siempre antes del pie de navegación."""
    if CLASS_BEGIN in texto and CLASS_END in texto:
        inicio = texto.index(CLASS_BEGIN)
        fin = texto.index(CLASS_END) + len(CLASS_END)
        return texto[:inicio] + bloque + texto[fin:]
    if ANCLA in texto:
        corte = texto.index(ANCLA)
        return texto[:corte] + "\n" + bloque + "\n" + texto[corte:]
    return texto.rstrip() + "\n\n" + bloque + "\n"


def retirar(texto: str) -> str:
    if CLASS_BEGIN not in texto or CLASS_END not in texto:
        return texto
    inicio = texto.index(CLASS_BEGIN)
    fin = texto.index(CLASS_END) + len(CLASS_END)
    return (texto[:inicio].rstrip("\n") + "\n" + texto[fin:].lstrip("\n")).replace("\n\n\n", "\n\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--remove", action="store_true")
    args = parser.parse_args()

    registry = load_registry()
    support = load_support_map(ROOT)
    items = extract_items(ROOT)
    esperado = class_bibliography(registry, support, items)

    tocadas = 0
    desfasadas: list[str] = []
    sin_obra: list[str] = []
    for path in class_files(ROOT):
        rel = path.relative_to(ROOT).as_posix()
        texto = path.read_text(encoding="utf-8")
        if args.remove:
            nuevo = retirar(texto)
        else:
            datos = esperado.get(rel)
            if not datos or not datos["obras"]:
                sin_obra.append(rel)
                continue
            nuevo = aplicar(texto, class_block(datos))
        if nuevo != texto:
            if args.check:
                desfasadas.append(rel)
            else:
                path.write_text(nuevo, encoding="utf-8")
                tocadas += 1

    if sin_obra:
        print(f"{len(sin_obra)} clases sin obra de apoyo; la primera: {sin_obra[0]}")
        return 1
    if args.check:
        if desfasadas:
            print(
                f"{len(desfasadas)} clases con la bibliografía desfasada; "
                f"la primera: {desfasadas[0]}"
            )
            return 1
        print("bibliografía de apoyo al día en todas las clases")
        return 0
    accion = "retirado de" if args.remove else "actualizado en"
    print(f"bloque de bibliografía {accion} {tocadas} clases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
