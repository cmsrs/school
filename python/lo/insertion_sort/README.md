# Sortowania przez wstawianie (Insertion Sort):

## Jak to działa:

1. Weź pierwszą wartość z nieposortowanej części tablicy.

2. Przenieś tę wartość w odpowiednie miejsce w posortowanej części tablicy.

3. Przejdź ponownie przez nieposortowaną część tablicy tyle razy, ile jest w niej wartości.

## Ręczne przejście przez tablicę:

- **Krok 1**: Zaczynamy od nieposortowanej tablicy.

    [8, 12, 9, 11, 3]

- **Krok 2**: Możemy uznać pierwszą wartość za początkowo posortowaną część tablicy. Jeśli to tylko jedna wartość, to musi być posortowana, prawda?

    [```8```, 12, 9, 11, 3]

- **Krok 3**: Kolejna wartość, 12, powinna zostać umieszczona w odpowiednim miejscu w posortowanej części tablicy. Ale 12 jest większe niż 8, więc już znajduje się na właściwej pozycji.

    [8, ```12```, 9, 11, 3]

- **Krok 4**: Rozważmy kolejną wartość - 9.

    [8, 12, ```9```, 11, 3]

- **Krok 5**: Wartość 9 musi zostać wstawiona w odpowiednie miejsce w posortowanej części tablicy, więc umieszczamy 9 pomiędzy 8 a 12.

    [8, ```9```, 12, 11, 3]

- **Krok 6**: Następna wartość to 11.

    [8, 9, 12, ```11```, 3]

- **Krok 7**: Wstawiamy ją pomiędzy 9 a 12 w posortowanej części tablicy.

    [8, 9, ```11```, 12, 3]

- **Krok 8**: Ostatnia wartość do wstawienia to 3.

    [8, 9, 11, 12, ```3```]

- **Krok 9**: Wstawiamy 3 przed wszystkimi pozostałymi wartościami, ponieważ jest najmniejsza.

    [```3```, 8, 9, 11, 12]

Na koniec tablica jest posortowana.

