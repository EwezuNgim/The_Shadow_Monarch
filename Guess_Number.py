# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:24:11 2023

@author: root
"""
import random
from Guess_Number_Logo import logo
print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
num=random.randint(0, 100)
difficulty=input("Choose a difficuty. Easy or Hard")

#Easy= 5 tries
#Hard=ten tries
if (difficulty.lower()=='easy'):
    counter=10
elif (difficulty.lower()=='hard'):
     counter=5

for i in range(0,counter):
    guess=int(input('What do you think the number is? '))
    if num==guess:
        print("You are correct !")
        break
    elif(num>guess):
        print(f"{guess} is less than the number")
    elif(num<guess):
       print(f"{guess} is greater than the number") 
       