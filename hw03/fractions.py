#! usr/bin/env python

n = raw_input("enter the numerator ")
n = int(n)
d = raw_input("whats the denominator? ")
d = int(d)

if (d == 0):
    raw_input("you asshole, now the program is going to break. Ready? (Y/N)")
    
t = n / d

if (t >= 1):
    n -= t* d
    if (n == 0):
        print t
    else:
        print t," ",n,"/",d
else:
    print n,"/",d
