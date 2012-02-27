#!/usr/bin/env python

from random import randrange
import math

def doSomething():
    "this is the doc string, this is not executed and just describes shit"
    
    print "somethin"



#def distance((x1,y1),(x2,y2))
def distance(a,b):
    # can unpack tuples in function definition
    x1,y2 = a
    x2,y2 = b
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def randTuple(n, lo, hi):
    "returns a random n-tuple"

    return tuple(randrange(lo,hi) for i in range(n))
    

def randTuple2(*hi):
    "returns a random n-tuple"
    # asterisk means you can call this with any number of arguments
    # and they will all go into variable hi
    #       asterisk arguments must be at the end of the argument list

    return tuple(randrange(i)  for i in hi)

    # passed in (800,600): randrange(800) then randrange(600)
    # each value passed in returns a random number with the passed in argument
    # as the maximum value

def randTuple3(*bounds):
    bounds = list(bounds)
    for i, bound in enumerate(bounds):
        if type(bound) == int:
            bounds[i] = [bound]     #makes it into a list so everything is the same type

    # unpacks arg, so if it is just one variable it
    # will remain that variable. If it is a tuple or list
    # of variables it will be split up to fill
    # the other variables in randrange
    # i.e.: randrange(min,max) etc...
    return tuple(randrange(*arg) for arg in bounds)
                        
def mymap(fn, seq):
    return [ fn(i) for i in seq]

def myreduce(fn,seq):
    result = seq[0]
    for v in seq[1:]:
        result = fn (result, v)   # applies the function to the previous result
                                  # and the next value in list seq

    return result


# called a decorator
def partial(fn, *args):
    def result(*args):
        a = partial_args + args
        fn(*a)
    return result
        
def logger(fn):
    def wrap(*a):
        print fn.__name__, a
        return fn(*a)
    return wrap
