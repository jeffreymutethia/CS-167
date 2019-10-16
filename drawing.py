"""
Author username(s): Jeff Mutethia(mutethjt)
Date: 09/26/2019
Assignment/problem number:4
Assignment/problem title: Drawing
"""

import turtle
import random

jeff = turtle.Turtle()
jeff.hideturtle()
jeff.speed(6)

def jeffcircles():    
    jeff.pencolor('red')
    jeff.fillcolor('yellow')
    jeff.begin_fill()
    for i in range(10):
        jeff.circle(10*i)
        jeff.up()
        jeff.sety((10*i) * (-1))
        jeff.down() 
    jeff.end_fill()


jeffcircles()

screen = jeff.getscreen()
screen.bgcolor('black')
screen.exitonclick()
