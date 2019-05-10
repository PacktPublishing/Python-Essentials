#!/usr/bin/env python3
"""Python Essentials

Chapter 7, Example Set 2
"""

import random

sevens = 0

def roll_dice_count_7(show=False):
    """
    >>> random.seed("test")
    >>> rolls = [roll_dice_count_7() for i in range(100)]
    >>> rolls # doctest: +ELLIPSIS
    [(6, 6), (3, 6), (2, 2), ... (3, 6), (1, 1), (1, 5)]
    """
    global sevens
    d= random.randint(1,6), random.randint(1,6)
    if d[0] + d[1] == 7: sevens += 1
    if show: print( "globals={0}, locals={1}".format(globals(), locals()) )
    return d

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=0 )
    random.seed("test")
    sevens= 0
    rolls = [roll_dice_count_7() for i in range(100)]
    count1= len(list(filter(lambda d: d[0]+d[1] == 7, rolls)))
    print( "len(list...)= {0}".format(count1) )
    print( "sevens={0}".format(sevens) )
    assert( count1 == sevens )
    roll_dice_count_7(show=True)