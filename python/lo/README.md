# Zadania – Kwadraty z Alfabetu

## Zadanie 1

Napisz funkcję `draw_square_from_alphabet`, która rysuje kwadrat o zadanej długości boku, wypełniony kolejnymi wielkimi literami alfabetu.  
Litery powinny być wypisywane wierszami, zaczynając od podanej litery startowej.  
Po literze `'Z'` należy kontynuować od `'A'`.

**Przykład:**  
Dla litery startowej `'X'` i długości boku `6`, wynik powinien wyglądać następująco:

```
X Y Z A B C 
D E F G H I 
J K L M N O 
P Q R S T U 
V W X Y Z A 
B C D E F G 
```


## Zadanie 2

Wykorzystaj funkcję `draw_square_from_alphabet(start, length)`, aby narysować **cztery kwadraty** z kolejnymi literami alfabetu (z zawijaniem po `'Z'`).

Każdy kwadrat ma inny rozmiar boku oraz inny punkt początkowy:

- **Pierwszy kwadrat** – bok: `3`, litera startowa: pierwsza litera **Twojego imienia**
- **Drugi kwadrat** – bok: `4`, litera startowa: pierwsza litera **Twojego nazwiska**
- **Trzeci kwadrat** – bok: `5`, litera startowa: litera oznaczająca **Twoją klasę** (np. `'H'` w `3H`)
- **Czwarty kwadrat** – bok: `6`, litera startowa: `'M'` dla mężczyzny, `'F'` dla kobiety

### Przykład

Dla osoby o danych:

- Imię: **Robert**
- Nazwisko: **Szczepański**
- Klasa: **3H**
- Płeć: **mężczyzna**

Litery startowe to: `R`, `S`, `H`, `M`

**Wynik:**

```
R S T 
U V W 
X Y Z 

S T U V 
W X Y Z 
A B C D 
E F G H 

H I J K L 
M N O P Q 
R S T U V 
W X Y Z A 
B C D E F 

M N O P Q R 
S T U V W X 
Y Z A B C D 
E F G H I J 
K L M N O P 
Q R S T U V 
```


