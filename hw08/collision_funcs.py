#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    x,y = pt
    xB,yB,wB,hB = box

    IN = False

    if (xB <= x) and (x < xB + wB):
        if (yB <= y) and (y < yB + hB):
            IN = True
    
    """ 
    if (wB > 0):
        if (xB <= x) and (x <= xB + wB):

            if (hB > 0):
                if (yB <= y) and (y <= yB + hB):
                    IN = True
            else:
                if (yB + hB <= y) and (y <= yB):
                    IN = True
    else:
        if (xB + wB <= x) and (x <= xB):
            
            if (hB > 0):
                if (yB <= y) and (y <= yB + hB):
                    IN = True
            else:
                if (yB + hB <= y) and (y <= yB):
                    IN = True
    """
    return IN

