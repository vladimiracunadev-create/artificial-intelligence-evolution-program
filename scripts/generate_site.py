from __future__ import annotations

import json
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
    # cualquier otra referencia relativa a archivos del repo → blob de GitHub
    text = re.sub(
        r"\((?:\.\./)+((?:frontier|datasets|docs|specializations|src|scripts)/[^)\s]*)\)",
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
        (out_dir / f"part-{part_id}.html").write_text(
            PAGE_TEMPLATE.format(
                title=f"Parte {part_id} — {part['title']}",
                description=part["description"][:150],
                crumb=f"Parte {part_id}",
                body=render(part_md),
            ),
            encoding="utf-8",
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
            (out_dir / f"{lesson['id']}.html").write_text(
                PAGE_TEMPLATE.format(
                    title=f"{lesson['id']} — {lesson['title']}",
                    description=str(lesson.get("summary", lesson["title"]))[:150],
                    crumb=f"Clase {lesson['id']} · Parte {part_id}",
                    body=render(md),
                ),
                encoding="utf-8",
            )
            count += 1
    return count


def main() -> None:
    curriculum = yaml.safe_load((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    payload = {
        "version": curriculum["version"],
        "lesson_count": sum(len(part["lessons"]) for part in curriculum["parts"]),
        "parts": curriculum["parts"],
    }
    (ROOT / "site" / "data").mkdir(parents=True, exist_ok=True)
    (ROOT / "site" / "data" / "catalog.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    out_dir = ROOT / "site" / "classes"
    out_dir.mkdir(parents=True, exist_ok=True)
    pages = build_class_pages(curriculum, out_dir)
    print(f"catálogo generado: {payload['lesson_count']} clases · páginas HTML: {pages}")


if __name__ == "__main__":
    main()
