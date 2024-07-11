#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """run-time code"""
    ch1 = 0
    ch2 = 0
    dra = 0
    total = 0
    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    while total < 100:
    # both players take turns
        cheater1.roll()
        cheater2.roll()

    # both players use their cheat methods
        cheater1.cheat()
        cheater2.cheat()

    #print(f"Cheater 1 rolled {cheater1.get_dice()}")
    #print(f"Cheater 2 rolled {cheater2.get_dice()}")
        total += 1
        if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
            #print("Draw!")
            dra += 1
        elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
            #print("Cheater 1 wins!")
            ch1 += 1
        else:
            #print("Cheater 2 wins!")
            ch2 += 1
    print(f'Out of {total}! rounds. Cheater 1 won {ch1}! times. Cheater 2 won {ch2}! times. And they Drew {dra}! times.')
if __name__ == "__main__":
    main()

