#### TODO
#### Build rainbow automations
#### Benchmark rainbow reference and optimized and possibly alternative
#### Decide on variants in Makefile

from os import system
from pathlib import Path

system("git clone https://github.com/fast-crypto-lab/rainbow-submission-round2.git")

RAINBOW_DIR = Path.cwd() / "rainbow-submission-round2"

#### Reference Implementation

RAINBOW_REF_DIR = RAINBOW_DIR / "Reference_Implementation"

#### Optimized Implementation

RAINBOW_OPT_DIR = RAINBOW_DIR / "Optimized_Implementation/amd64"