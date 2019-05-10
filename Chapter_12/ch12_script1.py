#!/usr/bin/env python3
"""Python Essentials

Chapter 12, Script 1
"""

c= float(input("Temperature °C: "))
f = 32+9*c/5
print("C={c:.0f}°, F={f:.0f}°".format(c=c,f=f))