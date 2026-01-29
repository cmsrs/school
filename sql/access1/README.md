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
4. Przeciągnij tabelę **klasy** do obszaru projektowania
5. Kliknij dwukrotnie na **\*** (wybór wszystkich kolumn)
6. W dolnej części, w kolumnie **lubi_przedmiot** wpisz:  
   `[Twój ulubiony przedmiot]` (używając własnego ulubionego przedmiotu)
7. Kliknij przycisk **Uruchom** (czerwony wykrzyknik)
8. zapisz kwerende jako `ulubiony_przedmiot`

## KROK 5: Utwórz raport PDF
1. Stwórz raport na podstawie zapytania z **kroku 4**
2. Przejdź do: **Tworzenie** → **Raport**
3. W nagłówku raportu wpisz swoje **imię i nazwisko**
4. Zapisz jako plik pdf: W podgląd wydruku → PDF lub XPS
5. Zapisz raport jako `ulubiony_przedmiot`

przykładowy raport pdf:

**[zestawienie_lubie_robert_szczepanski_4lb_nr30.pdf](https://raw.githubusercontent.com/cmsrs/school/main/sql/access1/zestawienie_lubie_robert_szczepanski_4lb_nr30.pdf)**


# ZADANIA DODATKOWE (dla chętnych na 5+)

## Pytanie 1

1. **Co jest nieoptymalne** w strukturze tej bazy danych?
2. **Zaproponuj lepszy projekt** w formie schematu.
3. **Jakie problemy** mogą wyniknąć z obecnego rozwiązania?

### Podpowiedź

Pomyśl o polu `ulubiony_przedmiot` jako tekście, który każdy może wpisać inaczej:
- `"matematyka"` vs `"Matematyka"` vs `"matma"` vs `"matematyk"`
- `"fizyka"` vs `"Fizyka"` vs `"fiz"`
- `"w-f"` vs `"WF"` vs `"wychowanie fizyczne"`

Co się stanie, gdy będziesz chciał sprawdzić, ilu uczniów lubi matematykę?

> **Za w pełni działającą implementację w Accessie - dodatkowa ocena!**

---

## Pytanie 2

A co jeśli uczeń lubi **kilka przedmiotów**? Na przykład:
- Matematykę **i** informatykę
- WF **i** historię
- Język polski **i** chemię **i** geografię

**Jak rozwiązać ten problem w projekcie bazy danych?**

> **Możesz narysować schemat relacyjny w Inkscape lub innym programie graficznym lub na kartce.**

---

**Uwaga:** Nazwy plików (bazy i raportu) oraz nagłówek raportu powinny umożliwiać łatwą identyfikację autora i klasy.