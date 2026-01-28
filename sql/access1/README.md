# Instrukcja wykonania zadania w Microsoft Access

## KROK 1: Pobierz i otwórz szablon
1. Pobierz plik: **[szablon_klasa.accdb](https://raw.githubusercontent.com/cmsrs/school/main/sql/access1/szablon_klasa.accdb)**
2. Zapisz jako: **moja_klasa_[nazwisko].accdb** (w miejsce `[nazwisko]` wpisz swoje nazwisko)

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

1. **TY** – Twoje imię, nazwisko, Twój ulubiony przedmiot, `klasa_id = 1`
2. **3 osoby** z Twojej klasy – `klasa_id = 1`
3. **3 osoby** z klasy 7d – `klasa_id = 2`

## KROK 4: Utwórz zapytanie
1. Przejdź do: **Tworzenie** → **Projekt kwerendy**
2. Przeciągnij tabelę **uczniowie** do obszaru projektowania
3. Kliknij dwukrotnie na **\*** (wybór wszystkich kolumn)
4. W dolnej części, w kolumnie **lubi_przedmiot** wpisz:  
   `[Twój ulubiony przedmiot]` (używając własnego ulubionego przedmiotu)
5. Kliknij przycisk **Uruchom** (czerwony wykrzyknik)

## KROK 5: Utwórz raport PDF
1. Stwórz raport na podstawie zapytania z **kroku 4**
2. W nagłówku raportu wpisz swoje **imię i nazwisko**
3. Zapisz plik jako:  
   **raport_[nazwisko]_[twoja_klasa].pdf**  
   (np. `raport_kowalski_3a.pdf`)

---

**Uwaga:** Nazwy plików (bazy i raportu) oraz nagłówek raportu powinny umożliwiać łatwą identyfikację autora i klasy.