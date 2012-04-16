#!/usr/bin/env python
"""
Raiden <-- cool ass name
"""

import pygame
from pygame.locals import *
from pygame.sprite import Sprite,Group,GroupSingle

from app import Application
from ships import BasicEnemy, Player
from bullets import Bullet

class Game(Application):
    def __init__(self):
        Application.__init__(self)

        self.screenRect = self.screen.get_rect()
        
        self.minDt = 200
        self.enemyGroup = Group()
        self.enemyGroup.add(BasicEnemy(100,100,0,1,self.screenRect,80))

        self.bulletGroup = Group()

        self.player = Player(self.screenRect)
        self.playerGroup = GroupSingle(self.player)
        self.playerWeaponType = 1
        self.playerFired = False
        self.playerMoveX = 0
        self.playerMoveY = 0
        self.playerMoveFlag = False

    def handle_event(self,event):
        if event.type == MOUSEBUTTONUP and event.button == 1:
             self.playerFired = True
        if event.type == KEYDOWN:
            ## need to put in KEYUP to turn off the thing...
            if event.key == K_DOWN:
                self.playerMoveY = 1
                self.playerMoveFlag = True
            if event.key == K_UP:
                self.playerMoveY = -1
                self.playerMoveFlag = True
            if event.key == K_LEFT:
                self.playerMoveX = -1
                self.playerMoveFlag = True
            if event.key == K_RIGHT:
                self.playerMoveX = 1
                self.playerMoveFlag = True
            if event.key == K_SPACE:
                self.playerFired = True
        
        if event.type == KEYUP:
            if event.key == K_DOWN:
                self.playerMoveY = 0
                self.playerMoveFlag = True
            if event.key == K_UP:
                self.playerMoveY = 0
                self.playerMoveFlag = True
            if event.key == K_LEFT:
                self.playerMoveX = 0
                self.playerMoveFlag = True
            if event.key == K_RIGHT:
                self.playerMoveX = 0
                self.playerMoveFlag = True

    def update(self, screen):
        dt = min(self.minDt, self.clock.get_time())
        self.enemyGroup.update(dt)

        if self.playerFired:
            self.bulletGroup.add(self.player.shoot(self.playerWeaponType))
            self.playerFired = False

        ## need to validate holding down the key... 
        if self.playerMoveFlag:
            self.player.setDirection(self.playerMoveX, self.playerMoveY)
            self.playerMoveFlag = False
            
        self.bulletGroup.update(dt)
        self.playerGroup.update(dt)

        pygame.sprite.groupcollide(self.enemyGroup, self.bulletGroup, True, True)
            
    def draw(self,screen):
        screen.fill((0,0,0))
        self.playerGroup.draw(screen)
        self.enemyGroup.draw(screen)
        self.bulletGroup.draw(screen)

        
if __name__ == "__main__":
    Game().run()
    print "finito"
