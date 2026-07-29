from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
urls = set()
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    urls.update(re.findall(r"https?://[^)\s]+", path.read_text(encoding="utf-8")))
print(f"{len(urls)} enlaces externos encontrados")
print("La comprobación HTTP se mantiene separada de CI local para no ocultar fallos de red.")
