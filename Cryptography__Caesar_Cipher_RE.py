# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:56:44 2023

@author: root
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
a=[]
def caesar(text,shift,direction):
    text=text.split()
    text=''.join(text)
    if direction.lower()=='encode':
        for word in text:
          if(alphabet.index(word) + shift<=25):
            a.append(alphabet[alphabet.index(word) + shift])
          else:
              a.append(alphabet[alphabet.index(word) + shift - 26])
        print(text)
        print("The encoded text is," ''.join(a))
    else:
        if direction.lower()=='decode':
            for word in text:
                a.append(alphabet[alphabet.index(word) - shift])
              
            print(text)
            print("The encoded text is", ''.join(a))
        else:
            print('Wrong key')

caesar(text,shift,direction)