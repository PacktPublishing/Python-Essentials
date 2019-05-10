#!/usr/bin/env python3
"""Python Essentials

Chapter 15, Script 1
"""
import sys
import argparse
import logging

logger= logging.getLogger(__name__)

def convert(c):
    """
    >>> convert(100)
    C=100°, F=212°
    """
    f = 32+9*c/5
    print("C={c:.0f}°, F={f:.0f}°".format_map(locals()))

def main():
    parser= argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose",
        action="store_const", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument("c", type=float)
    options= parser.parse_args()

    logging.getLogger().setLevel(options.verbose)
    logger.debug("Converting '{0!r}'".format(options.c))
    convert(options.c)

if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    main()
    logging.shutdown()