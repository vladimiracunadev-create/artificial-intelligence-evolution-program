from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_evolution import __version__

DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)
archive = shutil.make_archive(
    str(DIST / f"artificial-intelligence-evolution-program-v{__version__}"),
    "zip",
    root_dir=ROOT.parent,
    base_dir=ROOT.name,
)
print(archive)
