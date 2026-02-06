# Zadanie 5 - Gra Labirynt

## Opis zadania

Twoim zadaniem jest stworzenie gry, w której duszek (np. czerwony kwadrat) porusza się po labiryncie. Celem gracza jest dotknięcie żółtego przedmiotu, co spowoduje wypisanie komunikatu "Brawo!" przez 2 sekundy.

W przypadku dotknięcia zielonej ściany gra resetuje się - duszek wraca do środkowej części labiryntu.

### Przykład ustawienia początkowego

![labirynt](labirynt.png)

## Implementacja

### Obsługa kolizji ze ścianą

Kod odpowiadający za dotknięcie zielonej ściany oraz zresetowanie gry powinien być umieszczony w bloku `zawsze`.

![labirynt_kod](labirynt_kod.png)

### Konfiguracja kolorów

⚠️ **Pamiętaj o poprawnym ustawieniu:**
- Koloru tła (zielony)
- Koloru żółtego dla przedmiotu do zbierania

Poniżej wskazane jest narzędzie (pipetka), które pozwala pobrać dokładny kolor tła:

![pipetka](pipetka.png)

## Wskazówki

- Ustaw duszka w środkowej części labiryntu na początek
- Wykryj kolizję z zieloną ścianą i zresetuj pozycję duszka
- Dodaj timer do wyświetlania komunikatu "Brawo!" przez 2 sekundy