# Zadanie 1: Strona internetowa o sobie

Twoim celem jest stworzenie estetycznej i prostej strony internetowej, na której zaprezentujesz siebie oraz oferowane usługi. 
Możesz użyć fikcyjnych danych oraz tekstu zastępczego "Lorem Ipsum". Jeśli używasz obrazków z innych stron, dodaj pod obrazkiem informację o źródle oraz podaj licencję.

### Wymagania HTML

Strona powinna zawierać odpowiednie elementy HTML, które są niezbędne do poprawnego wyświetlania i indeksowania przez wyszukiwarki internetowe (SEO).

- W tagu ```<head>``` należy dodać: 
  - Tytuł strony. 
  - Kodowanie UTF-8. 
  - Autora 
  - Słowa kluczowe
  - Opis strony (ale zaleca się, aby długość opisu wynosiła do 160 znaków). 
- W tagu ```<body>``` należy dodać:
  - Tytuł strony (nagłówek h1), np. "John Doe - usługi informatyczne". Ważne jest, aby w tym znaczniku określić najważniejszą informację na temat zawartości strony.
  - Krótka biografia - podstawowe informacje o sobie: imię, zainteresowania, hobby, plany zawodowe oraz krótki opis usług.
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

- Utwórz katalog o nazwie ```imie_nazwisko```, zastępując znaki diakrytyczne ich odpowiednikami (np. „robert_szczepanski”) i używając wyłącznie małych liter. W katalogu umieść plik ```imie-nazwisko.html```, również zapisując go małymi literami i zamieniając znaki diakrytyczne (np. „robert-szczepanski.html”). W tym pliku dodaj znaczniki HTML, a style CSS umieść w sekcji <style>. Przykład można znaleźć w pliku: [john-doe.html](https://github.com/cmsrs/school/blob/main/html_and_css/john_doe/john-doe.html).
- W tym katalogu utwórz folder imgs, w którym umieścisz zdjęcia potrzebne na stronę.
- Zapisz plik na pendrive lub przechowaj w chmurze (np. Google Drive), aby móc go wykorzystać w kolejnym zadaniu.

Dobrze zaplanowane adresy URL mają kluczowe znaczenie dla wyszukiwarek internetowych i wpływają na pozycjonowanie strony.

# Zdanie 2: Sztuka publikowania w sieci

Publikowanie treści w internecie wymaga nie tylko dbałości o estetykę i funkcjonalność strony, ale także przestrzegania zasad prawnych i stosowania skutecznych metod angażowania użytkowników. Wybierz jedno z poniższych zadań do wykonania. Możesz skorzystać z fikcyjnych danych oraz tekstu zastępczego, takiego jak "Lorem Ipsum".

- Umieść odwołanie do polityki prywatności w widocznym miejscu na stronie. Możesz wyróżnić je np. poprzez umieszczenie linku na czerwonym tle, kierującego do pliku: ```imie_nazwisko/polityka-prywatnosci.html``` oraz utwórz stronę zawierającą regulamin – zapisz ją jako plik: ```imie_nazwisko/regulamin.html```. Następnie dodaj link do tej strony na stronie głównej, aby użytkownicy mogli łatwo do niej dotrzeć.

- Stwórz wersję strony w innym języku, np. angielskim. Dodaj przełącznik językowy na stronie głównej, umożliwiający użytkownikom zmianę wersji językowej. Link do strony w innym języku powinien mieć format:
```imie_nazwisko/imie-nazwisko-lang.html```, np.: ```john-doe.html/john-doe-en.html```.

- Dodaj menu na stronie oraz utwórz podstrony – każdą umieść w osobnym pliku. Przykładowe nazwy plików:
  - ```index.html``` – strona główna
  - ```o-mnie.html``` – sekcja "O mnie"
  - ```portfolio.html``` – przykłady realizacji
  - ```kontakt.html``` – mail oraz telefon kontaktowy
  - ```uslugi.html``` – oferta usług

- Utwórz prostą stronę internetową, która skutecznie zachęci użytkowników do skorzystania z Twoich usług. Wykorzystaj tzw. lead, czyli chwytliwe i angażujące wezwanie do działania, które ma na celu przyciągnięcie uwagi potencjalnych klientów i skłonienie ich do podjęcia konkretnej akcji – np. zapisania się na newsletter, skontaktowania się z Tobą lub skorzystania z oferty. Przykładowy lead znajdziesz na stronie: [lead.html](https://github.com/cmsrs/school/blob/main/html_and_css/lead/lead.html). Pamiętaj, że skuteczny lead powinien być krótki, treściwy i dobrze dopasowany do grupy docelowej. Może zawierać elementy perswazji, takie jak korzyści wynikające z oferty, ograniczona dostępność usługi („Tylko dziś!"), czy bezpośrednie wezwanie do działania („Zarezerwuj teraz!”). Utwórz lead z trafnym obrazkiem, który będzie nawiązywał do Twojej działalności i przyciągał uwagę użytkowników. Grafika powinna wspierać przekaz, wzbudzać zainteresowanie i zachęcać do skorzystania z oferty.

- Stwórz krótki film związany z Twoją działalnością lub pasją i opublikuj go w internecie, np. na YouTube. Opcjonalnie możesz umieścić link do filmu na swojej stronie. Pamiętaj, że publikowanie treści w sieci to nie tylko forma promocji, ale także sztuka przyciągania uwagi. Aby Twój film był bardziej angażujący: zadbaj o jakość nagrania, stwórz atrakcyjną miniaturę, dodaj ciekawy opis i tytuł.

### dodatkowe zadania

- Zabezpiecz adres e-mail przed spamem za pomocą JavaScript. Możesz zastosować prostą technikę ukrycia adresu e-mail w kodzie, np.:

```
document.addEventListener("DOMContentLoaded", function () {
    let user = "kontakt";
    let domain = "example.com";
    let emailElement = document.getElementById("email");
    emailElement.innerHTML = `<a href="mailto:${user}@${domain}">${user}@${domain}</a>`;
});
```

Dzięki temu boty skanujące stronę nie odczytają bezpośrednio adresu e-mail z kodu HTML.

- Napisz prosty skrypt w JavaScript, który doda do Twojej strony efekt wizualny, np. spadające płatki śniegu. Płatki powinny delikatnie opadać z góry strony, tworząc efekt zimowego klimatu.

Możesz użyć CSS do stylizacji płatków oraz JavaScript do animacji ich ruchu. Wykorzystaj funkcję setInterval() lub requestAnimationFrame(), aby uzyskać płynny efekt.


# Zadanie 3: Edycja obrazków w programie graficznym

Aby Twoja strona wyglądała profesjonalnie i wczytywała się szybciej, warto odpowiednio przygotować grafiki - np. zdjęcie profilowe i zdjęcia z wakacji i opcjonalnie logo - korzystając z programu graficznego (np. GIMP).

### Wymagania dotyczące obrazków:

- Dostosowanie rozmiaru - dopasuj wymiary obrazków do strony (Gimp: Obraz -> Skaluj obraz).
- Kadrowanie i obróbka - jeśli to konieczne, popraw wygląd zdjęć (Gimp: Narzędzie kadrowania, po zaznaczeniu kliknij dwukrotnie w obszar kadrowania).

Optymalizacja jakości - zachowaj czytelność, jednocześnie zmniejszając rozmiar plików.


# Zadanie 4: Wstawianie obrazków na stronę

Po przygotowaniu grafik umieść je na stronie, dbając o poprawne użycie znacznika ```<img>```. Pamiętaj o ustawieniu odpowiednich atrybutów, takich jak:

- src - ścieżka do pliku graficznego,
- alt - opis alternatywny dla osób korzystających z czytników ekranu,
- width i height - określenie wymiarów obrazka (opcjonalnie).

Dzięki temu Twoja strona będzie szybka w działaniu.