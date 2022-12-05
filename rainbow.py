'''
Benchmark rainbow
'''

# TODO
# Decide on variants in Makefile

from os import system, chdir
from file_ops import *
from benchmark import *
from constants import *
from pathlib import Path

RAINBOW_DIR = Path.cwd() / "rainbow"
RAINBOW_KEYS = RAINBOW_DIR / "keys"
RAINBOW_SIGS = RAINBOW_DIR / "sigs"
RAINBOW_SRC_DIR = Path.cwd() / "rainbow-submission-round2"

if not RAINBOW_DIR.exists():
    system(f"mkdir {RAINBOW_DIR}")

if not RAINBOW_KEYS.exists():
    system(f"mkdir {RAINBOW_KEYS}")

if not RAINBOW_SIGS.exists():
    system(f"mkdir {RAINBOW_SIGS}")

if not RAINBOW_SRC_DIR.exists():
    system("git clone https://github.com/fast-crypto-lab/rainbow-submission-round2.git")

def rainbow_exe(exe: Path, path: Path):
    system(f"{exe} > {path}")

# reference implementation

RAINBOW_REF_DIR = RAINBOW_SRC_DIR / "Reference_Implementation"
RAINBOW_REF_KEYS = RAINBOW_KEYS / "reference"
RAINBOW_REF_SIGS = RAINBOW_SIGS / "reference"
RAINBOW_REF_GEN = RAINBOW_REF_DIR / "rainbow-genkey"
RAINBOW_REF_SGN = RAINBOW_REF_DIR / "rainbow-sign"
RAINBOW_REF_VRF = RAINBOW_REF_DIR / "rainbow-verify"
RAINBOW_REF_STATS = RAINBOW_REF_KEYS / "rainbow_ref_gen_stats.json"

if not RAINBOW_REF_KEYS.exists():
    system(f"mkdir {RAINBOW_REF_KEYS}")

if not RAINBOW_REF_SIGS.exists():
    system(f"mkdir {RAINBOW_REF_SIGS}")

if not RAINBOW_REF_GEN.exists():
    cwd = Path.cwd()
    chdir(RAINBOW_REF_DIR)
    system("make")
    chdir(cwd)

#### key generation

gen_ref_times = {}

for n in range(NUM_KEYS):
    key_path = RAINBOW_REF_KEYS / f"rainbow_{n}"
    benchmark(rainbow_exe(RAINBOW_REF_GEN, key_path), gen_ref_times, n)

write_file(RAINBOW_REF_STATS, dumps(gen_ref_times, indent = 4))     

####TODO sign, verify

# optimized implementation

RAINBOW_OPT_DIR = RAINBOW_SRC_DIR / "Optimized_Implementation/amd64"
RAINBOW_OPT_KEYS = RAINBOW_KEYS / "optimized"
RAINBOW_OPT_SIGS = RAINBOW_SIGS / "optimized"
RAINBOW_OPT_GEN = RAINBOW_OPT_DIR / "rainbow-genkey"
RAINBOW_OPT_SGN = RAINBOW_OPT_DIR / "rainbow-sign"
RAINBOW_OPT_VRF = RAINBOW_OPT_DIR / "rainbow-verify"
RAINBOW_OPT_STATS = RAINBOW_OPT_KEYS / "rainbow_opt_gen_stats.json"

if not RAINBOW_OPT_KEYS.exists():
    system(f"mkdir {RAINBOW_OPT_KEYS}")

if not RAINBOW_OPT_SIGS.exists():
    system(f"mkdir {RAINBOW_OPT_SIGS}")

if not RAINBOW_OPT_GEN.exists():
    cwd = Path.cwd()
    chdir(RAINBOW_OPT_DIR)
    system("make")
    chdir(cwd)

#### key generation

gen_opt_times = {}

for n in range(NUM_KEYS):
    key_path = RAINBOW_OPT_KEYS / f"rainbow_{n}"
    benchmark(rainbow_exe(RAINBOW_OPT_GEN, key_path), gen_opt_times, n)

write_file(RAINBOW_OPT_STATS, dumps(gen_opt_times, indent = 4))     
