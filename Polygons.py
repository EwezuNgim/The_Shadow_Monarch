# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:35:12 2023

@author: root
"""

from turtle import *
import random
raph=Turtle()
raph.shape('turtle')
print(raph.position())
shape=[4,5,6,7,8,9,10]

def draw_polygons():
 for val in shape:
  for i in range(0,val):
    random_pen_colors()
    raph.forward(100)
    raph.left(360/val)


def random_pen_colors():
     '''a=random.randint(0, 255)
     b=random.randint(0, 255)
     c=random.randint(0, 255)
     '''
     col=['red','blue','green','chartreuse','violet','teal']  
     raph.color(random.choice(col))
draw_polygons()
screen=Screen()
screen.exitonclick()