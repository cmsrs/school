============================================================
35 ZESTAWÓW DANYCH DLA BAZY DANYCH SZKOŁY
============================================================

STRUKTURA:
- Każdy zestaw to osobny katalog (zestaw_01 do zestaw_35)
- W każdym katalogu znajdują się 4 pliki CSV:
  1. classes.csv       - 3 klasy (1A, 1B, 2A)
  2. students.csv      - 30 unikalnych uczniów
  3. grades_dictionary.csv - skala ocen 1,0-6,0
  4. student_grades.csv - oceny uczniów

FORMAT DANYCH:
- Separator: średnik (;)
- Format daty: DD.MM.RRRR
- Separator dziesiętny: przecinek (,)
- Kodowanie: UTF-8 z BOM

IMPORT DO MS ACCESS:
1. Utwórz pustą bazę danych w Access
2. Dla każdego pliku CSV:
   - Dane zewnętrzne → Plik tekstowy
   - Wybierz plik
   - W kroku 1: Zaznacz 'Pierwszy wiersz zawiera nazwy pól'
   - W kroku 2: Zmień separator na 'Średnik'
   - W kroku 3: Ustaw typy danych:
     * id: Liczba całkowita
     * grade_value: Liczba dziesiętna
     * grade_date: Data (format: DD.MM.RRRR)
   - W kroku 4: Zaznacz 'Dodaj klucz główny'

UWAGA: Ze względu na polski format dziesiętny (przecinek), w Accessie
kolumna grade_value w grades_dictionary.csv może być błędnie rozpoznana
jako tekst. Można to naprawić po imporcie zmieniając typ pola lub
używając funkcji konwertującej.

© Wygenerowano: {date('d.m.Y H:i:s')}