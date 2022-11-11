'''
Bits
'''

def str_to_bits(s: str) -> str:
    '''
    Converts `s` to bits, char-by-char
    '''
    return ''.join([f'{ord(c):b}' for c in s])
