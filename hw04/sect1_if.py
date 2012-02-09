#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n % 2 == 1:
    print "1. odd"
    odd = True
else:
    print "1. even"
    odd = False

print
print "I kept using the same N, was unclear if you wanted to make different variabls or keep changing the same one"
print

# 2. If n is odd, double it
if odd:
    n *= 2
    
print "2.", n


# 3. If n is evenly divisible by 3, add four
if n % 3 == 0:
    n += 4

print "3.", n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade < 60:
    s = "F"
    
if grade < 70 and grade > 60:
    s = "D"
    
if grade < 80 and grade > 70:
    s = "C"

if grade < 90 and grade > 80:
    s = "B"

if grade > 90:
    s = "A"
    
print "4.",s

