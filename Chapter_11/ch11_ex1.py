#!/usr/bin/env python3
"""Python Essentials

Chapter 11, Example Set 1
"""
import math

class MyAppError(Exception):
    """
    >>> raise MyAppError("Some Message") # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    Chapter_11.ch11_ex1.MyAppError: Some Message
    """
    pass

class Point:
    """
    Point on a plane.

    Distances are calculated using hypotenuse.
    This is the "as a crow flies" straight line distance.

    >>> p_1 = Point(22, 7)
    >>> p_1.x
    22
    >>> p_1.y
    7
    >>> p_1
    Point(22, 7)

    >>> p_1.copy() # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AttributeError: 'Point' object has no attribute 'copy'

    >>> p_2 = Point(20, 5)
    >>> p_2.y = 6
    >>> p_2
    Point(20, 6)

    >>> getattr(p_2, "x")
    20

    >>> sorted(p_2.__dict__.keys())
    ['x', 'y']
    """
    def __init__(self, x, y):
        """Create a new point

        :param x: X coördinate
        :param y: Y coördinate
        """
        self.x= x
        self.y= y
    def __format__(self, fmt):
        """Format a point.

        Given an overall format string like "{0:(^x:2.1f$, ^y:2.1f$})",
        this function will receive the "(^x:2.1f$, ^y:2.1f$})" portion as the
        :param:`fmt` parameter.

        The ^...$ is translated to {...} and the resulting format
        string is then applied to the values of x and y from the point.

        >>> p_1 = Point(22, 7)
        >>> "{0:(^x:2.1f$, ^y:2.1f$})".format(p_1)
        '(22.0, 7.0)'

        :param fmt: Format details after {name:...} in a format string.
        :returns: formatted point.
        """
        fmt = fmt.replace("^","{").replace("$","}")
        return fmt.format(x=self.x, y=self.y)
    def __repr__(self):
        """Returns string representation of this Point."""
        return "{cls}({x:.0f}, {y:.0f})".format(
            cls=self.__class__.__name__, x=self.x, y=self.y)
    def dist(self, point):
        """Distance to another point measured on a plane.

        >>> p_1 = Point(22, 7)
        >>> p_2 = Point(20, 5)
        >>> round(p_1.dist(p_2),4)
        2.8284

        :param point: Another instance of Point.
        :returns: float distance.
        """
        return math.hypot(self.x-point.x, self.y-point.y)
    def offset(self, d_x, d_y):
        """Mutate this point to apply an offset, relocating the
        point.

        >>> p_1 = Point(22, 7)
        >>> p_1.offset(-3, 3)
        >>> p_1.x
        19
        >>> p_1.y
        10

        :param d_x: distance on the X axis
        :param d_y: distance on the Y axis.
        """
        self.x += d_x
        self.y += d_y
    @property
    def r(self):
        """
        Distance from the origin.

        >>> p = Point(12,5)
        >>> round(p.r,1)
        13.0
        >>> p.r= 14 # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute

        """
        return math.sqrt( self.x**2 + self.y**2 )
    @property
    def θ(self):
        """
        Angle from the origin.

        >>> import math
        >>> p = Point(12,5)
        >>> round(math.degrees(p.θ),1)
        22.6
        """
        return math.atan2(self.y, self.x)

class Manhattan_Point(Point):
    """
    Point on a plane. Distances are calculated as the sum of Δx+Δy.
    This is the "Manhaattan" distance measured in segments parallel
    to x and y axes. It's faster than the base class Point
    hypoteneuse calculation.

    >>> p_1 = Point(22, 7)
    >>> p_2 = Manhattan_Point(20, 5)
    >>> round(p_1.dist(p_2),4)
    2.8284
    >>> round(p_2.dist(p_1),4)
    4
    >>> p_2
    Manhattan_Point(20, 5)
    """
    def dist(self, point):
        return abs(self.x-point.x)+abs(self.y-point.y)

class Units(float):
    units= None
    def __repr__(self):
        text = super().__repr__()
        return "{0} {1}".format(text, self.units)

class Height(Units):
    """
    >>> Height(61.5)
    61.5 inches
    >>> data = [Height(60), Height(61), Height(62)]
    >>> avg= Height(sum(data)/len(data))
    >>> avg
    61.0 inches
    """
    units= "inches"

class Weight(Units):
    """
    >>> data = [Weight(185), Weight(175), Weight(165)]
    >>> avg= Weight(sum(data)/len(data))
    >>> avg
    175.0 pounds
    """
    units= "pounds"

class Sample:
    """
    >>> p1 = Sample(10)
    >>> p2 = Sample(8.5)
    >>> p3 = Sample(9.2)
    >>> p2.sequence
    2
    >>> Sample.validate(13) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: Out of range
    >>> try:
    ...     Sample.validate(11)
    ...     s = Sample(11)
    ... except Exception as e:
    ...     print(e)
    """
    counter= 0
    def __init__(self, measure):
        Sample.counter += 1
        self.sequence = Sample.counter
        self.measure = measure
    @staticmethod
    def validate( measure ):
        m= float(measure)
        if 0 <= m < 12:
            pass
        else:
            raise ValueError("Out of range")

class SmallSample:
    """
    >>> p1 = SmallSample(10)
    >>> p2 = SmallSample(8.5)
    >>> p3 = SmallSample(9.2)
    >>> p2.sequence
    2
    >>> p2.extra= 5 # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AttributeError: 'SmallSample' object has no attribute 'extra'
    """
    counter= 0
    __slots__ = ["sequence", "measure"]
    def __init__(self, measure):
        SmallSample.counter += 1
        self.sequence = SmallSample.counter
        self.measure = measure

from collections.abc import Callable
class Fibonacci(Callable):
    """Computes the nth Fibonacci number.

    :math:`F_n = F_{n-1} + F_{n-2}`.

    F_0 = 0
    F_1 = 1
    F_2 = 1
    F_3 = 2
    F_4 = 3
    F_5 = 5
    F_6 = 8
    F_7 = 13

    >>> fib= Fibonacci()
    >>> fib(7)
    13
    >>> fib.cache
    {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}
    """
    def __init__(self):
        self.cache= {0: 0, 1: 1}
    def __call__(self, n):
        if n not in self.cache:
            self.cache[n]= self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

map_1 = """
>>> list(map( lambda x:x+1, [1, 2.3, (4+5j)] ))
[2, 3.3, (5+5j)]
"""

__test__ = { "map_1": map_1 }

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )