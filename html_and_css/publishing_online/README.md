# Zdanie: Sztuka publikowania w sieci

Twoim zadaniem jest stworzenie estetycznej i intuicyjnej strony internetowej, która przedstawi Ciebie, Twoje usługi lub wybrany produkt, jako przykład: [john doe](https://github.com/cmsrs/school/blob/main/html_and_css/README.md). Tworząc treść, zastosuj zasadę 5W (Who?, What?, Where?, When?, Why?), aby jasno określić, kim jesteś, co oferujesz i dlaczego warto skorzystać z Twojej oferty. Wykorzystaj również elementy graficzne i identyfikację wizualną, aby lepiej zobrazować działalność swojej firmy. Możesz posłużyć się fikcyjnymi danymi oraz tekstem zastępczym "Lorem Ipsum". Jeśli używasz obrazów z innych źródeł, pamiętaj o dodaniu informacji o ich pochodzeniu oraz licencji.

Publikowanie treści w internecie wymaga nie tylko dbałości o estetykę i funkcjonalność strony, ale także przestrzegania zasad prawnych i stosowania skutecznych metod angażowania użytkowników. Wybierz jedno z poniższych zadań do wykonania. Możesz skorzystać z fikcyjnych danych oraz tekstu zastępczego, takiego jak "Lorem Ipsum".

- Umieść odwołanie do polityki prywatności w widocznym miejscu na stronie. Możesz wyróżnić je np. poprzez umieszczenie linku na czerwonym tle, kierującego do pliku: ```imie_nazwisko/polityka-prywatnosci.html``` oraz utwórz stronę zawierającą regulamin – zapisz ją jako plik: ```imie_nazwisko/regulamin.html```. Następnie dodaj link do tej strony na stronie głównej, aby użytkownicy mogli łatwo do niej dotrzeć.

- Stwórz wersję strony w innym języku, np. angielskim, aby dotrzeć do szerszej grupy odbiorców. Skuteczna komunikacja wymaga nie tylko tłumaczenia treści, ale także dostosowania jej do kultury i oczekiwań użytkowników. Dodaj przełącznik językowy na stronie głównej, umożliwiający użytkownikom zmianę wersji językowej. Link do strony w innym języku powinien mieć format: 
```imie_nazwisko/imie-nazwisko-lang.html```, np.: ```john-doe.html/john-doe-en.html```.

przykład:

Na stronie john-doe.html dodajemy:

```
<div class="language-switcher">
  <a href="john-doe.html" class="lang-link pl active">Polski</a> | 
  <a href="john-doe-en.html" class="lang-link en">English</a>
</div>
```

Na stronie john-doe-en.html:

```
<div class="language-switcher">
  <a href="john-doe.html" class="lang-link pl">Polski</a> | 
  <a href="john-doe-en.html" class="lang-link en active">English</a>
</div>
```

Na obu stronach dodajemy następujace style:

```
.language-switcher {
    text-align: right;
    margin: 10px;
    font-size: 14px;
}

.lang-link {
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 5px;
}

.lang-link.pl {
    background-color: #f0f0f0;
    color: #333;
}

.lang-link.en {
    background-color: #f0f0f0;
    color: #333;
}

/* Podkreślenie aktywnego języka */
.lang-link.active {
    font-weight: bold;
    background-color: #007bff;
    color: white;
}
```


- Utwórz prostą stronę internetową, która skutecznie zachęci użytkowników do skorzystania z Twoich usług. Wykorzystaj tzw. lead, czyli chwytliwe i angażujące wezwanie do działania, które ma na celu przyciągnięcie uwagi potencjalnych klientów i skłonienie ich do podjęcia konkretnej akcji – np. zapisania się na newsletter, skontaktowania się z Tobą lub skorzystania z oferty. Przykładowy lead znajdziesz na stronie: [lead.html](https://github.com/cmsrs/school/blob/main/html_and_css/lead/lead.html). Pamiętaj, że skuteczny lead powinien być krótki, treściwy i dobrze dopasowany do grupy docelowej. Może zawierać elementy perswazji, takie jak korzyści wynikające z oferty, ograniczona dostępność usługi („Tylko dziś!"), czy bezpośrednie wezwanie do działania („Zarezerwuj teraz!”). Utwórz lead z trafnym obrazkiem, który będzie nawiązywał do Twojej działalności i przyciągał uwagę użytkowników. Grafika powinna wspierać przekaz, wzbudzać zainteresowanie i zachęcać do skorzystania z oferty. Lead powinien zawierać link do strony docelowej (utworzonej w zadaniu 1), na którą użytkownik zostanie przekierowany.

- Stwórz krótki film związany z Twoją działalnością lub pasją i opublikuj go w internecie, np. na YouTube. Opcjonalnie możesz umieścić link do filmu na swojej stronie. Pamiętaj, że publikowanie treści w sieci to nie tylko forma promocji, ale także sztuka przyciągania uwagi. Aby Twój film był bardziej angażujący: zadbaj o jakość nagrania, stwórz atrakcyjną miniaturę, dodaj ciekawy opis i tytuł.

## Zadanie do wykonania

Dodaj w stopce (footer) strony swoje imię i nazwisko jako autora pracy.

Następnie wybierz jeden z dostępnych nagłówków oraz zintegruj go ze swoją stroną. Numer nagłówka przydzielony zostanie na podstawie Twojego numeru w dzienniku Librus. Pamiętaj, że nagłówek powinien harmonijnie łączyć się z całą koncepcją wizualną i treścią Twojej strony – nie wystarczy go tylko wkleić, ale trzeba go właściwie dostosować do potrzeb projektu.

### 📥 Pobierz swój nagłówek

- Zestaw 1 → [Pobierz naglowek1.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek1.png)
- Zestaw 2 → [Pobierz naglowek2.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek2.png)
- Zestaw 3 → [Pobierz naglowek3.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek3.png)
- Zestaw 4 → [Pobierz naglowek4.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek4.png)
- Zestaw 5 → [Pobierz naglowek5.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek5.png)
- Zestaw 6 → [Pobierz naglowek6.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek6.png)
- Zestaw 7 → [Pobierz naglowek7.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek7.png)
- Zestaw 8 → [Pobierz naglowek8.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek8.png)
- Zestaw 9 → [Pobierz naglowek9.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek9.png)
- Zestaw 10 → [Pobierz naglowek10.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek10.png)
- Zestaw 11 → [Pobierz naglowek11.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek11.png)
- Zestaw 12 → [Pobierz naglowek12.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek12.png)
- Zestaw 13 → [Pobierz naglowek13.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek13.png)
- Zestaw 14 → [Pobierz naglowek14.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek14.png)
- Zestaw 15 → [Pobierz naglowek15.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek15.png)
- Zestaw 16 → [Pobierz naglowek16.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek16.png)
- Zestaw 17 → [Pobierz naglowek17.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek17.png)
- Zestaw 18 → [Pobierz naglowek18.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek18.png)
- Zestaw 19 → [Pobierz naglowek19.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek19.png)
- Zestaw 20 → [Pobierz naglowek20.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek20.png)
- Zestaw 21 → [Pobierz naglowek21.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek21.png)
- Zestaw 22 → [Pobierz naglowek22.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek22.png)
- Zestaw 23 → [Pobierz naglowek23.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek23.png)
- Zestaw 24 → [Pobierz naglowek24.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek24.png)
- Zestaw 25 → [Pobierz naglowek25.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek25.png)
- Zestaw 26 → [Pobierz naglowek26.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek26.png)
- Zestaw 27 → [Pobierz naglowek27.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek27.png)
- Zestaw 28 → [Pobierz naglowek28.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek28.png)
- Zestaw 29 → [Pobierz naglowek29.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek29.png)
- Zestaw 30 → [Pobierz naglowek30.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek30.png)
- Zestaw 31 → [Pobierz naglowek31.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek31.png)
- Zestaw 32 → [Pobierz naglowek32.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek32.png)
- Zestaw 33 → [Pobierz naglowek33.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek33.png)
- Zestaw 34 → [Pobierz naglowek34.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek34.png)
- Zestaw 35 → [Pobierz naglowek35.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek35.png)
- Zestaw 36 → [Pobierz naglowek36.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek36.png)
- Zestaw 37 → [Pobierz naglowek37.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek37.png)
- Zestaw 38 → [Pobierz naglowek38.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek38.png)
- Zestaw 39 → [Pobierz naglowek39.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek39.png)
- Zestaw 40 → [Pobierz naglowek40.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek40.png)
- Zestaw 41 → [Pobierz naglowek41.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek41.png)
- Zestaw 42 → [Pobierz naglowek42.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek42.png)
- Zestaw 43 → [Pobierz naglowek43.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek43.png)
- Zestaw 44 → [Pobierz naglowek44.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek44.png)
- Zestaw 45 → [Pobierz naglowek45.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek45.png)
- Zestaw 46 → [Pobierz naglowek46.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek46.png)
- Zestaw 47 → [Pobierz naglowek47.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek47.png)
- Zestaw 48 → [Pobierz naglowek48.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek48.png)
- Zestaw 49 → [Pobierz naglowek49.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek49.png)
- Zestaw 50 → [Pobierz naglowek50.png](https://raw.githubusercontent.com/cmsrs/school/main/basic/data/obrazy_rozpakowane/naglowek50.png)





### dodatkowe zadania

- Zabezpiecz adres e-mail przed spamem za pomocą JavaScript. Dzięki temu boty skanujące stronę nie odczytają bezpośrednio adresu e-mail z kodu HTML. Możesz zastosować prostą technikę ukrycia adresu e-mail w kodzie, np.:

```
document.addEventListener("DOMContentLoaded", function () {
    let user = "kontakt";
    let domain = "example.com";
    let emailElement = document.getElementById("email");
    emailElement.innerHTML = `<a href="mailto:${user}@${domain}">${user}@${domain}</a>`;
});
```

- Napisz prosty skrypt w JavaScript, który doda do Twojej strony efekt wizualny, np. spadające płatki śniegu. Płatki powinny delikatnie opadać z góry strony, tworząc efekt zimowego klimatu. Możesz użyć CSS do stylizacji płatków oraz JavaScript do animacji ich ruchu. Wykorzystaj funkcję setInterval() lub requestAnimationFrame(), aby uzyskać płynny efekt.
