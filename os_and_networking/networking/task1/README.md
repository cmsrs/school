# Zadanie praktyczne: Podstawy pracy z SSH i Apache na FreeBSD

## 🎯 Cel  
Nauczysz się łączyć przez SSH do serwera FreeBSD, przejdziesz do katalogu serwera WWW Apache i stworzysz swoją prostą stronę HTML.

---

## 🔐 Dane dostępowe do serwera

- **Adres IP serwera:** `192.168.88.202`  
  *(adres może się zmieniać w zależności od DHCP)*  
- **Nazwa użytkownika SSH:** `school`  
- **Hasło:** `school123`

---

## 🧭 Instrukcja krok po kroku

### 1. Połącz się z serwerem przez SSH
Uruchom terminal (lub program PuTTY, jeśli używasz Windows) i wpisz:

```bash
ssh school@192.168.88.202
```

Jeśli pojawi się pytanie o zaakceptowanie klucza, wpisz `yes` i naciśnij Enter.  
Następnie wpisz hasło:

```
school123
```

### 2. Przejdź do katalogu serwera Apache

```bash
cd /usr/local/www/apache24/data
```

Sprawdź, czy jesteś w odpowiednim katalogu:

```bash
pwd
```

Powinieneś zobaczyć:

```
/usr/local/www/apache24/data
```

### 3. Utwórz swój plik HTML

Zamień `klasa-imie-nazwisko` na swoje dane, np. `3lo-jan-kowalski`:

```bash
echo "Hello, world! 3lo-jan-kowalski" > 3lo-jan-kowalski.html
```

### 4. Sprawdź swój plik w przeglądarce

Otwórz przeglądarkę i wpisz:

```
http://192.168.88.202/3lo-jan-kowalski.html
```

Powinieneś zobaczyć:

```
Hello, world! 3lo-jan-kowalski
```

---

## ✅ Checklist do odhaczenia

- [ ] Połączyłem się z serwerem przez SSH  
- [ ] Przeszedłem do katalogu Apache  
- [ ] Utworzyłem plik HTML z poprawną nazwą i treścią  
- [ ] Sprawdziłem stronę w przeglądarce i działa

---

## ℹ️ Dodatkowe wskazówki

- Jeśli adres IP się zmieni, zapytaj nauczyciela o aktualny adres  
- Jeśli coś nie działa, sprawdź dokładnie komendy lub poproś o pomoc  
- Nie zmieniaj innych plików ani ustawień na serwerze

---

🧠 *Powodzenia!*
