def nwd_p(a, b):    
    while b:
        print(f"a={a}, b={b}")
        #a, b = b, a % b
        r = a % b
        a = b
        b = r
    print(f"a={a}, b={b}")        
    return a

def nwd_odejmowanie_p(a, b):
    while a != b:
        print(f"a={a}, b={b}")
        if a > b:
            a -= b
        else:
            b -= a
    print(f"a={a}, b={b}")
    return a

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def nww(a, b):
    return (a * b) // nwd(a, b)

def show_results(a,b):
    l1 = 2
    l2 = 3

    nwd_val = nwd(a, b)
    nww_val = nww(a, b)

    print(f"NWD({a}, {b}) = {nwd_val}  NWW({a}, {b}) = {nww_val}")
    print(f"a/b = {a}/{b} = (a/nwd)/(b/nwd) = {a//nwd_val}/{b//nwd_val}")
    num = (l1 * nww_val // a) + (l2 * nww_val // b)
    print(f"l1/a + l2/b = {l1}/{a} + {l2}/{b} = {num}/{nww_val}")


nr_librus = ''
#nr_librus = 40 
if nr_librus:
    show_results(nr_librus)
else:
    for number_librus in range(1, 41):
        a = number_librus + 200
        b = number_librus + 300
        print(f"*************numer_z_librusa={number_librus:02d}*****************")
        print(f"a = {a}, b = {b}")
        print(f"==nwd odejnowanie")
        nwd_odejmowanie_p(a, b)

        print(f"==nwd dzielnie")
        nwd_p(a, b)

        print(f"==dzialania")
        show_results(a,b)

        print(f"")
        print(f"")
        print(f"")
