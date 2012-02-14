#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""


s = raw_input("number of stones in each pile: ")
stones = map(int, s.split())

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

winner = 0
player = 1

for i in range(len(stones)):
    print alphabet[i],"   ",
#end
    
print " | Move"
print "====================================="

while winner == 0:
    acceptableInput = False

    while not acceptableInput:
        for i in stones:
            print i,"  ",
            
        question = " |   Player %d: [1-5] " %(player)
        move = raw_input(question)
        ## interpret the string entered

        pile = move[0]
        amount = int(move[2])

        ## find what pile they are removing from
        try:
            i = alphabet.index(pile)
        except ValueError:
            i = -2

        ## catch removing too many stones
        if amount > 5 or amount < 0:
            i = -1
            
        ## remove from the pile
        if not(i > 0):
            stones[i] -= amount
            acceptableInput = True
        elif i == -2:
            acceptableInput = False
            print "*Error* Not a pile"
        elif i == -1:
            acceptableInput = False
            print "*Error* not enough stones"

    ## end input checking


    ## check for all piles being empty
    count = 0
    for i in stones:
        count += i

    if count == 0:
        winner = player

    if player == 1:
        player = 2
    else:
        player = 1

## end game loop

print "Player %d Wins!!" %(winner)
