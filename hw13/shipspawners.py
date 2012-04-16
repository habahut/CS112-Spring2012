#! usr/bin/env python
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from ships import *

class ShipSpawner(object):
    xOrigin = -1
    yOrigin = -1
    
    def __init__(self, duration, group, bounds, theType = TriangleEnemy):
        self.group = group
        self.bounds = bounds
        self.duration = duration
        self.time = duration
        self.shipType = theType

    def randVelocity(self):
        return randrange(1,10),randrange(1,10)

    def setOrigin(self,x,y):
        self.xOrigin = x
        self.yOrigin = y

    def spawn(self):
        if self.xOrigin == -1:
            x = randrange(self.bounds.width - self.shipType.width) + self.bounds.left
            y = randrange(self.bounds.height - self.shipType.height) + self.bounds.top
        else:
            x = self.xOrigin
            y = self.yOrigin

        vx,vy = self.randVelocity()

        ship = self.shipType(x,y,vx,vy)
        self.group.add(ship)

    def update(self,dt):
        self.time += dt
        if self.time >= self.duration:
            self.time = 0
            self.spawn()
