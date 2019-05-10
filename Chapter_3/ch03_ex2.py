#!/usr/bin/env python3
"""Python Essentials

Chapter 3, Example Set 2

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

operators = """
>>> from decimal import Decimal
>>> Decimal('10.6')*2.3 # doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for *: 'decimal.Decimal' and 'float'
>>> Decimal(2.3)
Decimal('2.29999999999999982236431605997495353221893310546875')
>>> "Hello " + "world"
'Hello world'
>>> "<+>"*4
'<+><+><+><+>'
>>> "<+>"*-2
''
>>> (239,222)+(205,)
(239, 222, 205)
>>> (222,)*3
(222, 222, 222)
"""

string_parsing = """
>>> options = ("x", "y", "z")
>>> "|".join(options)
'x|y|z'
>>> "|".join( ("x",) )
'x'

>>> "property.name = value".partition("=")
('property.name ', '=', ' value')

>>> '01.03.05.15'.split('.')
['01', '03', '05', '15']

>>> '01.03.05.15'.partition('.')
('01', '.', '03.05.15')
"""

print_function = """
>>> print( "value", 355/113 )
value 3.1415929203539825
>>> print( "value", 355/113, sep='=' )
value=3.1415929203539825
>>> print( "value", 355/113, sep='=', end='!\\n' )
value=3.1415929203539825!
>>> import sys
>>> print( "Error Message", file=sys.stderr )
>>> message = ("Hello"
... "world")
>>> message
'Helloworld'
"""

script_example = """
>>> c = 13
>>> f = 32+9*c/5
>>> print( "C=", c, "F=", f)
C= 13 F= 55.4
"""

hash_values = """
>>> hash(3)
3
>>> x= 2**64
>>> hash(x)
8
>>> x.__hash__()
8
"""

text_processing = """
>>> text="numerator=355,denominator=115"
>>> text.split(",")
['numerator=355', 'denominator=115']
>>> items= _
>>> items[0].partition("=")
('numerator', '=', '355')
>>> items[1].partition("=")
('denominator', '=', '115')
"""

formatting = """
>>> from decimal import Decimal
>>> c=42
>>> "{0:d}°C is {1:.1f}°F".format(c, 32+9*c/5)
'42°C is 107.6°F'
>>> amount=Decimal("234.56")
>>> "Pay: ${0:*>10n} dollars".format(amount)
'Pay: $****234.56 dollars'
"""

regex = """
>>> import re
>>> date_pattern = re.compile( r"Birth Date:\s+(.*)" )
>>> match = date_pattern.match( "Should Not Match" )
>>> match
>>> match = date_pattern.match( "Birth Date: 3/8/87" )
>>> match # doctest: +ELLIPSIS
<_sre.SRE_Match object at ...>
>>> match.group()
'Birth Date: 3/8/87'
>>> match.group(1)
'3/8/87'
>>> match.groups()
('3/8/87',)
>>> import re
>>> time_pat= re.compile(r"(\d+):(\d+):(\d+\.?\d*)")
>>> m1= time_pat.match( "20:07:13.2" )
>>> m1 # doctest: +ELLIPSIS
<_sre.SRE_Match object at ...>
>>> m1.groups()
('20', '07', '13.2')
>>> h, m, s = m1.groups()
>>> int(h)
20
>>> int(m)
7
>>> float(s)
13.2
"""

locale = """
>>> import locale
>>> # Depends on context: may return 'C' or may return 'en_US.UTF-8'
>>> old= locale.setlocale(locale.LC_ALL,'')
>>> old in ( 'C', 'en_US.UTF-8' )
True
>>> locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
'en_US.UTF-8'
>>> "{0:n}".format(23.456)
'23.456'
>>> locale.setlocale(locale.LC_ALL,'sv_SE')
'sv_SE'
>>> "{0:n}".format(23.456)
'23,456'
>>> locale.currency(23.54)
'23,54 kr'

Reset the locale to OS default prevent problems in other tests.

>>> default = locale.setlocale(locale.LC_ALL,'')
>>> default in ( 'C', 'en_US.UTF-8' )
True
"""

__test__ = {
    'operators': operators,
    'print_function': print_function,
    'script_example': script_example,
    'string_parsing': string_parsing,
    'text_processing': text_processing,
    'formatting': formatting,
    'hash_values': hash_values,
    'regex': regex,
    'locale': locale,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )