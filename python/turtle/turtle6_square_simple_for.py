# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

# dwa karadraty jeden pod drugim
# sa to kwadraty o bokach 75 i oddalone od siebie o 75 jednostek
# pierwszy kwadrat ma grubosc linii 3 i kolor linii czerwony
# drugi kwadrat ma grubosc linii 7 i kolor linii niebieski

#zastosowanie petli for

import turtle

t = turtle.Turtle()
t.speed(5)

a = 75

#square 1
t.pensize(3)
t.color("red")
for i in range(4):
    t.forward(a)
    t.right(90)

#move to the next square
t.penup()
t.right(90)
t.forward(2*a)
t.left(90)
t.pendown()


#square 2
t.pensize(7)
t.color("blue")
for i in range(4):
    t.forward(a)
    t.right(90)



turtle.done()
