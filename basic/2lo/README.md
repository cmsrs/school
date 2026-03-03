# Zadanie: Architektura informacji i systemy liczbowe

Celem zadania jest przećwiczenie precyzyjnego wykonywania instrukcji, poprawnego nazewnictwa zasobów oraz konwersji liczb między systemami, które stanowią fundament informatyki.

---

### Krok 1: Przygotowanie dokumentacji (MS Word)
1. Pobierz plik graficzny (zestaw) przypisany do Twojego **numeru z dziennika Librus**.
2. Otwórz program MS Word i stwórz nowy dokument.
3. Wklej pobrany obraz do dokumentu.
4. **Zapisz plik**, stosując wyłącznie **małe litery**, bez polskich znaków i bez spacji.
   * Zamiast spacji użyj tzw. **podłogi** (podkreślnika) `_`.
   * Schemat nazwy: `klasa_imie_nazwisko.docx`
   * Przykład: `2lo_jan_kowalski.docx`
---

### Krok 2: Obliczenia systemów liczbowych
Musisz wyznaczyć swoją **liczbę bazową** i pokazać proces jej zamiany.

1. **Twoja liczba:** Do swojego numeru z dziennika dodaj **100**.  
   *(Przykład: Numer 12 + 100 = Twoja liczba to 112)*
2. **System Binarny (Dwójkowy):** W dokumencie Word rozpisz swoją liczbę jako sumę potęg liczby 2.
   * Skorzystaj z tabeli pomocniczej poniżej.
   * Przykład zapisu dla liczby 13:  
     $13 = 8 + 4 + 1 = 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 \rightarrow \mathbf{1101_2}$
3. **Systemy Hex i Oct:** Podaj wynik zamiany swojej liczby na system szesnastkowy (Hex) oraz ósemkowy (Oct).

**Tabela pomocnicza (Wagi bitów):**
| $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |


### 💡 Pro Tip: Szybka zamiana (bez dzielenia!)
Jeśli masz już wynik binarny, możesz zamienić go na Hex i Oct w kilka sekund:

* **System Ósemkowy (Oct):** Podziel swój ciąg binarny na grupy po **3 cyfry** (licząc od prawej!). Każdej grupie przypisz wartość (4, 2, 1).
    * Przykład: `100 001 000` -> `4 1 0` -> **410₈**
* **System Szesnastkowy (Hex):** Podziel ciąg na grupy po **4 cyfry** (licząc od prawej!). Każdej grupie przypisz wartość (8, 4, 2, 1).
    * Przykład: `1000 0100` -> `8 4` -> **84₁₆**

*Wskazówka: Aby w Wordzie napisać potęgę (indeks górny), użyj skrótu `Ctrl` + `Shift` + `+`.*

---

### Krok 3: Automatyczna weryfikacja (Python)
Programiści nie liczą wszystkiego ręcznie – tworzą narzędzia. Użyj poniższego kodu, aby sprawdzić, czy Twoje obliczenia w Wordzie są poprawne.

1. Skopiuj kod:
```python
# Tester systemów liczbowych
try:
    liczba = int(input("Wpisz swoją liczbę bazową (numer + 100): "))
    print(f"\n--- WYNIKI DLA LICZBY {liczba} ---")
    print(f"BIN (Dwójkowy): {bin(liczba)[2:]}")
    print(f"OCT (Ósemkowy): {oct(liczba)[2:]}")
    print(f"HEX (Szesnastkowy): {hex(liczba)[2:].upper()}")
    print("-" * 25)
except ValueError:
    print("Błąd: Wpisz poprawną liczbę całkowitą!")
```    

### Krok 4: Pakowanie i wysyłka (Deployment)
Informatyka to porządek w plikach. Twoje zadanie musi być spakowane profesjonalnie:

1. **Stwórz folder** (również używając tylko małych liter i "podłogi"): `klasa_imie_nazwisko`
   * Przykład: `2lo_jan_kowalski`
2. **Do środka włóż:**
   * Gotowy plik Word (`.docx`)
   * Pobraną grafikę z Twojego zestawu
3. **Zarchiwizuj dane:** Kliknij Prawym Przyciskiem Myszy na folder -> **Wyślij do** -> **Folder skompresowany (zip)**.
4. **Finalizacja i Oddanie:** Gotowy plik `.zip` pokaż do oceny.


> ### ⚠️ WAŻNA ZASADA (PRO TIP):
> Jeśli po spakowaniu folderu do ZIP przypomnisz sobie, że musisz coś poprawić w Wordzie:
> 1. **Nie edytuj pliku wewnątrz ZIP-a!** (Zmiany się nie zapiszą).
> 2. Usuń stary plik ZIP.
> 3. Popraw plik w zwykłym folderze.
> 4. Spakuj folder jeszcze raz.
---

### Kryteria oceny (Checklista)
| Zadanie | Punkty |
| :--- | :---: |
| [ ] Plik Word i folder nazwane zgodnie ze schematem | 1 pkt |
| [ ] Poprawny zapis sumy potęg binarnej w Wordzie | 2 pkt |
| [ ] Prawidłowe wyniki dla systemów HEX i OCT | 1 pkt |
| [ ] Poprawnie utworzone archiwum ZIP | 1 pkt |


### 🐍 Kod źródłowy: Jak działa ten system?
Dla zainteresowanych – oto jak wygląda kod, który generuje poprawne wyniki dla całej klasy w mniej niż 0.1 sekundy. Możecie go uruchomić, aby zobaczyć magię automatyzacji.

```python
# Generator arkusza ocen (Teacher's Tool)
print(f"{'Nr':<3} | {'Liczba':<6} | {'BIN':<10} | {'HEX':<5} | {'OCT':<5}")
print("-" * 40)

for nr in range(1, 41):
    liczba = nr + 100
    print(f"{nr:<3} | {liczba:<6} | {bin(liczba)[2:]:<10} | {hex(liczba)[2:].upper():<5} | {oct(liczba)[2:]:<5}")
```

> **Uwaga:** Jeśli struktura plików lub nazewnictwo będą błędne, punkty zostaną odjęte.
