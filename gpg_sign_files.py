from os import system, listdir
from pathlib import Path
from timeit import timeit

SIGS_DIR = Path.cwd() / "sigs"
DATA_DIR = Path.cwd() / "data"
KEYS_DIR = Path.cwd() / "keys"
all_keys_path = KEYS_DIR / "all_keys"
data = sorted(listdir(DATA_DIR))

#### Ensure only keys needed are available in key ring; TODO: trustdb

def get_key_type(fname: str) -> str:
    return fname.split("_")[0]

def get_key_len(fname: str) -> str:
    return fname.split("_")[1]

def get_key_IDs() -> "list[str]":
    system(f'gpg -k > {all_keys_path}')
    with all_keys_path.open("r") as f:
        lines = f.readlines()
        lines_IDs = filter(lambda s: s.startswith(" "), lines)
        lines_IDs = [line.strip() for line in lines_IDs]
        key_IDs = filter(lambda s: s != "", lines_IDs)
        key_files = filter(lambda s: s.startswith("uid"), lines)
        key_files = [key_file.split("<")[1].split(">")[0] for key_file in key_files]
    return list(key_IDs)

#### TODO: Get password from key file, add password argument to sign

key_ids = get_key_IDs()

def sign(fname: str, key_ID: str, sig_path: str, pwd: str):
    system(f"gpg --batch -u {key_ID} -o {sig_path} --passphrase {pwd} --sign ./data/{fname}")

#### TODO: Give the key to clear-sign 

if not SIGS_DIR.exists():
    system(f"mkdir {SIGS_DIR}")

for datum in data:
    for key_id in key_ids:
        pwd = "" # TODO
        sig_path = f"./sigs/{get_key_type(key_id)}/{datum}.sig"
        timeit(lambda: sign(datum, key_id, sig_path, pwd), number = 1)

#### TODO: sign/verify in right directory; GPG DSA key sizes
