'''
List decay
'''

from time import time, sleep

items = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def decay(decay_rate: float, max_duration: float, items: list[int] = items):
    '''
    Pops an element off of `items` and prints it to stdout every `decay_rate` seconds
    
    Exits after `max_duration` seconds
    '''
    start = time()
    now = start
    while now <= start + max_duration:
        x = items.pop()
        print(x)
        if not items:
            break
        sleep(decay_rate)
        now = time()

    if not items:
        print('ran out of items')
