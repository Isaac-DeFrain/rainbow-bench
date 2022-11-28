from os import system, listdir
from pathlib import Path
from timeit import timeit

SIGS_DIR = Path.cwd() / "sigs"
DATA_DIR = Path.cwd() / "data"

data = sorted(listdir(DATA_DIR))

#### Find optimal way to retrieve keys from GPG ring

keys = []

def sign(fname: str, key: str):
    system(f"gpg --clear-sign {fname} -o ./sigs/{fname}.gpg")

#### TODO: Give the key to clear-sign 

if not SIGS_DIR.exists():
    system(f"mkdir {SIGS_DIR}")

for datum in data:
    for key in keys:
        timeit(lambda: sign(datum, key), number = 1)

#### TODO: sign in right directory; add, commit, push
