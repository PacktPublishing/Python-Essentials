#!/usr/bin/env python3
"""Python Essentials

Chapter 1, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

__test__ = {
    'expression': """
>>> 355/113
3.1415929203539825
    """,
    'mixed_math': """
>>> 2 * 3.14 * 8j
50.24j
>>> _ **2
(-2524.0576+0j)
    """,
    'division': """
>>> 355 / 113
3.1415929203539825
>>> 355 // 113
3
    """,
    'assignment': """
>>> v = 23
>>> v
23
    """,
    'import 1': """
>>> import math
>>> math.pi
3.141592653589793
>>> math.sin( math.pi/6 )
0.49999999999999994
    """,
    'import 2': """
>>> import this # doctest: +ELLIPSIS
The Zen of Python, by Tim Peters
...

    """,
    'print': """
>>> print("π≈", 355/113)
π≈ 3.1415929203539825

>>> print(
...     "Hello world",
...     "π≈",
...     355/113
... )
Hello world π≈ 3.1415929203539825
    """,
    'cmath': """
>>> import math
>>> import cmath
>>> math.sqrt(-1) # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: math domain error
>>> cmath.sqrt(-1)
1j
    """,
    'import 3': """
>>> import this

>>> import this
    """
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )