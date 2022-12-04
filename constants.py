import pathlib as pl

# TODO key lengths

KEYS = {
#    'RSA'   : [1024, 2048, 3072, 4096],
#    'ELG'   : [1024, 2048, 3072, 4096],
    'DSA'   : [768, 896, 1024],
#### TODO: actual sizes of DSA keys
#    'ECDH'  : [1024, 2048, 3072, 4096],
#    'ECDSA' : [1024, 2048, 3072, 4096],
#    'EDDSA' : [1024, 2048, 3072, 4096],
}

# test parameters

NUM_DATA : int = 10
'''
Number of randomly generated data files
'''

NUM_KEYS : int = 1
'''
Number of keys per type and length
'''

# dir constants

DATA_DIR = pl.Path.cwd() / "data"
'''
Data directory path
'''

SIGS_DIR = pl.Path.cwd() / "sigs"
'''
Sigs directory path
'''
