from os import system
from constants import GPG_CONF_PATH, GPG_AGENT_CONF_PATH

# setup gpg config

system(f"cp gpg.conf {GPG_CONF_PATH}")
system(f"cp gpg-agent.conf {GPG_AGENT_CONF_PATH}")

# generat data and keys, sign, and verify

system("python gen_random_data.py")
system("python gpg_keys_batch_gen.py")
system("python gpg_sign_files.py")
system("python gpg_verify_sig.py")
