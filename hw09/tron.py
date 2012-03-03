#!/usr/bin/env python
"""
tron.py

The fucking awesome game of tron programmed by Trevor Haba himself. Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.






GOOD PLAN:

make tiles:
TILE = 10
WIDTH = 60
HEIGHT = 80

screen_width = (tile*width, tile*height)
draw.rect(x*tile, y*tile)

make the tile the size of the players unit
then you can just check the tile grid instead of by pixels
will make error checking easier when the player is of width > 1

 _______
|   |x,y|
---------
|   |   |
---------
"""

import pygame
from pygame.locals import *
import random
from time import sleep

## constants
RED = 255,0,0
BLUE = 255,0,0
BLACK = 0,0,0
WHITE = 255,255,255

BOUNDS = pygame.Rect(15,15,475,475)
SCREEN_SIZE = 500,500

pygame.init()

global screen
screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|HWSURFACE)

clock = pygame.time.Clock()

NORTH = 0,-1
SOUTH = 0,1
EAST = 1,0
WEST = -1,0

directions = [NORTH,SOUTH,EAST,WEST]

def startLoop():
    choice = 0

    x = 0
    y = 0
    screen.fill((0,0,0))
    from menu import drawMenu
    drawMenu(screen)
    pygame.display.flip()
    while choice == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 x,y = pygame.mouse.get_pos()
                 print x,y

        if (x > 0) and (x < 150):
            if (y > 80) and (y < 200):
                choice = 1
                
        if (x > 160) and (x <360):
            if (y > 80) and (y < 200):
                choice = 2
                
        if (x > 0) and (x < 360):
            if (y > 200) and (y < 320):
                choice = 3
                
    ##

    return choice

def pressedSpaceBar():
    ## reset state
    # number of pixels moved per round   
    p1dir = NORTH

    ai = False

    p1posx = []
    p1posy = []
    p2posx = []
    p2posy = []

    
    for i in range(8):
        p1posx.append(150)
        p1posy.append(250)
        
        p2posx.append(350)
        p2posy.append(250)

    p2posx.append(350)
    p2posy.append(250)
    
    mode = startLoop()
   
    if mode == 1:
        game = True
        ai = False
    elif mode == 2:
        game = True
        ai = True
    elif mode == 3:
        game = False

    if ai:
        lol = random.randint(0,3)
        p2dir = directions[lol]
    else: 
        p2dir = SOUTH

    return game,ai,p1posx,p1posy, p1dir, p2posx, p2posy, p2dir

def aiThink(spotsX, spotsY, direction, BOUNDS, opponentSpotsX, opponentSpotsY):  
    tx,ty = direction

    for i in range(10):
        if not (tx == 0):
            ## moving in X direction
            futureX = tx + spotsX[0]

            futureXBoundaryCheck = futureX + (tx * 10)
            if (futureXBoundaryCheck < BOUNDS.left) or (BOUNDS.right < futureXBoundaryCheck):
                dyMin = spotsY[0] - BOUNDS.top
                dyMin2 = BOUNDS.bottom - spotsY[0]
                #print "DODGING X WALL", dyMin, dyMin2
                if (dyMin > dyMin2):
                    #print "HERE", ty,tx
                    ty = -1
                    tx = 0
                    break
                else:
                    #print "THERE", ty,tx
                    ty = 1
                    tx = 0
                break
            else:    
                for i,opponentX in enumerate(opponentSpotsX):
                    if (opponentX == futureX):
                        if (spotsY[0] == opponentSpotsY[i]):
                            print "DODGING PLAYER"
                            tx,ty = aiChangeDirection(tx,ty)
                            break
                    if (futureX == spotsX[i]):
                        if (spotsY[0] == spotsY[i]):
                            print "DODGING SELF"
                            tx,ty = aiChangeDirection(tx,ty)
                            break
                    
                    futureX += tx
               
        else:
            ## traveling in Y direction
            futureY = ty + spotsY[0]

            futureYBoundaryCheck = futureY + (ty * 10)
            if (futureYBoundaryCheck < BOUNDS.top) or (BOUNDS.bottom < futureYBoundaryCheck):
                dxMin = spotsX[0] - BOUNDS.left
                dxMin2 = BOUNDS.right - spotsX[0]
                #print "DODGING Y WALL"
                if (dxMin > dxMin2):
                    #print "WOMP", ty,tx
                    tx = -1
                    ty = 0
                    break
                else:
                    #print "SLAM",ty,tx
                    tx = 1
                    ty = 0
                    break
            else:
                for i,opponentY in enumerate(opponentSpotsY):
                    if (opponentY == futureY):
                        if (spotsX[0] == opponentSpotsX[i]):
                            print "DODGING PLAYER"
                            tx,ty == aiChangeDirection(tx,ty)                            
                            break
                    if (futureY == spotsY[i]):
                        if (spotsX[0] == spotsX[i]):
                            print "DODGING SELF"
                            tx,ty = aiChangeDirection(tx,ty)
                            break
                            
                    futureY += ty
    ##
                        
    return tx,ty
    
