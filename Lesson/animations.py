#! usr/bin/env python

import pygame
from pygame import gfxdraw
from pygame.locals import *

SCREEN_SIZE = 640,480
FPS = 30

xlist = []
ylist = []

player = Rect(0,0, 16, 16)
bounds = Rect(0,0,200,200)

def center_mouse():
    x,y = screen.get_rect().center
    pygame.mouse.set_pos(x,y)
    pygame.mouse.get_pos()           # locks in the position of the mouse for
                                     # get rel to work properly

def update():
    x,y = pygame.mouse.get_rel()     # relative to the last time position was retrieved
    player.move_ip(x,y)
    if not bounds.contains(player):
        center_mouse()
        player.center = bounds.center

def draw(surf):
    surf.fill((80,80,80))
    surf.fill((0,0,0), bounds)
    surf.fill((255,0,0), player)


    
    x,y = pygame.mouse.get_pos()
    pygame.draw.circle(surf, (255,0,0), (x, y), 5,5)

    xlist.insert(0,x)
    ylist.insert(0,y)
    ty = ylist.pop()
    tx = xlist.pop()
    pygame.draw.circle(surf, (255,0,0), (tx,ty),15, 5)
    for i,x in enumerate(xlist):
        pygame.draw.circle(surf, (0,0,255), (x,ylist[i]), 10, 5)


def run():
    global screen
    
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|HWSURFACE)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    x,y = pygame.mouse.get_pos()

    for i in range(15):
        xlist.append(x)
        ylist.append(y)

    bounds.center = screen.get_rect().center

    done = False
    while not done:
        
        update()
        draw(screen)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_UP:
                pass
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":              # __name__ defaults to the module name
    run()                               # this if statement will only run if this 
                                        # file is the one that was run
    
    print "byebye"


