from os import system
from constants import *
from pathlib import Path

def mk_path(fpath: Path):
    parents = fpath.parents
    idx = parents.index(Path.cwd())
    for i in range(1, idx + 1):
        if not parents[idx - i].exists():
            system(f"mkdir {parents[idx - i]}")

def write_file(fpath: Path, contents: str = ""):
    '''
    Creates dir path from `cwd` to `fpath.parent` and writes `contents` to `fpath.name`
    '''
    mk_path(fpath)
    if not fpath.exists():
        system(f"touch {fpath}")
    with fpath.open("w", encoding="utf-8") as f:
        f.write(contents)
        f.close()
