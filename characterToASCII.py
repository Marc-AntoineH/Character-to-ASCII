#!/usr/bin/python
import sys


# Convert character into ASCII


def characterInput() :
    character = input("Enter only ONE character here: ")

    while len(character) != 1 :
        character = input("Enter only ONE character here: ")
    else :
        output = ord(character)
        print("The ASCII of", "'", character, "'", "is", output)
        relaunch()


def relaunch():
    answer = input("Do you want to convert another character [Y/n]: ").lower()

    if answer != "y" or "n" :
        answer = input("Do you want to convert another character [Y/n]: ").lower()
    if answer == "y" :
        characterInput()
    if answer == "n" :
        sys.exit()


characterInput()