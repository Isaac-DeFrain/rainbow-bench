from pathlib import Path
from os import listdir, system

SIGS_DIR = Path.cwd() / "sigs"
sig_types = listdir(SIGS_DIR)

KEYS_DIR = Path.cwd() / "keys"

for sig_type in sig_types:
    key_dir = KEYS_DIR / sig_type
    sig_dir = SIGS_DIR / sig_type
    for sig in listdir(sig_dir):
        key = sig.split("-")[0]
        