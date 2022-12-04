'''
Benchmark rainbow
'''

# TODO
# Decide on variants in Makefile

from os import system
from pathlib import Path

RAINBOW_DIR = Path.cwd() / "rainbow"

RAINBOW_SRC_DIR = Path.cwd() / "rainbow-submission-round2"

system("git clone https://github.com/fast-crypto-lab/rainbow-submission-round2.git")

# Reference Implementation

RAINBOW_REF_DIR = RAINBOW_SRC_DIR / "Reference_Implementation"

# Optimized Implementation

RAINBOW_OPT_DIR = RAINBOW_SRC_DIR / "Optimized_Implementation/amd64"

# TODO Alternative Implementation?