def aiChangeDirection(tx,ty):
    if (ty == 0):
        tx = 0
        ty = random.randint(0,1)
        if (ty == 0):
            ty = -1
    else:
        ty = 0
        tx = random.randint(0,1)
        if (tx == 0):
            tx = -1
            
    return tx,ty

def deathAnimation(spotx,spoty, speed):
    col = [(0,0,0),(220,0,0)]
    for i in range(60):
        for i in range(30):
            x = random.randint(0,10) + spotx[0]
            y = random.randint(0,10) + spoty[0]
            r = random.randint(0,1)
            
            pygame.draw.circle(screen, col[r], (x,y), 1)
    pygame.display.set_caption("Press the space bar to return to menu")
    pygame.display.flip()
    
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                wait = False

def movePlayer(spotsX, spotsY, direction, BOUNDS, opponentSpotsX, opponentSpotsY):
    x,y = direction
    
    x = spotsX[0] + x
    y = spotsY[0] + y

    exploded = False
    if (BOUNDS.left > x) or (x > BOUNDS.right):
        exploded = True
    if (BOUNDS.top > y) or (y > BOUNDS.bottom):
        exploded = True
    
    if not exploded:
        for i,opponentX in enumerate(opponentSpotsX):
            if (spotsX[0] == opponentX):
                if (spotsY[0] == opponentSpotsY[i]):
                    exploded = True
        for i,myX in enumerate(spotsX):
            if (x == myX):
                if (y == spotsY[i]):
                    exploded = True

    if exploded:
        deathAnimation(spotsX,spotsY, speed)

    spotsY.insert(0, y)
    spotsX.insert(0, x)

    return exploded, spotsX,spotsY

game,ai,p1posx,p1posy,p1dir,p2posx,p2posy,p2dir = pressedSpaceBar()
c = 1
aiThinkCounter = 1
while game:
    if c == 0:
        clock.tick(1)
        game,ai,p1posx,p1posy,p1dir,p2posx,p2posy,p2dir = pressedSpaceBar()
        c = 1
        aiThinkCounter = 1

    if game:
        screen.fill(BLACK)
        pygame.draw.rect(screen, (255,255,255), (BOUNDS.left+3,BOUNDS.top+3,BOUNDS.width - 6,BOUNDS.height - 6), 3)
        for i in range(len(p1posx) -1, -1 ,-1): 
            pygame.draw.circle(screen, (255, 0 ,0), (p1posx[i], p1posy[i]), 2)
            pygame.draw.circle(screen, (0, 0, 255), (p2posx[i], p2posy[i]), 2)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                c = 0
            ## P1
            if event.key == K_w:
                p1dir = NORTH
            elif event.key == K_a:
                p1dir = WEST
            elif event.key == K_s:
                p1dir = SOUTH
            elif event.key == K_d:
                p1dir = EAST
            ## P2
            if not ai:
                if event.key == K_UP:
                    p2dir = NORTH
                elif event.key == K_DOWN:
                    p2dir = SOUTH
                elif event.key == K_LEFT:
                    p2dir = WEST
                elif event.key == K_RIGHT:
                    p2dir = EAST
    ##
    speed = 1
    tx,ty = p1dir
    tx *= speed
    ty *= speed
    
    boom,p1posx,p1posy = movePlayer(p1posx,p1posy,(tx,ty), BOUNDS, p2posx,p2posy)

    if (boom):
        c = 0
        boom = False
        print "Player 2 wins this round"
    else:
        tx,ty = p2dir
        
        if ai:
            aiThinkCounter += 1
            if (aiThinkCounter % 3) == 0:
                aiThinkCounter = 0
                p2dir = aiThink(p2posx,p2posy, (tx,ty), BOUNDS, p1posx,p1posy)
                tx,ty = p2dir
    
    tx *= speed
    ty *= speed
    boom,p2posx,p2posy = movePlayer(p2posx,p2posy, (tx,ty), BOUNDS,p1posx,p1posy)
            

    if (boom):
        c = 0
        boom = False
        
        if ai:
            print "computer annihilated"
        else:
            print "Player 1 wins this round"

    clock.tick(30)
    pygame.display.flip()
##
    
print "game ended"        
