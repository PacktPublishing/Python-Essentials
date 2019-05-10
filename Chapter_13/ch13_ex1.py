#!/usr/bin/env python3
"""Python Essentials

Chapter 13, Example Set 1
"""

from functools import lru_cache
from glob import glob
import os

@lru_cache(100)
def find_source(directory):
    """
    >>> find_source("Chapter_13") # doctest: +ELLIPSIS
    ['Chapter_13...ch13_ex1.py', 'Chapter_13...ch13_ex2.py', 'Chapter_13...ch13_ex3.py']
    """
    return glob(os.path.join(directory,"*.py"))

fast_glob= lru_cache(100)(glob)

test_fast_glob = """
>>> fast_glob(os.path.join("Chapter_13","*.py")) # doctest: +ELLIPSIS
['Chapter_13...ch13_ex1.py', 'Chapter_13...ch13_ex2.py', 'Chapter_13...ch13_ex3.py']
"""

__test__ = {
    "test_fast_glob": test_fast_glob,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )