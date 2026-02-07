# Zadanie 5 - Gra Labirynt

## Opis zadania

Twoim zadaniem jest stworzenie gry, w której duszek (np. czerwony kwadrat) porusza się po labiryncie.
Gracz wygrywa, gdy dotknie żółtego przedmiotu. Wtedy na ekranie pojawia się napis „Brawo!” przez 2 sekundy.

Labirynt powinien mieć kształt taki jak na rysunku poniżej – to będzie Twoje tło.

Postaraj się, aby przejście labiryntu nie było ani za łatwe, ani za trudne.
Możesz to ustawić, zmieniając wielkość duszka oraz liczbę kroków, które wykonuje.


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
- **Grę możesz ulepszyć, regulując wielkość duszka (kwadratu) oraz zwiększając lub zmniejszając liczbę kroków.**

## Tutorial wideo (YouTube)
Jeśli potrzebujesz pomocy, obejrzyj tutorial wideo — pokazuje krok po kroku tworzenie gry.


▶️ **[Gra w labirynt w Scratch krok po kroku - kolizje, reset, wygrana](https://youtu.be/2SUKjwrRiIc)**
