# Zadanie 2 z html-a — Dodaj podstronę do swojej strony

Cel:
Twoim zadaniem jest rozbudować stronę stworzoną w Zadaniu 1 o dodatkową podstronę. Może to być np.:
- regulamin.html (krótki regulamin lub zasady korzystania ze strony), lub
- podstrona opisująca dodatkowe zagadnienie (np. "O nas", "Oferta", "Projekt"), linkowana z menu.

Zadanie podstawowe (dla wszystkich):
1. W folderze swojego projektu (np. `imie_nazwisko/`) dodaj nowy plik: `regulamin.html` lub inna podstrona np. `o-nas.html`.
2. Dodaj w głównym menu na stronie link do tej podstrony, tak aby użytkownik mógł się do niej łatwo dostać.
3. Podstrona powinna mieć nagłówek, kilka akapitów z treścią (możesz użyć fikcyjnych danych i "Lorem Ipsum") oraz link powrotny do strony głównej.

Przykład dodania linku w menu (w pliku `index.html`):
```html
<nav>
  <ul>
    <li><a href="index.html">Strona główna</a></li>
    <li><a href="regulamin.html">Regulamin</a></li>
    <li><a href="kontakt.html">Kontakt</a></li>
  </ul>
</nav>
```

Przykładowy prosty szablon `regulamin.html`:
```html
<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8">
  <title>Regulamin — Jan Kowalski</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Regulamin strony</h1>
    <nav>
      <a href="index.html">Strona główna</a>
    </nav>
  </header>

  <main>
    <section>
      <h2>1. Postanowienia ogólne</h2>
      <p>Ta strona jest projektem szkolnym. Treści są przykładowe i mogą zawierać fikcyjne dane.</p>
    </section>

    <section>
      <h2>2. Zasady korzystania</h2>
      <p>Użytkownicy powinni korzystać z zasobów strony zgodnie z prawem i dobrymi obyczajami.</p>
    </section>

    <p><a href="index.html">← Powrót na stronę główną</a></p>
  </main>

  <footer>
    <p>Autor: Jan Kowalski</p>
  </footer>
</body>
</html>
```

**Zadanie rozszerzone (dla osób na ocenę 6):**
- Stwórz wersję strony w drugim języku (np. angielskim). Dodaj prosty przełącznik języka w prawym górnym rogu, który prowadzi do odpowiedniej wersji plików (`imie-nazwisko.html` i `imie-nazwisko-en.html`).

Przykład przełącznika języka (w dwóch plikach):
```html
<div class="language-switcher">
  <a href="jan-kowalski.html" class="lang-link pl active">Polski</a> |
  <a href="jan-kowalski-en.html" class="lang-link en">English</a>
</div>
```

Przykładowe style dla przełącznika:
```css
.language-switcher { text-align: right; margin: 10px; font-size: 14px; }
.lang-link { text-decoration: none; padding: 5px 8px; border-radius: 4px; background: #efefef; color: #222; }
.lang-link.active { background: #007bff; color: #fff; font-weight: bold; }
```

Wymagania formalne — co oddajesz:
- Folder z Twoim imieniem i nazwiskiem (np. `jan_kowalski/`) lub pliki w katalogu projektu.
- Nowy plik podstrony: `regulamin.html` (lub `o-nas.html`, `oferta.html`).
- Zmiany w menu: link do nowej podstrony widoczny na stronie głównej.
- (Jeśli wersja rozszerzona) Plik w drugim języku: `twoje-imie-twoje-nazwisko-en.html` i przełącznik języka.

Kryteria oceniania (propozycja):
- 0–2 pkt — brak podstrony lub podstrona nie otwiera się / błędy podstawowe.
- 3–4 pkt — podstrona istnieje, jest poprawnie podlinkowana, treść logiczna i czytelna.
- 5 pkt — estetyczne formatowanie, poprawne linki, responsywność (podstawowa), dodatkowe elementy (np. zdjęcie, lista).
- +1 pkt — wersja w drugim języku
- +1 pkt — poprawne oznaczenie źródeł użytych obrazów / licencje.

Wskazówki:
- Użyj czytelnych nagłówków (h1, h2) i paragrafów (p).
- Jeśli używasz obrazów z internetu — podaj źródło i licencję (np. "Źródło: Pixabay, licencja...").
- Testuj stronę lokalnie, otwierając plik `index.html` w przeglądarce.
- Nazwy plików i folderów — bez spacji, używaj myślników lub podkreślników, np. `jan-kowalski`.


Przykład krótkiej treści regulaminu, którą możesz skopiować i edytować:
> Ten regulamin opisuje zasady korzystania ze strony szkolnego projektu. Materiały na stronie mają charakter edukacyjny. Zabronione jest kopiowanie treści bez zgody autora. Administrator zastrzega sobie prawo do zmian w regulaminie.