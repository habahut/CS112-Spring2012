#!/usr/bin/env python

import pygame
from pygame.locals import *


spaces = [0,0,0,0,0,0,0,0,0]
spaceLength = 100



BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
screenSize = 300,300

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(screenSize)

LEFT = 1

player = 1                  # even = player 1 odd = player 2
winner = 0

def makeMove (x, y, spaces):
    global player
    print 
    x /= 100
    y /= 100
    if spaces[x + (y * 3)] == 0:
        i = x+ (y*3)
        spaces[i] = player
        player *= -1
####


game = True

while game:
    events = pygame.event.get()

    for event in events:
        if event.type == QUIT:
            game = False
        elif event.type == KEYDOWN and event.key == K_q:
            game = False
        elif event.type == KEYDOWN and event.key == K_q:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            makeMove(event.pos[0], event.pos[1], spaces)
    #end
       
    for i in range(len(spaces)):        
            rowTemp = i / 3
            columnTemp = i % 3
            
            if spaces[i] == 1:                                     # draw X
                #print rowTemp,",",columnTemp
                sX = columnTemp * spaceLength + 20
                eX = sX + 60

                sY = rowTemp * spaceLength + 20
                eY = sY + 60
                pygame.draw.line(screen, RED, (sX, sY),(eX, eY), 4)
                pygame.draw.line(screen, RED, (sX + 60, sY),(eX - 60, eY), 4)
            #end          
            elif spaces[i] == -1:                                 #Draw Y
                #print rowTemp,",",columnTemp
                sX = columnTemp * spaceLength + 50
                sY = rowTemp * spaceLength + 50
                     
                pygame.draw.circle(screen, RED, (sX,sY),50,4)
            #end
    #end

    for row in range(1,3):
        for column in range(1,3):
            pygame.draw.line(screen, WHITE, (column * spaceLength, 0),(column * spaceLength, 300),5)
            pygame.draw.line(screen, WHITE, (0, column * spaceLength),(300,column * spaceLength),5)

    ## check for victory the most tedious way possible...
        #horizontal
    w = spaces[0] + spaces[1] + spaces[2]
    w1 = spaces[3] + spaces[4] + spaces[5]
    w2 = spaces[6] + spaces[7] + spaces[8]

        #vertical
    w3 = spaces[0] + spaces[3] + spaces[6]
    w4 = spaces[1] + spaces[4] + spaces[7]
    w5 = spaces[2] + spaces[5] + spaces[8]

    ## diag
    w6 = spaces[0] + spaces[4] + spaces[8]
    w7 = spaces[2] + spaces[4] + spaces[6]

    if w == 3 or w == -3:
        game = False    
        pygame.draw.line(screen, BLUE, (0,50),(300,50),10)
    elif w1 == 3 or w1 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (0,150),(300,150),10)
    elif w2 == 3 or w2 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (0,250),(300,250),10)
    elif w3 == 3 or w3 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (50,0),(50,300),10)
    elif w4 == 3 or w4 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (150,0),(150,300),10)
    elif w5 == 3 or w5 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (250,0),(250,300),10)
    elif w6 == 3 or w6 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (0,0),(300,300),10)
    elif w7 == 3 or w7 == -3:
        game = False
        pygame.draw.line(screen, BLUE, (300,0),(0,300),10)

    ## check for no win
    c = 0
    for symbol in spaces:
        if not(symbol == 0):
            c += 1

    if c == 9:
        game = False

    
    pygame.display.flip()

####


pygame.quit()





