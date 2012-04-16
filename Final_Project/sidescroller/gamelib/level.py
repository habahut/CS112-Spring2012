"""
level.py

"""

import os

from pygame import Rect, Surface
from pygame.sprite import Sprite, Group
import pygame

from settings import LEVEL_SIZE

class WorldObject(object):
    def __str__(self):
        return "no toString() method"

    def getType(self):
        return "WORLDOBJECT"
        

class Block(Sprite, WorldObject):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = Surface((w,h))
        self.image.fill(0)
        self.rect = Rect(x,y,w,h)

    def __str__(self):
        x,y = self.rect.topleft
        x1,y1 = self.rect.bottomright
        return "BLOCK: Coordinates: %d, %d - %d,%d "  %(x,y,x1,y1)

    def getType(self):
        return "BLOCK"

class Spike(Sprite, WorldObject):
    def __init__(self, x, y, w = 40, h = 80):
        Sprite.__init__(self)
        self.image = Surface((w,h))

        # make x,y the top left corner
        y -= h

        pygame.draw.line(self.image, (127,80,80), (x,y+h), (x+.5*w, y), 3)
        pygame.draw.line(self.image, (127,80,80), (x+.5*w, y), (x+w, y + h), 3)

        self.rect = Rect(x,y,w,h)

    def __str__(self):
        x,y = self.rect.topleft
        x1,y1 = self.rect.bottomright
        return "SPIKE: Coordinates: %d, %d - %d,%d "  %(x,y,x1,y1)

    def getType(self):
        return "SPIKE"

class NinjaStar(Sprite, WorldObject):
    def __init__(self,x,y,w=20, h=20):
        Sprite.__init__(self)
        self.image = Surface((w,h))

        #x,y must be the top left corner for consistency
        y -= h
        
        pygame.draw.line(self.image, (255,0,0), (x,y),(x+w,y+h), w/5)
        pygame.draw.line(self.image, (255,0,0), (x+w,y),(x,y+h), w/5)

        self.rect = Rect(x,y,w,h)

    def __str__(self):
        x,y = self.rect.topleft
        x1,y1 = self.rect.bottomright
        return "NinjaStar: Coordinates: %d, %d - %d,%d "  %(x,y,x1,y1)

    def getType(self):
        return "NINJASTAR"
"""
class Zone(object):
    def __init__(self, x,y,w,h, *t, *v):
        # *t is a list of #'s each corresponding to a change in the settings of the game
        self.rect = Rect(x,y,w,h)

        self.effects = []
        for effect in t:
            self.effects.append(t)

        # need to find some clever way to retrieve the types here and 
"""
class Level(object):

    def __init__(self):
        self.bounds = Rect((0,0), LEVEL_SIZE)
        print "self.bounds = ", self.bounds

        self.ceilingCoord = 0
        self.floorCoord = self.bounds.height - 40
        self.leftWall = 0
        self.rightWall = self.bounds.width - 40
        
        # make rects for level
        self.blocks = Group(Block(0,0,40,self.bounds.height), # left wall
                            Block(self.bounds.width - 40, 0, 40, self.bounds.height), # right wall
                            Block(0, self.bounds.height - 40, self.bounds.width, 40), # floor
                            Block(200,self.floorCoord-80, 20, 80), # extra bit
                            Spike(350, self.floorCoord, 40), # DEATH SPIKE
                            NinjaStar(350, self.floorCoord - 130) # ninja star 
                            )

        
        
        # render
        self.render_background()

    def render_background(self):
        self.background = Surface(self.bounds.size)
        self.background.fill((80,80,80))
        self.blocks.draw(self.background)
