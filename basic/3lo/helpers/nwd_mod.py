def nwd(a, b):    
    while b:
        print(f"a={a}, b={b}")
        a, b = b, a % b
    print(f"a={a}, b={b}")        
    return a



number_librus = 40
a = number_librus + 200
b = number_librus + 300


nwd(a, b)


