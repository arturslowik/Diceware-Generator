"""Diceware generator v0.1"""
# Code written by Artur S.
#
#

from random import randint
def diceRoll():
    #Array to store key for Diceware dictionary
    key = [str(randint(1, 6)) for i in range(0, 5)]
    #Random loop to generate key. Five "dice" rolls to obtain one key
    #for i in range(0, 5):
    #    i = randint(1, 6)
    #    key.append(str(i))
    #String function removes all formating and stores key in the form 12345
    return str((''.join(map(str, key))))

#This part opens dictionary file (diceware.txt) and loops through it to look for key and its value
data = diceRoll()
file = open("diceware.txt", "r")
for line in file:
    if data in line:
        print(line)
