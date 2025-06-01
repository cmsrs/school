# Przesyłanie i udostępnianie strony HTML na serwerze FreeBSD

## Opis projektu

Ten projekt pokazuje, jak przesłać spakowaną stronę HTML w pliku ZIP na serwer FreeBSD za pomocą `pscp`, rozpakować ją na serwerze i udostępnić przez serwer WWW Apache.


---

## 🚀 Jak używać

1. Przygotuj plik ZIP ze swoją stroną HTML (np. `3lo-jan-kowalski.zip` z np. `index.html` w środku).  
2. Prześlij plik na serwer:

    ```bash
    pscp 3lo-jan-kowalski.zip school@192.168.88.202:/home/school/
    ```

3. Zaloguj się na serwer przez SSH:

    ```bash
    ssh school@192.168.88.202
    ```

4. Przenieś plik ZIP do katalogu Apache i rozpakuj go:

    ```bash
    mv ~/3lo-jan-kowalski.zip /usr/local/www/apache24/data/lab
    cd /usr/local/www/apache24/data/lab
    unzip 3lo-jan-kowalski.zip
    ```

5. Otwórz swoją stronę w przeglądarce:


http://192.168.88.202/lab/3lo-jan-kowalski/index.html


## 🔐 Dane dostępowe do serwera

- **Adres IP serwera:** `192.168.88.202`  
  *(adres może się zmieniać w zależności od DHCP)*  
- **Nazwa użytkownika SSH:** `school`  
- **Hasło:** `school123`
