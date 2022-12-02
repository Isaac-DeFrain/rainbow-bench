from os import system, listdir
from pathlib import Path
from timeit import timeit
from constants import DATA_DIR, KEYS_DIR, SIGS_DIR

all_keys_path = KEYS_DIR / "all_keys"

data = sorted(listdir(DATA_DIR))

#### Ensure only keys needed are available in key ring; TODO: trustdb

def get_key_type(fname: str) -> str:
    return fname.split("_")[0]

def get_key_len(fname: str) -> str:
    return fname.split("_")[1]

def get_pwd(key_file_lines: "list[str]") -> str:
    pwd = ""
    for line in key_file_lines:
        if line.startswith("Passphrase"):
            pwd = line.split(":")[1].strip()
    return pwd

def get_key_ids_and_paths() -> "list[tuple[str, Path]]":
    system(f'gpg -k > {all_keys_path}')
    with all_keys_path.open("r") as f:
        lines = f.readlines()
        # get key ids
        lines_ids = filter(lambda s: s.startswith(" "), lines)
        lines_ids = [line.strip() for line in lines_ids]
        key_ids = filter(lambda s: s != "" and s != "DFCC27E65A41EC52EA7C69AC4D83E4285EECC440", lines_ids)
        # get key file paths
        key_files = filter(lambda s: s.startswith("uid"), lines)
        key_files = [key_file.split("<")[1].split(">")[0] for key_file in key_files]
        key_files = filter(lambda s: not s.startswith("flores"), key_files)
        key_paths = [KEYS_DIR / get_key_type(key_file) / key_file for key_file in key_files]
    return list(zip(key_ids, key_paths))

key_ids_and_paths = get_key_ids_and_paths()

def sign(fname: str, key_id: str, sig_path: Path, pwd: str):
    system(f"gpg --batch -u {key_id} -o {sig_path} --passphrase {pwd} --sign {DATA_DIR / fname}")

if not SIGS_DIR.exists():
    system(f"mkdir {SIGS_DIR}")

for datum in data:
    for key_id, key_path in key_ids_and_paths:
        with key_path.open("r", encoding="utf-8") as f:
            pwd = get_pwd(f.readlines())
        sig_path = SIGS_DIR / get_key_type(key_path.name) / f"{key_path.name}-{datum}.sig"
        if not sig_path.parent.exists():
            system(f"mkdir {sig_path.parent}")
        timeit(lambda: sign(datum, key_id, sig_path, pwd), number = 1)

#### TODO: sign/verify in right directory; GPG DSA key sizes
