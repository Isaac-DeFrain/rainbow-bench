'''
Generate random data of various sizes to sign
'''

from file_ops import *
from constants import *
from os import urandom

if __name__ == "__main__":
    for i in range(NUM_DATA):
        size = i * 100 + 100
        fpath = DATA_DIR / f"{i}_{size}"
        write_file(fpath, urandom(size).hex())
