from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution.labs import run_lab

if __name__ == "__main__":
    result = run_lab("robotics", seed=137)
    print(json.dumps(result, ensure_ascii=False, indent=2))
