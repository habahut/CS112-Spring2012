# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#

from math import sqrt
class Shape(object):
    def area(self):
        pass
    def perimeter(self):
        pass

class Rect(Shape):
    x = 0
    y = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return self.x*2 + self.y*2

###########################
#
#   how can this have the same area method as a rectangle?
#
class Square(Rect):
    s = 0
    
    def __init__(self,s):
        self.s = s

    def area(self):
        return self.s**2

    def perimeter(self):
        return self.s*4

###################
#
#   what formula is he using for perimeter and radius?
#
class Circle(Shape):
    radius = 0.0

    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14 * float(self.radius**2)

    def perimeter(self):
        return 3.14 * 2.0 * float(self.radius)


#################
#
#   this worked on my test cases...
#
class Polygon(Shape):
    pts = []

    def __init__(self, *p):
        for point in p:
            self.pts.append(point)

    def perimeter(self):
        dist = 0
        for i in range(0,len(self.pts)):
            x,y = self.pts[i]
            if (i+1 == len(self.pts)):
                i = -1
                
            nX,nY = self.pts[i+1]
            dx = x - nX
            dy = y - nY
            dx = dx**2
            dy = dy**2

            dist += sqrt(dx + dy)        
    
        return dist

    def area(self):
        if len(self.pts) > 2:
            area = 0.0
            for i in range(0,len(self.pts)-1):
                x,y = self.pts[0]
                x2,y2 = self.pts[i]
                x3,y3 = self.pts[i+1]
                
                aX = x2 - x
                aY = y2 - y

                bX = x3 - x2
                bY = y3 - y2

                cX = x - x3
                cY = y - y3

                d1 = aX**2 + aY**2
                aLength = sqrt(d1)

                d1 = bX**2 + bY**2
                bLength = sqrt(d1)

                d1 = cX**2 + cY**2
                cLength = sqrt(d1)

                perimeter = (aLength + bLength + cLength)/2

                herrons = (perimeter-aLength)
                herrons *= (perimeter-bLength)
                herrons *= (perimeter-cLength)
                herrons *= perimeter
                
                area += sqrt(float(herrons))
                #area += herrons

        return area

"""       
r = Rectangle(3,4)
print r.area()
sq = Square(5)
print sq.perimeter()
#     20
print isinstance(sq, Rectangle)
#     True
c = Circle(3)
print c.area()
#     28.274333882308138
"""
#     

# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
