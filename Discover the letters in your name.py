#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:59:45 2020

@author: TeresaAng
"""

import random 

# Do you want or not?
def wannaFindOut():
    findout = input("Do you want to explore the letters in your name? y or n \n\n")
    if findout == "y":
        print("\nGreat!")
    elif findout == "n":
        print("\nWell, I know you want it! ;-) \nSo, here we go:")
    else:
        print("\nOops! I think you meant to type: YES!!!!")

# The introduction
def names():
    giveFirstName = (input("What is your beautiful first name?\n") or firstName)
    print(giveFirstName, ", what a wonderfull name!", sep="")
    giveLastName = (input("Now I'm really curious about your last name! Would you tell"
                      "me that too, please?") or lastName)
    print("\nSo, you are: " + giveFirstName + " " + giveLastName + ". Nice to meet you!")
    return giveFirstName, giveLastName

# Counting letters
def counting():
    lenghtOfFirstName = len(firstName)
    lenghtOfLastName = len(lastName)
    lenghtOfName = lenghtOfFirstName + lenghtOfLastName
    print("\nYour first Name is ", lenghtOfFirstName, " symbols long and your "
          "last ", lenghtOfLastName, ". \nYour whole name is ", lenghtOfName, " symbols "
          "long.", sep="")
    return lenghtOfName

# Letters in your name
def lettersInYourName():
    vocals = ["a", "e", "i", "o", "u"]
    randomNumber = random.randint(0,lenghtOfName) % 5
    letterInTheName = vocals[randomNumber] in name
    print("\nThe random number ", randomNumber, " in the vocals-list is the letter '", 
          vocals[randomNumber], "' and this letter is in your name: ", 
          letterInTheName, "\n", sep="")
    for i in range(0,5):
        exist = vocals[i] in name   # Vorkommen
        print("The vocal '",  vocals[i], "' is in your name: ", exist, ".", sep="")

    
firstName = "Snow White"
lastName = "from the Fourth Kingdom"

wannaFindOut()

firstName, lastName = names()

name = firstName + " " + lastName

lenghtOfName = counting()

lettersInYourName()

