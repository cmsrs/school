# Zadania:

Należy napisać następujące zapytania SQL na stronie: [OnlineGDB](https://www.onlinegdb.com) (baza danych SQLite), korzystając z bazy danych dostępnej pod adresem: [SQLite.sql](https://github.com/cmsrs/school/blob/main/sql/sqlite.sql).

1. Dodanie kolumny sex do tabeli students

    Dodaj kolumnę sex do tabeli students, przechowującą informacje o płci (M - mężczyzna, F - kobieta).
    Uzupełnij przykładowe dane, modyfikując istniejącą strukturę (plik sqlite.sql).

2. Wyświetlenie wszystkich mężczyzn w tabeli students

    Pobierz wszystkich studentów, którzy są mężczyznami (sex = 'M') i należą do klasy (pomijając tych, którzy do żadnej klasy nie należą).
    Wynik powinien zawierać następujące kolumny: Imię, Nazwisko, Klasa.

3. (Dodatkowe) Wyświetlenie ocen dla studentów z punktu 2

    Do wyników z punktu 2 dołącz oceny każdego studenta.
    Wyświetl następujące kolumny: Imię, Nazwisko, Klasa, Oceny.
    Pokaż wszystkich studentów, nawet tych, którzy nie mają ocen.
    Oceny dla każdego studenta powinny być wyświetlone w jednej kolumnie, oddzielone przecinkiem.

4. (Dodatkowe) Zmiana imion wszystkich studentek na "KATE"

    Napisz zapytanie SQL zmieniające imię wszystkich studentek (sex = 'F') na "KATE".
    Składnia przykładowego zapytania SQL do aktualizacji wartości w tabeli:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Po wykonaniu zapytania wyświetl zawartość tabeli students.