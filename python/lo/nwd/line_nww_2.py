import turtle
import math

# --- Podaj liczby a i b ---
a = 6
b = 35
# --------------------------

# Oblicz NWW i NWD
nwd = math.gcd(a, b)
nww = a * b // nwd

turtle.speed(0)
turtle.hideturtle()

def draw_line_with_marks(x, y, length, step, color):
    """Rysuje linię długości length i zaznacza punkty co step."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward(length)

    turtle.pencolor(color)
    for pos in range(0, length + 1, step):
        turtle.penup()
        turtle.goto(x + pos, y)
        turtle.pendown()
        turtle.dot(6, color)

def main():
    start_x = -nww/2
    y1 = 80   # pasek a
    y2 = 40   # pasek b
    y3 = 0    # pasek NWD

    # pasek co a
    draw_line_with_marks(start_x, y1, nww, a, "blue")

    # pasek co b
    draw_line_with_marks(start_x, y2, nww, b, "red")

    # pasek co NWD
    draw_line_with_marks(start_x, y3, nww, nwd, "green")

    # podpis
    turtle.penup()
    turtle.goto(0, -40)
    turtle.pencolor("black")
    turtle.write(f"NWD({a},{b}) = {nwd}, NWW({a},{b}) = {nww}", align="center", font=("Arial", 14, "normal"))

    turtle.done()

main()
