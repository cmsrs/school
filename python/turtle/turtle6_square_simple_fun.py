# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

# dwa karadraty jeden pod drugim
# sa to kwadraty o bokach 75 i oddalone od siebie o 75 jednostek
# pierwszy kwadrat ma grubosc linii 3 i kolor linii czerwony
# drugi kwadrat ma grubosc linii 7 i kolor linii niebieski

#zastosowanie petli for oraz funkcji


import turtle

t = turtle.Turtle()
t.speed(5)
t.penup()
t.goto(0,100)
t.pendown()

a = 75

def square(b):
    for i in range(4):
        t.forward(b)
        t.right(90)

def move_to_next(c):
    t.penup()
    t.right(90)
    t.forward(c)
    t.left(90)
    t.pendown()

#square 1
t.pensize(3)
t.color("red")
square(a)

#move to the next square
move_to_next(a+10)

#square 2
t.pensize(7)
t.color("blue")
square(a+25)


turtle.done()
