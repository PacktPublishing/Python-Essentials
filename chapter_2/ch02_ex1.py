#!/usr/bin/env python3
"""Python Essentials

Chapter 2, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

simple_math = """
>>> 355/113
3.1415929203539825
>>> 355./113.
3.1415929203539825
>>> 355.//113.
3.0

>>> 9 & 5
1
>>> 9 | 5
13
>>> 9 ^ 3
10
>>> bin(9)
'0b1001'
>>> bin(5)
'0b101'

>>> 2**8530 # doctest: +ELLIPSIS
610749...581824

>>> 0x10
16
>>> 0o10
8
>>> 0b10
2
>>> 0xdeadbeef
3735928559
>>> oct(0xdeadbeef)
'0o33653337357'
"""

fractions = """
>>> from fractions import Fraction
>>> Fraction(355,113)
Fraction(355, 113)
>>> Fraction(4,2)*3
Fraction(6, 1)
>>> Fraction(2,3)*5.5
3.6666666666666665
>>> a= Fraction(355,113)*5
>>> a.numerator
1775
>>> a.denominator
113
"""

decimal= """
>>> from decimal import Decimal
>>> Decimal("2.72")
Decimal('2.72')
>>> (Decimal('512.97')+Decimal('5.97'))*Decimal('0.075')
Decimal('38.92050')
>>> (512.97+5.97)*0.075
38.920500000000004
>>> 6335.437
6335.437
>>> 6.335437E3
6335.437
>>> (5**6)**(1/6)
4.999999999999999
>>> Decimal(0.2)
Decimal('0.200000000000000011102230246251565404236316680908203125')
>>> Decimal('0.2')
Decimal('0.2')
>>> Decimal(1/2)
Decimal('0.5')
>>> Decimal(1/6)
Decimal('0.1666666666666666574148081281236954964697360992431640625')
>>> Decimal(1)/Decimal(6)
Decimal('0.1666666666666666666666666667')
"""

complex = """
>>> import cmath
>>> import math
>>> cmath.sqrt(4+3j)
(2.1213203435596424+0.7071067811865476j)
>>> math.sqrt(4+3j) # doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: can't convert complex to float
>>> cmath.e**(cmath.pi*1j)+1
1.2246467991473532e-16j
"""

logic="""
>>> True + 1
2
>>> 5 > 6 & 3 > 1
True
>>> (5 > 6) & (3 > 1)
False
"""

tuples= """
>>> t=("hello", 3.14, 23, None, True)
>>> t[0]
'hello'
>>> t[4]
True
>>> t[-1]
True
>>> t[-2]
>>> t[-3]
23
>>> t[-4]
3.14
>>> t[-5]
'hello'
>>> t[3] is None
True
>>> "hello" in t
True
>>> 2.718 in t
False
"""

strings = """
>>> "multifaceted"[5:10]
'facet'
>>> "multifaceted"[:5]
'multi'
>>> "multifaceted"[-5:]
'ceted'
>>> "word"[::-1]
'drow'
>>> "String with π×r²"
'String with π×r²'
>>> "String with \u03c0\u00d7r\N{superscript two}"
'String with π×r²'
>>> r'\\b[a-zA-Z_]\\w+\\b'
'\\\\b[a-zA-Z_]\\\\w+\\\\b'
>>> '\\b[a-zA-Z_]\\w+\\b'
'\\x08[a-zA-Z_]\\\\w+\\x08'
>>> rb"\\x[0-9a-fA-F]+"
b'\\\\x[0-9a-fA-F]+'
>>> 'String with π×r²'.encode("utf-8")
b'String with \xcf\x80\xc3\x97r\xc2\xb2'
>>> b'very \\xe2\\x98\\xba\\xef\\xb8\\x8e'.decode('utf-8')
'very ☺︎'
>>> "hello " + "world"
'hello world'
>>> "hello " * 3
'hello hello hello '
>>> "adjacent " 'literals'
'adjacent literals'
>>> "hello" is "hello"
True
>>> "hello" is "hello world"[:5]
False
>>> "hello" == "hello world"[:5]
True
>>> "WoRd".lower()
'word'
>>> "$12,345.00".replace("$","").replace(",","")
'12345.00'

>>> '01.03.05.15'.split('.')
['01', '03', '05', '15']
>>> "-".join(['01', '03', '05', '15'])
'01-03-05-15'

>>> '01.03.05.15'.partition('.')
('01', '.', '03.05.15')

>>> "pleonastic".endswith("tic")
True
>>> "rediscount".find("disc")
2
>>> "postlaunch".find("not")
-1
>>> "E:/programming".startswith("E:")
True
>>> "13210".isdigit()
True

>>> a = 2, 3
>>> colors = [(239, 222, 205), (250, 231, 181), (203, 65, 84)]
>>> a = print("hello world")
hello world
>>> a
>>> a is None
True
>>> word="vokalizers"
>>> word[2]= "c" # doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: 'str' object does not support item assignment

>>> word= word[:2]+"c"+word[3:]
>>> word
'vocalizers'
>>> "i" in "bankrupted"
False
>>> "bank" in "bankrupted"
True
"""

conversions= """
>>> from fractions import Fraction
>>> x=Fraction(2.718)
>>> float(x)
2.718
>>> from decimal import Decimal
>>> "{0:x}".format(12)
'c'
>>> "{0:#x}".format(12)
'0xc'
"""

__test__ = {
    'simple_math': simple_math,
    'fractions': fractions,
    'decimal': decimal,
    'complex': complex,
    'logic': logic,
    'tuples': tuples,
    'strings': strings,
    'conversions': conversions,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )