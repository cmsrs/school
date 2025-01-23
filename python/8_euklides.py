
def euklides(a, b):

    while b != 0:
        print("a: ", a, " b: ", b,  "a%b:", a % b)
        tmp = b
        b = a % b        
        a = tmp

    return a


a = int(input("Podaj pierwszą liczbę: ")) #282
b = int(input("Podaj drugą liczbę: ")) #78
x = euklides(a, b)

print(f"Największy wspólny dzielnik liczb {a} i {b} to: ", x)
