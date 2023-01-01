# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:56:37 2022

@author: User
"""
from tkinter import *

#import tkMessageBox

top = tkinter.Tk()
#window widget

def helloCallBack():
   messagebox.showinfo( "Invoice Generator", "Welcome to the Invoice Generator")

B =tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
L1 = Label(top, text="Customer Name")
L1.pack(side=LEFT)
#shoving t
Tb=Entry(top,bd=5)
Tb.pack(side=LEFT)
L2= Label(down, text="Ticket ID")
L2.pack(side=LEFT)
top.mainloop()
