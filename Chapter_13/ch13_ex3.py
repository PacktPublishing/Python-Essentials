#!/usr/bin/env python3
"""Python Essentials

Chapter 13, Example Set 3

This test suite will initialize logging, something that can interfere
with other logging-based test suites.

See ch13_ex2 for a module which also initializes logging.
When the entire package is tested as a whole, that module will interfere
with this module by initializing logging.

When this module is tested alone, however, there's no interference
from previous initializations of the logging system.

We can easily distinguish these two contexts. This leads to a dynamic
set of tests in the __test__ global variable, set below.
"""
import logging

class Logged(type):
    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.logger= logging.getLogger(name)
        return result

class Machine(metaclass=Logged):
    def __init__(self, machine_id, base, cost_each):
        self.logger.info("creating {0} at {1}+{2}".format(
            machine_id, base, cost_each))
        self.machine_id= machine_id
        self.base= base
        self.cost_each= cost_each
    def application(self, units):
        total= self.base + self.cost_each*units
        self.logger.debug("Applied {units} ==> {total}".format(
            total=total, units=units, **self.__dict__))
        return total

test_machine_stand_alone = """
This test suite shows how logging works in a stand-alone situation,
where logging has not been previously initialized.

In the __test__ global variable, below, uses this variation
only when this module is being run from the command prompt.

When this module is imported for testing, the stand-alone
test is not set in the __test__ global.

>>> import logging, logging.handlers, io
>>> buffer= io.StringIO()
>>> logging.basicConfig(stream=buffer, level=logging.DEBUG)
>>> m1= Machine(1, 100, 15)
>>> m2= Machine(2, 200, 12)
>>> m1.application(100)
1600
>>> m2.application(100)
1400
>>> logging.shutdown()
>>> print(buffer.getvalue())
INFO:Machine:creating 1 at 100+15
INFO:Machine:creating 2 at 200+12
DEBUG:Machine:Applied 100 ==> 1600
DEBUG:Machine:Applied 100 ==> 1400
<BLANKLINE>
"""

test_machine_after_ch13_ex2 = """
This test suite shows how logging works in a context
where logging has been previously initialized. The results are the same
because we've modified the logging configuration.

This is an unusual situation, and is created entirely by the desire
to have code samples (like the one above) show features in isolation.

>>> import logging, logging.handlers, io
>>> buffer= io.StringIO()

>>> #logging.basicConfig(stream=buffer, level=logging.DEBUG)

In the event that logging was already initialized, the basicConfig() method
won't do anything. Therefore, we have to manually create the basic configuration.

It looks like this:

>>> buffer_handler= logging.StreamHandler(buffer)
>>> buffer_handler.setFormatter( logging.Formatter("%(levelname)s:%(name)s:%(message)s") )
>>> logging.getLogger().addHandler(buffer_handler)
>>> logging.getLogger().setLevel(logging.DEBUG)

We've created a StreamHandler that writes to the StringIO object, buffer.
We've set the desired formatter, also.
This is what stream=buffer means in the config.

>>> m1= Machine(1, 100, 15)
>>> m2= Machine(2, 200, 12)
>>> m1.application(100)
1600
>>> m2.application(100)
1400
>>> logging.shutdown()
>>> print(buffer.getvalue())
INFO:Machine:creating 1 at 100+15
INFO:Machine:creating 2 at 200+12
DEBUG:Machine:Applied 100 ==> 1600
DEBUG:Machine:Applied 100 ==> 1400
<BLANKLINE>
"""

__test__ = {
    # The "after ex2" test can be run when logging was initialized
    # elsewhere. This is typical for testing the book as a whole.
    "test_machine_2_after_ch13_ex2": test_machine_after_ch13_ex2,
}

if __name__ == "__main__":
    # The "stand alone" test can be run only when this module
    # is run by itself. It can't be run when the entire book is being tested.
    # It's commented out to allow the entire book to be tested as a whole.
    __test__["test_machine_1_stand_alone"]= test_machine_stand_alone
    import doctest
    doctest.testmod( verbose=1 )
