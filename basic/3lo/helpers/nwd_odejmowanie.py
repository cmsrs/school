def nwd_odejmowanie(a, b):
    while a != b:
        print(f"a={a}, b={b}")
        if a > b:
            a -= b
        else:
            b -= a
    print(f"a={a}, b={b}")
    return a


number_librus = 40
a = number_librus + 200
b = number_librus + 300


nwd_odejmowanie(a, b)
