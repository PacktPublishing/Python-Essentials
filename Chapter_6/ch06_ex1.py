#!/usr/bin/env python3
"""Python Essentials

Chapter 6, Example Set 1
"""

list_example = """
>>> vred = (247, 83, 148)
>>> vred[1] = 23 # doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment
>>> fib_list = [1, 1, 3, 5, 8]
>>> fib_list.append(fib_list[-2] + fib_list[-1])
>>> fib_list
[1, 1, 3, 5, 8, 13]
>>> fib_list[2]
3
>>> fib_list[2:5]
[3, 5, 8]
>>> fib_list[2:]
[3, 5, 8, 13]
>>> fib_list[:-1]
[1, 1, 3, 5, 8]
>>> fib_list[::2]
[1, 3, 8]
>>> fib_list[1::2]
[1, 5, 13]
>>> fib_list[0]= 1
>>> x = fib_list[:]
>>> x[2:5]= [3]
>>> x
[1, 1, 3, 13]
>>> fib_list
[1, 1, 3, 5, 8, 13]
>>> fib_list.extend( [21, 34] )
>>> fib_list
[1, 1, 3, 5, 8, 13, 21, 34]
>>> fib_list.insert(0, 0)
>>> fib_list
[0, 1, 1, 3, 5, 8, 13, 21, 34]
>>> fib_list.reverse()
>>> fib_list
[34, 21, 13, 8, 5, 3, 1, 1, 0]
>>> fib_list.sort()
>>> fib_list
[0, 1, 1, 3, 5, 8, 13, 21, 34]
>>> fib_list.remove(34)
>>> fib_list
[0, 1, 1, 3, 5, 8, 13, 21]
>>> fib_list.pop()
21
>>> fib_list.pop(0)
0
>>> fib_list.count(1)
2
>>> fib_list.index(5)
3
>>> fib_list.copy()
[1, 1, 3, 5, 8, 13]
>>> 13 in fib_list
True
>>> 12 not in fib_list
True
"""

set_example_1 = """
>>> fib_set = {1, 1, 3, 5, 8}
>>> # order can't be guaranteed, skip the test
>>> fib_set #doctest: +SKIP
{8, 1, 3, 5}
>>> sorted(fib_set)
[1, 3, 5, 8]
>>> f_n = max(fib_set)
>>> f_n
8
>>> f_n1 = max(fib_set.difference({f_n}))
>>> f_n1
5
>>> fib_set.add(f_n+f_n1)
>>> sorted(fib_set)
[1, 3, 5, 8, 13]
"""

set_example_2 = """
>>> words = set("How I wish".split())
>>> words #doctest: +SKIP
{'How', 'I', 'wish'}
>>> sorted(words)
['How', 'I', 'wish']
>>> more = set("I could recollect pi".split())
>>> more #doctest: +SKIP
{'recollect', 'pi', 'I', 'could'}
>>> sorted(more)
['I', 'could', 'pi', 'recollect']
>>> words | more #doctest: +SKIP
{'wish', 'could', 'pi', 'I', 'How', 'recollect'}
>>> sorted(words | more)
['How', 'I', 'could', 'pi', 'recollect', 'wish']
>>> words & more
{'I'}
>>> words - more #doctest: +SKIP
{'How', 'wish'}
>>> sorted(words - more)
['How', 'wish']
>>> words ^ more #doctest: +SKIP
{'recollect', 'wish', 'pi', 'How', 'could'}
>>> sorted(words ^ more)
['How', 'could', 'pi', 'recollect', 'wish']
>>> {'I'} < words
True
>>> {'How', 'I', 'wish'} <= words
True
>>> {'How', 'I', 'wish'} == words
True
>>> 'I' in words
True
"""

dict_example = """
>>> sieve = {2: True, 3: True, 4: False, 5: True, 6: None, 7: None}
>>> sieve
{2: True, 3: True, 4: False, 5: True, 6: None, 7: None}
>>> sieve = dict(
... [(2, True), (3, True), (4, False), (5, True), (6, None), (7, None)]
... )
>>> sieve
{2: True, 3: True, 4: False, 5: True, 6: None, 7: None}
>>> cadaeic= dict( poe=3, e=1, near=4, a=1, raven=5, midnights= 9 )
>>> cadaeic # doctest: +SKIP
{'raven': 5, 'e': 1, 'near': 4, 'midnights': 9, 'poe': 3, 'a': 1}
>>> sorted(cadaeic.items())
[('a', 1), ('e', 1), ('midnights', 9), ('near', 4), ('poe', 3), ('raven', 5)]
>>> cadaeic['poe']
3
>>> cadaeic['so']= 2
>>> del cadaeic['so']
>>> cadaeic.update( {'so':2, 'dreary':6} )
>>> cadaeic.update( [('tired',5), ('and',3)], weary=5 )
>>> cadaeic # doctest: +SKIP
{'a': 1, 'weary': 5, 'near': 4, 'dreary': 6, 'e': 1, 'raven': 5, 'midnights': 9, 'and': 3, 'so': 2, 'poe': 3, 'tired': 5}
>>> sorted(cadaeic.items())
[('a', 1), ('and', 3), ('dreary', 6), ('e', 1), ('midnights', 9), ('near', 4), ('poe', 3), ('raven', 5), ('so', 2), ('tired', 5), ('weary', 5)]

>>> counter = {}
>>> counter.setdefault('a',0)
0
>>> counter['a'] += 1
>>> counter['b'] = counter.setdefault('b',0) + 1
>>> counter #doctest: +SKIP
{'a': 1, 'b': 1}

>>> sorted(counter.items())
[('a', 1), ('b', 1)]
"""

