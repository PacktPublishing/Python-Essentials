#!/usr/bin/env python3
"""Python Essentials

Chapter 13, Example Set 2

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.

This test suite will initialize logging, something that can interfere
with other logging-based test suites.

See ch13_ex3 for a module which also initializes logging.
When the entire package is tested as a whole, this module will interfere
with subsequent modules.
"""

import logging
from functools import wraps
def debug_log(func):
    log= logging.getLogger(func.__name__)
    @wraps(func)
    def decorated(*args, **kw):
        log.debug(">>> call(*{0}, **dict({1}))".format(args, sorted(kw.items())))
        try:
            result= func(*args, **kw)
            log.debug("<<< return {}".format(result))
            return result
        except Exception as ex:
            log.exception( "*** {}".format(ex) )
            raise
    return decorated

@debug_log
def some_function(ksloc):
    return 2.4*ksloc**1.05

@debug_log
def another_function(ksloc, a=3.6, b=1.20):
    return a*ksloc**b

test_debug_log = """
>>> import logging
>>> import io
>>> result= io.StringIO()
>>> logging.basicConfig(stream=result, level=logging.DEBUG)
>>> round(some_function(25),3)
70.477
>>> round(another_function(31, a=3.0, b=1.12),3)
140.426
>>> round(some_function("bad"),3) # doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
>>> logging.shutdown()
>>> print( result.getvalue() ) # doctest: +ELLIPSIS
DEBUG:some_function:>>> call(*(25,), **dict([]))
DEBUG:some_function:<<< return 70.47713658528114
DEBUG:another_function:>>> call(*(31,), **dict([('a', 3.0), ('b', 1.12)]))
DEBUG:another_function:<<< return 140.4256205777791
DEBUG:some_function:>>> call(*('bad',), **dict([]))
ERROR:some_function:*** unsupported operand type(s) for ** or pow(): 'str' and 'float'
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
<BLANKLINE>
"""

__test__ = {
    "test_debug_log": test_debug_log,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )
