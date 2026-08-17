from __future__ import annotations

import json
import posixpath
import re
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

PAGE_TEMPLATE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#070b17">
  <meta name="description" content="{description}">
  <link rel="icon" type="image/svg+xml" href="../assets/icon.svg">
  <link rel="stylesheet" href="../assets/styles.css">
  <link rel="stylesheet" href="../assets/class.css">
  <title>{title} · AI Evolution Program</title>
</head>
<body class="doc">
  <nav class="topbar">
    <a href="../index.html">🧠 AI Evolution Program</a>
    <span>{crumb}</span>
  </nav>
  <main class="content" id="top">
{body}
  </main>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
    document.querySelectorAll("pre > code.language-mermaid").forEach(code => {{
      const pre = code.parentElement;
      const div = document.createElement("pre");
      div.className = "mermaid";
      div.textContent = code.textContent;
      pre.replaceWith(div);
    }});
    mermaid.initialize({{ startOnLoad: true, theme: "dark" }});
  </script>
</body>
</html>
"""


def render(md_text: str) -> str:
    return markdown.markdown(md_text, extensions=MD_EXTENSIONS)


def write_lf(path: Path, content: str) -> None:
    """Escribe siempre con LF, en cualquier sistema operativo.

    Sin `newline="\\n"`, Python traduce a CRLF en Windows y el mismo comando
    produce artefactos distintos según dónde se ejecutó.
    """
    path.write_text(content, encoding="utf-8", newline="\n")


def rewrite_class_links(text: str, lesson_path: str) -> str:
    # clase → clase (nav superior y pie), mismo o distinto part
    text = re.sub(
        r"\((?:\.\./)+(?:classes/)?part-\d{2}-[^/)]+/(\d{3})-[^/)]+/README\.md\)",
        r"(\1.html)",
        text,
    )
    # índice de la parte
    part_id = lesson_path.split("/")[1].split("-")[1]
    text = text.replace("(../README.md)", f"(part-{part_id}.html)")
    # raíz del programa
    text = re.sub(r"\((?:\.\./){2,3}README\.md\)", "(../index.html)", text)
    # notebooks y archivos del repo
    text = re.sub(
        r"\((notebook[^)]*\.ipynb|lab\.py|lesson\.yaml)\)",
        rf"({REPO_URL}/blob/main/{lesson_path}/\1)",
        text,
    )
    # evaluación integrada en la misma página
    text = text.replace("(assessment.md)", "(#evaluacion)")
    text = text.replace("(README.md)", "(#top)")
    # enlaces de vuelta al eje de papers, que sí tienen página propia en el sitio
    text = re.sub(
        r"\((?:\.\./)+papers/foundational/(P\d{2}_[a-z0-9_]+)/README\.md\)",
        r"(../papers/\1.html)",
        text,
    )
    text = re.sub(
        r"\((?:\.\./)+papers/guides/([A-Z0-9_]+)\.md\)",
        lambda m: "(../papers/" + guide_page(m.group(1) + ".md") + ")",
        text,
    )
    text = re.sub(
        r"\((?:\.\./)+papers/annexes/([A-Z0-9_]+)\.md\)",
        lambda m: "(../papers/" + annex_page(m.group(1) + ".md") + ")",
        text,
    )
    text = text.replace("(../../../papers/annexes/README.md)", "(../papers/anexos.html)")
    text = text.replace("(../../../papers/README.md)", "(../papers/index.html)")
    # cualquier otra referencia relativa a archivos del repo → blob de GitHub.
    # Se excluye lo que termina en `.html`: eso ya lo reescribieron las reglas de
    # arriba y es una página DEL SITIO. Sin la exclusión, este catch-all las pisaba
    # y mandaba cada paper de una clase a un blob de GitHub inexistente.
    text = re.sub(
        r"\((?:\.\./)+((?:frontier|datasets|docs|specializations|src|scripts|papers|notebooks)"
        r"/(?![^)\s]*\.html\))[^)\s]*)\)",
        rf"({REPO_URL}/blob/main/\1)",
        text,
    )
    return text


def rewrite_part_links(text: str, part_dir: str) -> str:
    part_id = part_dir.split("-")[1]
    text = re.sub(r"\((\d{3})-[^/)]+/README\.md\)", r"(\1.html)", text)
    text = re.sub(r"\(\.\./(part-(\d{2})-[^/)]+)/README\.md\)", r"(part-\2.html)", text)
    text = text.replace("(../../README.md)", "(../index.html)")
    return text


def build_class_pages(curriculum: dict, out_dir: Path) -> int:
    count = 0
    for part in curriculum["parts"]:
        part_dir = Path(part["lessons"][0]["path"]).parent.name
        part_id = part_dir.split("-")[1]

        # página de la parte
        part_md = (ROOT / "classes" / part_dir / "README.md").read_text(encoding="utf-8")
        part_md = rewrite_part_links(part_md, part_dir)
        write_lf(
            out_dir / f"part-{part_id}.html",
            PAGE_TEMPLATE.format(
                title=f"Parte {part_id} — {part['title']}",
                description=part["description"][:150],
                crumb=f"Parte {part_id}",
                body=render(part_md),
            ),
        )
        count += 1

        for lesson in part["lessons"]:
            folder = ROOT / lesson["path"]
            md = folder.joinpath("README.md").read_text(encoding="utf-8")
            assessment = folder.joinpath("assessment.md").read_text(encoding="utf-8")
            # quitar H1 y pie de navegación del assessment integrado
            assessment = re.sub(r"^\s*# .+?\n", "", assessment, count=1)
            assessment = re.sub(r"\n---\n\n> \[⬅️.*$", "", assessment, flags=re.DOTALL)
            md += (
                "\n\n---\n\n"
                '<a id="evaluacion"></a>\n\n'
                "## 📝 Evaluación completa\n\n" + assessment.strip() + "\n"
            )
            md = rewrite_class_links(md, lesson["path"])
            write_lf(
                out_dir / f"{lesson['id']}.html",
                PAGE_TEMPLATE.format(
                    title=f"{lesson['id']} — {lesson['title']}",
                    description=str(lesson.get("summary", lesson["title"]))[:150],
                    crumb=f"Clase {lesson['id']} · Parte {part_id}",
                    body=render(md),
                ),
            )
            count += 1
    return count


# --------------------------------------------------------------------------- #
# eje de papers
# --------------------------------------------------------------------------- #


def guide_page(name: str) -> str:
    """COMO_LEER_UN_PAPER_DE_IA.md → guia-como-leer-un-paper-de-ia.html"""
    return "guia-" + name.removesuffix(".md").lower().replace("_", "-") + ".html"


def annex_page(name: str) -> str:
    """A01_ALGEBRA_Y_GEOMETRIA.md → anexo-a01-algebra-y-geometria.html"""
    if name in ("README.md", "readme.md"):
        return "anexos.html"
    return "anexo-" + name.removesuffix(".md").lower().replace("_", "-") + ".html"


def paper_href(source_rel: str, target: str) -> str:
    """Traduce un enlace relativo del repositorio a su equivalente en el sitio.

    Lo que tiene página propia se enlaza dentro del sitio; el resto —notebooks,
    evaluaciones, ficheros de frontera— apunta al repositorio, que es donde vive.
    """
    if target.startswith(("http://", "https://", "mailto:")):
        return target
    path, _, anchor = target.partition("#")
    if not path:
        return target
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source_rel), path))
    suffix = f"#{anchor}" if anchor else ""

    if resolved == "papers/README.md":
        return f"index.html{suffix}"
    if resolved == "papers/ROADMAP.md":
        return f"roadmap.html{suffix}"
    if resolved == "papers/catalog/PAPERS_INDEX.md":
        return f"catalogo.html{suffix}"
    if resolved.startswith("papers/guides/"):
        return guide_page(posixpath.basename(resolved)) + suffix
    if resolved.startswith("papers/annexes/"):
        return annex_page(posixpath.basename(resolved)) + suffix
    ficha = re.fullmatch(r"papers/foundational/(P\d{2}_[a-z0-9_]+)/README\.md", resolved)
    if ficha:
        return f"{ficha.group(1)}.html{suffix}"
    lesson = re.fullmatch(r"classes/part-\d{2}-[^/]+/(\d{3})-[^/]+/README\.md", resolved)
    if lesson:
        return f"../classes/{lesson.group(1)}.html{suffix}"
    if resolved == "README.md":
        return f"../index.html{suffix}"
    return f"{REPO_URL}/blob/main/{resolved}{suffix}"


def rewrite_paper_links(text: str, source_rel: str) -> str:
    return re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f"[{m.group(1)}]({paper_href(source_rel, m.group(2))})",
        text,
    )


def paper_page(source_rel: str, out_path: Path, title: str, crumb: str, description: str) -> None:
    md_text = rewrite_paper_links((ROOT / source_rel).read_text(encoding="utf-8"), source_rel)
    write_lf(
        out_path,
        PAGE_TEMPLATE.format(
            title=title,
            description=description[:150],
            crumb=crumb,
            body=render(md_text),
        ),
    )


def build_paper_pages(out_dir: Path) -> int:
    catalog = json.loads((ROOT / "papers" / "catalog" / "papers.json").read_text(encoding="utf-8"))
    out_dir.mkdir(parents=True, exist_ok=True)
    hub = '<a href="index.html">📜 Papers</a>'
    pages = 0

    paper_page("papers/README.md", out_dir / "index.html",
               "Eje de papers fundacionales", "📜 Papers",
               "52 papers fundacionales de la IA, con fichas verificables y miniaturas ejecutables.")
    paper_page("papers/ROADMAP.md", out_dir / "roadmap.html",
               "Ruta del eje de papers", f"{hub} · Ruta",
               "Niveles L0–L5, cuatro fases y definición de terminado del eje de papers.")
    paper_page("papers/catalog/PAPERS_INDEX.md", out_dir / "catalogo.html",
               "Índice de papers", f"{hub} · Índice",
               "Tabla maestra de los 52 papers fundacionales del programa.")
    pages += 3

    for guide in sorted((ROOT / "papers" / "guides").glob("*.md")):
        paper_page(f"papers/guides/{guide.name}", out_dir / guide_page(guide.name),
                   guide.stem.replace("_", " ").capitalize(), f"{hub} · Guía",
                   "Guía de lectura crítica de papers de inteligencia artificial.")
        pages += 1

    for annex in sorted((ROOT / "papers" / "annexes").glob("*.md")):
        paper_page(f"papers/annexes/{annex.name}", out_dir / annex_page(annex.name),
                   annex.stem.replace("_", " ").capitalize(), f"{hub} · Anexo",
                   "Anexo matemático del eje de papers: explicación y ejemplo resuelto.")
        pages += 1

    for item in catalog["papers"]:
        paper_page(f"papers/foundational/{item['dir']}/README.md", out_dir / f"{item['dir']}.html",
                   f"{item['id']} — {item['title_es']}", f"{hub} · {item['id']}", item["hito"])
        pages += 1

    (ROOT / "site" / "data").mkdir(parents=True, exist_ok=True)
    write_lf(
        ROOT / "site" / "data" / "papers.json",
        json.dumps({
            "updated": catalog["updated"],
            "paper_count": len(catalog["papers"]),
            "niveles": catalog["niveles"],
            "papers": [
                {
                    "id": item["id"],
                    "page": f"{item['dir']}.html",
                    "titulo": item["title_es"],
                    "original": item["title"],
                    "autoria": item["authors"],
                    "anio": item["year"],
                    "venue": item["venue"],
                    "nivel": item["level"],
                    "motor": item["lab"],
                    "hito": item["hito"],
                    "keywords": item["keywords"],
                    "notebook": f"notebooks/papers/{item['dir']}.ipynb",
                }
                for item in catalog["papers"]
            ],
        }, ensure_ascii=False, indent=2) + "\n",
    )
    return pages


def main() -> None:
    curriculum = yaml.safe_load((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    payload = {
        "version": curriculum["version"],
        "lesson_count": sum(len(part["lessons"]) for part in curriculum["parts"]),
        "parts": curriculum["parts"],
    }
    (ROOT / "site" / "data").mkdir(parents=True, exist_ok=True)
    write_lf(
        ROOT / "site" / "data" / "catalog.json",
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    )
    out_dir = ROOT / "site" / "classes"
    out_dir.mkdir(parents=True, exist_ok=True)
    pages = build_class_pages(curriculum, out_dir)
    paper_pages = build_paper_pages(ROOT / "site" / "papers")
    print(
        f"catálogo generado: {payload['lesson_count']} clases · "
        f"páginas HTML: {pages} de clases + {paper_pages} de papers"
    )


if __name__ == "__main__":
    main()
