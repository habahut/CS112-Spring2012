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

tiles = []
# -1 = mine
# # = number of agacent mines

def assignNumbers(tiles):
    #print "-=-=-=-=-=-=-= BEFORE HAND -=-=-=-=-="
    #for row in tiles:
    #    print row
    #print "+++++++++++++++++++++++++++++++++++++"
    
    for row,r in enumerate(tiles):
        for column,c in enumerate(r):
            count = 0
            anotherCounter = 0
            if not (tiles[row][column] == -4):
                for y in range(-1,2):
                    for x in range(-1,2):
                       
                        try:
                            anotherCounter += 1
                            totalY = row + y
                            totalX = column + x

                            if (totalY > -1) and (totalX > -1):
                                if (tiles[row + y][column + x] == -4):
                                    count += 1
                                else:
                                    pass
    
                        except IndexError:
                            pass                    
                
                tiles[row][column] = count
                count = 0
            anotherCounter = 0
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
    
    while not mapComplete:
        x = random.randint(0,len(tiles)-1)
        y = random.randint(0,len(tiles[0])-1)
        pos = x,y
        
        if (pos == posClicked):
            pass
        else:
            if not (tiles[x][y] == -4):
                tiles[x][y] = -4
                c += 1

        if (c == difficulty):
            mapComplete = True

    assignNumbers(tiles)
                    
    return tiles


def game(screen):
    #setup

    done = True
    while not done:
        "keep all the stuff together"
        "i.e. keep all movements within the update function"
        "don't move shit after you render"

        #input

        #num nums

        #update

        #render

        # refresh

if __name__ == "__main__":
    tiles = createMap(tiles,(1,5), 10)
    #tiles = [[-2, -1, -1],[-2,-2,-2],[-2,-1,-2]]
    #tiles = [[-4,-2,-4],[-4,-4,-4]]
    #tiles = assignNumbers(tiles)

    #print tiles[3][7]

    
    for row in tiles:
        print row
