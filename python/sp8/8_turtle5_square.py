# https://pythonsandbox.com/turtle
# https://www.migra.pl/programowanie/python-turtle

#4 kwadraty w 4 różnych kolorach (czerwony, zielony, niebieski, żółty)
#co drugi kwadrat ma dłuższe boki

import turtle

class TurtleDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(5)
        self.colors = ['#ff0000', '#00ff00', '#0000ff', "#ffff00"]

    def __draw_square(self, length, color):
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(length)
            self.t.left(90)
        self.t.end_fill()

    def __draw_pattern(self):
        for i in range(4):
            length = 50 if i % 2 == 0 else 100
            self.__draw_square(length, self.colors[i])
            self.t.left(90)

    def run(self):
        self.__draw_pattern()
        turtle.done()

TurtleDrawer().run()
