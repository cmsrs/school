def fib(n):
    print(f"fib_rek({n}) called")
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fib_result = fib(4)
print(fib_result)
  
