'''
Key file name operations
'''

import constants as cs

def get_key_type(fname: str) -> str:
    '''
    Key type from the key file's name
    '''
    return fname.split("_")[0]

def get_key_len(fname: str) -> int:
    '''
    Key len from the key file's name
    '''
    return int(fname.split("_")[1])

def key_groups(fnames: "list[str]", key_type: str) -> "list[tuple[int, list[str]]]":
    '''
    Association list: key length -> list of key file names
    '''
    len_fnames_pairs = lambda n: (n, list(filter(lambda fname: get_key_len(fname) == n, fnames)))
    return list(map(len_fnames_pairs, cs.KEYS[key_type]))
