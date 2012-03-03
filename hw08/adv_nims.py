#!/usr/bin/env python

###################### 
#  Helper Functions
######################

def splitparts(s):
    "split_ints takes a string and returns all chunks.  Chunks are any space separated or comma separated values"
    l = s.replace(","," ").split()
    
    return l
    
def a2idx(c):
    "converts a letter to it's index value"
    c = c.upper()
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    jk = alphabet.index(c)
    return jk

def idx2a(i):
    "converts an index to it's letter value"
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return alphabet[i]

##############################################
# Object Functions
#    functions relating to moves and stones
###############################################

def parse_stones(s):
    """given a list of nums (chunks) return a list of stone piles.  Piles cannot be less than 0
    and can be a maximum of 99 stones

    >>> parse_stones("12, 13")
    [12, 13]
    >>> parse_stones("0 200 4 5")
    [99, 4 5]
    """
    l = splitparts(s)

    for i,t in enumerate(l):
        l[i] = int(l[i])
        if l[i] > 99:
            l[i] = 99
        if l[i] < 0:
            l[i] = 0
    
    done = False
    while not done:
        try:
            l.remove(0)
        except ValueError:
            done = True        
    
    return l

# moves are [pile, amount] => [int, int]

def parse_move(s):
    """given an attempted move, parse the input into a "move list"

    >>> parse_move("A  3")
    [0, 3]
    >>> parse_move("this isn't valid")
    None
    """
    
    move = s.split()
    if (len(move) == 2):
        move[0] = a2idx(move[0])
        move[1] = int(move[1])
        m = move[0],move[1]
    else:
        m = "None"

    return m
    

def valid_move(mv, piles):
    """check if a given move can actually be completed

    >>> valid_move(None, [3,3])
    False
    >>> valid_move([0,3], [3,3])
    True
    >>> valid_move([1,20], [3,3])
    False
    >>> valid_move([20,2], [3,3])
    False
    """

    # mv = the move: [pile 0, 3 stones]
    # piles = the list of piles
    valid = False

    if mv == None:
        pass
    else:
        if (piles[mv[0]] < mv[1]):
            pass
        else:
            valid = True

    return valid

def move(mv, piles):
    piles[mv[0]] -= mv[1]

#####################################
#  Output Functions
#     functions which format strings
#####################################
def header(piles):
    "draw the header of the game table"
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    print "Welcome to advanced Nims!"
    print
    line = ""
    for i,t in enumerate(piles):
        line += "%s" %(alphabet[i])
    line += " | Move"

    return line
    
def prompt(piles, player):
    print "CALLED THE PROMPT"
    
    line = ""
    for i in piles:
        line += "%4d" %(i)
    
    return line

# do not touch, already done
def separater(piles):
    "creates a separater under the header, long enough to cover all the piles"
    total = 21 + len(piles)
    total += (len(piles) - 1) * 2
    return "=" * total

###########################################
#  MAIN -- DO NOT TOUCH BELOW THIS POINT 
###########################################
def main():
    piles = parse_stones(raw_input("Number of stones in each pile:  "))
    print ""

    print header(piles)
    print separater(piles)

    # init 
    player = 0      # player will be 0 or 1

    # loop as long as any value in piles != 0
    while any(piles): 
        inp = parse_move( raw_input(prompt(piles, player)) )

        # check for valid input
        if not valid_move(inp, piles):
            print "*Error*  Invalid Move"
            continue

        move(inp, piles)
        player = (player + 1) % 2

    # declare winner
    print "Player %d wins!!!" % (player + 1)

if __name__ == "__main__":
    #main()
    
    print header([5,5,5,5,5])
