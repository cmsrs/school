
def fib_iterative(n):
    a = 1
    b = 0
    for _ in range(n):
        tmp = a + b
        b = a
        a = tmp
    return b


old = 0
for n in range(1, 34):
    new = fib_iterative(n)
    if n > 1:        
        ratio = new / old
        print(f"fib({n})/fib({n-1}) = {ratio:.10f}")
    old = new

