# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle


import turtle

t = turtle.Turtle()
t.speed(5)

a = 75

#square 1
t.pensize(3)
t.color("red")
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)
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
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)
t.forward(a)
t.right(90)



turtle.done()

'''

na platformie https://pythonsandbox.com/turtle, wykonaj nastepujace zadania:

zadanie 1
narysuj 4 kwadraty jeden pod drugim: 
 - w kolorach linii odpoiednio: czerwony, zielony, niebieski, żółty
 - linie kazdego kwadratu o grubosciach, odpowiednio: 1, 3, 5, 7
 - długość boku kwadratu odpowiednio: 50, 75, 100, 125
 - kwadraty są oddalone od siebie o 10 jednostek
 w zadaniu postaraj sie wykorzystac: "pętle for", "funkcje" oraz  "listy"

zadanie 2
 przerob zadanie pierwsze tak, że jesli jest kwadrat o boku zielonym nadaj mu dlugosc boku = 20
 w przeciwnym wypadku daj mu długość boku = 100
 w zadaniu wykorzystaj warunek "if"

zadanie 3
 przerob zadanie pierwsze tak, że jesli jest kwadrat nieparzysty tj. 1 i 3 to ma mieć grubość linii 1
 w przeciwnym wypadku grubość linii ma wynosić 5
 w zadaniu wykorzystaj warunek "if"
 
'''