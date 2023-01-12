# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:19:33 2022

@author: User
"""
from tkinter import *
from PIL import ImageTk,Image
top=Tk()
top.geometry("270x270")
#Creating fxns
def forward(image_number):
    global l1
    global button_forward
    global button_back
    
    l1.grid_forget()
    l1=Label(image=img_list[image_number-1])
    button_next=Button(top,text="Next",command=lambda:forward(img_list[image_number+1]))
    button_back=Button(top,text="Previous",command=lambda:back(image_number-1))
    l1.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_next.grid(row=1,column=2)
    
    return


def back():
    global l1
    global button_forward
    global button_back
    if(l1==img_list[0]):
        button_back=Button(top,text="Previous",state=DISABLED)
    l1.grid_forget()
    l1=Label(image=img_list[image_number-1])
    button_next=Button(top,text="Next",command=lambda:forward(img_list[image_number+1]))
    button_back=Button(top,text="Previous",command=lambda:back(image_number-1))
    l1.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_next.grid(row=1,column=2)
    
    return


#Creating an exit button
button_exit=Button(top,text="Exit Program", command=top.quit)
#Place the button on the screen

#Using images
my_img=ImageTk.PhotoImage(Image.open('C:\\Users\\User\\Desktop\\ipNX\\Bruhhhhhhhhhhhhhhh.png'))
my_img2=ImageTk.PhotoImage(Image.open('C:\\Users\\User\\Downloads\\WhatsApp Image 2022-07-06 at 10.40.47 AM.jpeg'))
my_img3=ImageTk.PhotoImage(Image.open('C:\\Users\\User\\Downloads\\WhatsApp Image 2022-07-13 at 7.54.59 PM.jpeg'))
my_img4=ImageTk.PhotoImage(Image.open('C:\\Users\\User\\Downloads\\IMG_1918.jpg'))
my_img5=ImageTk.PhotoImage(Image.open('C:\\Users\\User\\Downloads\\IMG-20220406-WA0016.jpg'))
img_list=[my_img,my_img2,my_img3,my_img4,my_img5]
l1=Label(image=my_img)
l1.grid(row=0,column=0,columnspan=3)

#buttons
button_back=Button(top,text="Previous",command=lambda:back())
button_next=Button(top,text="Next",command=lambda:forward(2))
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_next.grid(row=1,column=2)
lambda:back()

top.mainloop()
