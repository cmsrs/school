# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#trojkat prostokatny wpisany w okrag

import turtle
import math

#promien okregu wpisanego w trojkat rownoboczny a * (  math.sqrt(3) / 6 )
#promien okregu opisanego w trojkat rownoboczny a * (  math.sqrt(3) / 3 )


t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

t.forward(100)
t.left(180 - 60)
t.forward(100)
t.left(180 - 60)
t.forward(100)

t.left(180 - 60)

t.penup()
t.forward(50)
t.pendown()

r = 100 * math.sqrt(3) / 6
#wpuisany okrag
t.circle(r)

t.penup()
t.right(90)
t.forward(r)
t.left(90)
t.pendown()
rr = 100 * math.sqrt(3) / 3
#opisany okrag
t.circle(rr)


turtle.done()