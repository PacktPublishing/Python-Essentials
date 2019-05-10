#!/usr/bin/env python3
"""Python Essentials

Chapter 10, Example Set 4
"""


import sys
from Chapter_10.ch10_ex1 import tests_run
import csv
import re

def log_parser(source):
    metrics_pat = re.compile(r"\s*([\w ]+):\s+(\d+\.?\d*)\s*")
    module_pat= re.compile(r"Running\s*(.*)")
    date_pat= re.compile(r"Finished at:\s*(.*)")
    sample= {}
    for line in source:
        match_metrics= metrics_pat.findall(line)
        if match_metrics:
            candidate= { name.lower().replace(" ","_"): value
                    for name, value in match_metrics }
            if 'time_elapsed' in candidate:
                sample.update( candidate )
            continue
        match_module= module_pat.search(line)
        if match_module:
            sample['module']= match_module.group(1)
            continue
        match_date= date_pat.search(line)
        if match_date:
            sample['datetime']= match_date.group(1)
    return sample

import csv
TEST_LOG_SUMMARY = ("module", "datetime", "tests_run", "failures", "errors", "skipped", "time_elapsed")

def mapper(name_iter, result):
    writer= csv.DictWriter(result, fieldnames=TEST_LOG_SUMMARY, delimiter='|')
    for name in name_iter:
        with open(name) as source:
            writer.writerow( log_parser(source) )
            
from collections import Counter
def reducer(source, result):
    reader= csv.DictReader(source, fieldnames=TEST_LOG_SUMMARY, delimiter='|')
    by_errors= Counter()
    for row in reader:
        by_errors[row['module'],row['errors']] += 1
    print( by_errors )

import glob
import io
pipeline = io.StringIO()
mapper( glob.glob("Chapter_10/log_*.txt"), pipeline)

pipeline.seek(0)
reducer( pipeline, sys.stdout )