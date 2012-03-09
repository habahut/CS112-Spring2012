#!/usr/bin/env python

import math

from random import randrange

import pygame
from pygame.locals import *
import random


## Settings
C_BLACK = 0,0,0
C_RED = 255,0,0


## from tiefighter.py
def draw_tie(surf, color, size):
    wall = size / 8

    surf.fill(C_BLACK)
    pygame.draw.rect(surf, color, (0, 0, wall, size))
    pygame.draw.rect(surf, color, (size-wall, 0, wall, size))
    pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
    pygame.draw.circle(surf, color, (size/2, size/2), size/4)

class TieFighter(object):
    def __init__ (self, x, y, vx, vy, bounds, size=40, color=C_RED):
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color

        self.bounds = bounds
        

        ## draws the tie fighter on this objects own personal image Rect
        ## stores the image permanently
        self.image = pygame.Surface((size,size))
        draw_tie(self.image, color, size)

        ## the image plane for this object
        self.rect = pygame.Rect(x,y,size,size)

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if (self.rect.left < self.bounds.left) or (self.rect.right > self.bounds.right):
            self.vx *= -1
            self.rect.x += self.vx * 2
        if (self.rect.top < self.bounds.top) or (self.rect.bottom > self.bounds.bottom):
            self.vy *= -1
            self.rect.y += self.vy * 2

class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)

        self.ties = []
        ## can init the tie fighter in the append call                 
        self.ties.append(TieFighter(200,200,3,3, self.bounds))

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            spawn = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True
                if event.type == MOUSEBUTTONDOWN:
                    spawn = True

            # update
            if (spawn):
                limX, limY = self.size
                self.ties.append(TieFighter(random.randint(0,limX),random.randint(0,limY),random.randint(-4,4), random.randint(-4,4), self.bounds))
                

            # draw
            self.screen.fill(C_BLACK)
            for tie in self.ties:
                tie.update()
                tie.draw(self.screen)
                 
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
