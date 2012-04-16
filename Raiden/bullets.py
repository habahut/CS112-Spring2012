#! usr/bin/env python


import pygame
from pygame.locals import *
from moves import Moves

class Bullet(Moves):
    width = 2
    height = 6
    ## i think these valuesre getting overwritten somehow

    def __init__(self, x,y, dx, dy, screenRect,v = 125, c = (255,0,0)):
        Moves.__init__(self,x,y,dx,dy,screenRect,v)
        self.color = c

        #pygame.draw.rect(self.image, self.color, self.image.get_rect(), 0)
        pygame.draw.rect(self.image, self.color, Rect(0,0, self.width, self.height), 0)
        

    def drawImage(self, surface):
        pass

    def update(self, dt):
        if self.screenRect.colliderect(self.rect):
            Moves.update(self,dt)
        else:
            self.kill()


"""                                                           """
"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
"""                                                           """

class Missle(Moves):
    width = 7
    height = 20
    color = 100,100,100
    trailColor1 = 255,40,40
    trailColor2 = 140,80,80
    trailColor = trailColor1
    timer = 0

    def __init__(self, x,y, dx,dy, screenRect, v=20):
        Moves.__init__(self,x,y,dx,dy,screenRect,v)
        self.image.fill((0,255,0))
        self.drawImage(self.image,1000)

    def drawImage(self, surface, dt):
        self.timer+= dt
        if self.timer >= 300:
            if self.trailColor == self.trailColor1:
                self.trailColor = self.trailColor2
                self.timer = 0
                
                #pygame.draw.ellipse(self.image, self.trailColor, ((0,15),(7,5)),0)
                pygame.draw.ellipse(self.image, self.color, ((0,0),(7,8)),0)
                pygame.draw.rect(self.image, self.color, ((0,0), (7,8)), 0)
            else:
                self.trailColor = self.trailColor1
                self.timer = 0

                #pygame.draw.ellipse(self.image, self.trailColor, ((0,15),(7,5)),0)
                pygame.draw.ellipse(self.image, self.color, ((0,0),(7,8)),0)
                pygame.draw.rect(self.image, self.color, ((0,0), (7,8)), 0)
                
    def update(self, dt):
        if self.screenRect.colliderect(self.rect):
            self.drawImage(self.image, dt)
            Moves.update(self,dt)
        else:
            self.kill()

    

class StrongBullet(Moves):
    pass

class Lazer(Moves):
    pass
