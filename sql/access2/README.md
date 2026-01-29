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
2. Jeśli tabele nie są widoczne, kliknij: **Pokaż tabelę** → dodaj `uczniowie` i `oceny`, możesz także przeciągnąć tabelę do obszaru roboczego,
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
2. Wpisz **8-12 ocen** dla różnych uczniów z Twojej klasy np.:

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
   - Kliknij zakładkę **Projekt kwerendy** na wstążce
   - Kliknij przycisk **Sumy** (ikonka Σ)
7. W dolnej części projektanta:
   - Przy `imie` i `nazwisko` zostaw **Grupowanie według**
   - Przy `ocena` zmień na **Policz**
8. Kliknij **Uruchom** (czerwony wykrzyknik ✓)
9. Zapisz zapytanie jako: `liczba_ocen_ucznia`

## KROK 6: Utwórz raport PDF
1. Stwórz raport na podstawie zapytania z **kroku 5**
2. W oknie nawigacji kliknij 2x na zapytanie `liczba_ocen_ucznia`
2. Przejdź do: **Tworzenie** → **Raport**
3. W nagłówku raportu wpisz swoje **imię i nazwisko klasa nr_dzienika**
4. Ustaw odpowiednią szerokość kolumn
5. Zapisz jako plik pdf: W podgląd wydruku → PDF lub XPS
6. Zapisz raport jako `liczba_ocen_ucznia`

przykładowy raport pdf:

**[liczba_ocen_ucznia_robert_szczepanski_4lb_nr30.pdf](https://raw.githubusercontent.com/cmsrs/school/main/sql/access2/liczba_ocen_ucznia_robert_szczepanski_4lb_nr30.pdf)**

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

## 💡 PYTANIE BONUSOWE (5+)

Jakie problemy mogą powstać, gdy każdy wpisuje nazwy przedmiotów oraz oceny samodzielnie?
Jak byś to naprawił?

> Możesz narysować schemat relacyjny w Inkscape lub innym programie graficznym lub na kartce - rozwiązujący te problemy.

---

**Kolejne problemy do rozważenia (tylko sugestia - robota w nieskończoność  😉 ):**

> To **NIE** jest do wykonania. To lista przykładów, jak szybko prosty system robi się skomplikowany w prawdziwym życiu. Wystarczy, że **rozumiesz, że takie problemy istnieją** – nie musisz ich implementować.

- Historia zmian ocen oraz data wprowadzenia danej oceny
- Nauczyciele przypisani do przedmiotów  
- Typy ocen (sprawdzian, kartkówka, odpowiedź ustna)
- Wagi ocen (różne znaczenie różnych typów)
- Semestry/okresy oceniania
- Uwagi do ocen
- Procentowa skala ocen (np. 87% = 5)
- Nieobecności i usprawiedliwienia
- **"Daj +1"** - system punktów bonusowych od nauczycieli
- **E-dziennik 2.0** - powiadomienia SMS do rodziców przy ocenie < 3
- **Algorytm przewidywania** - czy uczeń zda do następnej klasy
- **Ranking klas** - która klasa ma najlepsze średnie
- **Statystyki nauczycieli** - który wystawia najwięcej szóstek
- **Konkurencja między uczniami** - tabela liderów miesiąca
- **System nagród** - wirtualne odznaki za dobre oceny

---

**Uwaga:** Nazwy plików (bazy i raportu) oraz nagłówek raportu powinny umożliwiać łatwą identyfikację autora i klasy.