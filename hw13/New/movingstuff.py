#! usr/bin/env python

import pygame
from pygame import *

class Moves(object):
    width = 20
    height = 20
    
    def __init__(self,x,y,dx,dy):
        Sprite.__init__(self)
        self.rect = pygame.rect(x,y,width,height)
        self.image = pygame.Surface(self.rect.size)
        self.drawImage(self)

        self.dx = dx
        self.dy = dy

    def getPosition(self):
        return self.rect.x, self.rect.y

    def drawImage(self):
        pass

    def update(self):
        pass

    def hurt(self, d):
        self.kill()

class Bullet(Moves):
    width = 2
    height = 8
    damage = 10

    def setColor(self,color)
        self.color = color

    def drawImage(self)
        self.image.fill(self.color)

    def update(self):
        self.rect.y += self.dy
        self.rect.x += self.dx
        if self.rect.top == 0:
            self.kill()
    #uses update and getPosition from moves class

    def getDamage(self):
        return self.damage

class Missle(Bullet)
    damage = 25
    color = (150,150,150)
    trailC1 = (80,80,80)
    trailC2 = (255, 80, 80)
    count = 0

    def drawImage(self):
        pygame.draw.circle(self.image, color, (1,6), 2)
        count += 1
        if (count % 500) == 0:
            if c == self.trailC2:
                c = self.trailC1
            else:
                c = self.trailC2
            
        pygame.draw.circle(self.image, c, (1,1), 3)
        pygame.draw.rect(self.image, color, (0,2,2,5))


class Enemy(Moves)
    color = (0,255,0)
    width = 10
    height = 10
    timer = 0

    def drawImage(self):
        rect = self.image.get_rect()
        pygame.draw.line(self.image, color, (rect.width/2, rect.height, 0,0))
        pygame.draw.line(self.image, color, (0,0, rect.width, 0))
        pygame.draw.line(self.image, color, (rect.width,0, rect.width/2, rect.height))
        
    def update(self)
        self.rect.x += self.dx
        self.rect.y += self.dy

    def shoot(self):
        self.timer += 1
        if self.timer > 1000:
            self.timer = 0

            x = self.rect.x + self.rect.width/2
            y = self.rect.y + self.rect.height

            ## all bullets must have setColor run on them immediately
            b = Bullet(x,y,self.dx*2, self.dy*2)
            b.setColor(115,10,90)
            return b

class AdvancedEnemy(Moves)
    health = 3
    width = 20
    height = 20
    color = (0,0,255)
    timer = 0

    def hurt(self, d):
        self.health -= 1
        if health == 0:
            self.kill()

    def shoot(self):
        self.timer += 1
        if self.timer % 600:
            x = self.rect.x + self.rect.width/2
            y = self.rect.y + self.rect.height

            ## all bullets must have setColor run on them immediately
            b = Bullet(x,y,self.dx*2, self.dy*2)
            b.setColor(115,10,90)
            return b
        if self.timer == 2000:
            x = self.rect.x + self.rect.width/2
            y = self.rect.y + self.rect.height

            m = Missle(x,y,0, self.dy*2)
            return m
        
class Player(Moves):
    color = (200,0,200)
    width = 15
    height = 15
    shield = 50
    health = 100

    def takeScreen(s):
        self.screen = s

    def drawImage(self):
        rect = self.image.get_rect()
        rect2 = (rect.x+3,rect.y+3, width-3, height-3)
        pygame.draw.ellipse(self.image,self.color,rect2)
        pygame.draw.ellipse(self.image,((200,200,200)),rect)

    def hurt(self, d):
        if self.shields > 0:
            self.shields -= d

            if shields < 0:
                health += shields ## the overlapping negative can just be added
        else: ## all damage goes to health
            self.health -= d

        if self.health <= 0:
            self.kill()

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        ## block moving off screen here

class Routine(object):
    timer = 0
    k = False
    step = 0
    make = False

    def __init__(self, d, roa, typ, *ml):
        self.duration = d
        self.rateOfAction = roa

        # movelist is a list of tuples of x,y locations for the spawner
        self.moveList = list(ml)

    def getKill(self):
        return k

    def recieve(self):
        if make:
            
            

            make = False
    
    def update(self):
        timer += 1
        if timer < duration:
            k = True        
        else:
            if (timer % rateOfAction) == 0:
                s += 1
                self.x,self.y = moveList[s]
                

    
                
            

class Spawner(Moves):
    routine = None
    timer = 0
    spawnT = Enemy
    freq = 1000
    group = g

    def setGroup(self, g)
        self.group = g
        
    def setType(self, typ)
        self.spawnT = typ

    def setFreq(self, f)
        self.freq = f

    def setRoutine(self, r):
        self.routine = r
        
    def drawImage(self):
        self.image.fill(0,0,0)

    def update(self):        
        timer += 1
        if routine == None:
            if timer > 1000:
                s = spawnT(self.rect.x,self.rect.y,self.dx,self.dy)
                self.group.add(s)
                timer = 0
        else:
            self.routine.update()
            if self.routine.getKill():
                self.kill()
            else:
                self.x = self.routine.getX()
                self.y = self.route.getY()

                newObjType = self.routine.recieve()
                if not newObj == None:
                    dx 
                    group.add(newObjType(self.x,self.y,)

        ## make this dude flash white whenever a unit is spawned                


            
            
