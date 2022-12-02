from pathlib import Path
from os import listdir, system
from constants import KEYS_DIR, SIGS_DIR

sig_types = listdir(SIGS_DIR)

for sig_type in sig_types:
    key_dir = KEYS_DIR / sig_type
    sig_dir = SIGS_DIR / sig_type
    for sig in listdir(sig_dir):
        key = sig.split("-")[0]
        