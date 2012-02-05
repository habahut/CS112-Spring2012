#! usr/bin/env python


print "==========  ascii art time  =========="

n = raw_input ("enter a number: ")
s = raw_input ("enter a character: ")
s1 = raw_input ("enter another character: ")
name = raw_input ("enter your name: ")

s11 = s + s1

n = int(n)

if n <  3:
    n = 3
elif n > 40:
    n = 40

namelength = len(name)
nl = (60 - namelength - 12) /  2
print nl, "   ", namelength
print nl * 2 + namelength + 8
print
print

print 

for x in range(0,n/2):
    print s * 60

print s * nl,"    " , name, "    " , s1 * nl

for x in range(0,n/2):
    print s1*60
