'''
modular arithmetic
'''

# naive inverse implementation
def inverse(x: int, n: int) -> int:
    '''
    multiplicative inverse of `x` modulo `n`
    
    Raises `ValueError` if modulus is non-positive
    
    Returns 0 if `x` does not have an inverse
    '''
    if n <= 0:
        raise ValueError('Modulus must be positive')
    else:
        inv = 0
        for y in range(1, n):
            if (x * y) % n == 1:
                inv = y
                break
        return inv
