# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#4 kwadraty w 4 różnych kolorach (czerwony, zielony, niebieski, żółty)
#co drugi kwadrat ma dłuższe boki


import turtle

t = turtle.Turtle()
t.speed(5)
#colors = ['#ff0000', '#00ff00', '#0000ff', "#ffff00"]
colors = ['red', 'green', 'blue', "yellow"]

def draw_square(length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()


for i in range(4):
    length = 50 if i % 2 == 0 else 100
    draw_square(length, colors[i])
    t.left(90)

turtle.done()