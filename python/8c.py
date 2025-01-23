import turtle

# Ustawienia ekranu
screen = turtle.Screen()
screen.title("Prosty program z turtle")
screen.bgcolor("white")

# Tworzenie żółwia
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(3)

# Rysowanie kwadratu
for _ in range(4):
    t.forward(100)  # Idź do przodu o 100 jednostek
    t.left(90)      # Obróć w lewo o 90 stopni

# Zakończenie
turtle.done()