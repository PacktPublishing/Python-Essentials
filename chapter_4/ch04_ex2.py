#!/usr/bin/env python3
"""Python Essentials

Chapter 4, Example Set 2

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.

The id() function results are essentially random and are not included.
"""

variables = """
>>> pi = 3.14
>>> pi
3.14
>>> π = 355/113
>>> π
3.1415929203539825
>>> p_1, p_2 = .75, .75
>>> π̂=p_2+0.5*p_1
>>> π̂
1.125
"""

assignment = """
>>> brick_red = (203, 65, 84)
>>> r, g, b = brick_red
>>> r
203
>>> n, d = 355, 113
>>> line = "255 73 108 Radical Red"
>>> line.split()
['255', '73', '108', 'Radical', 'Red']
>>> r, g, b, *name = line.split()
>>> g
'73'
>>> name
['Radical', 'Red']
>>> " ".join(name)
'Radical Red'
"""

augmented = """
>>> a = 0
>>> a += 1
>>> a = a + 1
>>> a
2
>>> some_list = [1, 1, 2, 3]
>>> some_list += [5]
>>> some_list
[1, 1, 2, 3, 5]
>>> some_list.extend( [8] )
>>> some_list
[1, 1, 2, 3, 5, 8]
>>> c= 11
>>> print("f =", 32+9*c/5)
f = 51.8
"""

hash_function = """
>>> hash(3)
3
>>> x=3
>>> x.__hash__()
3
>>> hash(True)
1
>>> hash(False)
0
>>> type(True)
<class 'bool'>
"""

# a = some_function( some_complex_function( another_function( b ) ) )
# af = another_function(b)
# scf = some_complex_function(af)
# a = some_function(scf)

del_statement = """
>>> 2**2024 # doctest: +ELLIPSIS
192624...497216
>>> 2**2025 # doctest: +ELLIPSIS
385248...994432
>>> a = 2**2024
>>> del a
"""

namespace = """
>>> from types import SimpleNamespace
>>> red_violet= SimpleNamespace(red=192, green=68, blue=143)
>>> red_violet
namespace(blue=143, green=68, red=192)
>>> red_violet.blue
143
"""

__test__ = {
    'variables': variables,
    'assignment': assignment,
    'augmented': augmented,
    'hash': hash_function,
    'del_statement': del_statement,
    'namespace': namespace,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )