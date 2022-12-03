'''
Benchmark GPG signatures
'''

from benchmark import *
from key_ops import *
from file_ops import *
from constants import *
from pathlib import Path
from os import system, listdir

def get_pwd(key_file_lines: "list[str]"):
    for line in key_file_lines:
        if line.startswith("Passphrase"):
            return line.split(":")[1].strip()

def is_unprotected_key(key_name: str) -> bool:
    return all([not key_name.startswith(pname) for pname in PROTECTED_NAMES])

def get_full_key_name(key_file: str) -> str:
    return key_file.split("<")[1].split(">")[0]

def mk_path(dir: Path, key_name: str) -> Path:
    return dir / get_key_type(key_name) / key_name

def get_key_ids_and_paths() -> "list[tuple[str, Path]]":
    all_keys_path = KEYS_DIR / "all_keys"
    # print gpg keys to all_keys_path
    system(f'gpg -k > {all_keys_path}')
    with all_keys_path.open("r") as f:
        lines = f.readlines()
        # get key ids
        lines_ids = filter(lambda s: s.startswith(" "), lines)
        lines_ids = [line.strip() for line in lines_ids]
        key_ids = filter(lambda s: s not in PROTECTED_IDS, lines_ids)
        # get key file paths
        key_files = filter(lambda s: s.startswith("uid"), lines)
        key_files = [get_full_key_name(key_file) for key_file in key_files]
        key_files = filter(is_unprotected_key, key_files)
        key_paths = [mk_path(key_file) for key_file in key_files]
    return list(zip(key_ids, key_paths))

def sign(fname: str, key_id: str, sig_path: Path, pwd: str):
    '''
    GPG sign the file with the given key and passphrase
    '''
    system(f"echo {pwd} | gpg --batch --yes -u {key_id} -o {sig_path} --passphrase-fd 0 --sign {DATA_DIR / fname}")

if __name__ == "__main__":
    times = {}
    if not SIGS_DIR.exists():
        system(f"mkdir {SIGS_DIR}")
    for key_id, key_path in get_key_ids_and_paths():
        name = key_path.name
        n = get_key_len(name)
        sig_type = get_key_type(name)
        sig_type_dir = SIGS_DIR / sig_type
        for datum in sorted(listdir(DATA_DIR)):
            sig_path = sig_type_dir / f"{name}-{datum}.sig"
            if not sig_type_dir.exists():
                system(f"mkdir {sig_type_dir}")
            with key_path.open("r", encoding="utf-8") as f:
                pwd = get_pwd(f.readlines())
            benchmark(sign(datum, key_id, sig_path, pwd), times, n)
        write_file(SIGS_DIR / f"{sig_type}_sign_stats.json", dumps(times, indent=4))
