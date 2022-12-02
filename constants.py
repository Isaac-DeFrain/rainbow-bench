from pathlib import Path

NUM_DATA : int = 10
'''
Number of randomly generated data files
'''

NUM_KEYS : int = 1
'''
Number of keys per type and length
'''

DATA_DIR = Path.cwd() / "data"
'''
Data directory path
'''

KEYS_DIR = Path.cwd() / 'keys'
'''
Keys directory path
'''

SIGS_DIR = Path.cwd() / "sigs"
'''
Sigs directory path
'''
