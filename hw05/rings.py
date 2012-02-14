#!/usr/bin/env python

import pygame
from pygame.locals import *
from math import radians

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)


blueRect = pygame.Rect(0,20,250,250)
yellowRect = pygame.Rect(140,155,250,250)
blackRect = pygame.Rect(280,20,250,250)
greenRect = pygame.Rect(420,155,250,250)
redRect = pygame.Rect(560,20,250,250)

#pygame.draw.rect(screen, BLUE, blueRect)
#pygame.draw.arc(screen, BLUE, blueRect, radians(-50),radians(280), 20)
pygame.draw.circle(screen, BLUE, blueRect.center, 125, 20)



#pygame.draw.rect(screen, YELLOW, yellowRect)
#pygame.draw.arc(screen, YELLOW, yellowRect, radians(90), radians(0), 20)
pygame.draw.circle(screen, YELLOW, yellowRect.center, 125, 20)

#pygame.draw.rect(screen, BLACK, blackRect)
pygame.draw.circle(screen, BLACK, blackRect.center, 125, 20)
#pygame.draw.rect(screen, GREEN, greenRect)
pygame.draw.circle(screen, GREEN, greenRect.center, 125, 20)
#pygame.draw.rect(screen, RED, redRect)
pygame.draw.circle(screen, RED, redRect.center, 125, 20)

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)


print "ByeBye"
pygame.quit()
