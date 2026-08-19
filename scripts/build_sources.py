"""Construye `sources/bibliography.json` a partir de lo que las clases citan.

Es determinista y offline: agrupa las citas de las 183 clases en entradas,
deriva el localizador cuando la propia cita lo contiene (DOI, arXiv, URL) y
deja pendiente todo lo que no se puede derivar sin inventar.

Los datos que resuelve `scripts/refresh-sources` contra Open Library, Crossref
y las webs de los organismos se conservan entre ejecuciones: este script nunca
degrada una entrada ya verificada ni borra una fuente que dejó de resolver.

    python scripts/build_sources.py            # reconstruye el registro
    python scripts/build_sources.py --check    # falla si el registro está desfasado
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.sources import (  # noqa: E402
    REGISTRY_PATH,
    SCHEMA_VERSION,
    arxiv_doi,
    book_locator,
    isbn13_is_valid,
    dump_registry,
    extract_items,
    load_registry,
    normalize_url_key,
    normalize_work_key,
    paper_locator,
    slugify,
)

POLICY = (
    "Toda afirmación del programa se apoya en una entrada de este registro. "
    "Ninguna entrada se acepta sin localizador verificable. Lo que no resuelve "
    "se marca pendiente con motivo; no se borra ni se completa por intuición."
)

# --------------------------------------------------------------------------
# obras que ocupan varias URL del mismo sitio: la entrada es la obra, no la página
# --------------------------------------------------------------------------
SITE_WORKS: dict[str, dict] = {
    "aima.cs.berkeley.edu": {
        "id": "russell-norvig-aima",
        "type": "book",
        "authors": ["Russell, Stuart J.", "Norvig, Peter"],
        "title": "Artificial Intelligence: A Modern Approach",
        "published": "2020",
        "edition": "4.ª",
        "isbn13": "9780134610993",
        "authority": "Pearson",
        "homepage": "https://aima.cs.berkeley.edu/",
    },
    "deeplearningbook.org": {
        "id": "goodfellow-bengio-courville-deep-learning",
        "type": "book",
        "authors": ["Goodfellow, Ian", "Bengio, Yoshua", "Courville, Aaron"],
        "title": "Deep Learning",
        "published": "2016",
        "isbn13": "9780262035613",
        "authority": "MIT Press",
        "homepage": "https://www.deeplearningbook.org/",
    },
    "web.stanford.edu/~jurafsky/slp3": {
        "id": "jurafsky-martin-speech-and-language-processing",
        "type": "book",
        "authors": ["Jurafsky, Daniel", "Martin, James H."],
        "title": "Speech and Language Processing",
        "published": "2009",
        "edition": "2.ª (la 3.ª circula como borrador abierto sin ISBN)",
        "isbn13": "9780131873216",
        "authority": "Pearson Prentice Hall",
        "homepage": "https://web.stanford.edu/~jurafsky/slp3/",
    },
    "hastie.su.domains/elemstatlearn": {
        "id": "hastie-tibshirani-friedman-elements-statistical-learning",
        "type": "book",
        "authors": ["Hastie, Trevor", "Tibshirani, Robert", "Friedman, Jerome"],
        "title": "The Elements of Statistical Learning",
        "published": "2009",
        "edition": "2.ª",
        "isbn13": "9780387848570",
        "authority": "Springer",
        "homepage": "https://hastie.su.domains/ElemStatLearn/",
    },
    "incompleteideas.net": {
        "id": "sutton-barto-reinforcement-learning",
        "type": "book",
        "authors": ["Sutton, Richard S.", "Barto, Andrew G."],
        "title": "Reinforcement Learning: An Introduction",
        "published": "2018",
        "edition": "2.ª",
        "isbn13": "9780262039246",
        "authority": "MIT Press",
        "homepage": "http://incompleteideas.net/book/the-book-2nd.html",
    },
    "statlearning.com": {
        "id": "james-witten-hastie-tibshirani-introduction-statistical-learning",
        "type": "book",
        "authors": ["James, Gareth", "Witten, Daniela", "Hastie, Trevor", "Tibshirani, Robert"],
        "title": "An Introduction to Statistical Learning",
        "published": "2021",
        "authority": "Springer",
        "homepage": "https://www.statlearning.com/",
    },
    "szeliski.org": {
        "id": "szeliski-computer-vision",
        "type": "book",
        "authors": ["Szeliski, Richard"],
        "title": "Computer Vision: Algorithms and Applications",
        "published": "2022",
        "edition": "2.ª",
        "authority": "Springer",
        "homepage": "https://szeliski.org/Book/",
    },
    "probml.github.io": {
        "id": "murphy-probabilistic-machine-learning",
        "type": "book",
        "authors": ["Murphy, Kevin P."],
        "title": "Probabilistic Machine Learning",
        "published": "2022",
        "authority": "MIT Press",
        "homepage": "https://probml.github.io/pml-book/",
    },
    "nlp.stanford.edu/ir-book": {
        "id": "manning-raghavan-schutze-information-retrieval",
        "type": "book",
        "authors": ["Manning, Christopher D.", "Raghavan, Prabhakar", "Schütze, Hinrich"],
        "title": "Introduction to Information Retrieval",
        "published": "2008",
        "isbn13": "9780521865715",
        "authority": "Cambridge University Press",
        "homepage": "https://nlp.stanford.edu/IR-book/",
    },
    "d2l.ai": {
        "id": "zhang-lipton-li-smola-dive-into-deep-learning",
        "type": "book",
        "authors": ["Zhang, Aston", "Lipton, Zachary C.", "Li, Mu", "Smola, Alexander J."],
        "title": "Dive into Deep Learning",
        "published": "2023",
        "authority": "Cambridge University Press",
        "homepage": "https://d2l.ai/",
    },
}

#: Autoría de libros cuyo ISBN sale de la URL del editor y cuya ficha de Open
#: Library no la trae. El ISBN y el título los verifica el catálogo; esto solo
#: completa la autoría, que es dato de portada y no un localizador.
BOOK_AUTHORS: dict[str, dict] = {
    "9780262013192": {
        "authors": ["Koller, Daphne", "Friedman, Nir"],
        "authority": "MIT Press",
    },
    "9780262037310": {
        "authors": ["Peters, Jonas", "Janzing, Dominik", "Schölkopf, Bernhard"],
        "authority": "MIT Press",
    },
    "9780262042192": {
        "authors": ["Dorigo, Marco", "Stützle, Thomas"],
        "authority": "MIT Press",
    },
    "9780262201629": {
        "authors": ["Thrun, Sebastian", "Burgard, Wolfram", "Fox, Dieter"],
        "authority": "MIT Press",
    },
    "9780674576292": {
        "authors": ["Vygotsky, Lev S."],
        "authority": "Harvard University Press",
    },
    "9781098107956": {
        "authors": ["Huyen, Chip"],
        "authority": "O'Reilly Media",
    },
    "9780136291558": {
        "authors": ["Meyer, Bertrand"],
        "authority": "Prentice Hall",
    },
}


#: Dominios cuya publicación es normativa o especificación técnica.
STANDARD_DOMAINS = {
    "nist.gov",
    "nvlpubs.nist.gov",
    "csrc.nist.gov",
    "nvd.nist.gov",
    "owasp.org",
    "genai.owasp.org",
    "cheatsheetseries.owasp.org",
    "iso.org",
    "eur-lex.europa.eu",
    "digital-strategy.ec.europa.eu",
    "artificialintelligenceact.eu",
    "w3.org",
    "c2pa.org",
    "ietf.org",
    "rfc-editor.org",
    "datatracker.ietf.org",
    "json-schema.org",
    "unicode.org",
    "cisa.gov",
    "iec.ch",
    "oecd.org",
    "unesco.org",
    "modelcontextprotocol.io",
    "a2a-protocol.org",
    "openapis.org",
    "spec.openapis.org",
    "spdx.dev",
    "cyclonedx.org",
    "opentelemetry.io",
    "semver.org",
    "keepachangelog.com",
}

#: Organismo responsable por dominio. Sin entrada, se usa el propio dominio.
AUTHORITIES = {
    "nist.gov": "National Institute of Standards and Technology (NIST)",
    "nvlpubs.nist.gov": "National Institute of Standards and Technology (NIST)",
    "csrc.nist.gov": "National Institute of Standards and Technology (NIST)",
    "nvd.nist.gov": "National Institute of Standards and Technology (NIST)",
    "owasp.org": "Open Worldwide Application Security Project (OWASP)",
    "genai.owasp.org": "Open Worldwide Application Security Project (OWASP)",
    "cheatsheetseries.owasp.org": "Open Worldwide Application Security Project (OWASP)",
    "iso.org": "International Organization for Standardization (ISO)",
    "eur-lex.europa.eu": "Unión Europea — EUR-Lex",
    "w3.org": "World Wide Web Consortium (W3C)",
    "c2pa.org": "Coalition for Content Provenance and Authenticity (C2PA)",
    "ietf.org": "Internet Engineering Task Force (IETF)",
    "rfc-editor.org": "RFC Editor",
    "datatracker.ietf.org": "Internet Engineering Task Force (IETF)",
    "json-schema.org": "JSON Schema",
    "cisa.gov": "Cybersecurity and Infrastructure Security Agency (CISA)",
    "modelcontextprotocol.io": "Model Context Protocol",
    "a2a-protocol.org": "A2A Protocol",
    "opentelemetry.io": "OpenTelemetry (CNCF)",
    "anthropic.com": "Anthropic",
    "docs.anthropic.com": "Anthropic",
    "docs.claude.com": "Anthropic",
    "openai.com": "OpenAI",
    "platform.openai.com": "OpenAI",
    "ai.google.dev": "Google",
    "cloud.google.com": "Google Cloud",
    "research.google": "Google Research",
    "deepmind.google": "Google DeepMind",
    "sre.google": "Google",
    "microsoft.com": "Microsoft",
    "scikit-learn.org": "scikit-learn (proyecto)",
    "pytorch.org": "PyTorch Foundation",
    "tensorflow.org": "TensorFlow (Google)",
    "huggingface.co": "Hugging Face",
    "docs.langchain.com": "LangChain",
    "python.langchain.com": "LangChain",
    "langchain-ai.github.io": "LangChain",
    "mlflow.org": "MLflow (Linux Foundation)",
    "docs.python.org": "Python Software Foundation",
    "numpy.org": "NumPy",
    "pandas.pydata.org": "pandas",
    "docs.vllm.ai": "vLLM",
    "qdrant.tech": "Qdrant",
    "weaviate.io": "Weaviate",
    "milvus.io": "Milvus",
    "faiss.ai": "Meta AI — FAISS",
    "gymnasium.farama.org": "Farama Foundation",
    "plato.stanford.edu": "Stanford Encyclopedia of Philosophy",
    "jmlr.org": "Journal of Machine Learning Research",
    "papers.nips.cc": "NeurIPS Proceedings",
    "aclanthology.org": "ACL Anthology",
    "openreview.net": "OpenReview",
    "arxiv.org": "arXiv (Cornell University)",
    "doi.org": "DOI Foundation",
}

#: Documentación de proveedores de modelos: `reference` volátil, accessed obligatorio.
VOLATILE_DOMAINS = {
    "anthropic.com",
    "docs.anthropic.com",
    "docs.claude.com",
    "openai.com",
    "platform.openai.com",
    "ai.google.dev",
    "deepmind.google",
    "cloud.google.com",
    "huggingface.co",
    "mistral.ai",
    "docs.mistral.ai",
    "ai.meta.com",
    "llama.com",
    "cohere.com",
    "docs.cohere.com",
    "x.ai",
    "deepseek.com",
    "qwen.ai",
}

#: La misma obra citada con dos títulos distintos es una sola fuente.
#: La clave de la izquierda se reescribe a la de la derecha antes de agrupar.
MERGE_WORKS = {
    "the book of why: the new science of cause and effect": "the book of why",
    "probabilistic reasoning in intelligent systems: networks of plausible inference": (
        "probabilistic reasoning in intelligent systems"
    ),
}

ARXIV_RE = re.compile(r"^arxiv\.org/(?:abs|pdf)/(.+?)(?:v\d+)?(?:\.pdf)?$")
EMBEDDED_DOI_RE = re.compile(r"/(10\.\d{4,9}/[^/\s]+)$")
#: Varias editoriales ponen el ISBN-13 en la ruta (MIT Press, O'Reilly). Es un
#: dato que trae la propia cita, no una conjetura: se comprueba el dígito de control.
EMBEDDED_ISBN_RE = re.compile(r"(?<!\d)(97[89]\d{10})(?!\d)")

#: Editoriales y actas que publican artículos revisados por pares.
PAPER_DOMAINS = {
    "papers.nips.cc",
    "proceedings.neurips.cc",
    "proceedings.mlr.press",
    "jmlr.org",
    "aclanthology.org",
    "openreview.net",
    "dl.acm.org",
    "link.springer.com",
    "ieeexplore.ieee.org",
    "sciencedirect.com",
    "nature.com",
    "science.org",
    "pnas.org",
    "biorxiv.org",
    "cell.com",
    "jstor.org",
}
YEAR_RE = re.compile(r"\((\d{4})[a-z]?\)|\b(19\d{2}|20\d{2})\b")


def domain_of(url_key: str) -> str:
    return url_key.split("/")[0]


def site_work_for(url_key: str) -> dict | None:
    for prefix, spec in SITE_WORKS.items():
        if url_key == prefix or url_key.startswith(prefix + "/"):
            return spec
    return None


def group_of(url_key: str) -> tuple[str, str]:
    """(id de grupo, tipo) para un enlace usado por una clase."""
    if url_key.startswith("doi.org/"):
        doi = url_key[len("doi.org/") :]
        return f"doi:{doi}", "paper"
    match = ARXIV_RE.match(url_key)
    if match:
        return f"arxiv:{match.group(1)}", "paper"
    isbn = EMBEDDED_ISBN_RE.search(url_key)
    if isbn and isbn13_is_valid(isbn.group(1)):
        return f"isbn:{isbn.group(1)}", "book"
    embedded = EMBEDDED_DOI_RE.search(url_key)
    if embedded and domain_of(url_key) in PAPER_DOMAINS:
        return f"doi:{embedded.group(1)}", "paper"
    spec = site_work_for(url_key)
    if spec:
        return f"work:{spec['id']}", spec["type"]
    domain = domain_of(url_key)
    if domain in PAPER_DOMAINS:
        return f"url:{url_key}", "paper"
    if domain in STANDARD_DOMAINS:
        return f"url:{url_key}", "standard"
    if "/datasets/" in url_key:
        return f"url:{url_key}", "dataset"
    return f"url:{url_key}", "reference"


def link_text(item_text: str) -> str:
    match = re.search(r"\[([^\]]+)\]\(https?://", item_text)
    if match:
        return match.group(1)
    return re.sub(r"<?https?://\S+>?", "", item_text).strip()


def guess_year(text: str) -> str | None:
    match = YEAR_RE.search(text)
    if not match:
        return None
    return match.group(1) or match.group(2)


def guess_title(item_text: str) -> str:
    text = link_text(item_text)
    works = re.findall(r"\*([^*]{4,}?)\*", text)
    if works:
        return works[0].strip()
    quoted = re.findall(r"[\"“]([^\"”]{5,})[\"”]", text)
    if quoted:
        return quoted[0].strip()
    cleaned = re.sub(r"^\s*[^.]{0,80}?\(\d{4}[a-z]?\)\.?\s*", "", text)
    cleaned = re.split(r"\s+[—·]\s+", cleaned)[0]
    cleaned = re.sub(r"\s*\([^)]*\)\s*$", "", cleaned).strip(" .,;:")
    return cleaned or text.strip(" .,;:")


def guess_authors(item_text: str) -> list[str]:
    text = link_text(item_text)
    match = re.match(r"^(.{2,90}?)\s*\((?:\d{4}[a-z]?|eds?\.)", text)
    if not match:
        return []
    raw = match.group(1)
    raw = re.sub(r"\s*\(eds?\.\)\s*", "", raw)
    parts = re.split(r",\s*|\s*&\s*|\s+y\s+|\s*;\s*", raw)
    initials = re.compile(r"^(?:[A-ZÁÉÍÓÚÑÜ]\.?\s*){1,4}$")
    authors: list[str] = []
    for part in parts:
        part = part.strip()
        if not part or part.lower().rstrip(".") in {"et al", "otros"}:
            continue
        if initials.match(part):
            if authors:
                authors[-1] = f"{authors[-1]}, {part.rstrip(' .')}."
            continue
        authors.append(part.rstrip(" ."))
    return authors[:8]


def guess_version(item_text: str) -> str | None:
    text = link_text(item_text)
    patterns = (
        r"\b(?:AI\s+RMF|RMF)\s+(\d+\.\d+)",
        r"\bv(\d+\.\d+(?:\.\d+)?)\b",
        r"\bRev\.\s*(\d+)\b",
        r"ISO/IEC\s+([\d\-]+:\d{4})",
        r"Reglamento\s+\(UE\)\s+(\d{4}/\d+)",
        r"\b(\d{4}-\d{2}-\d{2})\b",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None


def build(root: Path = ROOT) -> dict:
    items = extract_items(root)
    # la clave se compara en minúsculas, pero el localizador conserva la URL
    # tal como la escribió la clase: hay rutas sensibles a mayúsculas
    # (`torch.nn.Conv2d`, `ElemStatLearn`, `QAI/qai.pdf`).
    originals: dict[str, str] = {}
    for item in items:
        for raw, key in zip(item.urls, item.url_keys):
            originals.setdefault(key, raw.strip().strip("<>").rstrip(".,;"))
    groups: dict[str, dict] = {}
    order: list[str] = []
    work_owner: dict[str, set[str]] = {}

    for item in items:
        url_keys = item.url_keys
        # la misma obra citada con dos títulos es una sola fuente, pero las dos
        # claves siguen siendo claves usadas: el grupo se queda con ambas
        work_keys = item.work_keys
        canon_keys = [MERGE_WORKS.get(key, key) for key in work_keys]
        if not url_keys and not work_keys:
            # remisión interna del repositorio, no una fuente externa
            continue
        if url_keys:
            gid, gtype = group_of(url_keys[0])
        else:
            gid = f"obra:{canon_keys[0]}"
            gtype = "paper" if re.search(r"[\"“][^\"”]{5,}[\"”]", item.text) else "book"

        entry = groups.get(gid)
        if entry is None:
            entry = {
                "gid": gid,
                "type": gtype,
                "url_keys": [],
                "aliases": [],
                "used_in": [],
                "citations": [],
            }
            groups[gid] = entry
            order.append(gid)
        for key in url_keys:
            if key not in entry["url_keys"]:
                entry["url_keys"].append(key)
        for key in dict.fromkeys(work_keys + canon_keys):
            if key not in entry["aliases"]:
                entry["aliases"].append(key)
            work_owner.setdefault(key, set()).add(gid)
        if item.class_path not in entry["used_in"]:
            entry["used_in"].append(item.class_path)
        entry["citations"].append(item.text)

    # la misma obra citada con enlace y sin enlace es una sola fuente: se fusiona
    for key, gids in list(work_owner.items()):
        loose = f"obra:{key}"
        rest = gids - {loose}
        if loose not in gids or len(rest) != 1:
            continue
        target = groups[next(iter(rest))]
        source = groups.pop(loose)
        order.remove(loose)
        for url_key in source["url_keys"]:
            if url_key not in target["url_keys"]:
                target["url_keys"].append(url_key)
        for alias in source["aliases"]:
            if alias not in target["aliases"]:
                target["aliases"].append(alias)
            work_owner[alias] = {gid for gid in work_owner[alias] if gid != loose} | {
                next(iter(rest))
            }
        for path in source["used_in"]:
            if path not in target["used_in"]:
                target["used_in"].append(path)
        target["citations"].extend(source["citations"])

    # varias páginas del mismo sitio que citan la misma obra son una sola fuente
    for key, gids in list(work_owner.items()):
        if len(gids) < 2 or not all(gid.startswith("url:") for gid in gids):
            continue
        domains = {domain_of(gid[4:]) for gid in gids}
        if len(domains) != 1:
            continue
        keep = next(gid for gid in order if gid in gids)
        target = groups[keep]
        for gid in [g for g in order if g in gids and g != keep]:
            source = groups.pop(gid)
            order.remove(gid)
            for url_key in source["url_keys"]:
                if url_key not in target["url_keys"]:
                    target["url_keys"].append(url_key)
            for alias in source["aliases"]:
                if alias not in target["aliases"]:
                    target["aliases"].append(alias)
                work_owner[alias] = {g for g in work_owner[alias] if g != gid} | {keep}
            for path in source["used_in"]:
                if path not in target["used_in"]:
                    target["used_in"].append(path)
            target["citations"].extend(source["citations"])

    # una obra citada por grupos distintos es el contenedor (revista, actas, serie)
    containers = {key for key, gids in work_owner.items() if len(gids) > 1}
    for key in containers:
        for gid in work_owner[key]:
            entry = groups[gid]
            if key in entry["aliases"]:
                entry["aliases"].remove(key)
            if not entry.get("container"):
                entry["container"] = key

    previous: dict[str, dict] = {}
    if REGISTRY_PATH.exists():
        for entry in load_registry(REGISTRY_PATH).get("entries", []):
            previous[entry["id"]] = entry

    today = dt.date.today().isoformat()
    entries: list[dict] = []
    used_ids: set[str] = set()

    for gid in order:
        group = groups[gid]
        citation = min(group["citations"], key=len)
        citation = re.sub(r"\s+—\s+uso:.*$", "", citation)
        spec = None
        if gid.startswith("work:"):
            spec = next(s for s in SITE_WORKS.values() if s["id"] == gid[len("work:") :])

        entry_id = spec["id"] if spec else _identifier(gid, group, citation, used_ids)
        used_ids.add(entry_id)

        entry: dict = {
            "id": entry_id,
            "type": group["type"],
            "authors": (spec or {}).get("authors") or guess_authors(citation),
            "title": (spec or {}).get("title") or guess_title(citation),
            "published": (spec or {}).get("published") or guess_year(citation),
        }
        if spec and spec.get("edition"):
            entry["edition"] = spec["edition"]

        version = guess_version(citation)
        if version and group["type"] == "standard":
            entry["version"] = version

        _apply_locator(entry, gid, group, spec, originals)

        entry["container"] = group.get("container")
        entry["url_keys"] = sorted(group["url_keys"])
        entry["aliases"] = sorted(group["aliases"])
        entry["used_in"] = sorted(group["used_in"])
        entry["uses"] = len(group["citations"])
        entry["citation"] = citation

        prior = previous.get(entry_id)
        if prior:
            _carry_over(entry, prior)

        declarada = BOOK_AUTHORS.get(entry.get("isbn13", ""))
        if declarada:
            if not entry.get("authors"):
                entry["authors"] = declarada["authors"]
            autoridad = entry.get("authority") or ""
            if not autoridad or re.match(r"^[\w.-]+\.[a-z]{2,}$", autoridad):
                entry["authority"] = declarada["authority"]
        entries.append(entry)

    entries.sort(key=lambda e: (e["type"], e["id"]))
    verified_on = today
    prior_registry = load_registry(REGISTRY_PATH) if REGISTRY_PATH.exists() else {}
    if prior_registry.get("verified_on"):
        verified_on = prior_registry["verified_on"]

    return {
        "schema_version": SCHEMA_VERSION,
        "verified_on": verified_on,
        "policy": POLICY,
        "includes": [
            {
                "registry": "papers/catalog/papers.json",
                "role": "eje de papers fundacionales, incluido por referencia y no modificado",
            }
        ],
        "entries": entries,
    }


def _identifier(gid: str, group: dict, citation: str, used: set[str]) -> str:
    if gid.startswith("doi:"):
        base = "doi-" + slugify(gid[4:], 70)
    elif gid.startswith("arxiv:"):
        base = "arxiv-" + slugify(gid[6:], 30)
    elif gid.startswith("url:"):
        base = slugify(gid[4:], 70)
    elif gid.startswith("obra:"):
        base = slugify(gid[5:], 70)
    else:
        base = slugify(gid, 70)
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    return candidate


def _apply_locator(
    entry: dict, gid: str, group: dict, spec: dict | None, originals: dict[str, str]
) -> None:
    """Deriva el localizador solo cuando la cita lo contiene. Nada se inventa."""
    domain = domain_of(group["url_keys"][0]) if group["url_keys"] else ""
    first = originals.get(group["url_keys"][0], "") if group["url_keys"] else ""
    entry["authority"] = (spec or {}).get("authority") or AUTHORITIES.get(domain, domain or None)

    if gid.startswith("doi:"):
        doi = _doi_from(first, gid[4:])
        entry["doi"] = doi
        entry["locator"] = paper_locator(doi)
        entry["status"] = "pendiente"
        entry["pending_reason"] = "DOI tomado de la cita; falta resolverlo contra Crossref"
        return
    if gid.startswith("arxiv:"):
        arxiv_id = gid[6:]
        entry["arxiv_id"] = arxiv_id
        doi = arxiv_doi(arxiv_id)
        if doi:
            entry["doi"] = doi
            entry["locator"] = paper_locator(doi)
            entry["status"] = "pendiente"
            entry["pending_reason"] = "DOI de arXiv derivado del identificador; falta resolverlo"
        else:
            entry["locator"] = f"https://arxiv.org/abs/{arxiv_id}"
            entry["status"] = "pendiente"
            entry["pending_reason"] = (
                "identificador arXiv antiguo sin DOI derivable; falta localizar el DOI del editor"
            )
        return
    if spec:
        if spec.get("isbn13"):
            entry["isbn13"] = spec["isbn13"]
            entry["isbn_source"] = "edicion-declarada"
            entry["locator"] = f"https://openlibrary.org/isbn/{spec['isbn13']}"
            entry["homepage"] = spec.get("homepage")
            entry["status"] = "pendiente"
            entry["pending_reason"] = "ISBN-13 declarado; falta resolverlo contra Open Library"
        else:
            entry["homepage"] = spec.get("homepage")
            entry["status"] = "pendiente"
            entry["pending_reason"] = "libro sin ISBN-13 localizado"
        return
    if gid.startswith("isbn:"):
        isbn = gid[5:]
        entry["isbn13"] = isbn
        entry["isbn_source"] = "url-del-editor"
        entry["locator"] = book_locator(isbn)
        entry["homepage"] = first or None
        entry["status"] = "pendiente"
        entry["pending_reason"] = (
            "ISBN-13 tomado de la URL del editor; falta resolverlo contra Open Library"
        )
        return
    if gid.startswith("url:"):
        entry["locator"] = _https(first) or ("https://" + gid[4:])
        entry["volatile"] = domain in VOLATILE_DOMAINS
        entry["status"] = "pendiente"
        entry["pending_reason"] = "URL tomada de la cita; falta comprobar que responde"
        return
    entry["status"] = "pendiente"
    entry["pending_reason"] = (
        "obra citada sin enlace: falta ISBN-13 (libro) o DOI (artículo) verificado"
    )


def _doi_from(original: str, fallback: str) -> str:
    """DOI con las mayúsculas que trae la cita; los escapes `%NN` se deshacen."""
    if original:
        raw = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", original.strip())
        for host in ("dl.acm.org/doi/", "link.springer.com/"):
            if host in original:
                match = EMBEDDED_DOI_RE.search(original)
                if match:
                    raw = match.group(1)
        raw = urllib.parse.unquote(raw).split("#")[0].split("?")[0]
        if raw.lower() == fallback.lower():
            return raw
    return fallback


def _https(url: str) -> str:
    """Localizador en https conservando la ruta original.

    Si la cita venía en http, `refresh-sources` comprueba si el sitio responde
    por https; si solo responde sin TLS, la entrada se queda pendiente diciéndolo.
    """
    if not url:
        return ""
    return re.sub(r"^http://", "https://", url)


#: Datos que aporta la red y que la reconstrucción no puede derivar sola.
CARRY_FIELDS = (
    "doi",
    "isbn13",
    "issn",
    "authority",
    "version",
    "published",
    "authors",
    "title",
    "edition",
    "homepage",
    "container",
)


def _carry_over(entry: dict, prior: dict) -> None:
    """Conserva lo que `refresh-sources` resolvió en red, sin heredar un
    localizador viejo: el localizador siempre se vuelve a derivar de la cita."""
    if not prior.get("checked"):
        return
    derived = entry.get("locator")
    for field in CARRY_FIELDS:
        if prior.get(field):
            entry[field] = prior[field]
    if entry["type"] == "book" and entry.get("isbn13"):
        entry["locator"] = book_locator(entry["isbn13"])
    elif entry["type"] == "paper" and entry.get("doi"):
        entry["locator"] = paper_locator(entry["doi"])
    entry["checked"] = prior["checked"]

    # el DOI y el ISBN no distinguen mayúsculas: un cambio de caja no invalida
    # la comprobación. Una URL sí, y entonces hay que volver a comprobarla.
    comparable = entry["type"] in ("book", "paper") or prior.get("locator") == derived
    if not comparable:
        entry["status"] = "pendiente"
        entry["pending_reason"] = "localizador corregido; falta recomprobarlo en red"
        return
    entry["status"] = prior.get("status", entry["status"])
    if entry["status"] == "verificada":
        entry.pop("pending_reason", None)
        if prior.get("accessed"):
            entry["accessed"] = prior["accessed"]
    elif prior.get("pending_reason"):
        entry["pending_reason"] = prior["pending_reason"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="no escribe; falla si hay desfase")
    args = parser.parse_args()

    registry = build()
    payload = json.dumps(registry, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        current = REGISTRY_PATH.read_text(encoding="utf-8") if REGISTRY_PATH.exists() else ""
        if current != payload:
            print("El registro está desfasado: ejecuta `python scripts/build_sources.py`.")
            return 1
        print(f"Registro al día: {len(registry['entries'])} entradas.")
        return 0

    dump_registry(registry, REGISTRY_PATH)
    pending = sum(1 for e in registry["entries"] if e["status"] == "pendiente")
    print(
        f"{REGISTRY_PATH.relative_to(ROOT)}: {len(registry['entries'])} entradas "
        f"({len(registry['entries']) - pending} verificadas, {pending} pendientes)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
