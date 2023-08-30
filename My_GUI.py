# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
#from tkinter import *
window=tk.Tk()
window.title("Let's start this rodeo!!")
window.geometry("500x200")

#Label
desc=tk.Label(text='Label')
#desc.pack()
desc.place(x=50,y=50)
desc.grid(column=4, row=0 )
#to position the label

'''desc["text"]="New Text"
desc.config(text='New Text')
THEY ARE THE SAME THING
'''#changing the value of a label
#can font be adjusted?



def click_button():
    print("I got clicked")
    desc['text']= f"{bar.get()}"
tog=tk.Button(text='Touch',command=click_button)
#tog.pack()
#tog.place(x=50,y=30)
tog.grid(column=4, row=1 )

#Entry
bar=tk.Entry()
#bar.pack()
#bar.place(x=50, y=15)
bar.grid(column=4, row=2 )
#an alternative to pack is place
#the best is grid



window.mainloop()