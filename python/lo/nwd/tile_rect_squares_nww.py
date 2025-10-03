import turtle
import math

"""
    Użytkownik (programista w kodzie) podaje a i b.
    Obliczamy nww = a * b // gcd(a, b).
    Rysujemy duży kwadrat o boku nww.
    Wypełniamy go prostokątami a x b, które w końcu wypełnią całe pole.
"""

# --- Podaj boki prostokąta ---
a = 12 
b = 35
# -----------------------------

# Oblicz NWW
nww = a * b // math.gcd(a, b)

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

def main():
    # Rysujemy duży kwadrat o boku NWW
    start_x = -nww/2
    start_y = -nww/2
    draw_rectangle(start_x, start_y, nww, nww)

    # Wypełniamy go prostokątami a x b
    cols = nww // a
    rows = nww // b

    for i in range(cols):
        for j in range(rows):
            x = start_x + i*a
            y = start_y + j*b
            draw_rectangle(x, y, a, b)

    turtle.done()

main()

