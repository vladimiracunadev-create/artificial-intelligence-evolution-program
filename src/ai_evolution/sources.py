"""Registro general de fuentes del programa.

Este módulo contiene la lógica compartida por `scripts/verify-sources`
(offline, determinista, bloquea CI) y `scripts/refresh-sources`
(en red, manual, no bloquea).

Reglas del registro (`sources/bibliography.json`):

* toda afirmación del programa se apoya en una entrada del registro;
* ninguna entrada se acepta sin localizador verificable;
* lo que no resuelve se marca `pendiente`, nunca se borra ni se inventa.

La extracción de fuentes usadas es determinista: se lee el bloque
`## 🔗 Referencias` de cada clase y de cada ítem se derivan dos facetas,
que son las mismas dos que produce la medición de línea base:

* `url`  — cada enlace http(s) del ítem, normalizado;
* `obra` — cada título en cursiva del ítem, normalizado.
"""

from __future__ import annotations

import json
import re
import unicodedata
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "sources" / "bibliography.json"
CLASSES_GLOB = "classes/*/*/README.md"
REF_HEADING = "## 🔗 Referencias"

SCHEMA_VERSION = 1

#: Tipos admitidos en el registro.
TYPES = ("book", "paper", "standard", "reference", "dataset")

#: Estados admitidos.
STATUSES = ("verificada", "pendiente")

#: Vocabulario controlado con el que cada clase declara el uso de una fuente.
#: Es mecánico a propósito: describe la función de la fuente en la clase.
#: Un motivo redactado por fuente y clase habría que inventarlo, y este
#: repositorio no inventa aparato crítico.
USE_ROLES = {
    "paper": "fuente primaria del mecanismo estudiado",
    "book": "desarrollo extendido del tema",
    "standard": "marco normativo de referencia",
    "reference": "referencia consultada en su fuente original",
    "dataset": "datos de referencia",
}

USE_MARK = "uso:"

#: Marcadores del bloque de cifras del README, que escribe el verificador.
README_BEGIN = "<!-- sources:inicio -->"
README_END = "<!-- sources:fin -->"

#: Insignia del registro (la del eje de papers vive aparte y no se toca).
BADGE_BEGIN = "<!-- sources-badge:inicio -->"
BADGE_END = "<!-- sources-badge:fin -->"


# --------------------------------------------------------------------------
# normalización
# --------------------------------------------------------------------------
def normalize_url_key(url: str) -> str:
    """Clave canónica de un enlace: sin esquema, sin `www.`, sin query.

    Se decodifican los escapes `%NN` para que `10.1016/0004-3702%2890%29…` y
    `10.1016/0004-3702(90)…` sean la misma fuente, y se compara en minúsculas.
    La clave sirve para casar citas; el localizador conserva la URL original.
    """
    key = url.strip().strip("<>").rstrip(".,;")
    key = re.sub(r"^https?://", "", key)
    key = re.sub(r"^www\.", "", key)
    key = key.split("#")[0].split("?")[0]
    return urllib.parse.unquote(key).rstrip("/").lower()


def normalize_work_key(work: str) -> str:
    """Clave canónica de una obra citada en cursiva."""
    key = re.sub(r"\s+", " ", work).strip()
    key = key.strip(" .,:;·—-")
    return key.lower()


def strip_accents(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text) if unicodedata.category(ch) != "Mn"
    )


def normalize_title(title: str) -> str:
    """Título comparable: sin acentos, sin puntuación, en minúsculas."""
    plain = strip_accents(title).lower()
    plain = re.sub(r"[^a-z0-9]+", " ", plain)
    return " ".join(plain.split())


def slugify(text: str, limit: int = 60) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", strip_accents(text).lower()).strip("-")
    if len(slug) > limit:
        slug = slug[:limit].rstrip("-")
    return slug or "sin-titulo"


# --------------------------------------------------------------------------
# localizadores
# --------------------------------------------------------------------------
def isbn13_is_valid(isbn: str) -> bool:
    """Dígito de control ISBN-13 (norma ISO 2108)."""
    digits = re.sub(r"[^0-9]", "", isbn or "")
    if len(digits) != 13 or not digits.startswith(("978", "979")):
        return False
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits[:12]))
    return (10 - total % 10) % 10 == int(digits[12])


DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


def doi_is_wellformed(doi: str) -> bool:
    return bool(doi and DOI_RE.match(doi.strip()))


