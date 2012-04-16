#! usr/env/bin python

from math import sqrt

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

class Bullet(Sprite):
    " default bullet, can be inherited for special types "
    width = 2
    height = 6
    color = (255,0,0)

    def __init__(self,x,y, xD, yD):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.xD = xD
        self.yD = yD

        ## self.image is this sprite's drawing surface
        self.rect = Rect(x,y, self.width, self.height)
        self.image = Surface(self.rect.size)

    def draw_image(self):
        pygame.draw.rect(self.image, self.color, self.x,self.y, self.width, self.height)
        

    def update(self, dt):
        self.x += (self.xD * dt)
        self.y += (self.yD * dt)

        

class Ship(Sprite):    
    width = 20
    height = 20
    shotTimer = 0
   
    def __init__(self, x, y, xD, yD, v = 5):
        Sprite.__init__(self)
        self.velocity = v
        self.xDir,self.yDir = self.normalizeDirection(xD,yD)
        self.xDir *= v
        self.yDir *= v

        self.rect = Rect(x,y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.drawImage()

    def drawImage(self):
        pass
        #self.image.fill((0,255,0))

    def normalizeDirection(self, xD, yD):
        distance = xD**2 + yD**2
        distance = sqrt(distance)

        return (xD/distance),(yD/distance)

    def changeSpeed(self, v):
        self.velocity = v
        
    def changeDirection(self, xD, yD):
        self.xDir,self.yDir = normalizeDirection(xD,yD)

    def shoot(self, dt):
        self.shotTimer += dt
        if self.shotTimer > 10000:
            self.shotTimer = 0
            cX = self.rect.x + self.width/2
            cy = self.rect.y + self.height
        
            newBullet = bullet(cX, cY, 0, 3)

            return newBullet
            ## new bullet going purely in y direction, overwritten
        else:
            return None

    def update(self, dt):
        self.rect.x = int(self.xDir * dt)
        self.rect.y = int(self.yDir * dt)
        # HANDLES MOVEMENT, ALL INHERITING THINGS WILL HANDLE SHOOTING

    def getPos(self):
        return self.rect.x,self.rect.y

    def getRect(self):
        return self.rect


class TriangleEnemy(Ship):
    #standard noob enemy
    color = (0,255,0)

    def draw_image(self):
        x = self.x
        y = self.y
        pygame.draw.line(self.image, color, (x,y+17),(x+17,x+17), 3)
        pygame.draw.line(self.image, color, (x+17,y+17), (x+10,y),3)
        pygame.draw.line(self.image, color, (x+10,y),(x,y+17), 3)                


class LeetEnemy(Ship):
    def __init__(self,x,y,xD,yD,v=10):
        Ship.__init__(self,x,y,v,xD,yD)

    def draw_image(self):
        x = self.x
        y = self.y
        pygame.draw.line(self.image, (200,200,200), (x+10,y),(x+10,y+20), 3)
        pygame.draw.line(self.image, (200,200,200), (x,y+10),(x+20,y+10), 3)


    def shoot(self, playerX, playerY):
        self.shotTimer += 1
        if self.shotTimer > 10000:
            shotTimer = 0
            bulletPathX = self.x - playerX
            bulletPathY = self.y - playerY

            d = bulletPathX**2 + bulletPathY**2
            d = sqrt(d)

            bulletPathX /= d
            bulletPathX *= 5
        
            bulletPathY /= d
            bulletPathY *= 5
        
            newBullet = Bullet(self.x + 10, self.y + 20, bulletPathX, bulletPathY)
            return newBullet
        else:
            return None
    


class Player(Ship):
    score = 0
    health = 100

    def __init__(self):
        Ship.__init__(self,200,650,10,0,0)

    def changedirection(self, dx, dy):
        self.xD = dx
        self.yD = dy

    def kill(self):
        self.health -= 10
        if self.health < 1:
            ##player dies
            self.kill()

    def shoot(self, mouseX, mouseY):
        shotTimer +=1

        dx = self.x - mouseX
        dy = self.y - mouseY

        d = dx**2 + dy**2
        d = sqrt(d)

        dx /= d
        dx *= 8
        dy /= d
        dy *= 8
    

        newBullet = Bullet(self.x+ self.widht / 2,self.y,dx,dy)
        return newBullet

    def getHealth(self):
        return health

    def draw(self):
        pygame.draw.rect(self.image, (0,0,255), (self.x,self.y),(self.width,self.height), 3)
        


    
