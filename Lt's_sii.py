# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:14:50 2022

@author: User
"""
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(len(letters))
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sym = ['@', '$', '!', '&', '%']
total = int(input("How long do you want it? There's a max of 5 symbols"))
no_of_alpha = int(input('Enter number of alphabets: '))
no_of_num = int(input('Enter number of figures:'))
no_of_sym = int(input('Number of symbols?: '))
if((no_of_alpha + no_of_num + no_of_sym) != total):
    no_of_alpha = int(input('Pls re-enter the number of alphabets: '))
    no_of_num = int(input('Pls re-enter the number of figures:'))
    no_of_sym = int(input('Pls re-enter the number of symbols?'))
Pwd = ""
for j in range(0, total):
    turn_of_char = random.randint(0, 2)
    if (turn_of_char == 0):
        Pwd+=(random.choice(letters))
    else:
        if(turn_of_char == 1):
            Pwd+=str(random.choice(num))

    if(turn_of_char == 2):
        Pwd+=(random.choice(sym))
alpha_kount = 0
num_kount = 0
sym_kount = 0
for items in Pwd:
    for stuff in letters:
        if(items == stuff):
            alpha_kount +=1
    for things in num:
        if(items == things):
            num_kount +=1
    for j in sym:
        if(items == j):
            sym_kount +=1
if(sym_kount==no_of_sym and alpha_kount==no_of_alpha and num_kount==no_of_num):
  print(Pwd)
#Fixing the number of digits
if(num_kount < no_of_num):
    korr_time1 = no_of_num - num_kount
    if(alpha_kount > no_of_alpha and num_kount < no_of_num):
        for i in range(0, korr_time1-1):
            for y in Pwd:
                for stuff in letters:
                    if(y == stuff):
                        y = random.choice(num)
                        num_kount +=1
                        alpha_kount-=1
                    if(alpha_kount==no_of_alpha):
                        break
    if(sym_kount > no_of_sym and num_kount < no_of_num):
        for s in range(0, korr_time1 -1):
            for r in Pwd:
                for stuff in sym:
                    if(r==stuff):
                        r=random.choice(num)
                        num_kount +=1
                        sym_kount-=1
                    if(sym_kount==no_of_sym):
                        break
                        
#Fixing the number of symbols
if(sym_kount < no_of_sym):
    korr_time2 = no_of_sym - sym_kount
    if(alpha_kount > no_of_alpha and sym_kount < no_of_sym):
        for j in range(0, korr_time2 - 1):
            for z in Pwd:
                for stuff in sym:
                    if(z == stuff):
                        z = random.choice(sym)
                        sym_kount +=1
                        alpha_kount-=1
                    if(alpha_kount==no_of_alpha):
                                break
    if(num_kount > no_of_num and sym_kount < no_of_sym):
        for h in range(0, korr_time2 -1 ):
            for y in Pwd:
                for stuff in num:
                    if(y==stuff):
                        y=random.choice(sym)
                        sym_kount +=1
                        num_kount-=1
                    if(num_kount==no_of_num):
                        break
#Fixing the numbr of alphabets                        
if(alpha_kount < no_of_alpha):
    korr_time3 = no_of_alpha - alpha_kount
    if(num_kount > no_of_num and alpha_kount < no_of_alpha):
        for k in range(0, korr_time3):
            for numbr in Pwd:
                for stuff in num:
                    if(numbr == stuff):
                        numbr = random.choice(letters)
                        alpha_kount +=1
                        num_kount-=1
                    if(num_kount==no_of_num):
                        break
                    
                    
    if(sym_kount > no_of_sym and alpha_kount < no_of_alpha):
        for t in range(0,korr_time3):
            for symbol in Pwd:
                for stuff in sym:
                    if(symbol==stuff):
                        symbol=random.choice(letters)
                        alpha_kount+=1
                        sym_kount-=1
                if(sym_kount==no_of_sym):
                    break
if(sym_kount==no_of_sym and alpha_kount==no_of_alpha and num_kount==no_of_num):
  print(Pwd)
print(sym_kount)
print(alpha_kount)
print(num_kount)