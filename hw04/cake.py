#!/usr/bin/env python

slices = 3
s = ""
q = True

while q:
    s = raw_input("cake or death? ")

    if s == "cake" or s == "Cake" or s == "CAKE":
        if slices > 0:
            print "here is a slice of cake"
            slices -= 1
        else:
            print "I'm sorry, there is no more cake"
        #end
    #end

    if s == "death" or s == "DEATH" or s == "Death":
        print "Hannibal Lecter has just eaten your brains"
        q = False
#end
