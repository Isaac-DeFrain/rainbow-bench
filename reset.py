from constants import DATA_DIR, KEYS_DIR, SIGS_DIR
from os import system
from gpg_sign_files import key_ids_and_paths
from shutil import rmtree

if __name__ == "__main__":
    for key_id, _ in key_ids_and_paths:
        system(f'gpg --batch --yes --delete-secret-and-public-keys {key_id}')
    rmtree(DATA_DIR)
    rmtree(KEYS_DIR)
    rmtree(SIGS_DIR)
