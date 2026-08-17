from __future__ import annotations

"""Genera PDFs imprimibles del programa: uno por parte, uno general y el eje de papers.

Requiere: pip install markdown PyYAML, y Chrome o Edge instalado (impresión headless).

Salida:
    docs/pdf/parte-NN.pdf (15)
    docs/pdf/programa-completo.pdf
    docs/pdf/papers-fundacionales.pdf

Uso::

    python scripts/generate_pdfs.py             # todo
    python scripts/generate_pdfs.py --papers    # solo el eje de papers
    python scripts/generate_pdfs.py --clases    # solo partes y programa completo
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "pdf"
MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
]

PRINT_CSS = """
@page { size: A4; margin: 18mm 15mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, "Times New Roman", serif; font-size: 10.5pt;
       line-height: 1.55; color: #111; margin: 0; }
h1, h2, h3, h4 { font-family: "Segoe UI", Arial, sans-serif; color: #0b2545; line-height: 1.2; }
h1 { font-size: 20pt; }
h2 { font-size: 14pt; border-bottom: 1.5px solid #0b2545; padding-bottom: 3pt; margin-top: 18pt; }
h3 { font-size: 11.5pt; margin-top: 12pt; }
pre { background: #f4f6f8; border: 0.5pt solid #ccc; border-radius: 4pt;
      padding: 8pt; font-size: 8.5pt; line-height: 1.4; overflow-x: hidden;
      white-space: pre-wrap; word-wrap: break-word; page-break-inside: avoid; }
code { font-family: Consolas, "Courier New", monospace; font-size: 0.92em;
       background: #f0f2f4; padding: 0 2pt; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9pt;
        page-break-inside: avoid; }
th, td { border: 0.5pt solid #888; padding: 3pt 6pt; text-align: left; }
th { background: #e8edf3; }
blockquote { border-left: 3pt solid #0b2545; margin: 8pt 0; padding: 4pt 10pt;
             background: #f6f8fa; color: #333; }
img { max-width: 100%; }
a { color: #0b2545; text-decoration: none; }
hr { border: none; border-top: 0.5pt solid #999; margin: 14pt 0; }
.portada { page-break-after: always; text-align: center; padding-top: 220pt; }
.portada h1 { font-size: 28pt; border: none; }
.portada .sub { font-size: 13pt; color: #444; margin-top: 10pt; }
.clase { page-break-before: always; }
pre.mermaid { background: #fff; border: none; text-align: center; }
pre.mermaid svg { max-width: 100%; height: auto; }
"""

MERMAID_JS = """
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
  document.querySelectorAll("pre > code.language-mermaid").forEach(code => {
    const div = document.createElement("pre");
    div.className = "mermaid";
    div.textContent = code.textContent;
    code.parentElement.replaceWith(div);
  });
  await mermaid.run({ querySelector: "pre.mermaid" });
  document.title = "MERMAID_READY";
</script>
"""


def find_browser() -> str:
    for candidate in BROWSERS:
        if Path(candidate).exists():
            return candidate
    raise SystemExit("no se encontró Chrome/Edge para imprimir PDF")


def strip_nav(md_text: str) -> str:
    # nav superior y pies de navegación no aportan en papel
    md_text = re.sub(r"^> (Inicio del programa|\[← Clase anterior\]|\[⬅️).*\n", "", md_text, flags=re.MULTILINE)
    md_text = re.sub(r"\n---\n\n## ⬅️ Clase anterior.*$", "", md_text, flags=re.DOTALL)
    md_text = re.sub(r"\n---\n\n> \[⬅️.*$", "", md_text, flags=re.DOTALL)
    # los enlaces relativos no funcionan en papel: dejar solo el texto
    md_text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", md_text)
    return md_text


def render_class(folder: Path) -> str:
    readme = strip_nav(folder.joinpath("README.md").read_text(encoding="utf-8"))
    assessment = strip_nav(folder.joinpath("assessment.md").read_text(encoding="utf-8"))
    assessment = re.sub(r"^\s*# .+?\n", "", assessment, count=1)
    combined = readme + "\n\n## 📝 Evaluación completa\n\n" + assessment
    return '<div class="clase">' + markdown.markdown(combined, extensions=MD_EXTENSIONS) + "</div>"


def build_part_html(part: dict, part_id: str) -> str:
    lessons_list = "".join(
        f"<li>{lesson['id']} — {lesson['title']}</li>" for lesson in part["lessons"]
    )
    cover = (
        f'<div class="portada"><h1>🧠 AI Evolution Program</h1>'
        f'<p class="sub">Parte {part_id} — {part["title"]}</p>'
        f'<p class="sub">{part["description"]}</p>'
        f'<ol style="text-align:left; max-width: 420pt; margin: 30pt auto 0; font-size: 10pt;">{lessons_list}</ol></div>'
    )
    body = cover + "".join(render_class(ROOT / lesson["path"]) for lesson in part["lessons"])
    return html_page(f"Parte {part_id} — {part['title']}", body)


def html_page(title: str, body: str) -> str:
    return (
        f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
        f"<title>{title}</title><style>{PRINT_CSS}</style></head>"
        f"<body>{body}{MERMAID_JS}</body></html>"
    )


def print_pdf(browser: str, html_path: Path, pdf_path: Path) -> None:
    subprocess.run(
        [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=90000",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
        capture_output=True,
        timeout=600,
    )
    if not pdf_path.exists() or pdf_path.stat().st_size < 10_000:
        raise SystemExit(f"PDF sospechosamente pequeño o ausente: {pdf_path}")


def strip_paper_nav(md_text: str) -> str:
    """Como strip_nav, más el pie de navegación propio de las fichas de papers."""
    md_text = re.sub(r"\n---\n+\[⬅️.*$", "", md_text, flags=re.DOTALL)
    md_text = re.sub(r"\n---\n+\[📇.*$", "", md_text, flags=re.DOTALL)
    return strip_nav(md_text)


def render_paper_doc(rel: str, *, drop_h1: bool = False) -> str:
    text = strip_paper_nav((ROOT / rel).read_text(encoding="utf-8"))
    if drop_h1:
        text = re.sub(r"^\s*# .+?\n", "", text, count=1)
    return '<div class="clase">' + markdown.markdown(text, extensions=MD_EXTENSIONS) + "</div>"


def build_papers_html() -> str:
    catalog = json.loads((ROOT / "papers" / "catalog" / "papers.json").read_text(encoding="utf-8"))
    items = "".join(
        f"<li>{item['id']} — {item['title_es']} ({item['year']})</li>" for item in catalog["papers"]
    )
    cover = (
        '<div class="portada"><h1>📜 Papers fundacionales de la IA</h1>'
        '<p class="sub">Artificial Intelligence Evolution Program · eje transversal</p>'
        f'<p class="sub">{len(catalog["papers"])} hitos · de Rosenblatt (1958) a los sistemas agentic · '
        f'actualizado {catalog["updated"]}</p>'
        '<p class="sub" style="font-size:10pt; margin-top:18pt;">Este documento enlaza a las fuentes '
        'primarias; no las reproduce. Los notebooks ejecutables viven en el repositorio.</p>'
        f'<ol style="text-align:left; max-width: 440pt; margin: 24pt auto 0; font-size: 9.5pt;">{items}</ol></div>'
    )

    body = [cover, render_paper_doc("papers/README.md"), render_paper_doc("papers/ROADMAP.md")]
    for guide in sorted((ROOT / "papers" / "guides").glob("*.md")):
        body.append(render_paper_doc(f"papers/guides/{guide.name}"))
    for item in catalog["papers"]:
        body.append(render_paper_doc(f"papers/foundational/{item['dir']}/README.md"))
        body.append(
            '<div class="clase"><h1>📝 Evaluación — ' + item["id"] + "</h1>"
            + markdown.markdown(
                strip_paper_nav(
                    re.sub(
                        r"^\s*# .+?\n", "",
                        (ROOT / "assessments" / "papers" / f"{item['dir']}.md").read_text(encoding="utf-8"),
                        count=1,
                    )
                ),
                extensions=MD_EXTENSIONS,
            )
            + "</div>"
        )
    return html_page("Papers fundacionales de la IA", "".join(body))


def build_papers_pdf(browser: str, tmp: Path) -> None:
    html_path = tmp / "papers-fundacionales.html"
    html_path.write_text(build_papers_html(), encoding="utf-8")
    pdf_path = OUT_DIR / "papers-fundacionales.pdf"
    print_pdf(browser, html_path, pdf_path)
    print(f"papers-fundacionales.pdf → {pdf_path.stat().st_size // 1024} kB")


def build_paper_pdfs(browser: str, tmp: Path) -> None:
    """Un PDF por paper: ficha + su evaluación, para leer o imprimir suelto."""
    catalog = json.loads((ROOT / "papers" / "catalog" / "papers.json").read_text(encoding="utf-8"))
    destino = OUT_DIR / "papers"
    destino.mkdir(parents=True, exist_ok=True)
    for item in catalog["papers"]:
        portada = (
            f'<div class="portada"><h1>{item["id"]}</h1>'
            f'<p class="sub">{item["title_es"]}</p>'
            f'<p class="sub" style="font-size:11pt;">{item["title"]}</p>'
            f'<p class="sub" style="font-size:10pt;">{", ".join(item["authors"])} · '
            f'{item["year"]} · {item["venue"]}</p>'
            f'<p class="sub" style="font-size:9.5pt; margin-top:24pt;">'
            f'Ficha pedagógica del Artificial Intelligence Evolution Program. '
            f'No es el paper original: es una guía de lectura en español que enlaza a la fuente '
            f'primaria. Consultado {item["consultado"]}.</p></div>'
        )
        cuerpo = portada + render_paper_doc(f"papers/foundational/{item['dir']}/README.md")
        evaluacion = ROOT / "assessments" / "papers" / f"{item['dir']}.md"
        if evaluacion.exists():
            cuerpo += render_paper_doc(f"assessments/papers/{item['dir']}.md")
        html_path = tmp / f"{item['dir']}.html"
        html_path.write_text(html_page(f"{item['id']} — {item['title_es']}", cuerpo), encoding="utf-8")
        pdf_path = destino / f"{item['dir']}.pdf"
        print_pdf(browser, html_path, pdf_path)
        print(f"  {item['id']} → {pdf_path.stat().st_size // 1024} kB")
    print(f"PDFs individuales: {len(catalog['papers'])} en {destino.relative_to(ROOT).as_posix()}/")


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera los PDFs imprimibles del programa")
    parser.add_argument("--papers", action="store_true", help="solo el eje de papers")
    parser.add_argument("--clases", action="store_true", help="solo partes y programa completo")
    parser.add_argument("--por-paper", action="store_true", help="un PDF por paper, en docs/pdf/papers/")
    args = parser.parse_args()
    hacer_clases = args.clases or not (args.papers or args.por_paper)
    hacer_papers = args.papers or not (args.clases or args.por_paper)

    curriculum = yaml.safe_load((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    browser = find_browser()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="ai-evolution-pdf-"))

    if args.por_paper:
        build_paper_pdfs(browser, tmp)
    if hacer_papers:
        build_papers_pdf(browser, tmp)
    if not hacer_clases:
        return

    all_bodies: list[str] = []
    for part in curriculum["parts"]:
        part_dir = Path(part["lessons"][0]["path"]).parent.name
        part_id = part_dir.split("-")[1]
        html = build_part_html(part, part_id)
        html_path = tmp / f"parte-{part_id}.html"
        html_path.write_text(html, encoding="utf-8")
        pdf_path = OUT_DIR / f"parte-{part_id}.pdf"
        print_pdf(browser, html_path, pdf_path)
        print(f"parte-{part_id}.pdf → {pdf_path.stat().st_size // 1024} kB")
        all_bodies.append(html.split("<body>", 1)[1].rsplit("<script", 1)[0])

    cover = (
        '<div class="portada"><h1>🧠 Artificial Intelligence Evolution Program</h1>'
        '<p class="sub">15 partes · 183 clases · de la IA simbólica a los sistemas agénticos</p>'
        '<p class="sub">Programa completo — materia, ejemplos trabajados y evaluaciones</p></div>'
    )
    general = html_page("AI Evolution Program — completo", cover + "".join(all_bodies))
    general_path = tmp / "programa-completo.html"
    general_path.write_text(general, encoding="utf-8")
    pdf_general = OUT_DIR / "programa-completo.pdf"
    print_pdf(browser, general_path, pdf_general)
    print(f"programa-completo.pdf → {pdf_general.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
