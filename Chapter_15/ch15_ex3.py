#!/usr/bin/env python3
"""Python Essentials

Chapter 15, Example Set 3
"""
from turtle import *

def on_screen():
    x, y = pos()
    w, h = screensize()
    return -w <= x < w and -h <= y < h

def spiral(angle, incr, size=10):
    while on_screen():
        right(angle)
        forward(size)
        size *= incr

if __name__ == "__main__":
    speed(10)
    spiral(size=10, incr=1.05, angle = 67)
    done()
