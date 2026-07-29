from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)
archive = shutil.make_archive(
    str(DIST / "artificial-intelligence-evolution-program-v0.1.0"),
    "zip",
    root_dir=ROOT.parent,
    base_dir=ROOT.name,
)
print(archive)
