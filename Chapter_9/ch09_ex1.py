#!/usr/bin/env python3
"""Python Essentials

Chapter 9, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""
from decimal import Decimal, InvalidOperation
from fractions import Fraction

def clean_number(text):
    """
    >>> clean_number("3.14159")
    3.14159
    >>> clean_number("two")
    >>> clean_number("1,956")
    >>> row = ['heading', '23', '2.718']
    >>> list(map(clean_number, row))
    [None, 23.0, 2.718]
    """
    try:
        value= float(text)
    except ValueError:
        value= None
    return value

def clean_number2(text):
    """
    >>> row = ['heading', '23', '2.718', "1,956"]
    >>> list(map(clean_number2, row))
    [None, 23.0, 2.718, 1956.0]
    >>> clean_number2(2j) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: can't convert complex to float
    """
    try:
        value= float(text)
    except ValueError:
        text= text.replace(",","").replace("$","")
        try:
            value= float(text)
        except ValueError:
            value= None
    return value

def clean_number3(text, num_type=Decimal):
    """
    >>> clean_number3("3.14159")
    Decimal('3.14159')
    >>> clean_number3("three")
    >>> clean_number3("1,956")
    Decimal('1956')
    >>> row = ['heading', '23', '9.8696', '1,959']
    >>> list(map(clean_number3, row))
    [None, Decimal('23'), Decimal('9.8696'), Decimal('1959')]
    >>> clean_number3(2.5j) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: conversion from complex to Decimal is not supported
    >>>
    >>> clean_number3(',2/0,', Fraction) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Fraction(2, 0)
    """
    try:
        value= num_type(text)
    except (ValueError, InvalidOperation):
        text= text.replace(",","").replace("$","")
        try:
            value= num_type(text)
        except (ValueError, InvalidOperation):
            value= None
    return value

def fraction_row(row):
    """
    >>> happy_row = ['heading', '23', '9.8696', '1,959', '3/2']
    >>> fraction_row(happy_row)
    [None, Fraction(23, 1), Fraction(12337, 1250), Fraction(1959, 1), Fraction(3, 2)]
    >>> sad_row = ['heading', '23', '9.8696', '1,959', '2/0']
    >>> fraction_row(sad_row)
    [None, None, None, None, None]
    """
    try:
        return [clean_number3(item,Fraction) for item in row]
    except (TypeError, ZeroDivisionError):
        return [None for item in row]

import os
import sys
def names(path="."):
    """
    >>> names() # doctest: +ELLIPSIS
    ['479371.csv', ... 'test_all.py']

    >>> names("fail")
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: 'fail'
    """
    try:
        return [name
            for name in os.listdir(path)
            if not name.startswith('.')]
    except OSError as exc:
        print( exc.__class__.__name__, exc )
        raise

class Shutdown_Request( BaseException ):
    pass

def one_request():
    global counter
    counter -= 1
    if counter == 2:
        raise OSError("Demo")
    elif counter == 0:
        raise Shutdown_Request
    print( "Serving", counter )

def server():
    """
    >>> server()
    Serving 3
    OSError Demo
    Serving 1
    Shutting Down
    """
    global counter
    counter= 4
    try:
        while True:
            try:
                one_request()
            except Exception as e:
                print(e.__class__.__name__, e)
    except Shutdown_Request:
        print("Shutting Down")

def lbyl_convert(text):
    """
    >>> lbyl_convert("123")
    123
    >>> lbyl_convert("-5")
    """
    if text.isdigit():
        num= int(text)
    else:
        num= None
    return num

def eafp_convert(text):
    """
    >>> eafp_convert("123")
    123
    >>> eafp_convert("-5")
    -5
    """
    try:
        num= int(text)
    except ValueError:
        num= None
    return num

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )