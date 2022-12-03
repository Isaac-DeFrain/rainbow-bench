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

KEYS_DIR = pl.Path.cwd() / 'keys'
'''
Keys directory path
'''

SIGS_DIR = pl.Path.cwd() / "sigs"
'''
Sigs directory path
'''

# gpg config paths

GPG_CONF_PATH = pl.Path("~/.gnupg/gpg.conf")
GPG_AGENT_CONF_PATH = pl.Path("~/.gnupg/gpg-agent.conf")

# protected gpg keys

PROTECTED_NAMES = {"flores", "isaac", "thomas", "quantifier"}
'''
GPG key names we don't want to delete
'''

PROTECTED_IDS = {
    "", # added for filter
    "DFCC27E65A41EC52EA7C69AC4D83E4285EECC440",
    "C47A8F3A21AC5BE14F6A9CADD53C7FEBADF65F26",
    "72FA8A68E358DD71F225C2734742109AD8D13E4C",
    "6694D8DE7BE8EE5631BED9502BD5824B7F9470E6",
    "1F4A67E1A53A43ECB4E4990E9CD8723E50881329",
    "E335338F7CA86F5F943EAB390D4F576A2041CACE"
}
'''
GPG key ids we don't want to delete
'''
