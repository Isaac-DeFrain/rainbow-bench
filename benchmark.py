'''
Benchmark operations
'''

import timeit as tm
from json import dumps

dumps = dumps

def init_dict(dict: "dict[int, list[float]]", n: int):
    try: 
        dict[n]
    except KeyError:
        dict[n] = []

def benchmark(op, times: "dict[int, list[float]]", n: int):
    '''
    Benchmark `op` with length `n` and `times`
    '''
    init_dict(times, n)
    times[n].append(tm.timeit(lambda: op, number=1))
