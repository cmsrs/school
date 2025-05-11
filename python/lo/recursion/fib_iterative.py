def fib_iterative(n):
    a = 1
    b = 0
    for _ in range(n):
        tmp = a + b
        b = a
        a = tmp
    return b


print ( 'fib(4)=', fib_iterative(4));
