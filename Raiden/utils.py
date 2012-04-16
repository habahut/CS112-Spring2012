#!/usr/bin/env python
"""
Utitlites and such
"""

from math import sqrt

timeScale = 1000.0

def normalize(a, b):
    if (a == 0) and (b == 0):
        return 0,0
    else:
        d = a**2 + b**2
        d = sqrt(float(d))
        return a/d,b/d

def getTimeScale():
    return timeScale

def setTimeScale(t):
    timeScale = t
    
    