def book_locator(isbn13: str) -> str:
    return f"https://openlibrary.org/isbn/{isbn13}"


def paper_locator(doi: str) -> str:
    return f"https://doi.org/{doi}"


def arxiv_doi(arxiv_id: str) -> str | None:
    """DOI que arXiv registra para cada artículo (`10.48550/arXiv.<id>`).

    Solo se aplica al identificador moderno `AAMM.NNNNN`; los identificadores
    antiguos (`cs/0301001`) quedan sin DOI derivado y la entrada nace pendiente.
    """
    if re.match(r"^\d{4}\.\d{4,5}$", arxiv_id):
        return f"10.48550/arXiv.{arxiv_id}"
    return None


# --------------------------------------------------------------------------
# extracción de fuentes usadas en las clases
# --------------------------------------------------------------------------
#: Enlace de markdown, tolerando paréntesis equilibrados dentro de la URL:
#: los DOI antiguos de Elsevier los llevan (`10.1016/0004-3702(75)90019-3`).
MD_URL_RE = re.compile(r"\[[^\]]*\]\((https?://(?:[^\s()]|\([^\s()]*\))*)\)")
ANGLE_URL_RE = re.compile(r"<(https?://[^>\s]+)>")
BARE_URL_RE = re.compile(r"https?://[^\s)>\]]+")
URL_RE = BARE_URL_RE  # compatibilidad con los usos sueltos
WORK_RE = re.compile(r"\*([^*]{4,}?)\*")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]*(?:\([^)]*\)[^)]*)*)\)")


def extract_urls(text: str) -> list[str]:
    """Todas las URL de una cita, sin trocear las que llevan paréntesis."""
    urls = [match.group(1) for match in MD_URL_RE.finditer(text)]
    rest = MD_URL_RE.sub("[·](·)", text)
    urls.extend(match.group(1) for match in ANGLE_URL_RE.finditer(rest))
    rest = ANGLE_URL_RE.sub("<·>", rest)
    urls.extend(BARE_URL_RE.findall(rest))
    return urls


@dataclass
class RefItem:
    """Un ítem del bloque de referencias de una clase."""

    class_path: str
    line_no: int
    text: str
    urls: list[str] = field(default_factory=list)
    works: list[str] = field(default_factory=list)

    @property
    def url_keys(self) -> list[str]:
        return [normalize_url_key(u) for u in self.urls]

    @property
    def work_keys(self) -> list[str]:
        return [normalize_work_key(w) for w in self.works]

    @property
    def declares_use(self) -> bool:
        """¿El ítem declara para qué usa la clase esa fuente?"""
        if USE_MARK in self.text:
            return True
        tail = ""
        match = list(MD_LINK_RE.finditer(self.text))
        if match:
            tail = self.text[match[-1].end() :]
        elif "—" in self.text:
            tail = self.text.rsplit("—", 1)[1]
        return len(tail.strip(" .·—-*_")) > 8


def class_files(root: Path = ROOT) -> list[Path]:
    return sorted(root.glob(CLASSES_GLOB))


def reference_block(text: str) -> str | None:
    match = re.search(
        rf"^{re.escape(REF_HEADING)}\s*$(.*?)(?=^## |^<!-- papers:inicio -->|\Z)",
        text,
        re.S | re.M,
    )
    return match.group(1) if match else None


def extract_items(root: Path = ROOT) -> list[RefItem]:
    """Todos los ítems de referencias de todas las clases, en orden estable."""
    items: list[RefItem] = []
    for path in class_files(root):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        block = reference_block(text)
        if block is None:
            continue
        offset = text[: text.index(REF_HEADING)].count("\n") + 1
        for number, raw in enumerate(block.splitlines(), start=1):
            line = raw.strip()
            if not line.startswith("- "):
                continue
            body = line[2:].strip()
            items.append(
                RefItem(
                    class_path=rel,
                    line_no=offset + number,
                    text=body,
                    urls=extract_urls(body),
                    works=WORK_RE.findall(body),
                )
            )
    return items


def used_keys(items: Iterable[RefItem]) -> tuple[dict[str, int], dict[str, int]]:
    """Devuelve (usos por clave de enlace, usos por clave de obra)."""
    urls: dict[str, int] = {}
    works: dict[str, int] = {}
    for item in items:
        for key in item.url_keys:
            urls[key] = urls.get(key, 0) + 1
        for key in item.work_keys:
            works[key] = works.get(key, 0) + 1
    return urls, works


