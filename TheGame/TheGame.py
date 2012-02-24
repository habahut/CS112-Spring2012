#!/usr/bin/env python

import pygame
import TheMap
from TheMap import level
from pygame.locals import *
from math import sqrt

SCREEN_SIZE = 500,500
BLACK = 0,0,0
WHITE = 255,255,255
GREY = 150,150,150

LEFT_MOUSE_BUTTON = 1


# need pointers, until then make these global...
global playerOrigin
playerOrigin = []
PLAYER = Rect(0,0,5,5)
playerMoveVector = [0,0]
playerMoveCount = [0,0]

LEVEL = level()

walls = []

FPS = 35

clock = pygame.time.Clock()

pygame.init()
global screen
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255,255,255))


SCREEN_CENTER = screen.get_rect().center

# the original screen is set as the starting point in the map
# the players original location is used as a reference

# this value is the absolute location with reference to the top left corner of the entire map
# playerMoveCount is the players position in reference to the screen
# use playerAbsoluteLocation for calculating hit boxes
playerAbsoluteLocation = [250,250]

# initialize the players location on the screen to the center of the screen
# this is used for drawing the player
playerScreenLocation = SCREEN_CENTER

def lockMouse(dx,dy):
    pygame.draw.circle(screen, (255,0,0), (int(dx),int(dy)), 3)
    pygame.draw.circle(screen, (0,0,0), (int(dx),int(dy)), 4)

def calcMouse():
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

    return dx,dy


# this shit is all fucked up because the way I'm recording where the player is
# does not match up with the method to record where the walls are
# the player's coordinates and the wall's coordinates are not matching up properly so
# I am walking through walls

# also able to move into the wall and then getting stuck instead of
# being blocked from moving into the wall in the first place
def playerMove(moveX,moveY, playerMoveCount, playerOrigin, walls):    
    tX = moveX + playerOrigin[0] - playerMoveCount[0]
    tY = moveY + playerOrigin[1] - playerMoveCount[1]

    wallXRange = [0,0]
    wallYRange = [0,0]

    canMoveX = True
    canMoveY = True
    
    for wall in walls:   
        if wall[2] > 0:         # wall goes left
            wallXRange[0] = wall[0] - 20
            wallXRange[1] = wall[0] + wall[2] + 20
        else:                   # wall goes right, switch em so wall[0] < wall[1]
            wallXRange[1] = wall[0] + 20
            wallXRange[0] = wall[0] + wall[2] - 20

        # same for Y value
        if wall[3] > 0:
            wallYRange[0] = wall[1] - 10
            wallYRange[1] = wall[1] + wall[3] + 10
        else:
            wallYRange[1] = wall[1] - 10
            wallYRange[0] = wall[1] + wall[3] + 10
        
        #print wallXRange[0],"      ", tX, "     ", wallXRange[1]
        #print wallYRange[0],"      ", tY, "     ", wallYRange[1]

        #check X then Y
        if (wallXRange[0] < tX) and (tX < wallXRange[1]):
            if (wallYRange[0] < tY) and (tY < wallYRange[1]):
                canMoveX = False

        # check Y then X, need to try both orders
        if (wallYRange[0] < tY) and (tY < wallYRange[1]):
            if (wallXRange[0] < tX) and (tX < wallXRange[1]):
                canMoveY = False
                
        #print "====================================="
    ## END FOR LOOP

    
    #print "big money moves: "
    if canMoveX:
        playerMoveCount[0] += -moveX
        #print playerMoveCount[0]
    if canMoveY:
        playerMoveCount[1] += -moveY
        #print playerMoveCount[1]

    return playerMoveCount

    """

    ## Attempt 2, check to see if any of the walls will be drawn
    ## over the center of the screen, that will mean the player cannot move
    ## there

    x,y = screen.get_rect().center
    x -= 5
    y -= 5
    player = pygame.Rect(x,y, 10,10)
    canMove = True
    for wall in walls:
        ## shift walls according to player movement
        ## need to add the negative value so the screen shifts properly
        ## aka, move character left so move the screen right

        #print wall
        #print playerMoveCount
        wall = list(wall)
        wall[0] += playerMoveCount[0] - moveX
        wall[1] += playerMoveCount[1] - moveY

        w = pygame.Rect(wall[0], wall[1], wall[2], wall[3])
        if w.colliderect(player):
            canMove = False

        if canMove:
            playerMoveCount[0] += moveX
            playerMoveCount[1] += moveY

    return playerMoveCount   
    """   
     

def fire():
    # change lock mouse such that the DX and DY things are computed in
    # the main method so that I can use them here without recalculating
    pass


def animateStuff():
    pass
    # create an "animation" class
    # stores the graphic info for each from of the animation
    # also stores the total number of frames
    # add to list of animations

    # go through list backwards, first do graphics and then check
    # to see if there are any frames left in the animation
    # if there are no frames left then remove it from the list

def drawRoom(walls):    
    for wall in walls:
        # Convoluted shit: store the absolute locations of the walls in
        # list: "walls," then move the aboslute value by the PLAYER_MOVE_COUNT
        # which is the x and y movements of the player
        w = list(wall)
        w[0] += playerMoveCount[0]
        w[1] += playerMoveCount[1]
        pygame.draw.rect(screen, (0,0,0), (w[0],w[1],w[2],w[3]), 5)


    return walls
    #check map quadrants
    # check within loaded quadrant to find room
    # draw the room
    


done = False
#pygame.mouse.set_visible(False)
pygame.mouse.set_pos(SCREEN_CENTER)
walls = LEVEL.addWalls()

wDown = aDown = sDown = dDown = False

while not done:
    screen.fill((255,255,255))

    walls = drawRoom(walls)

    #reset the players movements
    playerMoveVector[0] = 0
    playerMoveVector[1] = 0

    #draw the player
    pygame.draw.circle(screen, (0,0,0), SCREEN_CENTER, 10,3)

    #calculate the direction of the mouse
    mouseDX, mouseDY = calcMouse()

    # bootleg "hold key down" detectors...
    
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_p:
                done = True
            if event.key == K_w:
                wDown = True
            elif event.key == K_a:
                aDown = True
            elif event.key == K_s:
                sDown = True
            elif event.key == K_d:
                dDown = True
        elif event.type == KEYUP:
            if event.key == K_w:
                wDown = False
            elif event.key == K_a:
                aDown = False
            elif event.key == K_s:
                sDown = False
            elif event.key == K_d:
                dDown = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_MOUSE_BUTTON:
            pass
        
    ## END FOR LOOP

    # continued ghetto "hold key down" detector
    if wDown:
        playerMoveVector[1] = -2
    if aDown:
        playerMoveVector[0] = -2
    if sDown:
        playerMoveVector[1] = 2
    if dDown: 
        playerMoveVector[0] = 2

    #pygame.key.set_repeat(10,10)      #allows for keys to be held down
                                        # first number is how long till key is considered held down
                                        # second number is the length of each key repeat

    
    if not (playerMoveVector[0] + playerMoveVector[1] == 0):
        playerMoveCount = playerMove(playerMoveVector[0], playerMoveVector[1], playerMoveCount, SCREEN_CENTER, walls)
        #playerAbsoluteLocation[0] = SCREEN_CENTER + playerMoveCount[0]
        #playerAbsoluteLocation[1] = SCREEN_CENTER + playerMoveCount[1]
        
    # need to update playerAbsolutePosition some how so we can
    # keep track of where the player is...

    # check to verify player is still in the same zone
        
    lockMouse(mouseDX, mouseDY)
    clock.tick(FPS)

    pygame.display.flip()
#end while


print "game ended"

                
