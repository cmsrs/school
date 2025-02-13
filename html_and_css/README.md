# Zadanie 1: Strona internetowa o sobie

Twoim celem jest stworzenie estetycznej i prostej strony internetowej, na której zaprezentujesz siebie oraz oferowane usługi. 
Możesz użyć fikcyjnych danych oraz tekstu zastępczego "Lorem Ipsum".

### Wymagania HTML

Strona powinna zawierać odpowiednie elementy HTML, które są niezbędne do poprawnego wyświetlania i indeksowania przez wyszukiwarki internetowe (SEO).

- W tagu ```<head>``` należy dodać: 
  - Tytuł strony. 
  - Kodowanie UTF-8. 
  - Autora 
  - Opis strony. 
- W tagu ```<body>``` należy dodać:
  - Tytuł strony (nagłówek h1), np. "O mnie – [Twoje Imię]".
  - Krótka biografia – podstawowe informacje o sobie: imię, zainteresowania, hobby, plany zawodowe oraz krótki opis usług.
  - Sekcja ```Moje hobby``` (nagłówek h2) - lista przedstawiająca Twoje zainteresowania.
  - Sekcja ```Usługi``` (nagłówek h2) - przedstawienie oferowanych usług w formie tabeli (lub, opcjonalnie, w układzie flexbox jako zadanie dodatkowe).
  - Sekcja ```Kontaktowa``` (nagłówek h2), np. adres e-mail, link do profilu na LinkedIn.
  - Obrazek - Twoje zdjęcie lub avatar.
  - Umieść minimum 4 zdjęcia z wakacji - dwa obok siebie na dużym ekranie, a na mniejszych ekranach jedno pod drugim. Preferowane jest, abyś użył swoich zdjęć. Jeśli ich nie masz, możesz skorzystać z moich, które znajdziesz w katalogu ```./imgs/holiday/```.
  - Dodaj logo (opcjonalnie).

### Wymagania CSS - Stylizacja strony

- Zadbaj o estetyczny wygląd strony, wykorzystując kolory, czcionki, marginesy i paddingi.
- Użyj podstawowych właściwości CSS, m.in.:
  - Stylizacja tła, tekstu i nagłówków.
  - Wyśrodkowanie elementów.
  - Formatowanie list, tabel, div-ów i paragrafów.

### Responsywność strony

- Strona powinna dobrze wyglądać zarówno na komputerach, jak i urządzeniach mobilnych.
- Użyj ```media queries```, aby dostosować wygląd do różnych rozdzielczości.
- Sprawdź responsywność, zmieniając szerokość okna przeglądarki (sprawdz dla minimalnej szerokości strony: 320 px).

### Zapis pliku

- Nazwij plik w formacie ```imie-nazwisko.html``` (w pliku umieść znaczniki HTML, a style CSS umieść w sekcji ```<style>```). Zobacz przykład w pliku: [john-doe.html](https://github.com/cmsrs/school/blob/main/html_and_css/john-doe.html). 
- Zapisz plik na pendrive lub przechowaj w chmurze (np. Google Drive), aby móc wykorzystać go w kolejnym zadaniu.

# Zadanie 2: Edycja obrazków w programie graficznym

Aby Twoja strona wyglądała profesjonalnie i wczytywała się szybciej, warto odpowiednio przygotować grafiki - np. zdjęcie profilowe i zdjęcia z wakacji i opcjonalnie logo - korzystając z programu graficznego (np. GIMP).

### Wymagania dotyczące obrazków:

- Dostosowanie rozmiaru - dopasuj wymiary obrazków do strony (Gimp: Obraz -> Skaluj obraz).
- Kadrowanie i obróbka - jeśli to konieczne, popraw wygląd zdjęć (Gimp: Narzędzie kadrowania, po zaznaczeniu kliknij dwukrotnie w obszar kadrowania).

Optymalizacja jakości - zachowaj czytelność, jednocześnie zmniejszając rozmiar plików.


# Zadanie 3: Wstawianie obrazków na stronę

Po przygotowaniu grafik umieść je na stronie, dbając o poprawne użycie znacznika ```<img>```. Pamiętaj o ustawieniu odpowiednich atrybutów, takich jak:

- src - ścieżka do pliku graficznego,
- alt - opis alternatywny dla osób korzystających z czytników ekranu,
- width i height - określenie wymiarów obrazka (opcjonalnie).

Dzięki temu Twoja strona będzie szybka w działaniu.