# --------------------------------------------------------------------------
# registro
# --------------------------------------------------------------------------
def load_registry(path: Path = REGISTRY_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_registry(registry: dict, path: Path = REGISTRY_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def registry_keys(registry: dict) -> tuple[set[str], set[str]]:
    """Claves de enlace y de obra que cubre el registro."""
    urls: set[str] = set()
    works: set[str] = set()
    for entry in registry.get("entries", []):
        urls.update(normalize_url_key(u) for u in entry.get("url_keys", []))
        works.update(normalize_work_key(w) for w in entry.get("aliases", []))
        container = entry.get("container")
        if container:
            works.add(normalize_work_key(container))
    return urls, works


def registry_stats(registry: dict, items: list[RefItem] | None = None) -> dict:
    """Cifras del registro. Son las únicas que puede mostrar el README."""
    entries = registry.get("entries", [])
    by_type: dict[str, int] = {}
    for entry in entries:
        by_type[entry["type"]] = by_type.get(entry["type"], 0) + 1
    verified = sum(1 for e in entries if e.get("status") == "verificada")
    pending = sum(1 for e in entries if e.get("status") == "pendiente")
    items = items if items is not None else extract_items()
    url_uses, work_uses = used_keys(items)
    covered_urls, covered_works = registry_keys(registry)
    used_total = len(url_uses) + len(work_uses)
    covered_total = sum(1 for k in url_uses if k in covered_urls) + sum(
        1 for k in work_uses if k in covered_works
    )
    return {
        "entries": len(entries),
        "by_type": dict(sorted(by_type.items())),
        "verified": verified,
        "pending": pending,
        "classes": len({i.class_path for i in items}),
        "citations": len(items),
        "used_sources": used_total,
        "used_links": len(url_uses),
        "used_works": len(work_uses),
        "covered_sources": covered_total,
        "coverage_pct": round(100.0 * covered_total / used_total, 1) if used_total else 0.0,
        "with_isbn": sum(1 for e in entries if e.get("isbn13")),
        "with_doi": sum(1 for e in entries if e.get("doi")),
        "verified_on": registry.get("verified_on"),
    }


# --------------------------------------------------------------------------
# verificación offline
# --------------------------------------------------------------------------
REQUIRED_FIELDS = ("id", "type", "title", "status", "used_in")


def _check_schema(registry: dict, problems: list[str]) -> None:
    if registry.get("schema_version") != SCHEMA_VERSION:
        problems.append(
            f"schema_version debe ser {SCHEMA_VERSION}, es {registry.get('schema_version')!r}"
        )
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(registry.get("verified_on", ""))):
        problems.append("verified_on ausente o sin formato AAAA-MM-DD")
    if not registry.get("policy"):
        problems.append("falta la política del registro")
    if not isinstance(registry.get("entries"), list):
        problems.append("entries debe ser una lista")


def _check_entries(registry: dict, class_paths: set[str], problems: list[str]) -> None:
    seen_ids: set[str] = set()
    for entry in registry.get("entries", []):
        eid = entry.get("id", "<sin id>")
        for field_name in REQUIRED_FIELDS:
            if not entry.get(field_name):
                problems.append(f"{eid}: falta el campo obligatorio {field_name}")
        if eid in seen_ids:
            problems.append(f"{eid}: id duplicado")
        seen_ids.add(eid)
        if not re.match(r"^[a-z0-9][a-z0-9-]*$", str(eid)):
            problems.append(f"{eid}: el id no es kebab-case estable")
        if entry.get("type") not in TYPES:
            problems.append(f"{eid}: tipo {entry.get('type')!r} fuera de {TYPES}")
        if entry.get("status") not in STATUSES:
            problems.append(f"{eid}: estado {entry.get('status')!r} fuera de {STATUSES}")
        for path in entry.get("used_in", []):
            if path not in class_paths:
                problems.append(f"{eid}: used_in apunta a una clase inexistente ({path})")
        if not entry.get("used_in"):
            problems.append(f"{eid}: entrada sin uso en ninguna clase")
        if entry.get("status") == "pendiente":
            if not entry.get("pending_reason"):
                problems.append(f"{eid}: pendiente sin motivo declarado")
            continue
        _check_locator(entry, problems)


def _check_locator(entry: dict, problems: list[str]) -> None:
    """Reglas de localizador para entradas verificadas."""
    eid = entry["id"]
    etype = entry.get("type")
    locator = entry.get("locator", "")
    if etype == "book":
        isbn = entry.get("isbn13", "")
        if not isbn13_is_valid(isbn):
            problems.append(f"{eid}: ISBN-13 inválido o ausente ({isbn!r})")
        elif locator != book_locator(isbn):
            problems.append(f"{eid}: el locator de un libro debe ser {book_locator(isbn)}")
    elif etype == "paper":
        doi = entry.get("doi", "")
        if not doi_is_wellformed(doi):
            problems.append(f"{eid}: DOI ausente o mal formado ({doi!r})")
        elif locator != paper_locator(doi):
            problems.append(f"{eid}: el locator de un artículo debe ser {paper_locator(doi)}")
    else:
        if not locator.startswith("https://"):
            problems.append(f"{eid}: {etype} verificada necesita URL https de la fuente primaria")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(entry.get("accessed", ""))):
            problems.append(f"{eid}: {etype} verificada necesita fecha de consulta (accessed)")
        if not entry.get("authority"):
            problems.append(f"{eid}: {etype} verificada necesita organismo responsable")


