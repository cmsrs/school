# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#cztery trojkaty prostopadle obok siebie 

import turtle
import math

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


def draw_triangle():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90+45)
    t.forward(100 * math.sqrt(2) )

for i in range(4):    
    draw_triangle()
    t.right(45 + 90)


turtle.done()