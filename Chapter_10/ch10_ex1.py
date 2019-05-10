#!/usr/bin/env python3
"""Python Essentials

Chapter 10, Example Set 1
"""

file_1= """
>>> my_file = open( "Chapter_10/10letterwords.txt" )
>>> text= my_file.read().splitlines()
>>> text[:5]
['consultive', 'syncopated', 'forestland', 'postmarked', 'configures']
>>> text[-5:]
['mistouched', 'clamouring', 'coadjutrix', '', 'Tool completed successfully']

"""


file_2= """
>>> code_file = open("Chapter_1/ch01_ex1.py", "rt", encoding="utf-8", errors="replace")
>>> code_lines = list(code_file)
>>> code_lines[:5]
['#!/usr/bin/env python3\\n', '\"\"\"Python Essentials\\n', '\\n', 'Chapter 1, Example Set 1\\n', '\\n']
"""

file_2a= """
>>> code_file = open("Chapter_1/ch01_ex1.py", "rt", encoding="utf-8", errors="replace")
>>> code_lines = list(line.rstrip() for line in code_file)
>>> code_lines[:5]
['#!/usr/bin/env python3', '\"\"\"Python Essentials', '', 'Chapter 1, Example Set 1', '']

"""

file_2b= """
>>> code_file = open("Chapter_1/ch01_ex1.py", "rt", encoding="utf-8", errors="replace")
>>> txt_stripped = (line.rstrip() for line in code_file)
>>> txt_non_empty= (line for line in txt_stripped if line)
>>> code_lines= list(txt_non_empty)
>>> code_lines[:5]
['#!/usr/bin/env python3', '\"\"\"Python Essentials', 'Chapter 1, Example Set 1', 'Note that there are a several platform-specific examples in here which', 'may not work precisely as shown.']
"""


file_3= """
>>> raw_bytes = open("Chapter_10/favicon.ico", "rb" )
>>> data = raw_bytes.read()
>>> len(data)
894
>>> data[:22]
b'\\x00\\x00\\x01\\x00\\x01\\x00\\x10\\x10\\x00\\x00\\x00\\x00\\x18\\x00h\\x03\\x00\\x00\\x16\\x00\\x00\\x00'

>>> import struct
>>> struct.unpack( "<hhhbbbbhhii", data[:22] )
(0, 1, 1, 16, 16, 0, 0, 0, 24, 872, 22)
"""

import re
def tests_run(log_file):
    """
    >>> import io
    >>> data = io.StringIO(
    ... '''
    ... Tests run: 1, Failures: 2, Errors: 0, Skipped: 1, Time elapsed: 0.547 sec
    ... Other data
    ... Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.018 sec
    ... ''')
    >>> list( tests_run(data) ) # doctest: +NORMALIZE_WHITESPACE
    [[('Tests run', '1'), ('Failures', '2'), ('Errors', '0'), ('Skipped', '1'), ('Time elapsed', '0.547')],
    [('Tests run', '1'), ('Failures', '0'), ('Errors', '0'), ('Skipped', '0'), ('Time elapsed', '0.018')]]
    """
    data_pat = re.compile(r"\s*([\w ]+):\s+(\d+\.?\d*)\s*")
    for line in log_file:
        match= data_pat.findall(line)
        if match:
            yield match

def read_log():
    """
    >>> import os
    >>> try:
    ...     os.unlink("Chapter_10/summary.txt")
    ... except FileNotFoundError:
    ...     pass
    >>> read_log()
    >>> with open("Chapter_10/summary.txt") as result:
    ...    print( result.read() )
    [('Tests run', '1'), ('Failures', '0'), ('Errors', '0'), ('Time elapsed', '0')]
    [('Tests run', '1'), ('Failures', '0'), ('Errors', '0')]
    [('Total time', '15')]
    [('Final Memory', '2')]
    <BLANKLINE>
    """
    with open("Chapter_10/log_example.txt") as source:
        with open("Chapter_10/summary.txt", "w") as target:
            for stats in tests_run(source):
                print( stats, file=target )

def read_log2():
    """
    >>> import os
    >>> try:
    ...     os.unlink("Chapter_10/summary.txt")
    ... except FileNotFoundError:
    ...     pass
    >>> read_log2()
    >>> with open("Chapter_10/summary.txt") as result:
    ...    print( result.read() )
    [('Tests run', '1'), ('Failures', '0'), ('Errors', '0'), ('Time elapsed', '0')]
    [('Tests run', '1'), ('Failures', '0'), ('Errors', '0')]
    [('Total time', '15')]
    [('Final Memory', '2')]
    <BLANKLINE>
    """
    file_in= "Chapter_10/log_example.txt"
    file_out= "Chapter_10/summary.txt"
    with open(file_in) as source, open(file_out, "w") as target:
        for stats in tests_run(source):
            print( stats, file=target )

import http.client
def bad_rest():
    """
    >>> bad_rest() # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AttributeError: __exit__
    """
    with http.client.HTTPConnection("www.example.com") as host:
        host.request("GET", "/path/to/resources/12345")
        response= host.getresponse()
        print(response.read())

import contextlib
def good_rest():
    """
    This test requires a working internet connection.
    If there's no working connection, this test will fail.

    >>> good_rest() # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    b'<!doctype html>\\n<html>\\n<head>\\n    <title>Example Domain</title>...

    We've seen some slight variation in the response produced by this
    example. In some cases, it may be necessary to skip this test because
    firewalls may interfere with it.
    """
    with contextlib.closing(http.client.HTTPConnection("www.example.com")) as host:
        host.request("GET", "/path/to/resources/12345")
        response= host.getresponse()
        print(response.read())

__test__ = {
    'file_1': file_1,
    'file_2': file_2,
    'file_2a': file_2a,
    'file_2b': file_2b,
    'file_3': file_3,
}

if __name__ == "__main__":
    import doctest
    doctest.testmod( verbose=1 )