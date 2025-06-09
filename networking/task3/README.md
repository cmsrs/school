# Zadanie 3 – Programy wypisujące dane ucznia (Python i C)

## 🎯 Cel

Nauczyć się pisać i uruchamiać podstawowe programy:
- w języku **Python** (skryptowym),
- w języku **C** (kompilowanym),

które wypisują dane ucznia: **imię, nazwisko i klasę**.

---

## 🔐 Logowanie do serwera

Przed wykonaniem zadania zaloguj się na serwer FreeBSD przez SSH:

```bash
ssh school@192.168.88.202
```

Dane dostępowe:

    Adres IP serwera: 192.168.88.202
    (adres może się zmieniać – sprawdź na lekcji)

    Nazwa użytkownika SSH: school

    Hasło: school123

🐍 Część 1: Program w Pythonie
🔧 Instrukcje:

Utwórz plik o nazwie: imie_nazwisko_klasa.py


Przykład: jan_kowalski_2c.py

Zawartość pliku:

```
print("Imię: Jan")
print("Nazwisko: Kowalski")
print("Klasa: 2C")
```

Uruchom program:

```bash
python3.11 jan_kowalski_2c.py
```

💻 Część 2: Program w języku C
🔧 Instrukcje:

Utwórz plik o nazwie: imie_nazwisko_klasa.c

Przykład: jan_kowalski_2c.c

Zawartość pliku:

```
#include <stdio.h>

int main() {
    printf("Imię: Jan\n");
    printf("Nazwisko: Kowalski\n");
    printf("Klasa: 2C\n");
    return 0;
}
```

Skompiluj program:

```
gcc jan_kowalski_2c.c -o jan_kowalski_2c
```

Uruchom program:
 
```bash
./jan_kowalski_2c
```    

✅ Przykładowy wynik działania

Imię: Jan
Nazwisko: Kowalski
Klasa: 2C

📌 Uwaga

Gotowe programy należy pokazać i uruchomić na lekcji po zalogowaniu się na serwer.

