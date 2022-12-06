'''
Benchmark rainbow
'''

# TODO
# Decide on variants in Makefile

from os import system, chdir, listdir
from file_ops import *
from benchmark import *
from constants import *
from pathlib import Path

RAINBOW_DIR = Path.cwd() / "rainbow"
RAINBOW_KEYS = RAINBOW_DIR / "keys"
RAINBOW_SIGS = RAINBOW_DIR / "sigs"
RAINBOW_SRC_DIR = Path.cwd() / "rainbow-submission-round2"

def rainbow_exe(exe: Path, path: Path):
    system(f"{exe} > {path}")

# create dirs

mkdir(RAINBOW_DIR)
mkdir(RAINBOW_KEYS)
mkdir(RAINBOW_SIGS)

if not RAINBOW_SRC_DIR.exists():
    system("git clone https://github.com/fast-crypto-lab/rainbow-submission-round2.git")

# reference implementation

RAINBOW_REF_DIR  = RAINBOW_SRC_DIR / "Reference_Implementation"
RAINBOW_REF_KEYS = RAINBOW_KEYS / "reference"
RAINBOW_REF_SIGS = RAINBOW_SIGS / "reference"
RAINBOW_REF_GEN  = RAINBOW_REF_DIR / "rainbow-genkey"
RAINBOW_REF_SGN  = RAINBOW_REF_DIR / "rainbow-sign"
RAINBOW_REF_VRF  = RAINBOW_REF_DIR / "rainbow-verify"

# create reference dirs

mkdir(RAINBOW_REF_DIR)
mkdir(RAINBOW_REF_KEYS)
mkdir(RAINBOW_REF_SIGS)

if not RAINBOW_REF_GEN.exists():
    cwd = Path.cwd()
    chdir(RAINBOW_REF_DIR)
    system("make")
    chdir(cwd)

RAINBOW_REF_GEN_STATS = RAINBOW_REF_KEYS / "rainbow_ref_gen_stats.json"
RAINBOW_REF_SGN_STATS = RAINBOW_REF_SIGS / "rainbow_ref_sign_stats.json"
RAINBOW_REF_VRF_STATS = RAINBOW_REF_SIGS / "rainbow_ref_verify_stats.json"

ref_gen_times = {}
ref_sign_times = {}
ref_verify_times = {}

for n in range(NUM_KEYS):
    key_path = RAINBOW_REF_KEYS / f"rainbow_{n}"
    benchmark(rainbow_exe(RAINBOW_REF_GEN, key_path), ref_gen_times, n)
    for datum in listdir(DATA_DIR):
        sig_path = RAINBOW_REF_SIGS / f"{n}-{datum}.sig"
        benchmark(rainbow_exe(RAINBOW_REF_SGN, sig_path), ref_sign_times, n)
    for sigs in filter(lambda s: s.startswith(str(n)), listdir(RAINBOW_REF_SIGS)):
        verify_path = RAINBOW_REF_SIGS / f"{n}.verify"
        benchmark(rainbow_exe(RAINBOW_REF_VRF, verify_path), ref_verify_times, n)

write_file(RAINBOW_REF_GEN_STATS, dumps(ref_gen_times, indent = 4))
write_file(RAINBOW_REF_SGN_STATS, dumps(ref_sign_times, indent = 4))
write_file(RAINBOW_REF_VRF_STATS, dumps(ref_verify_times, indent = 4))

# optimized implementation

RAINBOW_OPT_DIR  = RAINBOW_SRC_DIR / "Optimized_Implementation/amd64"
RAINBOW_OPT_KEYS = RAINBOW_KEYS / "optimized"
RAINBOW_OPT_SIGS = RAINBOW_SIGS / "optimized"
RAINBOW_OPT_GEN  = RAINBOW_OPT_DIR / "rainbow-genkey"
RAINBOW_OPT_SGN  = RAINBOW_OPT_DIR / "rainbow-sign"
RAINBOW_OPT_VRF  = RAINBOW_OPT_DIR / "rainbow-verify"

# create optimized dirs

mkdir(RAINBOW_OPT_DIR)
mkdir(RAINBOW_OPT_KEYS)
mkdir(RAINBOW_OPT_SIGS)

if not RAINBOW_OPT_GEN.exists():
    cwd = Path.cwd()
    chdir(RAINBOW_OPT_DIR)
    system("make")
    chdir(cwd)

RAINBOW_OPT_GEN_STATS = RAINBOW_OPT_KEYS / "rainbow_opt_gen_stats.json"
RAINBOW_OPT_SGN_STATS = RAINBOW_OPT_SIGS / "rainbow_opt_sign_stats.json"
RAINBOW_OPT_VRF_STATS = RAINBOW_OPT_SIGS / "rainbow_opt_verify_stats.json"

opt_gen_times = {}
opt_sign_times = {}
opt_verify_times = {}

for n in range(NUM_KEYS):
    key_path = RAINBOW_OPT_KEYS / f"rainbow_{n}"
    benchmark(rainbow_exe(RAINBOW_OPT_GEN, key_path), opt_gen_times, n)
    for datum in listdir(DATA_DIR):
        sig_path = RAINBOW_OPT_SIGS / f"{n}-{datum}.sig"
        benchmark(rainbow_exe(RAINBOW_OPT_SGN, sig_path), opt_sign_times, n)
    for sigs in filter(lambda s: s.startswith(str(n)), listdir(RAINBOW_OPT_SIGS)):
        verify_path = RAINBOW_OPT_SIGS / f"{n}.verify"
        benchmark(rainbow_exe(RAINBOW_OPT_VRF, verify_path), opt_verify_times, n)

write_file(RAINBOW_OPT_GEN_STATS, dumps(opt_gen_times, indent = 4))
write_file(RAINBOW_OPT_SGN_STATS, dumps(opt_sign_times, indent = 4))
write_file(RAINBOW_OPT_VRF_STATS, dumps(opt_verify_times, indent = 4))
