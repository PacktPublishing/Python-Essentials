#!/usr/bin/env python3
"""Python Essentials

Chapter 8, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

generators= """
>>> (2*x+1 for x in range(5)) # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>
>>> tuple(2*x+1 for x in range(5))
(1, 3, 5, 7, 9)
>>> x= (2*x+1 for x in range(20))
>>> sum(x)
400
>>> sum(x)
0
>>> deck= list((r,s) for s in '♣♦♥♠' for r in range(1,14))
>>> deck # doctest: +ELLIPSIS
[(1, '♣'), (2, '♣'), (3, '♣'), ... (11, '♠'), (12, '♠'), (13, '♠')]
>>> len(deck)
52
>>> list(x for x in range(36) if x%5 == 0 or x%7 == 0)
[0, 5, 7, 10, 14, 15, 20, 21, 25, 28, 30, 35]
"""

comprehensions="""
>>> l= [2*x+1 for x in range(5)]
>>> l
[1, 3, 5, 7, 9]

>>> s= {x for x in range(36) if x%5 == 0 or x%7 == 0}
>>> s # doctest: +SKIP
{0, 35, 5, 7, 10, 14, 15, 20, 21, 25, 28, 30}
>>> sorted(s)
[0, 5, 7, 10, 14, 15, 20, 21, 25, 28, 30, 35]

>>> d = {n:2*n**2-3*n-14 for n in range(-5,6)}
>>> d
{0: -14, 1: -15, 2: -12, 3: -5, 4: 6, -2: 0, -5: 51, -4: 30, -3: 13, -1: -9, 5: 21}

"""

complex_comprehensions = """
>>> text= '''Poe, E.
... Near a Raven
...
... Midnights so dreary, tired and weary,
... Silently pondering volumes extolling all by-now obsolete lore.
... During my rather long nap - the weirdest tap!
... An ominous vibrating sound disturbing my chamber's antedoor.
... "This", I whispered quietly, "I ignore".'''
>>> for punct in ',.-!"':
...    text= text.replace(punct,'')
>>> words= {w.lower(): len(w) for w in text.split()}
>>> words # doctest: +SKIP
{'quietly': 7, 'Silently': 8, 'Raven': 5, 'dreary': 6, 'lore': 4, 'obsolete': 8, 'nap': 3, 'ominous': 7, 'rather': 6, 'An': 2, 'long': 4, 'tap': 3, 'pondering': 9, 'all': 3, 'bynow': 5, "chamber's": 9, 'weary': 5, 'so': 2, 'extolling': 9, 'Poe': 3, 'sound': 5, 'disturbing': 10, 'Midnights': 9, 'Near': 4, 'my': 2, 'weirdest': 8, 'whispered': 9, 'and': 3, 'This': 4, 'tired': 5, 'antedoor': 8, 'a': 1, 'I': 1, 'During': 6, 'volumes': 7, 'the': 3, 'E': 1, 'vibrating': 9, 'ignore': 6}
>>> [(w,words[w]) for w in sorted(words)] # doctest: +ELLIPSIS
[('a', 1), ('all', 3), ('an', 2), ... ('weary', 5), ('weirdest', 8), ('whispered', 9)]

>>> import datetime
>>> day_1 = (datetime.date(2015,m,1) for m in range(1,13))
>>> starts_on = { d.month: d.strftime("%A") for d in day_1 }
>>> starts_on
{1: 'Thursday', 2: 'Sunday', 3: 'Sunday', 4: 'Wednesday', 5: 'Friday', 6: 'Monday', 7: 'Wednesday', 8: 'Saturday', 9: 'Tuesday', 10: 'Thursday', 11: 'Sunday', 12: 'Tuesday'}

