def fib_time_interative(n):
    
    a = 1
    b = 0
    for _ in range(n):
        tmp = a + b
        b = a
        a = tmp
        
    return b



def fib_time_rec(n):
    """
    This function calculates the nth Fibonacci number using a recursive approach.
    It also measures the time taken to compute the result.
    """
    import time

    
    if n <= 1:
        return n
    else:
        result = fib_time_rec(n - 1) + fib_time_rec(n - 2)    
    
    return result


import time
    

for i in range(30, 45):
    start_time1 = time.time()
    fib_time_interative(i)
    end_time1 = time.time()
    t1 = end_time1 - start_time1

    start_time2 = time.time()
    fib_time_rec(i)
    end_time2 = time.time()
    t2 = end_time2 - start_time2


    print(f"n={i} interative time: {t1:.10f} seconds, recursive time: {t2:.10f} seconds")

