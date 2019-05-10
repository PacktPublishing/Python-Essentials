#!/usr/bin/env python3
'''Python Essentials

Chapter 15, Example Set 5 - mapper

TSNW - Total snow fall (1/10th inch)

MMXT - Monthly Mean maximum temperature (1/10th degree)

MXSD - Maximum snow depth reported during month (inch)

Different datasets will have different combinations of measures.
'''

import csv
import sys
import datetime
from decimal import Decimal

if __name__ == "__main__":

    rdr = csv.DictReader(sys.stdin)
    wtr = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    for row in rdr:
        date = datetime.datetime.strptime(row['DATE'], "%Y%m%d").date()
        if row['TSNW'] in ('0', '-9999', '9999'):
            continue # Zero or equipment error: reject
        wtr.writerow( [date.month, Decimal(row['TSNW'])/10] )