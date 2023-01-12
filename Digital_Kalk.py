# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:07:01 2022

@author: User
"""

from tkinter import *
top=Tk()
top.title("Calculator")

e=Entry(top,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_add(text):
    
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(text))
    return
def button_clear():
    e.delete(0,END)
    return
def button_plus():
    global i
    i=0
    numbr1=e.get()
    global f_num
    f_num=int(numbr1)
    e.delete(0,END)
    
def button_equal():
    second_numbr=(e.get())
    e.delete(0,END)
    if(i==0):
     e.insert(0,str(f_num + int(second_numbr)) )
    elif(i==1):
        var=int(num1) - int(second_numbr)
        e.insert(0, var)
def button_minus():
    global i
    i=1
    global num1
    num1=e.get()
    e.delete(0,END)
    
    

#Button Definitions
button_1=Button(top, text="1",padx=40, pady=20,command=lambda: button_add(1))
button_2=Button(top, text="2",padx=40, pady=20,command=lambda: button_add(2))
button_3=Button(top, text="3",padx=40, pady=20,command=lambda: button_add(3))
button_4=Button(top, text="4",padx=40, pady=20,command=lambda: button_add(4))
button_5=Button(top, text="5",padx=40, pady=20,command=lambda: button_add(5))
button_6=Button(top, text="6",padx=40, pady=20,command=lambda: button_add(6))
button_7=Button(top, text="7",padx=40, pady=20,command=lambda: button_add(7))
button_8=Button(top, text="8",padx=40, pady=20,command=lambda: button_add(8))
button_9=Button(top, text="9",padx=40, pady=20,command=lambda: button_add(9))
button_0=Button(top, text="0",padx=40, pady=20,command=lambda: button_add(0))
button_plus=Button(top, text="+",padx=40, pady=20,command=button_plus)
button_equal=Button(top, text="=",padx=80, pady=20,command=button_equal)
button_clear=Button(top, text="clear",padx=80, pady=20,command=button_clear)
button_minus=Button(top, text="-",padx=150, pady=20,command=button_minus)

#Button Placement
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)
button_minus.grid(row=6,column=0,columnspan=3)
top.mainloop()
