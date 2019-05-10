#!/usr/bin/env python3
"""Python Essentials

Chapter 12, Script 3
"""

def temp_convert():
    while True:
        u = input( "Units [F,C,quit]: " )
        if u.upper().startswith("F"):
            f= float(input("Temperature °F: "))
            c= 5*(f-32)/9
        elif u.upper().startswith("C"):
            c= float(input("Temperature °C: "))
            f = 32+9*c/5
        elif u == "quit":
            break
        else:
            print("Unknown units '{0}'".format(u))
            continue
        print("°C={c:.0f} °F={f:.0f}".format(c=c, f=f))

if __name__ == "__main__":
    temp_convert()