def _check_coverage(registry: dict, items: list[RefItem], problems: list[str]) -> None:
    url_uses, work_uses = used_keys(items)
    covered_urls, covered_works = registry_keys(registry)
    missing_urls = sorted(k for k in url_uses if k not in covered_urls)
    missing_works = sorted(k for k in work_uses if k not in covered_works)
    for key in missing_urls[:20]:
        problems.append(f"enlace usado y no registrado: {key}")
    if len(missing_urls) > 20:
        problems.append(f"... y {len(missing_urls) - 20} enlaces usados más sin registrar")
    for key in missing_works[:20]:
        problems.append(f"obra usada y no registrada: {key}")
    if len(missing_works) > 20:
        problems.append(f"... y {len(missing_works) - 20} obras usadas más sin registrar")

    used_urls_all, used_works_all = set(url_uses), set(work_uses)
    for entry in registry.get("entries", []):
        keys = {normalize_url_key(u) for u in entry.get("url_keys", [])}
        aliases = {normalize_work_key(w) for w in entry.get("aliases", [])}
        container = entry.get("container")
        if container:
            aliases.add(normalize_work_key(container))
        if not (keys & used_urls_all) and not (aliases & used_works_all):
            problems.append(f"{entry.get('id')}: entrada del registro que ninguna clase usa")


def _check_class_blocks(items: list[RefItem], root: Path, problems: list[str]) -> None:
    blocks: dict[str, str] = {}
    for path in class_files(root):
        rel = path.relative_to(root).as_posix()
        block = reference_block(path.read_text(encoding="utf-8"))
        if block is None:
            problems.append(f"{rel}: sin bloque «{REF_HEADING}»")
            continue
        signature = "\n".join(
            sorted(l.strip() for l in block.splitlines() if l.strip().startswith("- "))
        )
        if signature in blocks:
            problems.append(f"{rel}: bloque de fuentes idéntico al de {blocks[signature]}")
        else:
            blocks[signature] = rel
    for item in items:
        if not item.declares_use:
            problems.append(
                f"{item.class_path}:{item.line_no}: la fuente no declara el uso que la clase hace de ella"
            )


#: Ruta del mapa de manuales por parte y de la bibliografía legible.
SUPPORT_MAP_PATH = ROOT / "sources" / "support_map.json"
BIBLIOGRAPHY_MD = ROOT / "sources" / "BIBLIOGRAFIA.md"

#: Marcadores del bloque de bibliografía de apoyo dentro de cada clase.
CLASS_BEGIN = "<!-- bibliografia:inicio -->"
CLASS_END = "<!-- bibliografia:fin -->"

CHAPTER_RE = re.compile(
    r"\b(caps?\.\s*[0-9IVXivx]+(?:\s*[-–ay]+\s*[0-9IVXivx]+)*"
    r"|capítulos?\s*[0-9IVXivx]+(?:\s*[-–ay]+\s*[0-9IVXivx]+)*)",
    re.I,
)


def load_support_map(root: Path = ROOT) -> dict:
    return json.loads((root / "sources" / "support_map.json").read_text(encoding="utf-8"))


