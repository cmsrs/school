"""
Opis szyfru kolumnowego

Szyfr kolumnowy to klasyczna metoda szyfrowania transpozycyjnego, w której znaki tekstu są przestawiane w określonym układzie kolumnowym. Poniżej znajduje się szczegółowy opis działania tego szyfru na podstawie dostarczonego kodu.
1. Proces szyfrowania

Szyfrowanie odbywa się poprzez zapisanie tekstu w tabeli o określonej liczbie kolumn, a następnie odczytanie znaków kolumnami w odpowiedniej kolejności.
Kroki szyfrowania:

    Uzupełnienie tekstu: Jeśli długość tekstu nie jest wielokrotnością liczby kolumn, dodawane są znaki dopełniające („_”).
    Tworzenie tabeli: Tekst jest umieszczany w tabeli o liczbie kolumn równej key, wypełnianej rzędami od lewej do prawej.
    Odczytanie kolumnami: Znaki są odczytywane kolumnami od góry do dołu i zapisywane w nowej kolejności jako zaszyfrowany tekst.

Przykład dla tekstu "alamakotakamilapsaicos" i klucza 4:

Tworzymy tabelę:


alam
akot
akam
ilap
saic
os

"""

key = 4
originalPlaintext = "alamakotakamilapsaicos"  #oryginalny tekst


# Encrypt
def encrypt_column_cipher(plaintext, key):

    columnCipher = ""  # Zmienna przechowująca zaszyfrowany tekst

    while len(plaintext) % key != 0: #dopelniamy tekst "_" do wielokrotnosci key
        plaintext += "_"

    #print(plaintext)  exit()

    for i in range(key):
        for j in range(i, len(plaintext), key):
            columnCipher += plaintext[j]

    return columnCipher


encrypt = encrypt_column_cipher(originalPlaintext, key)
assert "aaaisolkklasaoaai_mtmpc_" == encrypt


# Decrypt
def decrypt_column_cipher(cipherText, key):
    rows = len(cipherText) // key  # Obliczamy liczbę wierszy
    plaintext = ""  # Zmienna przechowująca odszyfrowany tekst
    
    for j in range(rows):  # Iterujemy po wierszach
        for i in range(key):  # Iterujemy po kolumnach
            plaintext += cipherText[i * rows + j]
    
    return plaintext.rstrip("_")  # Usuwamy ewentualne dopełnienia "_"


decrypt = decrypt_column_cipher(encrypt, key)
assert decrypt == originalPlaintext
