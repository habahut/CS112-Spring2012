# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#

from math import sqrt
class Point(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x,y):
        self.x = x
        self.y = y

    def translate(self,x,y):
        self.x += x
        self.y += y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dx = dx**2
        dy = dy**2

        dist = sqrt(dx + dy)

        return dist

    ## I'm not sure how this can be wrong...
    def slope(self, other):
        #print "=========="
        #print self
        #print other
        mx = other.x - self.x
        my = other.y - self.y

        if mx == 0:
            #print "SLOPE = ", my
            return my
        elif my ==0:
            #print "SLOPE = ", mx
            return mx
        else:
            #print "SLOPE = ", (float(my) / float(mx))
            return float(my)/float(mx)

    #same here, how is this wrong?
    def extrapolate(self, slope, distance):
        #print "SLOPE", slope

        x = self.x + (slope * distance)
        y = self.y + (slope * distance)

        return Point(x,y)


    def __str__(self):
        return  "("+str(self.x)+ "," +str(self.y)+")"

    def __eq__(self, other):
        if isinstance(other,Point):
            if other.x == self.x:
                if other.y == self.y:
                    return True

        return False

# Advanced Section:
# ---------------------------------------
# Add the following function:
#     slope(self, other):
#         calculate the slope between two points
#
#     extrapolate(self, slope, distance):
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
#     __eq__(self, other):
#         checks if other is a Point and is equal to self
#
#     __str__(self):
#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
