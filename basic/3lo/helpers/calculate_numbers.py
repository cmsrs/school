def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def nww(a, b):
    return (a * b) // nwd(a, b)

def show_results(number_librus):
    a = number_librus + 200
    b = number_librus + 300
    l1 = 2
    l2 = 3

    nwd_val = nwd(a, b)
    nww_val = nww(a, b)

    print(f"==numer_z_librusa={number_librus}============")
    print(f"a = {a}, b = {b}")
    print(f"NWD({a}, {b}) = {nwd_val}  NWW({a}, {b}) = {nww_val}")
    print(f"a/b = {a}/{b} = (a/nwd)/(b/nwd) = {a//nwd_val}/{b//nwd_val}")
    num = (l1 * nww_val // a) + (l2 * nww_val // b)
    print(f"l1/a + l2/b = {l1}/{a} + {l2}/{b} = {num}/{nww_val}")


#nr_librus = ''
nr_librus = 40 
if nr_librus:
    show_results(nr_librus)
else:
    for i in range(1, 41):
        show_results(i)
