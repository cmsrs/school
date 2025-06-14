# 🧪 Zadanie praktyczne 2: Sprawdzanie logów Apache na FreeBSD

## 🎯 Cel  
Celem tego zadania jest nauczenie się monitorowania ruchu na stronie WWW działającej na serwerze FreeBSD z użyciem logów Apache. Dowiesz się, jak połączyć się z serwerem przez SSH i sprawdzić logi odwiedzin strony.

---

## 🔐 Dane dostępowe do serwera

- **Adres IP serwera:** `192.168.88.202` *(adres może się zmieniać, zapytaj nauczyciela)*
- **Nazwa użytkownika SSH:** `school`
- **Hasło:** `school123`

---

## 🧭 Instrukcja krok po kroku

### 1. Połącz się z serwerem przez SSH

Uruchom terminal (Linux/macOS) lub program PuTTY (Windows), następnie wpisz:

```bash
ssh school@192.168.88.202
```

Zaakceptuj klucz (yes), a potem wpisz hasło:
school123

2. Odwiedź stronę w przeglądarce
Na swoim komputerze otwórz przeglądarkę i przejdź do:

```
http://192.168.88.202/
```

Odśwież stronę kilka razy lub poproś kolegę/koleżankę, żeby też ją odwiedził(a).

3. Sprawdź logi serwera Apache w czasie rzeczywistym
W terminalu na serwerze wpisz polecenie:

```
tail -f /var/log/httpd-access.log
```

Powinieneś zobaczyć wpisy podobne do:

```
192.168.88.101 - - [13/Jun/2025:12:34:56 +0200] "GET / HTTP/1.1" 200 2456
```

Każde odświeżenie strony lub wejście innego użytkownika powoduje nowy wpis w logu.

4. Zatrzymaj podgląd logów
Aby zakończyć działanie tail, naciśnij:

```
Ctrl + C
```

## ✅ Checklist do odhaczenia

- [ ] Połączyłem się z serwerem przez SSH  
- [ ] Odwiedziłem stronę http://192.168.88.202/
- [ ] Uruchomiłem podgląd logów Apache
- [ ] Zobaczyłem wpisy odpowiadające odwiedzinom
- [ ] Rozumiem, co oznaczają poszczególne elementy wpisów w logach

 

## ℹ️ Dodatkowe wskazówki

Jeśli nie widzisz nowych logów, odśwież stronę lub odwiedź ją z innego urządzenia.

tail -f pozwala obserwować logi na żywo — przydatne przy testowaniu i diagnostyce.

Jeśli adres IP serwera się zmienił, zapytaj nauczyciela o nowy.

🧠 Powodzenia!
Dzięki temu zadaniu nauczyłeś się podstaw analizy logów serwera WWW. To kluczowa umiejętność administratora systemów!