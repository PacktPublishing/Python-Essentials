#!/usr/bin/env python3
"""Python Essentials

Chapter 10, Example Set 3
"""

import contextlib
import sqlite3 as SQL

def schema():
    with SQL.connect("Chapter_10/sqlite.sdb") as db:
        db.execute( """CREATE TABLE IF NOT EXISTS word(
                   letter VARCHAR(1),
                   word VARCHAR(10),
                   PRIMARY KEY (letter))
                   """)

def populate():
    with SQL.connect("Chapter_10/sqlite.sdb") as db:
        db.execute( """DELETE FROM word""" )
        with open("Chapter_10/10letterwords.txt") as source:
            txt_stripped= (l.strip() for l in source)
            txt_non_empty= (l for l in txt_stripped
                            if l and not l.startswith("Tool") )
            #txt_non_empty= filter(lambda l: l and not l.startswith("Tool"), txt_stripped )
            for word in txt_non_empty:
                db.execute( """INSERT INTO WORD(letter, word)
                           VALUES (:1, :2)""", (word[0], word) )


def counts():
    with SQL.connect("Chapter_10/sqlite.sdb") as db:
        counts= db.execute( """SELECT letter, COUNT(*)
                           FROM word
                           GROUP BY letter
                           ORDER BY 1""" )
        for letter, count in counts:
            print( letter, count )

shelf_1 = """
>>> schema()
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
