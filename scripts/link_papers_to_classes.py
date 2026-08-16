"""Enlaces de vuelta: de cada clase a los papers que la fundamentan.

Las fichas de `papers/` ya enlazan **hacia** las clases. Esto cierra el circuito
en el otro sentido, insertando en el README de cada clase enlazada un bloque con
los papers correspondientes.

El bloque va delimitado por marcadores, así que la operación es **idempotente**:
volver a ejecutar el script actualiza el bloque en lugar de duplicarlo, y borrar
un enlace en `papers.json` lo retira de la clase.

Uso::

    python scripts/link_papers_to_classes.py            # inserta o actualiza
    python scripts/link_papers_to_classes.py --check    # falla si algo está desactualizado
    python scripts/link_papers_to_classes.py --remove   # retira todos los bloques
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.papers import load_papers  # noqa: E402

INICIO = "<!-- papers:inicio -->"
FIN = "<!-- papers:fin -->"
ANCLA = "\n---\n\n## ⬅️ Clase anterior"


def bloque(papers: list[dict]) -> str:
    """Construye el bloque de enlaces de vuelta para una clase."""
    filas = "\n".join(
        f"| [{p['id']} · {p['title_es']}](../../../papers/foundational/{p['dir']}/README.md) "
        f"| {p['year']} | {p['hito']} "
        f"| [notebook](../../../notebooks/papers/{p['dir']}.ipynb) |"
        for p in papers
    )
    return (
        f"{INICIO}\n"
        "\n---\n\n"
        "## 📜 Papers que fundamentan esta clase\n\n"
        "> Bloque generado por `python scripts/link_papers_to_classes.py`. "
        "La fuente es [`papers/catalog/papers.json`](../../../papers/catalog/papers.json).\n\n"
        "| Paper | Año | Qué desbloqueó | Miniatura |\n"
        "|---|---:|---|---|\n"
        f"{filas}\n\n"
        "Cada ficha explica el problema anterior, la matemática mínima, los límites y los errores "
        "de atribución más frecuentes. Para leerlas con método: "
        "[cómo leer un paper de IA](../../../papers/guides/COMO_LEER_UN_PAPER_DE_IA.md) · "
        "[anexos matemáticos](../../../papers/annexes/README.md).\n"
        f"{FIN}"
    )


def aplicar(texto: str, nuevo: str) -> str:
    """Inserta o reemplaza el bloque, siempre antes del pie de navegación."""
    if INICIO in texto and FIN in texto:
        antes, resto = texto.split(INICIO, 1)
        _, despues = resto.split(FIN, 1)
        return antes + nuevo + despues
    if ANCLA in texto:
        antes, despues = texto.split(ANCLA, 1)
        return antes.rstrip("\n") + "\n\n" + nuevo + ANCLA + despues
    return texto.rstrip("\n") + "\n\n" + nuevo + "\n"


def retirar(texto: str) -> str:
    if INICIO not in texto or FIN not in texto:
        return texto
    antes, resto = texto.split(INICIO, 1)
    _, despues = resto.split(FIN, 1)
    return antes.rstrip("\n") + "\n" + despues.lstrip("\n")


def mapa_clase_a_papers() -> dict[str, list[dict]]:
    destino: dict[str, list[dict]] = {}
    for item in load_papers()["papers"]:
        for ruta in item["clases_del_programa"]:
            destino.setdefault(ruta, []).append(item)
    return destino


def main() -> int:
    parser = argparse.ArgumentParser(description="Enlaza cada clase con sus papers")
    parser.add_argument("--check", action="store_true", help="falla si algún bloque está desactualizado")
    parser.add_argument("--remove", action="store_true", help="retira los bloques insertados")
    args = parser.parse_args()

    destino = mapa_clase_a_papers()
    desactualizadas: list[str] = []
    tocadas = 0

    if args.remove:
        for readme in ROOT.glob("classes/*/*/README.md"):
            texto = readme.read_text(encoding="utf-8")
            limpio = retirar(texto)
            if limpio != texto:
                readme.write_text(limpio, encoding="utf-8", newline="\n")
                tocadas += 1
        print(f"bloques retirados de {tocadas} clases")
        return 0

    for ruta, papers in sorted(destino.items()):
        readme = ROOT / ruta / "README.md"
        if not readme.is_file():
            print(f"AVISO: no existe {ruta}/README.md")
            continue
        texto = readme.read_text(encoding="utf-8")
        nuevo = aplicar(texto, bloque(sorted(papers, key=lambda p: p["id"])))
        if nuevo != texto:
            if args.check:
                desactualizadas.append(ruta)
            else:
                readme.write_text(nuevo, encoding="utf-8", newline="\n")
                tocadas += 1

    if args.check:
        if desactualizadas:
            print("clases con enlaces de vuelta desactualizados:")
            for ruta in desactualizadas:
                print(" ·", ruta)
            return 1
        print(f"enlaces de vuelta al día en {len(destino)} clases")
        return 0

    print(f"enlaces de vuelta escritos: {tocadas} clases modificadas de {len(destino)} enlazadas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
