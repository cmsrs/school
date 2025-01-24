

a = 282  #int(input("Podaj pierwszą liczbę: ")) #282
b = 78  #int(input("Podaj drugą liczbę: ")) #78

while (a != b):
    #print("a: ", a, " b: ", b)

    if( a > b ):
        a  = a - b
    else:
        b = b - a

print(f"Największy wspólny dzielnik liczb to: ", a)






