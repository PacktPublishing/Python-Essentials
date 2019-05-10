#!/usr/bin/env python3
"""Python Essentials

Chapter 14, Example Set 1

Note that there are a several platform-specific examples in here which
may not work precisely as shown.

Most floating-point math should be wrapped in ``round( , 4)`` to be
completely platform-neutral.
"""

import doctest
import unittest
import glob
import os

def doctest_suite():
    files = glob.glob("Chapter*/ch*_ex*.py")
    by_chxx= lambda name: name.partition(".")[2].partition("_")[0]
    modules = sorted(
        (".".join(f.replace(".py","").split(os.sep)) for f in files),
        key=by_chxx)
    suites= [doctest.DocTestSuite( m ) for m in modules]
    return unittest.TestSuite( suites )

from Chapter_7.ch07_ex1 import FtoC

class Test_FtoC(unittest.TestCase):
    def setUp(self):
        self.temps= [50, 60, 72]
    def test_single(self):
        self.assertAlmostEqual(0.0, FtoC(32))
        self.assertAlmostEqual(100.0, FtoC(212))
    def test_map(self):
        temps_c = list(map(FtoC, self.temps))
        self.assertEqual(3, len(temps_c))
        rounded = [round(t,3) for t in temps_c]
        self.assertEqual([10.0, 15.556, 22.222], rounded)

class Test_FtoC2(unittest.TestCase):
    ε = 1E-6
    def runTest(self):
        c32 = FtoC(32)
        assert isinstance(c32, float), "Wrong type of result"
        assert abs(c32) <= self.ε
        c212 = FtoC(212)
        assert isinstance(c212, float), "Wrong type of result"
        assert abs(c212-100) <= self.ε

import csv
from types import SimpleNamespace
class Test_FtoC_Bulk(unittest.TestCase):
    ε = 1E-6
    def runTest(self):
        with open("Chapter_14/sample_data.csv") as source:
            rdr = csv.DictReader(source)
            cases = (SimpleNamespace(**row_dict) for row_dict in rdr)
            for case in cases:
                self.assertAlmostEqual( float(case.c), FtoC(float(case.f)) )

def suite():
    return unittest.TestSuite( [
        doctest_suite(),
        unittest.defaultTestLoader.loadTestsFromTestCase(Test_FtoC),
        unittest.defaultTestLoader.loadTestsFromTestCase(Test_FtoC2),
        unittest.defaultTestLoader.loadTestsFromTestCase(Test_FtoC_Bulk),
        ] )

if __name__ == "__main__":
    runner= unittest.TextTestRunner( verbosity=1 )
    all_tests = unittest.TestSuite( suite() )
    runner.run( all_tests )
