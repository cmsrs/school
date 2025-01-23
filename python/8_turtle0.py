# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#trojkat prostokatny wpisany w okrag

import turtle
import math

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

t.forward(100)
t.left(90)
t.forward(100)

t.left(90+45)
t.forward(100 * math.sqrt(2) )

t.left(180)
r = 50 * math.sqrt(2)

t.penup()
t.forward(r)
t.right(45+90)
t.forward(r)
t.left(90)
t.pendown()
t.circle(r)

turtle.done()