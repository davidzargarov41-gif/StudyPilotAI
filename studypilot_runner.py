"""StudyPilot AI 0.1.0 launcher for Railway."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path


def main() -> None:
    folder = Path(__file__).resolve().parent
    version = "NEW_v020_23KB"
    archive = folder / f"studypilot_{version}.pyz"
    if not archive.is_file():
        matches = sorted(folder.glob(f"*{version}.pyz"))
        if not matches:
            raise RuntimeError(f"Не найден архив StudyPilot версии {version}")
        archive = matches[0]
    sys.path.insert(0, str(archive))
    from studypilot.bot import run

    asyncio.run(run())


if __name__ == "__main__":
    main()
