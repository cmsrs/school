import turtle
import math


"""
Program rysuje dwa paski:

    Pasek pierwszy — długość = NWW(a,b), punkty co a jednostek.

    Pasek drugi — długość = NWW(a,b), punkty co b jednostek.

To pokazuje, że oba paski spotykają się dopiero w punkcie NWW(a,b).


Algorytm (opis)

    Podajemy a i b.

    Liczymy NWW(a, b).

    Rysujemy poziomą linię (pasek 1) długości nww.

        Zaznaczamy na nim punkty co a.

    Pod spodem rysujemy drugą linię (pasek 2) długości nww.

        Zaznaczamy na nim punkty co b.

    Obie linie „spotykają się” na końcu w punkcie nww.
"""



# --- Podaj liczby a i b ---
a = 6
b = 35
# --------------------------

# Oblicz NWW
nww = a * b // math.gcd(a, b)

turtle.speed(0)
turtle.hideturtle()

def draw_line_with_marks(x, y, length, step, color):
    """Rysuje linię długości length i zaznacza punkty co step."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward(length)

    # zaznacz punkty
    turtle.pencolor(color)
    for pos in range(0, length + 1, step):
        turtle.penup()
        turtle.goto(x + pos, y)
        turtle.pendown()
        turtle.forward(0)  # kropka
        turtle.dot(6, color)

def main():
    start_x = -nww/2
    y1 = 5
    y2 = -5

    # rysuj górny pasek co a
    draw_line_with_marks(start_x, y1, nww, a, "blue")

    # rysuj dolny pasek co b
    draw_line_with_marks(start_x, y2, nww, b, "red")

    # podpis NWW
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pencolor("black")
    turtle.write(f"NWW({a},{b}) = {nww}", align="center", font=("Arial", 14, "normal"))

    turtle.done()

main()


