#!/usr/bin/env python

import math

def quadratic(a,b,c):
    x1 = ( -b + math.sqrt(b**2 - 4*a*c) ) / ( 2 * a)
    x2 = ( -b - math.sqrt(b**2 - 4*a*c) ) / ( 2 * a)

    return x1,x2

out1,out2 = quadratic(1,6,3)

print out1, out2
