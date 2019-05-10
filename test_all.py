#!/usr/bin/env python3
"""Run all the chapter modules, doctests or performance() function

This is run from the top-level directory, where all of the sample
data files are also located.

When runnning individual examples, the working directory is expected
to be the top-level directory, also.

Note that we exclude Chapter_15.ch15_ex4 because it imports Flask
at the top level, causing problems.
"""
import doctest
import glob
import unittest
import sys
import os

def doctest_suite():
    def flask_module(name):
        return name in ("Chapter_15/ch15_ex4.py",)
    files = glob.glob("Chapter*/ch*_ex*.py")
    passed_files= filter( lambda x: not flask_module(x), files )
    by_chxx= lambda name: name.partition(".")[2].partition("_")[0]
    modules = sorted(
        (".".join(f.replace(".py","").split(os.sep)) for f in passed_files),
        key=by_chxx)
    suites= [doctest.DocTestSuite( m ) for m in modules]
    return unittest.TestSuite( suites )

def unittest_suite():
    import Chapter_14.ch14_ex1
    suite= unittest.defaultTestLoader.loadTestsFromModule(Chapter_14.ch14_ex1)
    return suite

if __name__ == "__main__":
    suite= unittest.TestSuite( [doctest_suite(), unittest_suite()] )
    runner= unittest.TextTestRunner( verbosity=1 )
    runner.run( suite )
