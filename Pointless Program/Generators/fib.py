#! usr/bin/env python


# fib is a generator
#"yields" a massive list of shit
#       make a list of spawn locations in routine
def fib():
    a = 1
    b = 1
    while True:
        b,a = a+b,b
        yield b

def enum(call):
    c = 0
    for v in call:
        yield c,v
        c += 1

print list(enum(["a","b","c"]))


# generator will get deleted like everything else
# when the object referncing it dies
#
# so use a generator to define enemy paths, the generator will be removed
# on the enemies death

"""
def tick():
    yield clock.tick(30)

for dt in tick():
    pass
"""
"""
f = fib()
print f.next()
print f.next()

import time
for n in fib():
    print n
    time.sleep(1)
"""
