#! / usr/bin/env python

inp = raw_input("enter a number :")
print "input was %s" %inp

x,y = 3,3
print x,y











print """
I wish
i could write
haiku"""


print hex(128) 
print bin(128)

a ="63"
a = int(a)

a += 1

print a


abs(-5)  # returns 5
str(15)  # turns shit into a string
min(a, 5)  
max (a, 2000)
int("0xff", 16)
print int("0xDEAD", 16)
print hex(2000)


#string formatting
name = "jim"
item = "pear"
print "Hi " + name + ", thanks for the " + item +"."

statement =  "Hi %s, thanks for the %s."
print statement %(name,item)          # other formats %d %f, to type a percent use %%, percent becomes escape character

print "%4d"%6       # for table formatting
print "%04d"%16
