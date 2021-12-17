# simulation of gambling game from lectures

import random

# simulation of one round of playing the game

def play():
    # start with $5 pot of money
    pot = 5

    # play until you have $0 or at least $20
    while pot > 0 and pot < 20:
        # bet $1 and roll two dice
        pot -= 1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        sum_dice = dice1 + dice2

        if sum_dice == 12:
            # you won $6
            pot += 6
        elif 8 <= sum_dice <= 11:
            # you won $2
            pot += 2

    # return whether you made money (or not)
    return pot > 0

# simulation of multiple rounds of playing game

def expt(rounds):
    wins = 0
    for i in range(rounds):
        wins += play()
    print(f"{wins} wins out of {rounds} rounds")
