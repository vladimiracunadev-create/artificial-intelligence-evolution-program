
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from .catalog import REPO_ROOT, find_lesson, lessons, load_curriculum
from .labs import run_lab
from .papers import find_paper, load_papers, papers
from .papers_lab import run_paper_lab
from .validation import validate_repository


def cmd_catalog(args: argparse.Namespace) -> int:
    for part in load_curriculum()["parts"]:
        print(f"{part['id']} · {part['title']} ({len(part['lessons'])} clases)")
        if args.verbose:
            for lesson in part["lessons"]:
                print(f"  {lesson['id']} · {lesson['title']} [{lesson['lab_kind']}]")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    lesson = find_lesson(args.lesson)
    result = run_lab(lesson.lab_kind, seed=args.seed or lesson.number)
    print(json.dumps({"lesson": lesson.id, "title": lesson.title, **result}, ensure_ascii=False, indent=2))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    result = validate_repository(strict=args.strict)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


def cmd_frontier(args: argparse.Namespace) -> int:
    data = yaml.safe_load((REPO_ROOT / "frontier" / "current-topics.yaml").read_text(encoding="utf-8"))
    for item in data["topics"]:
        print(f"{item['maturity']:10} · {item['name']} · revisado {item['reviewed']}")
    return 0


def cmd_progress(args: argparse.Namespace) -> int:
    total = len(lessons())
    completed = set()
    if args.file:
        path = Path(args.file)
        if path.exists():
            completed = {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}
    print(json.dumps({"completed": len(completed), "total": total, "percentage": round(len(completed) / total * 100, 2)}, indent=2))
    return 0


def cmd_papers(args: argparse.Namespace) -> int:
    data = load_papers()
    print(f"eje de papers · {len(data['papers'])} hitos · actualizado {data['updated']}")
    for item in papers():
        print(f"{item.id} · {item.year} · {item.level:2} · {item.title_es}")
        if args.verbose:
            print(f"      motor: {item.lab} · ficha: {item.ficha_path}")
            print(f"      hito : {item.hito}")
    return 0


def cmd_paper(args: argparse.Namespace) -> int:
    paper = find_paper(args.paper)
    raw = next(item for item in load_papers()["papers"] if item["id"] == paper.id)
    print(json.dumps({
        "id": paper.id,
        "titulo": paper.title,
        "titulo_es": paper.title_es,
        "autoria": list(paper.authors),
        "anio": paper.year,
        "venue": paper.venue,
        "nivel": paper.level,
        "hito": paper.hito,
        "problema": raw["problema"],
        "propuesta": raw["propuesta"],
        "ficha": paper.ficha_path,
        "notebook": paper.notebook_path,
        "evaluacion": paper.assessment_path,
        "fuentes_primarias": raw["fuentes_primarias"],
        "consultado": raw["consultado"],
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_paper_lab(args: argparse.Namespace) -> int:
    paper = find_paper(args.paper)
    result = run_paper_lab(paper.lab, seed=args.seed or paper.year % 100)
    print(json.dumps({"paper": paper.id, "titulo": paper.title_es, **result}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-evolution", description="CLI del Artificial Intelligence Evolution Program")
    sub = parser.add_subparsers(dest="command", required=True)

    catalog = sub.add_parser("catalog")
    catalog.add_argument("--verbose", action="store_true")
    catalog.set_defaults(func=cmd_catalog)

    run = sub.add_parser("run")
    run.add_argument("lesson")
    run.add_argument("--seed", type=int)
    run.set_defaults(func=cmd_run)

    validate = sub.add_parser("validate")
    validate.add_argument("--strict", action="store_true")
    validate.set_defaults(func=cmd_validate)

    frontier = sub.add_parser("frontier")
    frontier.set_defaults(func=cmd_frontier)

    progress = sub.add_parser("progress")
    progress.add_argument("--file")
    progress.set_defaults(func=cmd_progress)

    papers_cmd = sub.add_parser("papers", help="catálogo del eje de papers fundacionales")
    papers_cmd.add_argument("--verbose", action="store_true")
    papers_cmd.set_defaults(func=cmd_papers)

    paper_cmd = sub.add_parser("paper", help="ficha resumida de un paper (P01…P16)")
    paper_cmd.add_argument("paper")
    paper_cmd.set_defaults(func=cmd_paper)

    paper_lab = sub.add_parser("paper-lab", help="ejecuta la miniatura de un paper")
    paper_lab.add_argument("paper")
    paper_lab.add_argument("--seed", type=int)
    paper_lab.set_defaults(func=cmd_paper_lab)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
