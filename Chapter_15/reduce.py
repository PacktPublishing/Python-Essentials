#!/usr/bin/env python3
'''Python Essentials

Chapter 15, Example Set 5 - reducer 1 - months with snow
'''

import csv
import sys
from collections import Counter
from decimal import Decimal

if __name__ == "__main__":
    rdr= csv.DictReader(
        sys.stdin, fieldnames=("month","snowfall"),
        delimiter='\t', lineterminator='\n')
    counts = Counter()
    for line in rdr:
        counts[line['month']] += Decimal(line['snowfall'])
    print( counts )