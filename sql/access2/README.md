# 📊 Zadanie 2: System ocen w klasie

## 🎯 Cel zadania
Rozszerzenie bazy danych z Zadania 1 o system oceniania. Nauczysz się tworzyć nowe tabele, relacje między nimi oraz używać funkcji agregujących w MS Access.

---

## KROK 1: Otwórz swoją bazę z Zadania 1
1. Znajdź na dysku plik: **moja_klasa_[nazwisko].accdb**
2. Otwórz go w MS Access
3. Upewnij się, że masz:
   - Tabelę **klasy** z wpisanymi klasami
   - Tabelę **uczniowie** z 7 osobami
   - Zapytanie **ulubiony_przedmiot**

## KROK 2: Dodaj nową tabelę "oceny"
1. Kliknij: **Tworzenie** → **Tabela**
2. Przełącz się do **Widoku projektu** (kliknij prawym na nagłówek tabeli → Widok projektu)
3. Stwórz 4 kolumny:

| Nazwa pola | Typ danych | Uwagi |
|------------|------------|-------|
| `id` | **Autonumer** | Zaznacz jako **Klucz główny** (ikonka klucza) |
| `uczen_id` | **Liczba** | Będzie łączyć z tabelą `uczniowie` |
| `przedmiot` | **Krótki tekst** | Nazwa przedmiotu szkolnego |
| `ocena` | **Liczba** | Ocena od 1 do 6 |

4. Zapisz tabelę jako: **oceny**

## KROK 3: Utwórz relację między tabelami
1. Kliknij: **Narzędzia bazy danych** → **Relacje**
2. Jeśli tabele nie są widoczne, kliknij: **Pokaż tabelę** → dodaj `uczniowie` i `oceny`
3. Połącz tabele:
   - Przeciągnij pole **`id`** z tabeli `uczniowie`
   - Upuść na pole **`uczen_id`** w tabeli `oceny`
4. W oknie **Edytuj relacje** zaznacz:
   - ✅ **Wymuszaj integralność danych**
   - ⬜ Kaskadowe aktualizowanie powiązanych pól (opcjonalnie)
   - ⬜ Kaskadowe usuwanie powiązanych rekordów (NIE zaznaczaj!)
5. Kliknij **Utwórz**
6. Zapisz i zamknij okno relacji (✅ na pasku narzędzi)

## KROK 4: Wpisz przykładowe oceny
1. Otwórz tabelę **oceny** (kliknij 2x w oknie nawigacji)
2. Wpisz **8-12 ocen** dla różnych uczniów z Twojej klasy:

| uczen_id | przedmiot | ocena |
|----------|-----------|-------|
| 1 | matematyka | 5 |
| 1 | język polski | 4 |
| 2 | matematyka | 3 |
| 2 | WF | 6 |
| 3 | historia | 4 |
| 4 | biologia | 5 |
| 1 | chemia | 4 |
| 5 | matematyka | 2 |

**❗ WAŻNE:** Używaj tylko `uczen_id`, które istnieją w tabeli `uczniowe`!

## KROK 5: Stwórz zapytanie zliczające oceny
1. Kliknij: **Tworzenie** → **Projekt kwerendy**
2. W oknie **Pokaz tabelę**:
   - Zaznacz `uczniowie` → **Dodaj**
   - Zaznacz `oceny` → **Dodaj**
   - Kliknij **Zamknij**
3. Access automatycznie połączy tabele (zobaczysz linię łączącą)
4. Kliknij 2x na pola z tabeli `uczniowie`:
   - `imie`
   - `nazwisko`
5. Kliknij 2x na pole `ocena` z tabeli `oceny`
6. Włącz funkcje agregujące:
   - Kliknij zakładkę **Projekt** na wstążce
   - Kliknij przycisk **Sumy** (ikonka Σ)
7. W dolnej części projektanta:
   - Przy `imie` i `nazwisko` zostaw **Grupowanie po**
   - Przy `ocena` zmień na **Liczba**
8. Kliknij **Uruchom** (czerwony wykrzyknik ✓)
9. Zapisz zapytanie jako: `liczba_ocen_ucznia`

## KROK 6: Wygeneruj raport PDF
1. W oknie nawigacji kliknij 2x na zapytanie `liczba_ocen_ucznia`
2. Naciśnij **Ctrl + P** (tak jak w Wordzie!)
3. W oknie drukowania:
   - **Drukarka:** wybierz `Microsoft Print to PDF`
   - **Zakres stron:** zaznacz `Wszystko`
4. Kliknij **Drukuj**
5. Zapisz plik jako: **raport2_[twoje_nazwisko].pdf**
6. Wyślij plik PDF na Teams/email

---

## ✅ Co sprawdzę w Twojej pracy?

| Element | Punkty | 
|---------|--------|
| **Tabela `oceny`** z 4 kolumnami | 2 pkt |
| **Relacja** z integralnością danych | 2 pkt |
| **8-12 ocen** w tabeli `oceny` | 2 pkt |
| **Zapytanie** poprawnie zliczające oceny | 3 pkt |
| **Raport PDF** z wynikami | 1 pkt |
| **RAZEM** | **10 pkt** |

**Skala ocen:**
- **9-10 pkt** = 5
- **7-8 pkt** = 4  
- **5-6 pkt** = 3
- **0-4 pkt** = 2

---

## 🆘 Rozwiązywanie problemów

### ❌ "Błąd przy wpisywaniu oceny"
**Powód:** `uczen_id` nie istnieje w tabeli `uczniowie`
**Rozwiązanie:** Sprawdź jakie ID masz w tabeli `uczniowie` i używaj tylko tych

### ❌ "Przycisk Sumy (Σ) jest wyszarzony"
**Rozwiązanie:** Najpierw dodaj pola do zapytania, dopiero potem kliknij Sumy

### ❌ "Wszyscy mają LiczbaOcen = 1"
**Rozwiązanie:** Upewnij się, że przy kolumnie `ocena` masz **Liczba**, a nie **Grupowanie po**

### ❌ "Nie ma Microsoft Print to PDF"
**Alternatywa:**
1. Kliknij prawym na zapytanie
2. Wybierz **Eksportuj** → **PDF lub XPS**

---

## ⭐ Zadanie dodatkowe (dla chętnych)
Stwórz zapytanie pokazujące **średnią ocen** każdego ucznia:
1. W istniejącym zapytaniu zmień **Liczba** na **Średnia**
2. Zmień nazwę kolumny na `srednia_ocen`
3. Dodaj zaokrąglenie do 2 miejsc po przecinku

---

**Termin wykonania: 3 tygodnie**

**Pracując w domu – zrób zrzut ekranu Accessa jako dowód samodzielnej pracy!**

---

*Powodzenia! Pytania zadawaj na lekcji lub przez dziennik elektroniczny.*