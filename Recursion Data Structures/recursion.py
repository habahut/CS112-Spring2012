#! usr/bin/env python

def factorial(n):
    if n <= 1:
        return n
    else:
        print n, " * factorial (",n-1,")"
        return n * factorial(n-1)


def beer(amount):
    if amount <= 0:
        print "no bottles of beer on the wall, no bottles of beer, cry a lot"
        return
    else:
        print amount, " bottles of beer on the wall, ", amount, "bottles of beer on the wall, take one down pass it around ", amount-1, " bottles of beer on the wall"
        beer(amount-1)

def fib(n):
    if n == 1:
         return 0
    elif n == 2:
        return 1
    else:
        print "fib(",n-1,") + fib(",n-2,")"
        return fib(n-1)+fib(n-2)


print fib(40)
