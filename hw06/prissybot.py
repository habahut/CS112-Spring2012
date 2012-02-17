#! usr/bin/env/ python
import time

name = raw_input ("Sup, enter your name: ")

statement = "Hello there, %s say hi to me  " %(name)
response1 = raw_input (statement)

print "You mean, \"", response1, "\" sir!"
print

age = raw_input ("yo how old are you? ")
age = int(age)
age += 10

print "pshh I'm ", age, " that means I'm older than you and can tell you waht to do"
print 

print "whats the remainder of 1 million divided by 12? "
time.sleep(2)

print "too slow noob its ", 1000000 % 12, "!!!"
print

n1 = raw_input("lets try another math problem, I'll try not to crush you this time... enter a number: ")
n2 = raw_input("ok now enter another number: ")
n3 = raw_input("one more: ")
Canswer1 = int(n1) + int(n2) * int(n3)

print Canswer1
print

statement = "What is %s + %s * %s " %(n1,n2,n3)
Panswer1 = raw_input (statement) 

if Canswer1 == int(Panswer1):
    print "wow you got it, you must have counted on your fingers"
else:
    print "hahahahahhahahh you suck"

print "ok one more time"
n1 = raw_input("enter a number: ")
n2 = raw_input("enter another number: ")
n3 = raw_input("enter a third number: ")

Canswer2 = int(n1) * int(n2) * int(n3)

statement = "What is %s * %s * %s  "  %(n1,n2,n3)
Panswer2 = raw_input (statement) 

print

if Canswer2 == int(Panswer2):
    print "bleh that was easy anyway"
else:
    print "hahahahah oh man go back to kindergarden"

print
print
print "aight peace noob i'm out"
