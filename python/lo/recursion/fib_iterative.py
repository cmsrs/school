def fib_iterative(n):
    a = 1
    b = 0
    for _ in range(n):
        tmp = a + b
        b = a
        a = tmp
    return b

for i in range(10):
    print ( 'fib(', i, ')=', fib_iterative(i))

