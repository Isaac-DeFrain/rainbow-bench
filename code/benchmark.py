import timeit
import os
import secrets
print(secrets.token_hex(20))

os.system('export GNUPGHOME="../gpg"')
#$ cat >foo <<EOF
#     %echo Generating a basic OpenPGP key
#    Key-Type: DSA
#     Key-Length: 1024
#     Subkey-Type: ELG-E
#     Subkey-Length: 1024
#     Name-Real: Joe Tester
#     Name-Comment: with stupid passphrase
#     Name-Email: joe@foo.bar
#    Expire-Date: 0
#     Passphrase: abc
#     # Do a commit here, so that we can later print "done" :-)
#     %commit
#     %echo done
#EOF
#$ gpg --batch --generate-key foo