def part_of(class_path: str) -> str:
    match = re.search(r"classes/part-(\d\d)", class_path)
    return match.group(1) if match else ""


def entries_by_id(registry: dict) -> dict[str, dict]:
    return {entry["id"]: entry for entry in registry.get("entries", [])}


def lookup_index(registry: dict) -> tuple[dict[str, dict], dict[str, dict]]:
    """Índices clave→entrada para casar una cita con su entrada del registro."""
    by_url: dict[str, dict] = {}
    by_work: dict[str, dict] = {}
    for entry in registry.get("entries", []):
        for key in entry.get("url_keys", []):
            by_url.setdefault(normalize_url_key(key), entry)
        for key in entry.get("aliases", []):
            by_work.setdefault(normalize_work_key(key), entry)
    return by_url, by_work


def entry_for_item(item: RefItem, by_url: dict, by_work: dict) -> dict | None:
    for key in item.url_keys:
        if key in by_url:
            return by_url[key]
    for key in item.work_keys:
        if key in by_work:
            return by_work[key]
    return None


def format_authors(entry: dict) -> str:
    authors = entry.get("authors") or []
    if not authors:
        # sin autoría resuelta se cita la editorial, nunca el dominio de la web
        authority = entry.get("authority") or ""
        return "" if re.match(r"^[\w.-]+\.[a-z]{2,}$", authority) else authority
    if len(authors) > 3:
        return f"{authors[0]} et al."
    if len(authors) == 1:
        return authors[0]
    return f"{', '.join(authors[:-1])} y {authors[-1]}"


def format_work(entry: dict) -> str:
    """«Autores — *Título*», que es como se cita una obra, no un identificador."""
    authors = format_authors(entry)
    title = entry.get("title") or entry["id"]
    return f"{authors} — *{title}*" if authors else f"*{title}*"


def format_edition(entry: dict) -> str:
    bits = [entry.get("edition"), entry.get("published")]
    return " · ".join(str(bit) for bit in bits if bit) or "—"


def format_locator(entry: dict) -> str:
    """Localizador legible: ISBN o DOI enlazado, más la web de la obra si la hay."""
    parts = []
    if entry.get("isbn13"):
        parts.append(f"[ISBN {entry['isbn13']}](https://openlibrary.org/isbn/{entry['isbn13']})")
    elif entry.get("doi"):
        parts.append(f"[DOI {entry['doi']}](https://doi.org/{entry['doi']})")
    elif entry.get("locator"):
        parts.append(f"[fuente primaria]({entry['locator']})")
    if entry.get("homepage"):
        parts.append(f"[web de la obra]({entry['homepage']})")
    if entry.get("status") == "pendiente":
        # el dígito de control se comprueba sin red; lo que falta es la ficha
        parts.append(
            "_pendiente de confirmar en su catálogo_" if parts else "_sin localizador verificado_"
        )
    return " · ".join(parts) or "—"


def chapter_note(text: str) -> str:
    match = CHAPTER_RE.search(text)
    return match.group(1).strip() if match else ""


def class_bibliography(registry: dict, support: dict, items: list[RefItem]) -> dict[str, dict]:
    """Para cada clase: los libros que cita y el manual de referencia de su parte.

    Los papers dicen de dónde salió el mecanismo; esto dice con qué obra se
    estudia. Nada se escribe a mano: sale del registro y del mapa de apoyo.
    """
    by_url, by_work = lookup_index(registry)
    by_id = entries_by_id(registry)
    citado: dict[str, dict[str, str]] = {}
    normas: dict[str, list[dict]] = {}
    for item in items:
        entry = entry_for_item(item, by_url, by_work)
        if entry is None:
            continue
        if entry["type"] == "book":
            note = chapter_note(item.text)
            previo = citado.setdefault(item.class_path, {})
            if entry["id"] not in previo or (note and not previo[entry["id"]]):
                previo[entry["id"]] = note
        elif entry["type"] == "standard":
            lista = normas.setdefault(item.class_path, [])
            if entry not in lista:
                lista.append(entry)

    resultado: dict[str, dict] = {}
    for path in sorted({item.class_path for item in items}):
        filas: list[dict] = []
        vistos: set[str] = set()
        parte = part_of(path)
        manuales = {m["id"]: m for m in support.get("parts", {}).get(parte, [])}
        for entry_id, note in sorted(citado.get(path, {}).items()):
            entry = by_id.get(entry_id)
            if entry is None:
                continue
            papel = "citada en las referencias de esta clase"
            if note:
                papel += f" · {note}"
            if entry_id in manuales:
                papel += f" · obra de referencia de la parte {parte}"
            filas.append({"entry": entry, "papel": papel})
            vistos.add(entry_id)
        for manual in manuales.values():
            if manual["id"] in vistos:
                continue
            entry = by_id.get(manual["id"])
            if entry is None:
                continue
            filas.append(
                {
                    "entry": entry,
                    "papel": f"obra de referencia de la parte {parte} · {manual['scope']}",
                }
            )
            vistos.add(manual["id"])
        resultado[path] = {"obras": filas, "normas": normas.get(path, [])}
    return resultado


