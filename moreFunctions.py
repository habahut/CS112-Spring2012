#!/usr/bin/env python

import frifuncs

frifuncs.doSomething()

reload(frifuncs)

print frifuncs.randTuple2(800,600)

screen_size = (800,600)


# putting a star before a tuple when calling an argument will unpack
# the tuple during the call
print frifuncs.randTuple2(*screen_size)

print frifuncs.randTuple3(600,500,[200,400])


### look up doctest for awesome testing example and shit....

# a lambda is a non-named function
sq = lambda x: x**2
sq(4)

# another example:
map(lambda x: x**2,range(30))

def f(x,y):
    print x,y

abc = f
abc(3,4)

def sq(x):
    return x**2

print frifuncs.mymap(sq,[4,5,3])


def add(x,y):
    return x+y


# this thing wraps the mult function
@frifuncs.logger
def mult(x,y):
    return x*y

LL = range(1,10)
print frifuncs.myreduce(add,LL)
print frifuncs.myreduce(mult,LL)


def greeter(greeting, name):
    print greeting,name


#greeter("hello","nurse")
#aloha = frifuncs.partial(greeter, "aloha")
#aloha('steve')

add = frifuncs.logger(add)

print add(3,6)

