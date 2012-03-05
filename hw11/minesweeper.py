#! usr/bin/env python

"""
MODEL:
    DATA
    ----> all the information, never draws anything

VIEW:
    how you draw the data
    ----> knows how to draw the model, but will never change the variables


CONTROL:
    how the user interacts with the model
    ----> translates from data to the drawing and back
    biggest chunk.


"""

import pygame
from pygame.locals import *
import random


## set that shit up
def setup(size):
    pygame.init()
    screen = pygame.display.set_mode(size, DOUBLEBUF|HWSURFACE)
    clock = pygame.time.Clock()

    return clock,screen

def menu(screen):
    menuFont = pygame.font.Font(None, 30)
    easy = pygame.Rect(0,0,300,100)
    medium = pygame.Rect(0,110,300,100)
    hard = pygame.Rect(0,220,300,100)
    q = pygame.Rect(0,330,300,100)
    
    pygame.draw.rect(screen, (0,255,0), easy, 5)
    text = menuFont.render("Easy",True,(0,255,0), (0,0,0))
    textLoc = text.get_rect()
    textLoc.center = easy.center
    screen.blit(text,textLoc)
                
    pygame.draw.rect(screen, (0,0,255), medium, 5)
    text = menuFont.render("Medium",True,(0,0,255), (0,0,0))
    textLoc = text.get_rect()
    textLoc.center = medium.center
    screen.blit(text,textLoc)
    
    pygame.draw.rect(screen, (255,0,0), hard, 5)
    text = menuFont.render("Hard",True,(0,0,255), (0,0,0))
    textLoc = text.get_rect()
    textLoc.center = hard.center
    screen.blit(text,textLoc)
    
    pygame.draw.rect(screen, (255,255,255), q, 5)
    text = menuFont.render("Quit",True,(0,255,0), (0,0,0))
    textLoc = text.get_rect()
    textLoc.center = q.center
    screen.blit(text,textLoc)

    pygame.display.flip()

    d = 0
    p=1000,1000
    while d == 0:
        for event in pygame.event.get():
            #print event
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                p = pygame.mouse.get_pos()
                
        if easy.collidepoint(p):
            d = 10
        elif medium.collidepoint(p):
            d = 15
        elif hard.collidepoint(p):
            d = 30
        elif q.collidepoint(p):
            d = -1
            
    ##
            
    if (d > 0):
        screenSize = d*20,d*20 + 50
        s = pygame.display.set_mode(screenSize, DOUBLEBUF|HWSURFACE)
    else:
        s = None
        
    return d,s


#### make the map
def countAdjacent(L, column, row, value):
    count = 0
    for y in range(-1,2):
        for x in range(-1,2):               
            try:
                totalY = row + y
                totalX = column + x

                if (totalY > -1) and (totalX > -1):
                    if (L[row + y][column + x] == value):
                        #if not (y + x == 0):
                        count += 1
            except IndexError:
                pass                    
         
    return count

def assignNumbers(tiles):
    for row,r in enumerate(tiles):
        for column,c in enumerate(r):
            count = 0
            if not (tiles[row][column] == -4):
               tiles[row][column] = countAdjacent(tiles, column, row, -4)

    return tiles
                                
def createMap(tiles, posClicked, difficulty):
    row = []
    for j in range(difficulty):
        for i in range(difficulty):
            row.append(-2)
        tiles.append(row)
        row = []

    mapComplete = False
    c = 0
    
    xClick,yClick = posClicked
    mineCount = float(difficulty) * 1.2
    
    while not mapComplete:
        x = random.randint(0,len(tiles)-1)
        y = random.randint(0,len(tiles[0])-1)
        
        if (x == xClick) and (y == yClick):
            pass
        else:
            if not (tiles[x][y] == -4):
                tiles[x][y] = -4
                c += 1

        if (c == mineCount):
            mapComplete = True

    assignNumbers(tiles)
                    
    return tiles

##### draw functions
def draw(screen, board, mineCount):
    spacer = 20
    scoreFont = pygame.font.Font(None,30)
    scoreBoard = pygame.Rect(0,0, (len(board) * spacer), 50)

    pygame.draw.rect(screen, (0,0,0), scoreBoard)

    mineCountWindow = pygame.Rect(0,0,100,35)
    mineCountWindow.center = scoreBoard.center

    pygame.draw.rect(screen, (80,80,80), mineCountWindow)

    mineCountS = "%3d" %(mineCount)
    text = scoreFont.render(mineCountS,True,(80,80,80), (255,0,0))
    textLoc = text.get_rect()
    textLoc.center = mineCountWindow.center
    screen.blit(text,textLoc) 

    numFont = pygame.font.Font(None, 18)
    for r in range(len(board)):
        for c in range(len(board)):
            spot = pygame.Rect(c*spacer, r*spacer + 50, spacer, spacer)
            
            if board[r][c] == -2:
                screen.fill((160,160,160), spot)
                pygame.draw.rect(screen, (220,220,220), (c*spacer + 3, r*spacer + 53, spacer - 3, spacer - 3), 3)
            elif board[r][c] == -4:
                screen.fill((160,160,160),spot)             
                pygame.draw.line(screen,(255,0,0), spot.topleft,spot.bottomright,2)
                pygame.draw.line(screen, (255,0,0), spot.bottomleft,spot.topright, 2)
            elif board[r][c] == -1:
                x = c * spacer
                y = r * spacer + 50
                pygame.draw.line(screen, (255,0,0), (x+10,y+3), (x+4,y+6), 2)
                pygame.draw.line(screen, (255,0,0), (x+4,y+6), (x+10,y+6), 2)
                pygame.draw.line(screen, (255,0,0), (x+7,y+6), (x+10,y+3), 2)
                pygame.draw.line(screen, (20,20,20), (x+12,y+3), (x+12,y+18), 2)
            else:
                screen.fill((160,160,160),spot)
                if not (board[r][c] == 0):
                    text = numFont.render(str(board[r][c]),True,(80,80,80), (160,160,160))
                    textLoc = text.get_rect()
                    textLoc.center = spot.center
                    screen.blit(text,textLoc)                      

