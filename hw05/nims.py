#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""


stones = int(raw_input("Number of stones in the pile: "))
stonesPerTurn = int(raw_input("Number of stones per turn: "))



winner = 0
player = 1


while winner == 0:
    acceptableInput = False

    while not acceptableInput:
        print stones, " stones left.",
            
        question = " |   Player %d: [1-%d] " %(player, stonesPerTurn)

        move = int(raw_input(question))

        ## catch removing too many stones
        if move > stonesPerTurn or move < 0:
            i = 1
        elif move > stones:
            i = 2
        else:        # no problems
            i = 0
                
        ## remove from the pile
        if i == 0:
            stones -= move
            acceptableInput = True
        elif i == 1:
            acceptableInput = False
            print "*Error* cannot take more stones than ", stonesPerTurn
        elif i == 2:
            acceptableInput = False
            print "*Error* not enough stones"

    ## end input checking

    if player == 1:
        player = 2
    else:
        player = 1

    ## check for all piles being empty
    if stones == 0:
        winner = player

## end game loop

print "Player %d Wins!!" %(winner)
