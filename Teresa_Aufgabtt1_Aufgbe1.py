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
    print(letterInTheName)
    
firstName = "Snow White"
lastName = "from the Fourth Kingdom"
name = firstName + " " + lastName

#wannaFindOut() #???

#firstName, lastName = names() #???

lenghtOfName = counting()

lettersInYourName()

##############################################################################
"""
vorkommen = vokale[stelle-1] in vokale 
print("Der ", stelle, ". Vokal in der Liste ist '", vokale[stelle-1],
      "' und er kommt in meinem Namen vor: ", vorkommen, ".", sep="")

i = 0
for i in range(0,5):
    vork = vokale[i] in name   # Vorkommen
    print("Der Vokal '",  vokale[i], "' kommt in meinem Namen vor: ", vork, ".", sep="")
    
"""