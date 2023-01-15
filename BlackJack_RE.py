# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:07:49 2023

@author: root
"""
from BlackJack_LOGO import logo
print(logo)
import random
cards=[11,2,3,4,5,6,7,8,9.10,10,10,10]
stack1=[]
#User's cards
stack2=[]
#Dealer's cards
print("Hello, Welcome to BlackJack")
def deal_cards():
    player=random.choice(cards)
    stack1.append(player)
    print(f"Your cards so far {stack1}")
    dealer=random.choice(cards)
    stack2.append(dealer)
    print(f"The dealer has {stack2[0]}")
    player_choice=input("Do you want another card? Type 'yes' or 'no ")
    if player_choice=='yes':
        deal_cards()
    #Stop dealing and determine winner
    elif player_choice=='no':
        player_total=sum(stack1)
        dealer_total=sum(stack2)
        if player_total and dealer_total< 21:
            if player_total> dealer_total:
                print("You Win")
            else:
                if player_total==dealer_total:
                    print("Draw")
                else:
                  print("You Lose")
        else:
            #count ace as 1 instead of 11 when score> 21
            for i in cards:
                if i ==11:
                    cards[cards.index(11)]=1
            if player_total==dealer_total:
                print("Draw")
            elif player_total< dealer_total:
                print("You Win")
            else:
                print("You Lose")
deal_cards()
            
        
    
    
            
        
    
    