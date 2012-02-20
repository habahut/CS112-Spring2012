#!/usr/bin/env python

import pygame
from pygame.locals import *
from math import sqrt

SCREEN_SIZE = 500,500
BLACK = 0,0,0
WHITE = 255,255,255
GREY = 150,150,150

LEFT_MOUSE_BUTTON = 1

PLAYER = Rect(0,0,5,5)

FPS = 30

clock = pygame.time.Clock()

pygame.init()
global screen
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))


def lockMouse():
    px,py = pygame.mouse.get_pos()
    x,y = screen.get_rect().center
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

    pygame.draw.circle(screen, (255,0,0), (int(dx),int(dy)), 3)
    pygame.draw.circle(screen, (0,0,0), (int(dx),int(dy)), 4)


done = False
#pygame.mouse.set_visible(False)
pygame.mouse.set_pos(screen.get_rect().center)

while not done:
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,0), screen.get_rect().center, 10,3)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_p:
                done = True
            if event.key == K_w:
                pass
            elif event.key == K_a:
                pass
            elif event.key == K_s:
                pass
            elif event.key == K_d:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_MOUSE_BUTTON:
            pass

    lockMouse()
    clock.tick(FPS)

    pygame.display.flip()
#end while


print "done"

                
