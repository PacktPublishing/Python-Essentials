#!/usr/bin/env python3
"""Python Essentials

Chapter 7, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

def prod(sequence):
    """
    >>> prod([1,2,3,4])
    24
    >>> prod(range(1,6))
    120
    """
    p= 1
    for item in sequence:
        p *= item
    return p

def main_sail_area(boom, mast):
    """
    boom is usually called E, mast is usually called P

    >>> main_sail_area(15, 45)
    375.0
    """
    return (boom*mast)/1.8

def jib(foot, height):
    """
    jib(foot,height) -> area of given jib sail.

    >>> jib(12,40)
    240.0
    """
    return (foot*height)/2

from numbers import Number
def FtoC(f:Number) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (f-32)*5/9

def boat_summary(name, rig, sails):
    """
    >>> mn= main_sail_area(15, 43)
    >>> mz= main_sail_area(11, 31.5)
    >>> y = jib(15.5, 49)
    >>> ss= jib(12.5, 32)
    >>> [mn, mz, y, ss]
    [358.3333333333333, 192.5, 379.75, 200.0]
    >>> boat_summary("Red Ranger", "ketch", [mn, mz, y, ss])
    Boat Red Ranger, ketch rig, 1131 sq. ft.
    >>> boat_summary(sails=[mn, mz, y, ss], rig="ketch", name="Red Ranger" )
    Boat Red Ranger, ketch rig, 1131 sq. ft.
    >>> boat_summary("Red Ranger", sails=[mn, mz, y, ss], rig="ketch", name="Red Ranger") #doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: boat_summary() got multiple values for argument 'name'
    """
    print( "Boat {0}, {1} rig, {2:.0f} sq. ft.".format(
        name, rig, sum(sails))
    )

def mean_diff(data_sequence):
    """
    >>> mean_diff([])
    >>> mean_diff([4,4,5,6])
    4 0.75
    4 0.75
    5 0.25
    6 1.25
    """
    s0, s1 = 0, 0
    for item in data_sequence:
        s0 += 1
        s1 += item
    if s0 < 2:
        return
    m= s1/s0
    for item in data_sequence:
        print( item, abs(item-m) )

def get_data(input_string):
    """
    >>> get_data("hi=mom")
    ('hi', 'mom')
    >>> get_data("hi=mom # with a comment.")
    ('hi', 'mom')
    >>> get_data("# nothing here.")
    ('', '')
    """
    input_string= input_string.strip()
    input_string, _, _ = input_string.partition("#")
    input_string= input_string.rstrip()
    name, _, value = input_string.partition('=')
    return name, value

def remove_mod(some_list, modulus):
    """
    >>> data= list(range(10))
    >>> remove_mod( data, 5 )
    >>> remove_mod( data, 7 )
    >>> data
    [1, 2, 3, 4, 6, 8, 9]
    """
    for item in some_list[:]:
        if item % modulus == 0:
            some_list.remove(item)

default_examples = """
>>> int("48897")
48897
>>> int("48897", 16)
297111
>>> int("48897", base=16)
297111
"""

def sail_area(foot, height, roach_adj=1/.9):
    """
    Generalized sail area with optional roach_adj factor.
    For main and mizzen sails, roach_adj is generally 1/.9.
    For jib sails, roach_adj is 1.0.

    >>> sail_area(15, 45)
    375.0
    >>> main_sail_area(15, 45)
    375.0
    >>> sail_area(12, 40, roach_adj=1.0)
    240.0
    >>> jib(12, 40)
    240.0
    """
    return (height*foot)/2*roach_adj

import random
def dice(n=2, sides=6):
    """
    >>> random.seed("test")
    >>> dice()
    [6, 6]
    >>> dice(6)
    [3, 6, 2, 2, 1, 5]
    >>> dice(4, sides=8)
    [7, 3, 4, 6]
    >>> dice(4, sides=4)
    [3, 3, 4, 3]
    """
    return [random.randint(1,sides) for i in range(n)]

def dicea(n= 2, d=6, adj=0):
    """
    >>> random.seed("test")
    >>> dicea(3, d=6, adj=-3)
    [3, 3, 0]
    """
    return [random.randint(1,d)+adj for i in range(n)]

def more_dice(n, collection=[]):
    """
    Good

    >>> random.seed("test")
    >>> hand1= []
    >>> more_dice(5, hand1)
    [6, 6, 3, 6, 2]
    >>> hand1
    [6, 6, 3, 6, 2]
    >>> hand1.remove(3)
    >>> hand1.remove(2)
    >>> hand1
    [6, 6, 6]
    >>> more_dice(2, hand1)
    [6, 6, 6, 2, 1]
    >>> hand1
    [6, 6, 6, 2, 1]
    >>> hand2= []
    >>> more_dice(5, hand2)
    [5, 4, 2, 2, 5]
    >>> hand2
    [5, 4, 2, 2, 5]

    Bad
    >>> random.seed("test")
    >>> hand1= more_dice(5)
    >>> hand1
    [6, 6, 3, 6, 2]
    >>> hand1.remove(3)
    >>> hand1.remove(2)
    >>> more_dice(2, hand1)
    [6, 6, 6, 2, 1]
    >>> hand1
    [6, 6, 6, 2, 1]
    >>> hand2= more_dice(5)
    >>> hand2
    [6, 6, 6, 2, 1, 5, 4, 2, 2, 5]
    """
    for i in range(n):
        collection.append(random.randint(1,6))
    return collection

def more_dice_good(n, collection=None):
    """
    >>> random.seed("test")
    >>> hand1= more_dice_good(5)
    >>> hand1
    [6, 6, 3, 6, 2]
    >>> hand1.remove(3)
    >>> hand1.remove(2)
    >>> more_dice_good(2, hand1)
    [6, 6, 6, 2, 1]
    >>> hand1
    [6, 6, 6, 2, 1]
    >>> hand2= more_dice_good(5)
    >>> hand2
    [5, 4, 2, 2, 5]
    """
    if collection is None:
        collection = []
    for i in range(n):
        collection.append(random.randint(1,6))
    return collection

def prod2( *args ):
    """
    >>> prod2( 1, 2, 3, 4 )
    24
    >>> prod2(*range(1, 10))
    362880
    """
    p= 1
    for item in args:
        p *= item
    return p

def boat_summary2(name, rig, **sails):
    """
    >>> boat_summary2("Red Ranger", rig="ketch",
    ...     main=358.3, mizzen=192.5, yankee=379.75, staysl=200 )
    Boat Red Ranger, ketch rig, 1131 sq. ft.
    >>> rr_args = dict(
    ...    name="Red Ranger", rig="ketch",
    ...    main=358.3, mizzen=192.5, yankee=379.75, staysl=200
    ... )
    >>> boat_summary2( **rr_args )
    Boat Red Ranger, ketch rig, 1131 sq. ft.
    """
    print("Boat {0}, {1} rig, {2:.0f} sq. ft.".format(
        name, rig, sum(sails.values())))

def roll_nl(n=2, d=6):
    """
    >>> random.seed("test")
    >>> roll_nl()
    12
    """
    def dice():
        nonlocal total
        points= tuple(random.randint(1,d) for _ in range(n))
        total = sum(points)
        return points
    total= 0
    dice()
    return total

lambda_example = """
>>> colors = [
... (255,160,137),
... (143, 80,157),
... (255,255,255),
... (162,173,208),
... (255, 67,164),
... ]
>>> sorted(colors)
[(143, 80, 157), (162, 173, 208), (255, 67, 164), (255, 160, 137), (255, 255, 255)]
>>> sorted(colors,
...     key= lambda rgb: (rgb[0]+rgb[1]+rgb[2])/3)
[(143, 80, 157), (255, 67, 164), (162, 173, 208), (255, 160, 137), (255, 255, 255)]
>>> sorted(colors,
...     key= lambda rgb: max(rgb[0], rgb[1], rgb[2]))
[(143, 80, 157), (162, 173, 208), (255, 160, 137), (255, 255, 255), (255, 67, 164)]
>>> sorted(colors,
...     key= lambda rgb: 0.5*max(rgb[0], rgb[1], rgb[2])+0.5*min(rgb[0], rgb[1], rgb[2]))
[(143, 80, 157), (255, 67, 164), (162, 173, 208), (255, 160, 137), (255, 255, 255)]

>>> def brightness(rgb):
...     return (rgb[0]+rgb[1]+rgb[2])/3
>>> sorted(colors, key= brightness)
[(143, 80, 157), (255, 67, 164), (162, 173, 208), (255, 160, 137), (255, 255, 255)]

"""

def roller( n: int, d: int = 6 ) -> tuple:
    """
    >>> random.seed("test")
    >>> roller(2)
    (6, 6)
    """
    return tuple(random.randint(1,d) for _ in range(n))

__test__ = {
    'default_examples': default_examples,
    'lambda_example': lambda_example,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=0 )