def class_block(datos: dict) -> str:
    """Bloque de bibliografía de apoyo que se inserta en el README de una clase."""
    filas = "\n".join(
        f"| {format_work(fila['entry'])} | {format_edition(fila['entry'])} "
        f"| {format_locator(fila['entry'])} | {fila['papel']} |"
        for fila in datos["obras"]
    )
    normas = ""
    if datos["normas"]:
        enlaces = " · ".join(
            f"[{norma.get('title') or norma['id']}]({norma.get('locator')})"
            for norma in datos["normas"][:5]
        )
        normas = f"\n**Normas y documentación oficial que aplica esta clase:** {enlaces}\n"
    return (
        f"{CLASS_BEGIN}\n"
        "\n---\n\n"
        "## 📚 Bibliografía de apoyo\n\n"
        "> Bloque generado por `python scripts/link_sources_to_classes.py`. Cada obra lleva su "
        "localizador verificado en "
        "[`sources/bibliography.json`](../../../sources/bibliography.json).\n\n"
        "Los papers dicen **de dónde salió** el mecanismo. Estas obras lo **desarrollan** con el "
        "espacio que una clase no tiene: teoría completa, demostraciones y ejercicios.\n\n"
        "| Obra | Edición | Localizador | Papel en esta clase |\n"
        "|---|---|---|---|\n"
        f"{filas}\n"
        f"{normas}"
        f"{CLASS_END}"
    )


def part_titles(root: Path = ROOT) -> dict[str, str]:
    """Títulos de las 15 partes, leídos de `curriculum.yaml` sin dependencias."""
    texto = (root / "curriculum.yaml").read_text(encoding="utf-8")
    titulos: dict[str, str] = {}
    actual = None
    for linea in texto.splitlines():
        marca = re.match(r"\s*-?\s*id:\s*['\"]?(\d\d)['\"]?\s*$", linea)
        if marca:
            actual = marca.group(1)
            continue
        titulo = re.match(r"\s*title:\s*(.+?)\s*$", linea)
        if titulo and actual and actual not in titulos:
            titulos[actual] = titulo.group(1).strip("'\"")
    return titulos


def readme_block(registry: dict, support: dict, root: Path = ROOT) -> str:
    """Bloque del README: qué obra sostiene cada parte. Sin contadores."""
    by_id = entries_by_id(registry)
    titulos = part_titles(root)
    filas = []
    for parte, manuales in sorted(support.get("parts", {}).items()):
        obras = []
        for manual in manuales:
            entry = by_id.get(manual["id"])
            if entry:
                obras.append(f"{format_work(entry)} — {format_locator(entry)}")
        filas.append(f"| **{parte}** · {titulos.get(parte, '')} | " + "<br>".join(obras) + " |")
    return "\n".join(
        [README_BEGIN, "", "| Parte | Obra que la sostiene |", "|---|---|", *filas, "", README_END]
    )


def badge_block(stats: dict) -> str:
    return (
        f"{BADGE_BEGIN}\n"
        "[![Bibliografía](https://img.shields.io/badge/bibliograf%C3%ADa-"
        "libros%20%C2%B7%20normas%20%C2%B7%20documentaci%C3%B3n-0b7285?style=for-the-badge)]"
        "(sources/BIBLIOGRAFIA.md)\n"
        f"{BADGE_END}"
    )


