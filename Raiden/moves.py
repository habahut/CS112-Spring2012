"""
ships and such
"""

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

import utils

class Moves(Sprite):
    color = 80,80,80
    width,height = size = 10,10

    def __init__(self, x, y, dx, dy, sR, v = 25):
        Sprite.__init__(self)
        self.dx,self.dy = utils.normalize(dx,dy)
        self.v = v

        self.screenRect = sR
        self.timeScale = utils.getTimeScale()
        
        # need to create the surface and rect every time, like so
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()

        # all enemies have bottom as x and y for convenience
        #print "X,Y: ", x,y
        self.rect.topleft = x,y
    
    def update(self, dt):        
        dt = float(dt)/self.timeScale
        self.rect.x += self.dx * self.v * dt
        self.rect.y += self.dy * self.v * dt
        
    def drawImage(self, surface):
        #surface.fill(color)
        pass # i think this should be blank...
        
    def shoot(self):        pass

"""                                                           """
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"""                                                           """

class explodes(Sprite):
    explosionRadius = 60

    def kill(self):
        xplo = self.Explosion(self.rect.center, self.explosionRadius)
        Explosion.group.add(xplo)
        Sprite.kill(self)
    
