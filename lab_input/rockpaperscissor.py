#!/usr/bin/python3
"""rock paper scissor mini project"""

import random
import time
#dict to set values to str
#lib = {'Rock':'1','Paper':'2','Scissor':'3'}
#list to allow OPP to pick
lis = ['Rock','Paper','Scissors']

def main():
    OPP = random.choice(lis)
    YOU = input('Pick rock, paper, or scissors: \n>')
    YOU = YOU.capitalize()
    if YOU not in lis:
        print('Please pick a valid option')
        time.sleep(1)
        main()
    if YOU == 'Rock':
        rock(OPP)
    elif YOU == 'Paper':
        paper(OPP)
    else:
        scissor(OPP)

#you picked rock
def rock(OPP):
    if OPP == 'Rock':
        draw(OPP)
    elif OPP == 'Paper':
        loss(OPP)
    else:
        win(OPP)

#you picked paper
def paper(OPP):
    if OPP == 'Paper':
        draw(OPP)
    elif OPP == 'Scissors':
        loss(OPP)
    else:
        win(OPP)

#you picked scissor
def scissor(OPP):
    if OPP == 'Scissors':
        draw(OPP)
    elif OPP == 'Rock':
        loss(OPP)
    else:
        win(OPP)

#You Draw
def draw(OPP):
    print(f'You look and see that your opponent picked {OPP.lower()}.')
    time.sleep(2)
    print('You Draw!')
    response()

#You lose
def loss(OPP):
    print(f'You look and see that your opponent picked {OPP.lower()}.')
    time.sleep(2)
    print('You Lose!')
    response()

#You win
def win(OPP):
    print(f'You look and see that your opponent picked {OPP.lower()}.')
    time.sleep(2)
    print('You Win!')
    response()

#seeing if you want to play again
def response():
    time.sleep(1)
    play = input('Would you like to play again?: (y or n)\n>')
    play = play.lower()
    if play == 'y':
        main()
    elif play == 'n':
        exit()
    else:
        print('Please enter a valid response.')
        response()
main()
