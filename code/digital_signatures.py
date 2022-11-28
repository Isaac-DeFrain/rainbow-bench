'''
Digital signatures
'''

import hashlib
from secrets import token_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

# AES
# key: 16, 24, 32 bytes
# block: 16 bytes

# utils
def pad(s: str) -> str:
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def unpad(s: str) -> str:
    return s[:-ord(s[len(s) - 1:])]

# AES encryption
def encrypt(pt: str, key: bytes = b'') -> tuple[bytes, bytes]:
    valid = {16, 24, 32}
    if not valid.__contains__(len(key)):
        key = token_bytes(32)
    iv = token_bytes(16)
    aes = AES.new(key, AES.MODE_CBC, iv)
    return key, b64encode(iv + aes.encrypt(pad(pt).encode('utf-8')))

# AES decryption
def decrypt(ct: bytes, key: bytes):
    ct = b64decode(ct)
    iv = ct[:16]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(ct[16:]).decode('utf-8'))

# returns first 32 chars of hash as hex string
def sha256(s: str) -> str:
    m = hashlib.sha256()
    m.update(s.encode('utf-8'))
    return m.hexdigest()[32:]

# sign via sha256
def sign(msg: str, key: bytes) -> bytes:
    hashed = sha256(msg)
    _, encrypted = encrypt(hashed, key)
    return encrypted

# verify signature
def verify(msg: str, sig: bytes, key: bytes) -> bool:
    return sig == sign(msg, key)