>>> import math
>>> step_radian = ( (s, math.pi*s/256) for s in range(128) )
>>> cos_table = { s: math.cos(r) for s, r in step_radian }
>>> [(a,round(cos_table[a],4)) for a in range(128)] # doctest: +ELLIPSIS
[(0, 1.0), (1, 0.9999), (2, 0.9997), ... (125, 0.0368), (126, 0.0245), (127, 0.0123)]
"""

def model_iter(until):
    """
    >>> list(model_iter(6))
    [0, 1, 3, 6, 10, 15]
    >>> mean = sum(model_iter(6))/6
    >>> round(mean, 4)
    5.8333
    >>> head, *rest = model_iter(6)
    >>> head
    0
    >>> rest
    [1, 3, 6, 10, 15]
    """
    for n in range(0, until):
        yield n*(n+1)//2

map_filter = """
>>> mapping= map( lambda x: 2*x**2-2, range(5) )
>>> list(mapping)
[-2, 0, 6, 16, 30]
>>> fb= filter( lambda n: n%5==0 or n%7==0, range(16) )
>>> [n for n in fb]
[0, 5, 7, 10, 14, 15]
"""

def text_cleaner( source ):
    """
    >>> text = '''
    ... # options
    ... db=name # database
    ...  task=delete # task
    ... '''.splitlines()
    >>> for line in text_cleaner(text):
    ...    print(line)
    db=name
    task=delete
    """
    stripped = (line.strip() for line in source)
    partitioned = (line.partition("#") for line in stripped)
    decommented = (data.rstrip() for data, sharp, comment in partitioned)
    non_empty = (line for line in decommented if line)
    return non_empty

import types
def get_options( source ):
    """
    >>> text = ["# options\\n", "db=name # database\\n", "task=delete # task\\n", "\\n"]
    >>> get_options( text )
    namespace(db='name', task='delete')
    """
    cleaned= text_cleaner(source)
    nv = (line.partition("=") for line in cleaned)
    dict_opt = { name: (value or True) for name, _, value in nv }
    return types.SimpleNamespace( **dict_opt )

reductions = """
>>> data = ["21", "3", "35", "4"]
>>> min(data)
'21'
>>> min(data, key=int)
'3'
"""

get_opendatasites = """
>>> import csv
>>> with open("opendatasites1.csv", newline="", encoding='mac-roman') as source:
...     rdr= csv.reader(source)
...     content= list(rdr)
>>> content # doctest: +ELLIPSIS
[['Item', 'Link', 'Type'], ...]
>>> head, *data = content
>>> head
['Item', 'Link', 'Type']
>>> len(data)
303
"""

get_metrics = """
>>> import csv
>>> with open("metric.csv", newline="") as source:
...     rdr= csv.reader(source)
...     content= list(rdr)
>>> content # doctest: +ELLIPSIS
[['date', 'count'], ['2013-09-10', '289'], ['2013-09-11', '616'], ...]
>>> head, *data = content
>>> head
['date', 'count']
>>> len(data)
90
>>> data # doctest: +ELLIPSIS
[['2013-09-10', '289'], ['2013-09-11', '616'], ... ['2013-12-07', '752'], ['2013-12-08', '739']]
>>> data.sort( key=lambda x: int(x[1]) )
>>> data # doctest: +ELLIPSIS
[['2013-10-21', '30'], ['2013-10-27', '171'], ... ['2013-11-11', '1068'], ['2013-10-04', '1441']]
>>> by_count= sorted( data, key=lambda x: int(x[1]) )
>>> by_count # doctest: +ELLIPSIS
[['2013-10-21', '30'], ['2013-10-27', '171'], ... ['2013-11-11', '1068'], ['2013-10-04', '1441']]

>>> wrapped = [(int(x[1]), x) for x in data]
>>> wrapped.sort()
>>> by_count = [x[1] for x in wrapped]
>>> by_count # doctest: +ELLIPSIS
[['2013-10-21', '30'], ['2013-10-27', '171'], ... ['2013-11-11', '1068'], ['2013-10-04', '1441']]

>>> wrapped = map( lambda item: (int(item[1]), item), data )
>>> sorted= sorted(wrapped)
>>> by_count = map( lambda pair: pair[1], sorted )
>>> list(by_count) # doctest: +ELLIPSIS
[['2013-10-21', '30'], ['2013-10-27', '171'], ... ['2013-11-11', '1068'], ['2013-10-04', '1441']]

"""

__test__ = {
    'generators': generators,
    'comprehensions': comprehensions,
    'complex_comprehensions': complex_comprehensions,
    'map_filter': map_filter,
    'reductions': reductions,
    'not_used': get_opendatasites,
    'get_metrics': get_metrics,
}


if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=0 )