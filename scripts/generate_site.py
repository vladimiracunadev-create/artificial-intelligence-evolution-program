from __future__ import annotations

import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
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
print(f"catálogo generado: {payload['lesson_count']} clases")
