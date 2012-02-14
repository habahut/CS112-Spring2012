#!/usr/bin/env python
"""lists.py

A bunch of excercises to see if you understand list comprehensions
"""

# Solve the following problems with one python statement.  It is fine 
# to break up the statement into multiple lines as long as it is only
# one actual command.
#
# This is fine:
#   print [ (x,y) 
#           for x in range(10)
#           for y in range(10) ]
#

# 1. Read a bunch of numbers from the input separated by spaces and 
#    convert them to ints
#nums = map(int, raw_input("enter some numbers seperated by spaces ").split())
print "1.", [ int(s) for s in raw_input("Enter some numbers separated by spaces:  ").split() ]

# 2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3
print "2.", [ int(s) for s in raw_input("Enter some numbers separated by spaces:  ").split() ][:3]

# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts
print "3.", [ len(s.strip()) for s in raw_input("Enter some qords seperated by commas  ").split(",")]

# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index
#        ex:  [ [0,3], [1,6], [2,9]...]
print "4.", [ list(enumerate(range(3,100,3))) ]
#print "4.", [ (i,v) for i,v in enumerate(range(3,100,3)) ]

# 5. create a list of every card in a deck of cards
print "5.", [ [value, suit] for suit in ["hearts","spades","clubs","diamonds"] for value in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]]

# 6.  Create a 5 by 5 array filled with zeros
print "6.", [ [0 for n in range(5)]
              for n2 in range(5) ]


# 7.  Make a list of every perfect square between 1 and 1000
print "7.", [ n**2 for n in range(1, 32) ]

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
from math import sqrt
print "8.", [ n for n in range(1,1000) if sqrt(n)%1 == 0]

# 9.  List every python file in this directory
import os
print "9.", [s for s in os.listdir(".") if s.endswith("py")]

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])
print "10.", [ (x,y,z) for x in range(20)
                       for y in range(20)
                       for z in range(20)
                       if  x**2 + y**2 == z**2 and x <= y ]



# I couldn't in good concious include this, but it is fun to 
# figure out/find.

## NOT REQUIRED
# 11.  Print a list of every prime number less than 100
print "11.", []
