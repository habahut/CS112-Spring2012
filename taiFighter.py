#! /usr/bin/env python

import pygame
import random
from pygame import draw
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((300,300))

clock = pygame.time.Clock()
FPS = 30
screen.fill((0,0,0))
#pygame.mouse.set_visible(False)

done = False
LEFT = 1
dir = 1
col = 120
scale = 1

def drawTieFighter(surf, pos, size = 40, col=(100,100,100)):
    width = size / 8

    x,y = pos
    
    draw.rect(screen, col, (x+0, y+0, width, size))
    draw.rect(screen, col, (x+size - width, y, width, size))
    draw.rect(screen, col, (x, y + (size - width)/2, size,width))
    draw.circle(screen, col, (x + size/2, y+ size / 2), size/4)
###

def move(x,y, dx, dy, bounds):
    tx = x + dx
    ty = y + dy

    #print tx,ty

    if (ty < bounds.top):
        dy *= -1
        y += 1
    elif (ty > bounds.bottom - 40):
        dy *= -1
        y -= 1

    if (tx > bounds.right - 40):
        dx *= -1
        x -= 1
    elif (tx < bounds.left):
        dx *= -1
        x += 1

    x += dx
    y += dy
    
    return x,y,dx,dy
###

screen_bounds = screen.get_rect()
tie_x,tie_y = 100,125
tie_dx = 1
tie_dy = 1
ties = []
color = []

while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
            """
        elif event.type == KEYDOWN and event.key == K_UP:
            scale += .01
        elif event.type == KEYDOWN and event.key == K_DOWN:
            scale -= .01
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button==LEFT:
            #x,y = pygame.mouse.get_pos()
            p = [random.randint(0,700), random.randint(0,700)]
            pos.append(p)
            size.append(random.randint(20,80))
            color.append(col)
            col += dir
            if col > 250:
                col = 240
                dir *= -1
                print col
            elif col < 100:
                col = 110
                dir *= -1
                """
    ###    

    tie_x,tie_y,tie_dx,tie_dy = move(tie_x,tie_y, tie_dx, tie_dy, screen_bounds)
    ties.append([tie_x, tie_y])
    

    for col in color:
        col -= 1
    color.append(255)

    if len(ties) > 255:
        ties.pop(0)
        color.pop(0)
    for i in range(len(ties)):    
        drawTieFighter(screen,ties[i], 40, (color[i],color[i],color[i]) )
    

            

    pygame.display.flip()
    clock.tick(FPS)
###

print "I'm frozen like a bitch."

