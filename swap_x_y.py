import os
from pathlib import Path
from typing import List
import shutil

IMAGERY_DIR = "./tiles"
ZOOM_LEVELS = range(16, 17)


def GetSubdirectories(p: Path) -> List[Path]:
    return [x for x in p.iterdir() if x.is_dir()]


def main():
    """ Swaps tiles from z/x/y.png structure to /z/y/x.png and vice versa """
    for n in ZOOM_LEVELS:
        sat_path = Path(IMAGERY_DIR, str(n))
        sat_subdirs = GetSubdirectories(sat_path)

        for i, subdir in enumerate(sat_subdirs):
            print(f"Opening {subdir}")
            tiles = list(subdir.glob("*.png"))

            for tile in tiles:
                corrected_path = Path(IMAGERY_DIR + "_corrected", tile.parents[1].name, tile.stem, tile.parents[0].name + ".png")
                corrected_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(tile, corrected_path)


if __name__ == "__main__":
    main()
