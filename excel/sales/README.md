# Sprzedaż – Ćwiczenie

## Cel ćwiczenia
Ćwiczenie ma na celu użycie następujących funkcji i narzędzi w Excelu:  
- **Text to Columns**  
- **IF**  
- **SUM**  
- **SUMIF**  
- **Sortowanie**  
- **Tabele przestawne (Pivot Tables)**  
- **Wykres kołowy (Pie Chart)**

---

## Zadanie
Twoim zadaniem jest **zaimportowanie pliku [sales_data.csv](https://raw.githubusercontent.com/cmsrs/school/main/excel/sales/sales_data.csv)** do **MS-Excela** lub **Libreoffice calc**, a następnie przygotowanie zestawienia zgodnie z przykładowym PDF-em: [robert_szczepanski_1b.pdf](robert_szczepanski_1b.pdf).

---

## Kroki do wykonania

1. **Import danych**  
   - Pobierz plik [sales_data.csv](https://raw.githubusercontent.com/cmsrs/school/main/excel/sales/sales_data.csv) następnie otwórz go w: **MS-Excela** lub **Libreoffice calc**.

2. **Rozdzielenie kolumny sprzedawcy**  
   - Rozdziel kolumnę z nazwiskami i imionami sprzedawców przy użyciu **Text to Columns**.

3. **Formatowanie kolumn cenowych**
   - Ustaw format walutowy dla kolumn **cena z magazynu** oraz **cena sprzedaży**.

3. **Dodanie kolumny 'Zysk'**  
   - Dodaj pustą kolumnę zatytułowaną **Zysk** po kolumnie `cena_sprzedazy`.  
   - Oblicz wartość zysku:  
     ```
     Zysk = cena_sprzedazy - cena_z_magazynu
     ```  
   - Upewnij się, że kolumny są ustawione jako walutowe (jeśli potrzeba, zamień kropkę na przecinek).

4. **Dodanie kolumny 'Prowizja sprzedawcy'**  
   - Dodaj kolumnę **Prowizja sprzedawcy** po kolumnie `Zysk`.  
   - Oblicz prowizję według warunku:  
     ```
     IF(cena_sprzedazy > 1000, Zysk * 0.2, Zysk * 0.1)
     ```
   - Zasada:  
     - 10% dla produktów mniejszych niż 1000 zł  
     - 20% dla produktów większych niż 1000 zł

5. **Podsumowania**  
   - Oblicz:  
     - Suma ceny sprzedazy  
     - Suma wartości ceny sprzedazy powyżej 1000 zł
     - Suma wartości sprzedaży do 1000 zł (włącznie)
   - Wykorzystaj funkcje **SUM** oraz **SUMIF**.

6. **Tabela przestawna (Pivot Table)**  
   - Utwórz tabelę przestawną z danymi dla każdego sprzedawcy (po nazwisku).  
   - Wyświetl w tabeli:  
     - Suma ceny sprzedazy  
     - Liczba produktów sprzedanych przez danego sprzedawcę  
     - Suma prowizji danego sprzedawcy
   - Wyniki posortuj alfabetycznie według nazwiska sprzedawcy.     

7. **Wykres**  
   - Utwórz wykres taki jak w PDF-ie (Pie Chart).

9. **Eksport do PDF**  
   - Zamień skoroszyt na PDF:  
     - Użyj opcji **Drukuj**  
     - Dopasuj dane tak, aby wszystkie znalazły się na jednej stronie PDF-a.