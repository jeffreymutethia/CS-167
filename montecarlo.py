"""
Author username(s): Jeff Mutethia(mutethjt)
Date: 10/13/2019
Assignment/problem number: HW07
Assignment/problem title: Monte Carlo and Friends
"""

import random
import math
import turtle


#Part 1. Estimating π

pie = turtle.Turtle()
pie.hideturtle()
pie.speed(6)

def draw_square():
    pie.pencolor('black')
    for i in range(4):
        pie.forward(100)
        pie.left(90)



def pi_est(N): #Define the function, and set parameters
    hits = 0
    points = 0
    r = 1
    pie.pencolor('red')
    pie.goto(0,0)
    pie.circle(r * 100)
    pie.penup()
    pie.left(90)
    pie.forward(100)
    pie.right(90)
    pie.pendown()
    draw_square()
    
    for i in range(N):
        x = random.random() #Generate random x value
        y = random.random()
        d = math.sqrt((x**2) + (y**2)) #Use the distance formula to tell the position of d
        if d <= r:#Check if d is within the circle
            hits = hits + 1
            pie.penup()
            pie.goto((x*100), ((y+r)*100))
            pie.pendown()
            pie.dot(3, 'red')
        elif d > r:
            pie.penup()
            pie.goto((x*100), ((y+r)*100))
            pie.pendown()
            pie.dot(3, 'blue')

        points = points + 1
        

    pi = ((hits/points)*4)
    print(pi)
    return pi

"""
Test:
pi_est(1000)
screen = pie.getscreen()
screen.exitonclick()
"""

#Part 2. Estimating sequence probabilities

def flip():
    coin = random.random()
    if coin < 0.5:
        return 1 
    else:
        return 0


def six_heads():
    headcount = 0
    totalcount = 0
    previoushead = ''
    currenthead = ''
    while (headcount < 5):
        count = flip()
        if count == 1:
            currenthead = 'H'
            if currenthead == previoushead:
                headcount = headcount + 1         
            else:
                headcount = 0
            previoushead = 'H' 
        if count == 0:
            headcount = 0
            previoushead = ''
        totalcount = totalcount + 1
    return totalcount

def average_six(n):
    total = 0
    for i in range(n):
        times = six_heads()
        total = times + total
    average = total/n
    return average


#Part 3. Simulating strange behavior

def hhh():
    headcount = 0
    totalcount = 0
    previoushead = ''
    currenthead = ''
    while (headcount < 2):
        count = flip()
        if count == 1:
            currenthead = 'H'
            if currenthead == previoushead:
                headcount = headcount + 1
            else:
                headcount = 0
            previoushead = 'H'
        if count == 0:
            headcount = 0
            previoushead = ''
        totalcount = totalcount + 1
    return totalcount

def hht():
    headcount = 0
    totalcount = 0
    previoushead = ''
    currenthead = ''
    while (headcount < 1):
        count = flip()
        if count == 1:
            currenthead = 'H'
            if currenthead == previoushead:
                headcount = headcount + 1
            else:
                headcount = 0
            previoushead = 'H'
        if count == 0:
            headcount = 0
            previoushead = 'T'
        totalcount = totalcount + 1
    while (count == 1):
        count = flip()
        totalcount = totalcount + 1
    return totalcount
      
def simulate_flips(n):
    total = 0
    total2 = 0
    for i in range(n):
        times = hhh()
        times2 = hht()
        total = times + total
        total2 = times2 + total2
    average = total/n
    average2 = total2/n
    
    print(average)
    print(average2)









        
    
    


         
                
        
        
        
    
    

    




    


    




