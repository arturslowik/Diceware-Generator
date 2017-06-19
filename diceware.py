"""Diceware generator v0.1"""
# Code written by Artur S.
#
#
from random import randint
def diceRoll():
    #Array word stores randomly generated number. For loop ensures it is done 5 times to create one word.
    #Diceware definition says that one word is created by 5 results.
    word = [str(randint(1, 6)) for i in range(0, 5)]

    #String function removes all formating and stores word in the form 12345 required by Diceware
    return str((''.join(map(str, word))))

#This part gets reult of diceRoll() as variable, opens dictionary file and loops through it.
words = diceRoll()
with open("diceware.txt") as file:
    for line in file:
        if words in line:
            print(line)
