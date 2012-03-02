#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
    inRect = True
    for point in poly:
        if not (rect.collidepoint(point)):
            inRect = False

    return inRect


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly):
    "create a rectangle which surounds a polygon"
    xMin,yMin = poly[0]
    xMax,yMax = poly[0]
    
    for point in poly:
        x,y = point
        if (xMin > x):
            xMin = x
        elif (xMax < x):
            xMax = x

        if (yMin > y):
            yMin = y
        elif (yMax < y):
            yMax = y

    r = Rect(xMin,yMin, (xMax + 1 - xMin), (yMax + 1 - yMin))
    return r
