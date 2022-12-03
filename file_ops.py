from os import system
from constants import *
from pathlib import Path

def mk_path(fpath: Path):
    if fpath != Path.cwd():
        if not fpath.parent.exists():
            system(f"mkdir {fpath.parent}")
            mk_path(fpath.parent)

def write_file(fpath: Path, contents: str = ""):
    '''
    Creates dir path from `cwd` to `fpath.parent` and writes `contents` to `fpath.name`
    '''
    if not fpath.exists():
        mk_path(fpath)
        system(f"touch {fpath}")
    with fpath.open("w", encoding="utf-8") as f:
        f.write(contents)
        f.close()
