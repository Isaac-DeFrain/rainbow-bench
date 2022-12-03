'''
Benchmark GPG verify signatures
'''

from benchmark import *
from key_ops import *
from constants import *
from os import listdir, system
from file_ops import write_file
from gpg_sign_files import get_key_ids_and_paths

def get_key_len(fname: str) -> str:
    return fname.split("_")[1]

def is_sig_dir(fname: str) -> bool:
    fpath = SIGS_DIR / fname
    return fname in KEYS.keys() and fpath.is_dir()

def is_sig_file(fname: str) -> bool:
    suffix = fname.split(".")[-1]
    return suffix == "sig"

verify_path = SIGS_DIR / "verify"

#### TODO: Do append correctly

def verify(fname: str, key_id: str, sig_type: str):
    '''
    GPG verify signature and append output to `verify_path`
    '''
    system(f"gpg --batch --yes -u {key_id} --verify {SIGS_DIR / sig_type / fname} >> {verify_path}")

if __name__ == "__main__":
    times = {}
    write_file(verify_path)
    for sig_type in filter(is_sig_dir, listdir(SIGS_DIR)):
        sig_type_dir = SIGS_DIR / sig_type
        for sig_name in filter(is_sig_file, listdir(sig_type_dir)):
            # sig_name = {key_name}-{datum}.sig
            key_name = sig_name.split("-")[0]
            n = get_key_len(key_name)
            for key_id, key_path in get_key_ids_and_paths():
                if key_name == key_path.name:
                    benchmark(verify(sig_name, key_id, sig_type), times, n)
        write_file(SIGS_DIR / f"{sig_type}_verify_stats.json", dumps(times, indent=4))
