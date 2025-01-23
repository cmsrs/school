
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

print()
sum = a + b
print(f"Suma tych liczb to: {sum}")

if b != 0:
    print(f"Dzielenie tych liczb to: {a / b}")
else:
    print("Nie mozna dzielic przez zero!")