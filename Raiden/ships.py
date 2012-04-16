#! usr/bin/env python

import pygame
from pygame.locals import *

from moves import Moves
from bullets import Bullet, Missle
class BasicEnemy(Moves):
    width = 20
    height = 10
    color = (0,255,0)
    
    def __init__(self, x, y, dx, dy, screenRect, v = 25):
        Moves.__init__(self,x,y,dx,dy,screenRect,v)

        self.drawImage(self.image)

    def update(self,dt):
        if self.screenRect.colliderect(self.rect):            
            Moves.update(self,dt)
        else:
            self.kill()

    def drawImage(self, surface):
        #don't need this i think...        rect = surf.get_rect()
        pygame.draw.line(surface, self.color, (0,0), (self.width,0),2)
        pygame.draw.line(surface, self.color, (0,0), (self.width/2, self.height), 2)
        pygame.draw.line(surface, self.color, (self.width/2,self.height), (self.width,0), 2)


"""                                                           """
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"""                                                           """
 

class Player(Moves):
    width = 25
    height = 25
    color = 208,32,144
    weaponType = 1
    bulletVelocity = 300
    bulletColor = 255,69,0

    def __init__(self, screenRect):
        print "MADE PLAYER"
        Moves.__init__(self,175, 550,0,0,screenRect,40)
        self.rect.topleft = 175,550
        pygame.draw.circle(self.image, self.color, (self.width/2,self.height/2),12, 0)

    def setVelocity(self, newV):
        self.velocity = newV

    def setDirection(self, newxD, newyD):
        self.dx = newxD
        self.dy = newyD

    def update(self, dt):
        dt = float(dt)/self.timeScale
        
        xTemp = self.rect.x + (self.dx * self.v * dt)
        if self.screenRect.left < xTemp and self.screenRect.right > xTemp:
            self.rect.x = xTemp
            
        #reuse variables for enhanced speed.... maybe it makes a difference?
        xTemp = self.rect.y + (self.dy * self.v * dt)
        if self.screenRect.top < xTemp and self.screenRect.bottom > xTemp:
            self.rect.y = xTemp

    def shoot(self, weaponType = 0):
        #CHANGE ME!!!
        weaponType = 1
        ## CHANGE ME

        x,y = self.rect.midtop
        if self.weaponType == 0:
            return Bullet(x,y-5, 0, -1, self.screenRect,
                            self.bulletVelocity, self.bulletColor)
        elif self.weaponType == 1:
            return Missle(x,y-5,0,-1, self.screenRect)
    
