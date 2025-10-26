import turtle

t = turtle.Turtle()
t.speed(5)

def draw_square(length, color):
    for _ in range(4):
        t.color(color)
        t.forward(length)
        t.right(90)


def start_from(x):
    t.penup()
    t.goto(x, 100)
    #t.left(90)
    #t.forward(200)
    #t.right(90)    
    t.pendown()

def move_to_the_next_square(aa, distant):
    t.penup()
    t.right(90)
    t.forward(aa + distant)
    t.left(90)
    t.pendown()

def draw_squares(sides_of_the_squares, colors_fun):
    distant = 20
    i = 0
    for a in sides_of_the_squares:
        draw_square(a, colors_fun[i])
        #t.write(f"{a}:{colors_fun[i]}")
        move_to_the_next_square(a, distant)
        i += 1

def bubble_sort(arr, colors):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                # Swap arr[j] and arr[j+1]
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp                    
                tmp = colors[j]
                colors[j] = colors[j+1]
                colors[j+1] = tmp                    



"""
    def sort_insert(sides_of_the_squares, colors):
        n = len(sides_of_the_squares)
        for i in range(1, n):
            square_len = sides_of_the_squares[i]
            color = colors[i]

            j = i - 1
            while j >= 0 and  sides_of_the_squares[j] > square_len:
                sides_of_the_squares[j + 1] = sides_of_the_squares[j]
                colors[j + 1] = colors[j]
                j -= 1

            sides_of_the_squares[j + 1] = square_len
            colors[j + 1] = color
"""

colors_in = ['red', 'blue', 'green', 'blue', 'green', 'red']
sides_of_the_squares_in = [ 54, 10, 25, 11, 48, 55 ]


start_from(-70)
draw_squares( sides_of_the_squares_in, colors_in)

start_from(70)
bubble_sort(sides_of_the_squares_in, colors_in)
draw_squares(sides_of_the_squares_in, colors_in)


#zad4
#start_from(True)
#draw_squares(True)

turtle.done()
