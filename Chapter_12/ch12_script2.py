#!/usr/bin/env python3
"""Python Essentials

Chapter 12, Script 2
"""

def c_to_f():
    c= float(input("Temperature °C: "))
    f = 32+9*c/5
    print("C={c:.0f}°, F={f:.0f}°".format(c=c,f=f))

if __name__ == "__main__":
    c_to_f()