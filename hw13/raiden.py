#! /usr/bin/env python
"""
Raiden.py   <---- cool fucking name

"""

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from ships import *
from shipspawners import ShipSpawner

## lock the mouse within a set boundary, to make aiming more difficult
def lockMouse(screen, t):
    dx,dy = t
    pygame.draw.circle(screen, (255,0,0), (int(dx),int(dy)), 3)
    pygame.draw.circle(screen, (0,0,0), (int(dx),int(dy)), 4)

def calcMouse(r):
    px,py = pygame.mouse.get_pos()
    x,y = r.center
    dx = px - x
    dy = py - y

    if not (dx + dy == 0):
        distance = dx**2 + dy**2
        distance = sqrt(distance)
        dx /= distance
        dy /= distance
    
        dx *= 30
        dy *= 30
    else:
        dx = 0
        dy = 0
    
    dx += x
    dy += y
    
    return dx,dy


class Game(Application):
   
    #settings
    min_dt = 100

    def __init__(self):
        Application.__init__(self)

        self.bounds = self.screen.get_rect()
        self.shipGroup = Group()
        self.playerBulletGroup = Group()
        self.bulletGroup = Group()

        

        self.enemySpawners = [ ShipSpawner(5000, self.shipGroup, self.bounds),
                          ShipSpawner(10000, self.shipGroup, self.bounds, LeetEnemy) ]

        self.enemySpawners[1].setOrigin(40,40)

        self.player = Player()
        self.playerGroup = pygame.sprite.GroupSingle(self.player)
        self.playerFired = 0,0

        
    def handle_event(self, event):
        #input
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.playerFired = mouse.get_pos()
                elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                    pass
                    #bomb
                if event.type == KEYDOWN and event.key == "w":
                    self.enemySpawners[1].update(10000)

    def update(self):
        #update
        dt = min(self.min_dt, self.clock.get_time())
        
        ## putting all the move and shooting information in the ships class
        for spawner in self.enemySpawners:
            spawner.update(dt)

        self.shipGroup.update(dt)

        for ship in self.shipGroup:
            ## check if ship is still on the screen
            if (self.bounds.colliderect(ship.getRect())):
                if isinstance(ship, TriangleEnemy):
                    b = ship.shoot(dt)
                elif isinstance(ship, LeetEnemy):
                    b = ship.shoot(dt, self.player.getPos())
                if not(b == None):
                    self.bulletGroup.add(b)
            else:
                ship.kill()

        for bullet in self.bulletGroup:
            bullet.update(dt)
            if bullet.collide_point(self.player.getRect()):
                self.player.kill()
                bullet.kill()
                if self.player.getHealth() <= 0:
                    pass
                    # end the game here..

        if not(self.playerFired == (0,0)):
               self.playerBulletGroup.add(self.player.shoot(self.playerFired))
               self.playerFired = 0,0

        pygame.sprite.groupcollide(self.playerBulletGroup, self.shipGroup, True,True)

        
    def draw(self, screen):
        screen.fill((0,0,0))
        lockMouse( screen, calcMouse(self.bounds) )
        self.shipGroup.draw(screen)
        self.playerGroup.draw(screen)
        self.bulletGroup.draw(screen)
        self.playerBulletGroup.draw(screen)


if __name__ == "__main__":
    Game().run()
    print "done"
