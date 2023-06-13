# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:43:56 2023

@author: root
"""
import time
from turtle import Screen
from NewSnake import Snake
from Food import Food
from score import Scoreboard

xenzia =Snake()
food=Food()
scores=Scoreboard()

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title('My Snake Xenzia')
screen.tracer(0)
xenzia.make_snake()
screen.listen()
screen.onkey(xenzia.up, 'w')
screen.onkey(xenzia.down, 'z')
screen.onkey(xenzia.right, 'd')
screen.onkey(xenzia.left, 'a')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    '''for part in segments:
       part.forward(distance)
   '''
    # motion with this is uniform, a bit boring tho
    xenzia.move()
    # Detect when snake eats ball 
    if xenzia.segments[0].distance(food)< 15:
        food.new_loc()
        xenzia.extend()
        scores.score+=1
        scores.display_score()
    #Detect COLLISION 
    if xenzia.segments[-1].xcor() > 295 or xenzia.segments[-1].xcor()<-295 or xenzia.segments[-1].ycor()>275 or xenzia.segments[-1].ycor()<-275:
        game_is_on=False
        #scores.end_of_game()
        scores.reset()
        xenzia.reset()
        game_is_on=True
    #Detect COLLISION WITH SELF
    for i in range(0,len(xenzia.segments)-1):
        print(xenzia.segments[i].position())
        if xenzia.segments[-1].distance(xenzia.segments[i]) <10:
            game_is_on=False
            #scores.end_of_game()
            scores.reset()
            xenzia.reset()
            game_is_on=True
screen.exitonclick()
