#!/usr/bin/env python3
"""Python Essentials

Chapter 5, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

bool_function = """
>>> red_violet= (192, 68, 143)
>>> bool(red_violet)
True
>>> empty = ()
>>> type(empty)
<class 'tuple'>
>>> bool(empty)
False
"""

comparisons = """
>>> "11" < "2"
True
>>> 5 > 3 > 1
True
"""

float_approximation = """
>>> a=1
>>> b=(a/105)*3*5*7
>>> a == b
False
>>> abs(a-b)
2.220446049250313e-16
>>> a = 3.14
>>> b = 3.14
>>> a == b
True
>>> a is b
False
>>> hash(a)
322818021289917443
>>> hash(b)
322818021289917443
>>> hash(12)
12
>>> hash(12*2**61)
12
"""

logic_operators = """
selection = "yankee" if wind < 15 else "stays’l"
valid= line and line[0] != "#"
>>> not 12
False
>>> total= 0
>>> count= 0
>>> average = total != 0 and total/count
>>> average
False
>>> 0 and 12
0
>>> () and "non-false"
()
>>> 12 and ()
()
>>> parameter = None
>>> x = parameter or 42
>>> x
42
>>> x = 42 if parameter is None else parameter
>>> x
42
"""

equality_test = """
>>> a=1
>>> b=(a/105)*3*5*7
>>> ε = 1E-6
>>> if abs(a-b)<ε:
...     print("{a} \N{ALMOST EQUAL TO} {b}".format(a=a, b=b))
1 ≈ 1.0000000000000002
"""

if_statement_1 = """
>>> count = 0
>>> if count == 0:
...     print("Insufficient Data")
... else:
...     print("Mean = {0:.2f}".format(total/count))
Insufficient Data
>>> count, total = 3, 25
>>> if count == 0:
...     print("Insufficient Data")
... else:
...     print("Mean = {0:.2f}".format(total/count))
Mean = 8.33
"""

if_statement_2 = """
>>> y = 2015
>>> if y % 400 == 0:
...     leap = True
... elif y % 100 == 0:
...     leap = False
... elif y % 4 == 0:
...     leap = True
... else:
...     leap = False
>>> leap
False

>>> if y % 400 == 0:
...     leap = True
... elif y % 400 != 0 and y % 100 == 0:
...     leap = False
... elif y % 400 != 0 and y % 100 != 0 and y % 4 == 0:
...     leap = True
... elif y % 400 != 0 and y % 100 != 0 and y % 4 != 0:
...     leap = False
... else:
...    raise Exception("Logic Error")
>>> leap
False
"""

assertions = """
>>> a, b = 2, 1
>>> assert a > b > 0
>>> assert a > b > 0, "a={0} and b={1}".format(a, b)
>>> if not a:
...     print("a could be None")
>>> if a is None:
...     print("a is None")
"""

__test__ = {
    'bool_function': bool_function,
    'logic_operators': logic_operators,
    'comparisons': comparisons,
    'float_approximation': float_approximation,
    'equality_test': equality_test,
    'if_statement_1': if_statement_1,
    'if_statement_2': if_statement_2,
    'assertions': assertions,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )