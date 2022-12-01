'''
Benchmark GPG unattended batch key generation
'''

from timeit import timeit
from os import system, listdir
from secrets import token_hex
from pathlib import Path
from json import dumps

# parameters

NUM_KEYS = 3
KEYS_DIR = Path.cwd() / 'keys'

# key generation utils

# TODO key lengths
keys = {
    'RSA'   : [1024, 2048, 3072, 4096],
#    'ELG'   : [1024, 2048, 3072, 4096],
    'DSA'   : [896, 1024],
#### TODO: actual sizes of DSA keys
#    'ECDH'  : [1024, 2048, 3072, 4096],
#    'ECDSA' : [1024, 2048, 3072, 4096],
#    'EDDSA' : [1024, 2048, 3072, 4096],
}

def create_file(fpath: Path):
    '''
    Checks if `fpath` exists and creates corresponding dirs and file if necessary
    '''
    # file
    if not fpath.exists():
        # key type dir
        if not fpath.parent.exists():
            # all keys dir
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
    for num in range(NUM_KEYS):
        for key_len in keys[key_type]:
            key_gen_file(key_type, key_len, num)

# generate keys from files

key_dirs = filter(is_key_dir, listdir(KEYS_DIR))

times = {}

for dir_name in key_dirs:
    path = KEYS_DIR / dir_name
    keyfiles = listdir(path)
    groups = map(lambda n: (n, list(filter(lambda fname: fname.split("_")[1] == str(n), keyfiles))), keys[dir_name])
    for n, key_files in groups:
        for key_file in key_files:
            try: 
                times[n]
            except KeyError:
                times[n] = []
            times[n].append(timeit(lambda: key_gen(path / key_file), number=1))
    fpath = KEYS_DIR / f"{dir_name}_stats.json"
    if not fpath.exists():
        system(f"touch {fpath}")
    with fpath.open("w") as f:
        f.write(dumps(times, indent=4))
        f.close()
