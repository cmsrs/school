def fib_rek(n):
    #print(f"fib_rek({n}) called")
    if n <= 1:
        return n
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)


fib = fib_rek(4)
print(fib)
  