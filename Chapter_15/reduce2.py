#!/usr/bin/env python3
'''Python Essentials

Chapter 15, Example Set 5 - reducer 2 - city/month snow
'''

import csv
import sys
from collections import defaultdict, namedtuple

Datum = namedtuple('Datum', ('station', 'month', 'snowfall'))

def parser(reader):
    for line in rdr:
        station, month = line['station-month'].split('-')
        yield Datum( station, month, line['snowfall'] )

def group_by_station(parsed_reader):
    init= next(parsed_reader)
    data = [init]
    for line in parsed_reader:
        if data[0].station != line.station:
            yield data
            data = []
        data.append( line )
    yield data

if __name__ == "__main__":
    rdr= csv.DictReader(
        sys.stdin, fieldnames=("station-month","snowfall"),
        delimiter='\t', lineterminator='\n')
    for station_data in group_by_station( parser(rdr) ):
        maximum= max(station_data, key=lambda x: x.snowfall)
        print( maximum.station, maximum.month, maximum.snowfall )