"""
Naiwny algorytm wyszukiwania wzorca w tekście.

Parametry:
text (str): Tekst, w którym szukamy wzorca.
pattern (str): Wzorzec, który chcemy znaleźć w tekście.

Zwraca:
int: Indeks pierwszego wystąpienia wzorca w tekście lub -1, jeśli wzorzec nie został znaleziony.


Wyjaśnienie działania:

    Pobieramy długość wzorca mm.
    Przechodzimy pętlą for przez możliwe pozycje wzorca w tekście.
    Wewnątrz każdej iteracji sprawdzamy znak po znaku, czy wzorzec pasuje do tekstu.
    Jeśli uda się dopasować wszystkie mm znaków, zwracamy indeks pierwszego wystąpienia wzorca.
    Jeśli pętla się zakończy bez znalezienia wzorca, zwracamy -1.

"""

def naive_search(text, pattern):
    mm = len(pattern)
    for i in range(len(text) - mm + 1):
        j = 0
        while j < mm and text[i + j] == pattern[j]: # porównujemy znak po znaku
            j += 1
        if j == mm: # jeśli doszliśmy do końca wzorca
            return i # zwracamy indeks pierwszego wystąpienia wzorca

    return -1

       #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
text = 'sdcostsdfdsasfsdfdasdfdsafdsafcostreytetr'
pattern = 'cost'


result = naive_search(text, pattern)
assert result > -1
#print(f"Pattern found at index: {result}")


result = naive_search(text, "sdcost") # pierwsze wystąpienie wzorca na indeksie 0
assert result == 0


result = naive_search(text, "xxxxxxxxxxxxxxxxxxx") # wzorca nie ma w tekście
assert result == -1



