# 📊 Zadanie 2 uproszczone (zadanie na ocene 4): System ocen w klasie

## KROK 1: Pobierz i otwórz szablon
1. Pobierz plik: **[szablon_klasa_uczniowie_oceny.accdb](https://raw.githubusercontent.com/cmsrs/school/main/sql/access2_proste/szablon_klasa_uczniowie_oceny.accdb)**
2. Zapisz jako: **moja_klasa_oceny_[nazwisko].accdb** (w miejsce `[nazwisko]` wpisz swoje nazwisko)

## KROK 2: Wpisz dane klas (2 minuty)
1. Otwórz tabelę **klasy**
2. Wpisz następujące dane:

| id | nazwa_klasy | status |
|----|-------------|--------|
| 1  | (Twoja klasa) | lo     |
| 2  | 7d          | sp     |

*Zastąp `(Twoja klasa)` rzeczywistą nazwą swojej klasy*

## KROK 3: Wpisz dane uczniów
Otwórz tabelę **uczniowie** i wpisz 7 osób:

1. **TY** – Twoje imię, nazwisko, Twój ulubiony przedmiot oraz nr_dziennika, `klasa_id = 1`
2. **3 osoby** z Twojej klasy – `klasa_id = 1`
3. **3 osoby** z klasy 7d – `klasa_id = 2`

## KROK 4: Wpisz przykładowe oceny
1. Otwórz tabelę **oceny** (kliknij 2x w oknie nawigacji)
2. Wpisz **8-12 ocen** dla różnych uczniów z Twojej klasy oraz 7d np.:

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

**WAŻNE:** Używaj tylko `uczen_id`, które istnieją w tabeli `uczniowie`!

**❗ WAŻNE:** Znajdź swoje id w tabeli uczniów i sobie przypisz największą liczbę ocen (np. 4-5 różnych ocen).

## KROK 5: Stwórz zapytanie zliczające oceny
1. Kliknij: **Tworzenie** → **Projekt kwerendy**
2. W oknie **Pokaz tabelę**:
   - Zaznacz `uczniowie` → **Dodaj**
   - Zaznacz `oceny` → **Dodaj**
   - Kliknij **Zamknij**
3. Access automatycznie połączy tabele (zobaczysz linię łączącą)
4. Kliknij 2x na pola z tabeli `uczniowie`:
   - `id`
   - `imie`
   - `nazwisko`
5. Kliknij 2x na pole `ocena` z tabeli `oceny`
6. Włącz funkcje agregujące:
   - Kliknij zakładkę **Projekt kwerendy** na wstążce
   - Kliknij przycisk **Sumy** (ikonka Σ)
7. W dolnej części projektanta:
   - Przy `id`, `imie` i `nazwisko` zostaw **Grupowanie według**
   - Przy `ocena` zmień na **Policz**
8. Kliknij **Uruchom** (czerwony wykrzyknik ✓)
9. Zapisz zapytanie jako: `liczba_ocen_ucznia`

## Zadanie na ocenę 5

1. Stwórz tabelę `przedmioty` o kolumnach:
   - id (autonumerowanie, klucz główny)
   - nazwa_przedmiotu (krótki tekst)

2. Dodaj kilka przedmiotów (np. matematyka, polski, WF)

3. W tabeli `oceny` dodaj kolumnę `przedmiot_id`

4. Połącz relacją:
   oceny.przedmiot_id → przedmioty.id

5. (dla chętnych)
   Zmodyfikuj zapytanie tak, aby zamiast nazwy przedmiotu z tekstu korzystało z tabeli `przedmioty`

   > Opcjonalnie usuń kolumnę przedmiot z tekstu lub przestań jej używać
   > Dlaczego lepiej mieć tabelę przedmiotów niż wpisywać nazwę ręcznie?