'''
GPG constants
'''

import os
import key_ops
import pathlib as pl

KEYS_DIR = pl.Path.cwd() / 'keys'
'''
Keys directory path
'''

# gpg config paths

GPG_CONF_PATH = pl.Path("~/.gnupg/gpg.conf")
GPG_AGENT_CONF_PATH = pl.Path("~/.gnupg/gpg-agent.conf")

def key_names_and_ids() -> "tuple[set[str], set[str]]":
    gpg_keys_path = KEYS_DIR / "og_gpg_keys"
    # print gpg keys to all_keys_path
    if not KEYS_DIR.exists():
        os.system(f"mkdir {KEYS_DIR}")
    os.system(f'gpg -k > {gpg_keys_path}')
    with gpg_keys_path.open("r") as f:
        lines = f.readlines()
        # get key names
        key_files = filter(lambda s: s.startswith("uid"), lines)
        key_names = [key_ops.get_full_key_name(key_file) for key_file in key_files]
        # get key ids
        lines_ids = filter(lambda s: s.startswith(" "), lines)
        key_ids = [line.strip() for line in lines_ids]
    return (set(key_names), set(key_ids))

# protected gpg keys

PROTECTED_GPG_NAMES = key_names_and_ids()[0]
'''
GPG key names we don't want to delete
'''

PROTECTED_GPG_IDS = key_names_and_ids()[1]
'''
GPG key ids we don't want to delete
'''
