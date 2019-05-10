#!/usr/bin/env python3
"""Python Essentials

Chapter 10, Example Set 2
"""

import contextlib
import shelve
def populate():
    with contextlib.closing(
      shelve.open("Chapter_10/shelf","n")) as shelf:
        with open("Chapter_10/10letterwords.txt") as source:
            txt_stripped= (l.strip() for l in source)
            txt_non_empty= (l for l in txt_stripped
                            if l and not l.startswith("Tool") )
            #txt_non_empty= filter(lambda l: l and not l.startswith("Tool"), txt_stripped )
            for word in txt_non_empty:
                key = "word_list:{0}".format(word[0])
                try:
                    word_list= shelf[key]
                except KeyError:
                    word_list= []
                word_list.append(word)
                shelf[key]= word_list

def counts():
    with contextlib.closing(shelve.open("Chapter_10/shelf","r")) as shelf:
        #query_word_list = sorted(k for k in shelf.keys()
        #                         if k.startswith("word_list:"))
        query_word_list = sorted(
            filter(
                lambda k: k.startswith("word_list:"), shelf.keys()))
        for key in query_word_list:
            class_name, _, letter = key.partition(":")
            print( letter, len(shelf[key]) )

shelf_1 = """
>>> populate()
>>> counts()
a 55
b 81
c 111
d 62
e 22
f 56
g 36
h 49
i 36
j 14
k 7
l 34
m 59
n 25
o 68
p 119
q 6
r 46
s 100
t 32
u 36
v 21
w 17
x 3
"""

__test__ = {
    'shelf_1': shelf_1,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )
