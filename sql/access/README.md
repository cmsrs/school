# Ms-Access – zadanie

## 🎯 Cel ćwiczenia
Praktyczne wykorzystanie MS Access do importu danych, tworzenia relacji, kwerend i raportów na podstawie rzeczywistych danych szkolnych.

## 📊 Struktura bazy danych
![Schemat bazy danych](../sqlite/school_structure.png)

*Diagram przedstawia relacje między tabelami zawierającymi dane o klasach, uczniach i ocenach.*

## 📋 Zadanie do wykonania

1. zaimportuj nastepujace pliki - import csv
### 1. **Import danych CSV**
Każdy uczeń otrzymuje **unikalny zestaw danych** (numer odpowiada numerowi w dzienniku Librus).

**Pliki do zaimportowania** (znajdziesz w folderze `zestawienia/zestawy_danych_access`):
- `classes.csv` - dane o klasach
- `students.csv` - dane o uczniach  
- `grades_dictionary.csv` - słownik ocen
- `student_grades.csv` - oceny uczniów

### 2. **Utworzenie relacji między tabelami**
W MS Access:
- Przejdź do zakładki **Narzędzia bazy danych → Relacje**
- Połącz tabele odpowiednimi relacjami zgodnie ze schematem

Narzędzia bazy danych -> Relacje

### 3. **Tworzenie kwerendy**
Utwórz kwerendę SQL, która wyświetli następujące informacje:
- **Klasa** ucznia
- **Imię** i **nazwisko**
- **Średnią ocen** (zaokrągloną do 2 miejsc po przecinku)
- **Sumę wszystkich ocen**
- **Liczbę otrzymanych ocen**


### 4. **Generowanie raportu**
Na podstawie utworzonej kwerendy stwórz **raport** w MS Access, który:
- Będzie czytelnie prezentował dane
- Zostanie posortowany według średniej ocen (malejąco)


### 5. **Eksport do PDF**
Wygeneruj plik **PDF** z utworzonego raportu.

**Wzór raportu:** `zestawienia/zestawienia_pdf_znak/zestawienie_XX.pdf`


## 💯 Kryteria oceny

| Ocena | Opis |
|:------|:------|
| **2** | Import danych i utworzenie kwerendy wyświetlającej tylko uczniów i klasy |
| **3** | Poprawnie utworzona kwerenda z punktu 3 |
| **4** | Kwerenda (pkt 3) + raport (pkt 4) |
| **5** | Kwerenda + raport + poprawnie wygenerowany PDF |
| **6** | Wszystkie powyższe + dodatkowe zadanie rozszerzające|

Zadanie na ocenę celującą (6)

Rozszerz strukturę bazy danych o przedmioty szkolne:

    Zaproponuj zmiany w strukturze bazy:

        W jakich tabelach powinny znaleźć się dane o przedmiotach?

        Jakie nowe relacje należy utworzyć?

    Wprowadź zmiany ręcznie w swojej bazie:

        Dodaj tabelę subjects (przedmioty)

        Zmodyfikuj istniejące tabele/relacje

        Uzupełnij przykładowymi danymi

    Utwórz kwerendę, która wyświetli wszystkie oceny wraz z przedmiotem dla danego ucznia

        Zastawienie ma zawierać następujące kolumny: Nazwa przedmiotu, ocena










