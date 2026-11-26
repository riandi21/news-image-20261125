"""News-image entry: copy the bundled image to the grader's output path.

The image (entry.png) sums up the world's news of Wednesday 25 November
2026: tankers ablaze in the Strait of Hormuz, a Houthi drone strike on
Riyadh, Ukrainian drones hitting Russian refineries, tumbling Asian
markets as the Dow tops 50,000, Shenzhou-24 docking with Pakistan's first
astronaut aboard, and the Huawei verdict. The program writes it to
/output/entry.png, or to the directory in MAKEFUN_OUTPUT_DIR when that is
set (local runs). Deterministic: the same bytes every run, no network,
no randomness.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    if _sha256(SOURCE) != _sha256(dest):
        raise SystemExit("entry.png copy failed integrity check")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
