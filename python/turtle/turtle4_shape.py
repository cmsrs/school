# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#wieloboki (prawie kola) narysowane obok siebie, oddalone o 10 jednostek

import turtle

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


def draw_shape(len):
    for _ in range(20):
        t.forward(len)
        t.left(18)


for _ in range(10):
    t.penup()
    t.forward(10)
    t.pendown()
    draw_shape(50)

turtle.done()