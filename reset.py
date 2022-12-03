from os import system
from constants import *
from shutil import rmtree
from gpg_sign_files import get_key_ids_and_paths

def delete_gpg_keys():
    '''
    ⚠️ PROCEED WITH CAUTION ⚠️

    DELETES ALL UNPROTECTED GPG SECRET AND PUBLIC KEYS

    Configure PROTECTED_IDS and PROTECTED_NAMES in constants
    '''
    for key_id, _ in get_key_ids_and_paths():
        system(f'gpg --batch --yes --delete-secret-and-public-keys {key_id}')

if __name__ == "__main__":
    delete_gpg_keys()
    # delete data, keys, sigs dirs
    rmtree(DATA_DIR)
    rmtree(KEYS_DIR)
    rmtree(SIGS_DIR)
    # reset gpg config
    system(f'echo "" > {GPG_CONF_PATH}')
    system(f'echo "" > {GPG_AGENT_CONF_PATH}')
