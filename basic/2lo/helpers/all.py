# Generator arkusza ocen (Teacher's Tool)
print(f"{'Nr':<3} | {'Liczba':<6} | {'BIN':<10} | {'HEX':<5} | {'OCT':<5}")
print("-" * 40)

for nr in range(1, 41):
    liczba = nr + 100
    print(f"{nr:<3} | {liczba:<6} | {bin(liczba)[2:]:<10} | {hex(liczba)[2:].upper():<5} | {oct(liczba)[2:]:<5}")
