# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

import turtle
import random

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

for i in range(90, 0, -10):    
    c1 = random.random()
    c2 = random.random()
    c3 = random.random()
    t.begin_fill()
    t.fillcolor(c1, c2, c3)
    t.circle(i)
    t.end_fill()


turtle.done()