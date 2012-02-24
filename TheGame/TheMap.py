#! usr/bin/env python

if __name__ == "__main__":
    # When this program is run it should show the entire map
    # divide all the coordinates by 10 so it can fit?
    # rooms that have been entered will be revealed, the rest is in
    # the fog of war
    # also include a black boundary for the edge of each level
    import pygame
    from pygame.locals import *

    SCREENSIZE = 1000,1000
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE)
    screen.fill(255,255,255)
###

    
class level():
    #quadrant 1

    transitionZone = []
    coords = []
    #read from the file?
    def getRoom(self):
        # find the room, then return this shit:

        
        #each wall is one index of the list...
        #super annoying method of storing: (x,y, DX, DY)
        
        self.coords.append((100,100,90,0))
        self.coords.append((100,100, 0,700))
        self.coords.append((100,800, 300,0))
        self.coords.append((400,800, 0,-700))
        self.coords.append((400,100, -100,0))

        # the walls are returned in reference to the room being the screen
        # the walls are searched for by room, which references the entire map...

        return self.coords
    ###
    
    def getTransitionZone():
        return self.transitionZone #= (300,100,350,200)
        

    def addWalls(self):
        # need to pass in the X and Y Coordinates, to figure out what room
        walls = self.getRoom()

        #

        return walls
        
