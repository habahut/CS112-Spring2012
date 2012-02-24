#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    
    print "hello,", str(name).lower()


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    temp = False
    try:
        int(w)
        temp = True
    except ValueError:
        print "Error: Invalid Demensions"

    if temp:
        try:
            int(h)
        except ValueError:
            temp = False
            print "Error: Invalid Demensions"

    if temp:
        if (w < 1) or (h < 1):
            print "Error: Invalid Dimensions"
            temp = False


    # actually draw the box here
    if temp:
        out = ""
        if (w == 1):
            out += "+"
        else:
            #print "here"
            out += "+"
            for i in range(0,w-2):
                out+= "-"
                #print "                 in the loop"
            out += "+"

        if not (out == ""):
            print out

        out = ""
        for j in range(0,h-2):
            #print "here"

            out = "|"
            out += " " * (w-2)
            out += "|"
            print out


        out = ""
        if (h > 1):
            if (w == 1):
                pass
            elif (w == 2):
                #print "there"
                out += "+"
            else:
                #print "wtf"
                
                out += "+"
                for i in range(0,w-2):
                    out+= "-"
                out+= "+"
                
            if not (out == ""):
                print out


if  __name__ == "__main__":
    box(1,1)

# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

def tree(s1,s2)
    return "lol"