counter_example = '''
>>> from collections import Counter
>>> text = """Poe, E.
... Near a Raven
...
... Midnights so dreary, tired and weary,
... Silently pondering volumes extolling all by-now obsolete lore.
... During my rather long nap - the weirdest tap!
... An ominous vibrating sound disturbing my chamber's antedoor.
... "This", I whispered quietly, "I ignore"."""
>>> freq= Counter(text)
>>> # 'r' and 'i' are tied, test is awkwardly incorrect sometimes
>>> freq.most_common(5) #doctest: +SKIP
[(' ', 35), ('e', 23), ('n', 18), ('r', 17), ('i', 17)]
>>> sorted(freq.most_common(5), key= lambda x: (-x[1], x[0]))
[(' ', 35), ('e', 23), ('n', 18), ('i', 17), ('r', 17)]
'''

for_example= """
>>> text = '''Poe, E.
...      Near a Raven
...
... Midnights so dreary, tired and weary.'''
>>> text = text.replace(",","").replace(".","").lower()
>>> cadaeic= {}
>>> for word in text.split():
...     cadaeic[word]= len(word)
>>> cadaeic # doctest: +SKIP
{'raven': 5, 'midnights': 9, 'dreary': 6, 'e': 1, 'weary': 5, 'near': 4, 'a': 1, 'poe': 3, 'and': 3, 'so': 2, 'tired': 5}
>>> sorted(cadaeic.items())
[('a', 1), ('and', 3), ('dreary', 6), ('e', 1), ('midnights', 9), ('near', 4), ('poe', 3), ('raven', 5), ('so', 2), ('tired', 5), ('weary', 5)]
>>> for word in sorted(cadaeic):
...    print(word,  cadaeic[word])
...
a 1
and 3
dreary 6
e 1
midnights 9
near 4
poe 3
raven 5
so 2
tired 5
weary 5

>>> for item in 1,2,3:
...     print(item)
...     if item == 2:
...         print("Found",item)
...         break
... else:
...     print("Found Nothing")
...
1
2
Found 2

>>> for item in 1,2,3:
...     print(item)
...     if item == 0:
...         print("Found",item)
...         break
... else:
...     print("Found Nothing")
...
1
2
3
Found Nothing

"""

range_example = """
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> tuple(range(-1,3))
(-1, 0, 1, 2)
"""

fizzbuzz= """
>>> for n in range(1, 21):
...    status= str(n)
...    if n % 5 == 0: status += " fizz"
...    if n % 7 == 0: status += " buzz"
...    print(status)
1
2
3
4
5 fizz
6
7 buzz
8
9
10 fizz
11
12
13
14 buzz
15 fizz
16
17
18
19
20 fizz
"""

while_not_exists = """
>>> condition= lambda x: x%5 == 0 and x%7 == 0
>>> numbers = iter(range(1,101))
>>> n = next(numbers)
>>> while not condition(n):
...     n = next(numbers)
>>> print(n)
35

>>> condition= lambda x: False
>>> numbers = iter(range(1,101))
>>> n = next(numbers)
>>> while not condition(n): #doctest: +ELLIPSIS
...     n = next(numbers)
Traceback (most recent call last):
...
StopIteration

>>> condition= lambda x: x%5 == 0 and x%7 == 0
>>> n = 1
>>> while n != 101 and not condition(n):
...     n += 1
>>> print(n)
35
"""

def perfect():
    """
    >>> perfect()
    6
    """
    for n in range(1, 100):
        factors = []
        for x in range(1,n):
            if n % x == 0: factors.append(x)
        if sum(factors) == n:
            break
    return n

def perfect2():
    """
    >>> perfect2()
    6
    """
    for n in range(1, 100):
        factors = [x for x in range(1,n) if n % x == 0]
        if sum(factors) == n:
            break
    return n


__test__ = {
    'list_example': list_example,
    'set_example_1': set_example_1,
    'set_example_2': set_example_2,
    'dict_example': dict_example,
    'counter_example': counter_example,
    'for_example': for_example,
    'range_example': range_example,
    'fizzbuzz': fizzbuzz,
    'while_not_exists': while_not_exists,
}


if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )