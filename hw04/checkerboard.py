#! usr/bin/env python

h = int(raw_input("what is the height of the checker board? "))
w = int(raw_input("what is the width of the checker board? "))

s1 = "#"
s2 = "-"

for i in range (0,h):
    for j in range (0, w):
        print s1,
        s3 = s1
        s1 = s2
        s2 = s3
    #end for

    if w % 2 == 0:
        s3 = s1
        s1 = s2
        s2 = s3
    #end if
    print
#end for
