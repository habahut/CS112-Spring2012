#!/usr/bin/env python

from functions import *
import NewFolder.day3

"""
import functions as better_name

better_name.A
better_name.B
"""

def print_globals():
    k = None
    for k in globals():
        print k

print_globals()