def bibliography_md(registry: dict, support: dict, items: list[RefItem], stats: dict) -> str:
    """`sources/BIBLIOGRAFIA.md`: la bibliografía legible, generada del registro."""
    by_id = entries_by_id(registry)
    titulos = part_titles()
    por_clase = class_bibliography(registry, support, items)
    lineas = [
        "# 📚 Bibliografía de apoyo del programa",
        "",
        "> Fichero generado por `python scripts/verify-sources --write` desde",
        "> [`bibliography.json`](bibliography.json) y [`support_map.json`](support_map.json).",
        "> No se edita a mano.",
        "",
        "Los [papers fundacionales](../papers/README.md) dicen **de dónde salió** cada idea.",
        "Esta bibliografía dice **con qué se estudia**: la obra que desarrolla el contenido de",
        "cada parte con el espacio que una clase no tiene.",
        "",
        "## Obra de referencia por parte",
        "",
    ]
    for parte, manuales in sorted(support.get("parts", {}).items()):
        lineas.append(f"### Parte {parte} — {titulos.get(parte, '')}")
        lineas.append("")
        for manual in manuales:
            entry = by_id.get(manual["id"])
            if entry is None:
                continue
            lineas.append(f"- {format_work(entry)} · {format_edition(entry)} — {format_locator(entry)}")
            lineas.append(f"  - **{manual['scope']}**: {manual['why']}")
        lineas.append("")

    libros = sorted(
        (e for e in registry["entries"] if e["type"] == "book"),
        key=lambda e: normalize_title(e.get("title", "")),
    )
    lineas += [
        "## Todas las obras que citan las clases",
        "",
        "| Obra | Edición | Localizador | Clases |",
        "|---|---|---|---:|",
    ]
    for entry in libros:
        lineas.append(
            f"| {format_work(entry)} | {format_edition(entry)} | {format_locator(entry)} "
            f"| {len(entry.get('used_in', []))} |"
        )

    normas = sorted(
        (e for e in registry["entries"] if e["type"] == "standard"),
        key=lambda e: normalize_title(e.get("title", "")),
    )
    lineas += [
        "",
        "## Normas y especificaciones",
        "",
        "| Norma | Versión | Fuente | Clases |",
        "|---|---|---|---:|",
    ]
    for entry in normas:
        lineas.append(
            f"| {entry.get('title') or entry['id']} | {entry.get('version') or '—'} "
            f"| [{entry.get('authority') or 'fuente'}]({entry.get('locator')}) "
            f"| {len(entry.get('used_in', []))} |"
        )

    sin_obra = [path for path, datos in por_clase.items() if not datos["obras"]]
    lineas += [
        "",
        "## Estado del registro",
        "",
        f"- Obras registradas: **{stats['entries']}** "
        f"({stats['by_type'].get('book', 0)} libros, {stats['by_type'].get('paper', 0)} artículos, "
        f"{stats['by_type'].get('standard', 0)} normas, "
        f"{stats['by_type'].get('reference', 0)} documentos de referencia).",
        f"- Con localizador resuelto contra su autoridad: **{stats['verified']}**; "
        f"pendientes con motivo declarado: **{stats['pending']}**.",
        f"- Clases sin bibliografía de apoyo: **{len(sin_obra)}**.",
        f"- Última resolución en red: **{stats['verified_on']}** "
        "(`python scripts/refresh-sources`).",
        "",
        "El detalle por entrada, con el motivo de cada pendiente, está en",
        "[`bibliography.json`](bibliography.json); el método, en [`README.md`](README.md).",
        "",
    ]
    return "\n".join(lineas)


def _replace_block(text: str, begin: str, end: str, replacement: str) -> tuple[str, bool]:
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        return text, False
    return pattern.sub(lambda _: replacement, text, count=1), True


def _check_support_map(registry: dict, support: dict, problems: list[str]) -> None:
    """El mapa de apoyo solo referencia obras del registro con ISBN-13 válido."""
    by_id = entries_by_id(registry)
    partes = {part_of(p.as_posix()) for p in class_files()}
    partes.discard("")
    faltan = sorted(partes - set(support.get("parts", {})))
    for parte in faltan:
        problems.append(f"support_map.json: la parte {parte} no declara obra de referencia")
    for parte, manuales in support.get("parts", {}).items():
        if not manuales:
            problems.append(f"support_map.json: la parte {parte} no declara obra de referencia")
        for manual in manuales:
            entry = by_id.get(manual.get("id", ""))
            if entry is None:
                problems.append(
                    f"support_map.json: la parte {parte} apunta a {manual.get('id')!r}, "
                    "que no existe en el registro"
                )
                continue
            if entry["type"] != "book":
                problems.append(
                    f"support_map.json: {entry['id']} no es un libro, es {entry['type']}"
                )
            if not isbn13_is_valid(entry.get("isbn13", "")):
                problems.append(
                    f"support_map.json: {entry['id']} entra como obra de referencia sin "
                    "ISBN-13 con dígito de control válido"
                )
            for campo in ("scope", "why"):
                if not manual.get(campo):
                    problems.append(
                        f"support_map.json: {entry['id']} en la parte {parte} no declara {campo}"
                    )


