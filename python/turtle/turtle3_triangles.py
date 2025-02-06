# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#cztery trojkaty prostopadle obok siebie 
# odpowidnio o boku: 100, 150, 200, 250

import turtle
import math

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


def draw_triangle(a):
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90+45)
    t.forward(a * math.sqrt(2) )


j = 100
for i in range(4):   
    draw_triangle(j)
    t.right(45 + 90)
    j += 50


turtle.done()