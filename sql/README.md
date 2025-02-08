# Zadania:

Należy napisać następujące zapytania SQL na stronie: [OnlineGDB](https://www.onlinegdb.com) (baza danych SQLite), korzystając z bazy danych dostępnej pod adresem: [SQLite.sql](https://github.com/cmsrs/school/blob/main/sql/sqlite.sql).
Zachęcam do zapoznania się z przykładowymi zapytaniami zamieszczonymi w pliku: [query.sql](https://github.com/cmsrs/school/blob/main/sql/query.sql).


1. Dodanie kolumny ```sex``` (płeć) do tabeli students

    Dodaj kolumnę ```sex``` do tabeli students, przechowującą informacje o płci (M - mężczyzna, F - kobieta).
    Uzupełnij ręcznie przykładowe dane, modyfikując istniejącą strukturę (plik sqlite.sql).

2.  Pobierz wszystkich studentów, którzy są mężczyznami (sex = 'M') i należą do klasy (pomijając tych, którzy do żadnej klasy nie należą).
    Wynik powinien zawierać następujące kolumny: Imię, Nazwisko, Płeć, Klasa.

3. (Dodatkowe) Wyświetlenie ocen dla studentów z punktu 2

    Do wyników z punktu 2 dołącz oceny każdego studenta.
    Wyświetl następujące kolumny: Imię, Nazwisko, Płeć, Klasa, Oceny.
    Pokaż wszystkich studentów, nawet tych, którzy nie mają ocen.
    Oceny dla każdego studenta powinny być wyświetlone w jednej kolumnie, oddzielone przecinkiem.

4. (Dodatkowe) Zmiana imion wszystkich studentek na "KATE"

    Napisz zapytanie SQL zmieniające imię wszystkich studentek (sex = 'F') na "KATE".
    Składnia przykładowego zapytania SQL do aktualizacji wartości w tabeli:
    Po wykonaniu zapytania aktualizującego studentów wyświetl zawartość tabeli ```students```.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

5. Zaproponuj sposób dodania przedmiotów do istniejącej bazy danych. Określ, w jakich tabelach powinny się znaleźć i jakie relacje między nimi należy utworzyć.
    
    