#! usr/bin/env python

import pygame
from pygame.locals import *

# settings
BLACK = 0,0,0
RED = 255,0,0
BLUE = 0,255,0
GREEN= 0,0,255

size = 400,400

clock = pygame.time.Clock()


#initialize
pygame.init()
screen = pygame.display.set_mode(size)

done = False
seperation = 8

while not done:
    #input
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            seperation += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            seperation -= 1

    pygame.key.set_repeat(100,100)      #allows for keys to be held down
                                        # first number is how long till key is considered held down
                                        # second number is the length of each key repeat

    #draw!
    screen.fill(BLACK)
    for i in range(0,400,seperation):
        pygame.draw.line(screen,RED,(0,i),(i,399))
        pygame.draw.line(screen,RED,(399,i),(i,0))
       
        pygame.draw.line(screen,RED,(0,399-i),(i,0))
        pygame.draw.line(screen,RED,(i,399),(399,399-i))

    pygame.display.flip()
    clock.tick(30)
