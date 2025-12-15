# Sprzedaż 

## Ćwiczenie ma na celu użycie komend
- text to columns
- if
- sum
- sumif
- sort
- pivot tables
- pie chart

Twoim zdaniem jest zaimportować plik: sales_data.csv do excela następnie zrobić zestawienie pokazane w pdf-ie: robert_szczepanski_1f.pdf

Aby to zrealizowac nalezy nastepujace czynnosci wykonac:

1. pobieramy plik sales_data.csv do exela
2. rozdzielamy kolumne sprzedawcza na imie i nazwisko (data -> tekst jako kolumny)
3. dodajemy pusta kolumne zatytuowana 'zysk' po  kolumnie 'cena sprzedazy' zasilamy ta kolumne danymi zysk = cena_sprzedazy - cena z magazynu (pamietaj o prawidlowym ustawieniu wartosci kulumn jako walutowe - zamien kropke na przecinek jesli bedzie taka koniecznosc)
4. dodajemy kolumne 'prowizja sprzedawcy' po kolumnie 'zysk'
jesli cena_sprzedazy > 1000 -> zysk * 0.2
przeciwnie zysk * 0.1
tj.:
prowizja: 
- 10% dla produktow mniejszych niz 1000zl
- 20% dla produktow wiekszych niz 1000zl

5 liczymy nastepujace dane:
- Suma ceny sprzedazy
- suma wartosci ceny sprzedazy powyzej 1000
- suma wartosci ceny sprzedazy ponizej 1000
(za pomoca sum oraz sumif)

5. Tworzymy pivot table (tabele przestawna) i dodajemy dane jak w pdf-e
dla kazdego ze sprzedawcy (po nazwisku)
dodajemy Suma z ceny sprzedazy, liczba produktów jakie dany sprzedawca sprzedal oraz suma prowizji danego sprzedawcy

6 tworzymy wykres taki jak w pdf-ie

7. dodajemy do tego skoroszytu dane z p5

8. zamieniamy na pdf (w drukuj oraz dopasowywujemy dane aby zmieniscily sie na jednej stronie - pdf-a)









miesiac
nr tranzakcji
kod produktu
opis produktu
cena z magazynu
cena sprzedazy
sprzedawca
wojewodztwo

zysk
prowizja: 
- 10% dla produktow mniejszych niz 1000zl
- 20% dla produktow wiekszych niz 1000zl


Opis danych:

    Miesiąc: Zakres od stycznia do grudnia 2024 roku.

    Nr transakcji: Unikalny identyfikator transakcji (T001-T130).

    Kod produktu: Unikalny kod produktu (PROD001-PROD100).

    Opis produktu: Krótki opis produktu elektronicznego/RTV/AGD.

    Cena z magazynu: Cena zakupu/koszt produktu (zł).

    Cena sprzedaży: Cena końcowa dla klienta (zł).

    Sprzedawca: Imię i nazwisko sprzedawcy (6 różnych osób).

    Województwo: Losowo przydzielone województwa z Polski.