def death(board,tiles):
    for y in range(len(tiles[0])):
        for x in range(len(tiles[0])):
            if (tiles[y][x] == -4):
                board[y][x] = -4
                
    return board

### update functions
def revealSurround(board,tiles,x,y):
    if not (board[y][x] == -10):

        board[y][x] = tiles[y][x]
        if (board[y][x] == 0):
            board[y][x] = -10
        
            for yR in range(-1,2):
                for xR in range(-1,2):
                    if (yR + xR == 0):
                        pass
                    else:   
                        try:
                            totalY = yR + y
                            totalX = xR + x

                            causeError = tiles[totalY][totalX]

                            ## YO FUCK PYTHONS STUPID ASS LIST LOOPING NONSENSE
                            if (totalY > -1) and (totalX > -1):
                                if (causeError == 0):
                                    # RECURSION?!?!?! FUCK YEAHHHH
                                    revealSurround(board,tiles, totalX, totalY)  
                                else:
                                    board[totalY][totalX] = causeError
                                                                             
                        except IndexError:
                            pass
    ## endif

    return board
                
        

def makeMove(board,tiles,move,moveType):
    x,y = move
    boom = 0
    trueCount = 0
    
    if moveType == 2: # right click
        if (board[y][x] == -2):
            board[y][x] = -1
            boom = 1
            if (tiles[y][x] == -4):
                trueCount = 1
        elif (board[y][x] == -1):
            board[y][x] = -2
            boom = -1
            if (tiles[y][x] == -4):
                trueCount = -1
    elif moveType == 3: #right and left click
        v = countAdjacent(board,x,y,-1) # check for flags
        if (v == tiles[y][x]):
            for y2 in range(-1,2):
                for x2 in range(-1,2):               
                    try:
                        totalY = y2 + y
                        totalX = x2 + x

                        causeError = tiles[totalX][totalY]
                        makeMove(board,tiles,(totalX,totalY),1)
                        
                    except IndexError:
                        pass             
    elif moveType == 1:
        if not(board[y][x] == -1):
            if (tiles[y][x] == -4):
                board = death(board,tiles)
                boom = -100
            elif (tiles[y][x] == 0):                
                board = revealSurround(board,tiles,x,y)
    
                for z in range(len(tiles[0])):
                    for t in range (len(tiles[0])):
                        if (board[z][t] == -10):
                            board[z][t] = 0
            else:
                board[y][x] = tiles[y][x]

    return board,boom,trueCount

def game():
    print "Please do the left+right mouse click slowly, or it will not activate properly!"
    clock,screen = setup((500,500))
    difficulty,screen = menu(screen)

    board = []
    tiles = []

    if (difficulty > 0):
        row = []
        for j in range(difficulty):
            for i in range(difficulty):
                row.append(-2)
            board.append(row)
            row = []

        # difficulty can now be used for other purposes
        mineTotal = float(difficulty) * 1.2

        screen.fill((160,160,160))
        draw(screen,board, 0)
        pygame.display.flip()
        done = False
        madeMap = False
        mineCount = 0
        mineDisplay = 0
    else:
        done = True

    pygame.display.set_caption("Please do the left+right mouse click slowly, or it will not activate properly!")

    while not done:
        "keep all the stuff together"
        "i.e. keep all movements within the update function"
        "don't move shit after you render"

        x = -1
        y = -1
        moveType = 0
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP and event.button == 1:
                buttons = pygame.mouse.get_pressed()
                one,two,three = buttons
                if (three):
                    moveType = 3
                else:
                    moveType = 1
                    
                x,y = pygame.mouse.get_pos()
                y-= 50
                x /= 20
                y /= 20
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                buttons = pygame.mouse.get_pressed()
                one,two,three = buttons
                if (one):
                    moveType = 3
                else:
                    moveType = 2
                    
                x,y = pygame.mouse.get_pos()
                y -= 50
                x /= 20
                y /= 20
            

        #num nums
        if not madeMap:
            madeMap = True
            tiles = createMap(tiles,(x,y),difficulty)
            

        #update
        if not (moveType == 0):
            move = x,y
            board,boom,trueBoom = makeMove(board,tiles,move,moveType)
            if boom == -100:
                done = True
                print "YOU LOSE!!"
            else:
                mineDisplay += boom
                mineCount += trueBoom

        #render
        draw(screen,board,(mineTotal - mineDisplay))

        # refresh
        pygame.display.flip()
        clock.tick(30)
            
        if mineCount == mineTotal:
            done = True
            print "YOU WIN!!!!!"

    

if __name__ == "__main__":
    #tiles = createMap(tiles,(1,5), 10)
    
    """
    board = [[-2,-2,-2],[-2,-2,-2],[-2,-2,-2]]
    tiles = [[1,0,0],[0,0,0],[0,0,1]]
    revealSurround(board,tiles,0,1)
    
    """
    board = []
    tiles = []
    game()
