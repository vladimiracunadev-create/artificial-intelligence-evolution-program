from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.validation import validate_repository

parser = argparse.ArgumentParser()
parser.add_argument("--strict", action="store_true")
args = parser.parse_args()
result = validate_repository(strict=args.strict)
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["ok"] else 1)
