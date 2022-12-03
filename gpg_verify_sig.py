from pathlib import Path
from os import listdir, system
from constants import KEYS_DIR, SIGS_DIR
from timeit import timeit
from gpg_sign_files import key_ids_and_paths, get_key_type


sig_types = listdir(SIGS_DIR)
verify_path = SIGS_DIR / "verify"

def get_key_len(fname: str) -> str:
    return fname.split("_")[1]

#### TODO: Do append corrently

def verify(fname: str, key_id: str, sig_type: str):
    system(f"gpg --batch --yes -u {key_id} --verify {SIGS_DIR / sig_type / fname} >> {verify_path}")

if not verify_path.exists():
    system(f"touch {verify_path}")

times = {}

for sig_type in sig_types:
    sig_dir = SIGS_DIR / sig_type
    for sig in listdir(sig_dir):
        key_name = sig.split("-")[0]
        for key_id, key_path in key_ids_and_paths:
            if key_name == key_path.name:
                timeit(lambda: verify(sig, key_id, sig_type), number = 1)


    groups = map(lambda n: (n, list(filter(lambda fname: fname.split("_")[1] == str(n), keyfiles))), keys[dir_name])
    for n, key_files in groups:
        for key_file in key_files:
            try: 
                times[n]
            except KeyError:
                times[n] = []
            times[n].append(timeit(lambda: key_gen(path / key_file), number=1))
    fpath = KEYS_DIR / f"{key_type}_stats.json"
    if not fpath.exists():
        system(f"touch {fpath}")
    with fpath.open("w") as f:
        f.write(dumps(times, indent=4))
        f.close()