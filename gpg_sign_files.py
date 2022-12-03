from os import system, listdir
from pathlib import Path
from timeit import timeit
from constants import DATA_DIR, KEYS_DIR, SIGS_DIR, PROTECTED_IDS, PROTECTED_NAMES

all_keys_path = KEYS_DIR / "all_keys"

data = sorted(listdir(DATA_DIR))

def get_key_type(fname: str) -> str:
    return fname.split("_")[0]

def get_pwd(key_file_lines: "list[str]") -> str:
    pwd = ""
    for line in key_file_lines:
        if line.startswith("Passphrase"):
            pwd = line.split(":")[1].strip()
    return pwd

def unprotected_key(key_name: str) -> bool:
    return all([not key_name.startswith(pname) for pname in PROTECTED_NAMES])

def get_key_ids_and_paths() -> "list[tuple[str, Path]]":
    system(f'gpg -k > {all_keys_path}')
    with all_keys_path.open("r") as f:
        lines = f.readlines()
        # get key ids
        lines_ids = filter(lambda s: s.startswith(" "), lines)
        lines_ids = [line.strip() for line in lines_ids]
        key_ids = filter(lambda s: s not in PROTECTED_IDS, lines_ids)
        # get key file paths
        key_files = filter(lambda s: s.startswith("uid"), lines)
        key_files = [key_file.split("<")[1].split(">")[0] for key_file in key_files]
        key_files = filter(unprotected_key, key_files)
        key_paths = [KEYS_DIR / get_key_type(key_file) / key_file for key_file in key_files]
    return list(zip(key_ids, key_paths))

key_ids_and_paths = get_key_ids_and_paths()

def sign(fname: str, key_id: str, sig_path: Path, pwd: str):
    '''
    GPG sign the file with the given key and passphrase
    '''
    system(f"echo {pwd} | gpg --batch --yes -u {key_id} -o {sig_path} --passphrase-fd 0 --sign {DATA_DIR / fname}")

if not SIGS_DIR.exists():
    system(f"mkdir {SIGS_DIR}")

# TODO collect and write stats

times = {}

for key_id, key_path in key_ids_and_paths:
    for datum in data:
        with key_path.open("r", encoding="utf-8") as f:
            pwd = get_pwd(f.readlines())
        sig_path = SIGS_DIR / get_key_type(key_path.name) / f"{key_path.name}-{datum}.sig"
        if not sig_path.parent.exists():
            system(f"mkdir {sig_path.parent}")
        timeit(lambda: sign(datum, key_id, sig_path, pwd), number = 1)
