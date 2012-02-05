#! usr/bin/env python

n1 = raw_input("Enter a number: ")
n2 = raw_input("Enter another number: ")
n3 = raw_input("Enter another number: ")
n4 = raw_input("Enter another number: ")
n5 = raw_input("Enter another number: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)

line = "%6d  | %10s | %12s"

print "Input:    Binary       Hexadecimal"
print "==============================================="
print line %(n1,bin(n1),hex(n1))
print line %(n2,bin(n2),hex(n2))
print line %(n3,bin(n3),hex(n3))
print line %(n4,bin(n4),hex(n4))
print line %(n5, bin(n5), hex(n5))

