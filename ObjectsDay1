#! /usr/bin/env python

import pygame
from pygame.locals import *

#globals
BACKGROUND = 80,80,80

SCREEN_SIZE = SCREEN_WIDTH,SCREEN_HEIGHT = (800,600)
FPS = 30
RECT_SIZE = 120,80

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

bounds = screen.get_rect()
rect = pygame.Rect((0,0), RECT_SIZE)
rect.center = bounds.center

grabbed = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                done = True
        elif event.type == MOUSEBUTTONDOWN:
            grabbed = True
        elif event.type == MOUSEBUTTONUP:
            grabbed = False


    #draw
    screen.fill(BACKGROUND)
    if grabbed:
        rect.center = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (255,0,0), rect)
    pygame.draw.rect(screen, (0,0,0), rect, 5)

    #refresh
    pygame.display.flip()
    clock.tick(FPS)
