import os
from pathlib import Path

NUM_DATA = 10

def write_file(fname:str, contents: str):
    fpath = Path.cwd() / "data" / fname
    if not fpath.exists():
        if not fpath.parent.exists():
            os.system(f"mkdir {fpath.parent}")
        os.system(f"touch {fpath}")
    with fpath.open("w", encoding="utf-8") as f:
        f.write(contents)
        f.close()

for i in range(NUM_DATA):
    size = i * 100 + 100
    fname = f"{i}_{size}"
    write_file(fname, os.urandom(size).hex())
    