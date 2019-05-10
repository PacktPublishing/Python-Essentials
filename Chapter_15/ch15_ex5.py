#!/usr/bin/env python3
'''Python Essentials

Chapter 15, Example Set 5 - pipeline

We have two datasets:

-   479371.csv has snowfall and depth

-   526212.csv has snowfall and temperature

'''

import subprocess
import platform

dataset = "526212.csv"
#dataset = "479371.csv"

if platform.system() == "Windows":
    command = """type {dataset} | python -m Chapter_15.map | sort |
    python -m Chapter_15.reduce"""
else:
    command = """cat {dataset} | python3 -m Chapter_15.map | sort |
    python3 -m Chapter_15.reduce"""
command = command.format_map(locals())

if __name__ == "__main__":
    result= subprocess.check_output(command, shell=True)
    for line in result.splitlines():
        print( line.decode("ASCII") )
