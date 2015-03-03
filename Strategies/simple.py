__author__ = "Linus"

from random import randint

# This is an example for making your own strategy.

# This file contains a strategy called Copier which copies a random move the opponent
# has made in the past.


def Copier(weights, soldiers):
    # This is the main program. It takes two inputs: "weights" (a list of weights for the castles,
    # like [4,3,3,2,2,2,1,1,1,1]) and "soldiers" (the number of soldiers).

    # Here, put the calculations you want to do before the game begins.

    opponentsMoves = []
    # We can't copy the opponent on the first move, so make our own strat.
    castles = len(weights)
    firstMove = [0]*castles # The list [0, 0, ..., 0]
    for i in xrange(soldiers):
        # add a soldier to a random castle
        randomCastle = randint(0, castles-1)
        firstMove[randomCastle] += 1

    # Now, let the game begin.
    while True:

        # Here, calculate your fiendishly clever next move.
        if opponentsMoves == []:
            myMove = firstMove
        else:
            randomIndex = randint(0, len(opponentsMoves)-1)
            myMove = opponentsMoves[randomIndex]


        # Magic line of code, do not change ever:
        opponentsLastMove = yield myMove
        # This plays your move,
        # and stores the opponent's reply in opponentsLastMove.
        
        # Of course, we want to remember it:
        opponentsMoves.append(opponentsLastMove)

        # That's it! This code will loop forever,
        # or until the game ends, whichever comes first.
