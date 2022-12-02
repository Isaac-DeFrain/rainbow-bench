from os import system

system("python gen_random_data.py")
system("python gpg_keys_batch_gen.py")
system("python gpg_sign_files.py")
