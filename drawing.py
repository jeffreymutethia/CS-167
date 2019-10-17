"""
Author: Jeff Mutethia(mutethjt)
Date: 09/26/2019
Problem number:4
Problem title: Drawing
"""

"""
Draws a spiral with alternating shades of black and yellow, red outline, black background.

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
