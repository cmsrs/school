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

def selection_sort(arr, colors):
    n = len(arr)
    for i in range(n-1):
        minimum_index  = i
        for j in range(i+1, n):
            #print(i,j)
            if arr[j] < arr[minimum_index]:
                minimum_index = j 
        tmp = arr[i]
        arr[i] = arr[minimum_index]
        arr[minimum_index] = tmp
        tmp = colors[i]
        colors[i] = colors[minimum_index]
        colors[minimum_index] = tmp                    

    return arr



colors_in = ['red', 'blue', 'green', 'blue', 'green', 'red']
sides_of_the_squares_in = [ 54, 10, 25, 11, 48, 55 ]


start_from(-70)
draw_squares( sides_of_the_squares_in, colors_in)

start_from(70)
selection_sort(sides_of_the_squares_in, colors_in)
draw_squares(sides_of_the_squares_in, colors_in)


#zad4
#start_from(True)
#draw_squares(True)

turtle.done()
