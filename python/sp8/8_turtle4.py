# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle


import turtle
import math

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


def draw_shape(t, len):
    for i in range(20):
        t.forward(len)
        t.left(18)


for _ in range(10):
    t.penup()
    t.forward(10)
    t.pendown()
    draw_shape(t, 50)

turtle.done()