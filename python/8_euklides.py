
def euklides(a, b):

    while b > 0:
        print("a: ", a, " b: ", b,  "a%b:", a % b)
        tmp = b
        b = a % b        
        a = tmp

    return a


a = 282 #int(input("Podaj pierwszą liczbę: "))
b = 78  #int(input("Podaj drugą liczbę: "))
x = euklides(a, b)

print(f"Największy wspólny dzielnik liczb {a} i {b} to: ", x)
