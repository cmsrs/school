# Sortowanie bąbelkowe (Bubble Sort):

## Jak to działa:

1. Przejdź przez tablicę, jeden element po drugim.

2. Dla każdego elementu porównaj go z następnym elementem.

3. Jeśli bieżący element jest większy niż następny, zamień je miejscami, aby większy element znalazł się dalej.

4. Przejdź przez tablicę tyle razy, ile jest w niej elementów.

## Ręczne przejście przez tablicę – pierwsza iteracja pętli:

- **Krok 1**: Zaczynamy od nieposortowanej tablicy.
[8, 12, 9, 11, 3]

- **Krok 2**: Patrzymy na dwie pierwsze wartości. Czy mniejsza wartość jest pierwsza? Tak, więc nie musimy ich zamieniać.

[```8```, ```12```, 9, 11, 3]

- **Krok 3**: Przesuwamy się o jeden krok i patrzymy na wartości 12 i 9. Czy mniejsza wartość jest pierwsza? Nie.

[8, ```12```, ```9```, 11, 3]

- **Krok 4**: Musimy więc je zamienić miejscami, aby 9 była pierwsza.

[8, ```9```, ```12```, 11, 3]

- **Krok 5**: Przesuwamy się o jeden krok dalej, patrzymy na 12 i 11.

[8, 9, ```12```, ```11```, 3]

- **Krok 6**: Musimy je zamienić miejscami, aby 11 znalazła się przed 12.

[8, 9, ```11```, ```12```, 3]

- **Krok 7**: Patrzymy na 12 i 3 — czy trzeba je zamienić? Tak.

[8, 9, ```11```, ```12```, 3]

- **Krok 8**: Zamieniamy 12 i 3, aby 3 znalazła się pierwsza.

[8, 9, 11, ```3```, ```12```]


<img src="./bubble_sort.png">

Rys. 1. Implementacja algorytmu sortowania bąbelkowe w python

<img src="./zamiana_zmiennych.png">

Rys. 2. Ilustracja zamiany wartości dwóch zmiennych
