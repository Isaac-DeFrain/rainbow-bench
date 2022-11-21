'''
3DES attack

https://doc.sagemath.org/html/en/reference/cryptography/sage/crypto/block_cipher/des.html
'''

from sage.crypto.block_cipher.des import DES
from math import ceil, log

def keys() -> list[str]:
    '''
    Generates all 56-bit keys
    '''
    quantity = pow(2, 56)
    res = []
    n = ceil(log(quantity, 10))
    for k in range(1, quantity + 1):
        diff = n - ceil(log(k, 10))
        res.append('0' * diff + str(k))
    return res

des = DES()
msg = 'Hello'

alpha = list(map(lambda k: des.encrypt(msg, k), keys()))
beta  = list(map(lambda k: des.decrypt(msg, k), keys()))
