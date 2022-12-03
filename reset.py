from os import system
from shutil import rmtree
from gpg_sign_files import key_ids_and_paths
from constants import DATA_DIR, KEYS_DIR, SIGS_DIR, GPG_CONF_PATH, GPG_AGENT_CONF_PATH

if __name__ == "__main__":
    for key_id, _ in key_ids_and_paths:
        system(f'gpg --batch --yes --delete-secret-and-public-keys {key_id}')
    rmtree(DATA_DIR)
    rmtree(KEYS_DIR)
    rmtree(SIGS_DIR)
    system(f'echo "" > {GPG_CONF_PATH}')
    system(f'echo "" > {GPG_AGENT_CONF_PATH}')
