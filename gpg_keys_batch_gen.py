'''
Benchmark GPG unattended batch key generation
'''

import timeit
from os import system, listdir
from secrets import token_hex
from pathlib import Path

# parameters

NUM_KEYS = 1
KEYS_DIR = Path.cwd() / 'keys'

# key generation utils

# TODO key lengths
keys = {
    'RSA'   : {'min': 1024, 'max': 4096},
    'ELG'   : {'min': 1024, 'max': 4096},
    'DSA'   : {'min': 1024, 'max': 4096},
    'ECDH'  : {'min': 1024, 'max': 4096},
    'ECDSA' : {'min': 1024, 'max': 4096},
    'EDDSA' : {'min': 1024, 'max': 4096}
}

def create_file(fpath: Path):
    '''
    Checks if `fpath` exists and creates corresponding dirs and file if necessary
    '''
    # file
    if not fpath.exists():
        # alog dir
        if not fpath.parent.exists():
            # keys dir
            if not fpath.parent.parent.exists():
                system(f'mkdir {fpath.parent.parent}')
            system(f'mkdir {fpath.parent}')
        system(f'touch {fpath}')

def is_key_dir(fname: str) -> bool:
    '''
    Filter predicate for key dirs
    '''
    fpath = KEYS_DIR / fname
    return fname in keys and fpath.is_dir()

def key_gen_file(key_type: str, key_len: int, num: int):
    '''
    Generate a gpg key file for unattended batch key generation
    '''
    fname = f'{key_type}_{key_len}_{num}'
    fpath = KEYS_DIR / key_type / fname
    create_file(fpath)
    pwd = token_hex(32)
    contents = f'''Key-Type: {key_type}
Key-Length: {key_len}
Name-Real: {key_type}
Name-Comment: {num}
Name-Email: {key_type}_{key_len}_{num}
Expire-Date: 0
Passphrase: {pwd}
%commit
'''
    with fpath.open("w") as f:
        f.write(contents)
        f.close()

def key_gen(fpath: Path):
    '''
    Generate gpg key from file `fpath`
    '''
    system(f'gpg --batch --generate-key {fpath}')

##########################################

# Notes

# RSA keys: 1024-4096 bits

# --verify

##########################################

# generate key files

for key_type in keys.keys():
    for n in range(NUM_KEYS):
        min_len = keys[key_type]['min']
        max_len = keys[key_type]['max']
        key_gen_file(key_type, min_len, n)
        key_gen_file(key_type, max_len, n)

# generate keys from files

key_dirs = filter(is_key_dir, listdir(KEYS_DIR))

# TODO benchmark

for dir_name in key_dirs:
    path = KEYS_DIR / dir_name
    key_files = listdir(path)
    for key_file in key_files:
        key_gen(path / key_file)
