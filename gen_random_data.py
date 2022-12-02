from os import system, urandom
from constants import NUM_DATA, DATA_DIR

def write_file(fname: str, contents: str):
    fpath = DATA_DIR / fname
    if not fpath.exists():
        if not fpath.parent.exists():
            system(f"mkdir {fpath.parent}")
        system(f"touch {fpath}")
    with fpath.open("w", encoding="utf-8") as f:
        f.write(contents)
        f.close()

for i in range(NUM_DATA):
    size = i * 100 + 100
    fname = f"{i}_{size}"
    write_file(fname, urandom(size).hex())
    