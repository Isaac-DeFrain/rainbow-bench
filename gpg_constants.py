'''
GPG constants
'''

import os
import json
import key_ops
import pathlib as pl

KEYS_DIR = pl.Path.cwd() / 'keys'
'''
Keys directory path
'''

# gpg config paths

GPG_CONF_PATH = pl.Path("~/.gnupg/gpg.conf")
GPG_AGENT_CONF_PATH = pl.Path("~/.gnupg/gpg-agent.conf")

protected_gpg_keys_path = KEYS_DIR / "protected_gpg_keys.json"

def key_names_and_ids():
    gpg_keys_path = KEYS_DIR / "og_gpg_keys"
    protected_gpg_keys_dict = {}
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
    protected_gpg_keys_dict["names"] = key_names
    protected_gpg_keys_dict["ids"] = key_ids
    with protected_gpg_keys_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(protected_gpg_keys_dict, indent=4))
        f.close()

key_names_and_ids()

def protected_gpg_ids() -> "set[str]":
    with protected_gpg_keys_path.open("r", encoding="utf-8") as f:
        dict = json.load(f)
        return dict["ids"]

def protected_gpg_names() -> "set[str]":
    with protected_gpg_keys_path.open("r", encoding="utf-8") as f:
        dict = json.load(f)
        return dict["names"]

# protected gpg keys

PROTECTED_GPG_NAMES = set(protected_gpg_names())
'''
GPG key names we don't want to delete
'''

PROTECTED_GPG_IDS = set(protected_gpg_ids())
'''
GPG key ids we don't want to delete
'''
