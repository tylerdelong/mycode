#!/usr/bin/python3

"""This is a test file to see if I can create a list from an input"""

#this is my input prompt
mylist = input('Please type items you want in your list. Seperate Items using the space bar \n>')

mylist = mylist.split(' ')
print(f'Did you list {mylist}?')
