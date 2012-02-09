#! /usr/bin/env python

#voodoo
import pygame
from pygame.locals import *

screen_size = 640,480
background = 0,0,0

pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

done= False

while not done:

    event = pygame.event.poll()   #checks keyboard for something happening?

    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == KEYDOWN and event.key == K_r:
        print "r touched"
        background = 255,0,0
    elif event.type == KEYDOWN and event.key == K_b:
        background == 0,255,0
        print "b touched"
    elif event.type == KEYDOWN and event.key == K_g:
        background == 0,0,255
        print "g touched"
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse", pygame.mouse.get_pos(),   # (0,0) is top left corner


    screen.fill(background)
    pygame.display.flip()
    clock.tick(30)
    
print "bye bye"

"""
name_in = raw_input(" enter a name; ")
if name_in == "paul":
    print "you are cool"
elif name_in == "alec" or name_in == "jonah" or name_in == "jack":
    print "your a TA"
else:
    print "you need some learnin"
"""
    