def _check_class_bibliography(
    registry: dict, support: dict, items: list[RefItem], root: Path, problems: list[str]
) -> None:
    """Cada clase muestra su bibliografía de apoyo, y coincide con el registro."""
    esperado = class_bibliography(registry, support, items)
    for path in class_files(root):
        rel = path.relative_to(root).as_posix()
        datos = esperado.get(rel)
        if not datos or not datos["obras"]:
            problems.append(f"{rel}: sin bibliografía de apoyo")
            continue
        texto = path.read_text(encoding="utf-8")
        if CLASS_BEGIN not in texto or CLASS_END not in texto:
            problems.append(
                f"{rel}: falta el bloque de bibliografía de apoyo "
                "(`python scripts/link_sources_to_classes.py`)"
            )
            continue
        actual = texto[texto.index(CLASS_BEGIN) : texto.index(CLASS_END) + len(CLASS_END)]
        if actual.replace("\r\n", "\n") != class_block(datos):
            problems.append(
                f"{rel}: la bibliografía de apoyo no coincide con el registro "
                "(`python scripts/link_sources_to_classes.py`)"
            )


def sync_outputs(
    registry: dict,
    support: dict,
    items: list[RefItem],
    stats: dict,
    root: Path = ROOT,
    write: bool = False,
) -> list[str]:
    """Escribe (o compara) lo que se deriva del registro: README y bibliografía."""
    problems: list[str] = []
    readme = root / "README.md"
    text = readme.read_text(encoding="utf-8")
    updated = text
    for begin, end, block in (
        (README_BEGIN, README_END, readme_block(registry, support, root)),
        (BADGE_BEGIN, BADGE_END, badge_block(stats)),
    ):
        updated, found = _replace_block(updated, begin, end, block)
        if not found:
            problems.append(f"README.md: falta el bloque {begin} … {end}")
    if updated != text:
        if write:
            readme.write_text(updated, encoding="utf-8")
        else:
            problems.append(
                "README.md: la bibliografía de apoyo no coincide con el registro "
                "(`python scripts/verify-sources --write` la regenera)"
            )

    destino = root / "sources" / "BIBLIOGRAFIA.md"
    contenido = bibliography_md(registry, support, items, stats)
    actual = destino.read_text(encoding="utf-8") if destino.exists() else ""
    if actual.replace("\r\n", "\n") != contenido:
        if write:
            destino.write_text(contenido, encoding="utf-8")
        else:
            problems.append(
                "sources/BIBLIOGRAFIA.md: desfasada respecto del registro "
                "(`python scripts/verify-sources --write` la regenera)"
            )
    return problems


def verify(root: Path = ROOT, write_readme: bool = False) -> dict:
    """Comprobación offline y determinista. Es la que bloquea CI."""
    problems: list[str] = []
    registry_path = root / "sources" / "bibliography.json"
    if not registry_path.exists():
        return {"ok": False, "problems": [f"no existe {registry_path}"], "stats": {}}
    try:
        registry = load_registry(registry_path)
    except json.JSONDecodeError as exc:  # pragma: no cover - error de formato
        return {"ok": False, "problems": [f"el registro no parsea: {exc}"], "stats": {}}
    support = load_support_map(root)

    items = extract_items(root)
    class_paths = {p.relative_to(root).as_posix() for p in class_files(root)}

    _check_schema(registry, problems)
    _check_entries(registry, class_paths, problems)
    _check_coverage(registry, items, problems)
    _check_class_blocks(items, root, problems)
    _check_support_map(registry, support, problems)
    _check_class_bibliography(registry, support, items, root, problems)

    stats = registry_stats(registry, items)
    problems.extend(sync_outputs(registry, support, items, stats, root, write=write_readme))

    return {"ok": not problems, "problems": problems, "stats": stats}
