#! /usr/bin/env python

import pygame
from pygame.locals import *

#settings
BACKGROUND= 80,80,80
BLACK = 0,0,0
WHITE = 255,255,255
GREEN = 0,255,0
RED = 255,0,0
SCREEN_SIZE = 800,600
RECT_SIZE = 120,80

FPS = 30

## init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

## setup game objects
bounds = screen.get_rect()
rects = [ pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE)]
rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

##game loop
clock = pygame.time.Clock()
done = False
grabbed = False

bigfont = pygame.font.Font(None, 80)



while not done:
    x = 0
    y = 0
    dx = 0
    dy = 0
    
    #input
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    grabbed = rect
                if grabbed:
                    rects.remove(grabbed)
                    rects.append(grabbed)
                    x,y = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            grabbed = None
            dx,dy = pygame.mouse.get_pos()
            dx -= x
            dy -= y

    #update
    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds)

    #draw
    screen.fill(BACKGROUND)
    
    text = bigfont.render("DRAG THE RECTANGLES", True, BLACK,BACKGROUND)
    location = text.get_rect()
    location.center = bounds.center
    screen.blit(text, location)
    
    for rect in rects:
        others = rects[:]
        others.remove(rect)
        
        if rect == grabbed:
            color = WHITE
        elif rect.collidelist(others) != -1:
            color = GREEN
        else:
            color = RED
            
        pygame.draw.rect(screen, color,rect)
        pygame.draw.rect(screen, color, rect)
            
        pygame.draw.rect(screen, (0,0,0),rect, 5)


    #refresh
    pygame.display.flip()
    clock.tick(FPS)







    
