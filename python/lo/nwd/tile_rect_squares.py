import turtle
import math

# --- Podaj tutaj boki prostokąta ---
a = 500   # szerokość prostokąta
b = 300   # wysokość prostokąta
# -----------------------------------

# oblicz NWD
side = math.gcd(a, b)

turtle.speed(0)
turtle.hideturtle()

def draw_rectangle(x, y, w, h):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)

def draw_square(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

# wycentrowanie prostokąta
start_x = -a/2
start_y = -b/2

# rysuj prostokąt
draw_rectangle(start_x, start_y, a, b)

# ile kwadratów zmieści się w poziomie i pionie
cols = a // side
rows = b // side

# rysuj kwadraty o boku nwd(a,b)
for i in range(cols):
    for j in range(rows):
        x = start_x + i*side
        y = start_y + j*side
        draw_square(x, y, side)

turtle.done()
