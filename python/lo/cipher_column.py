key = 4
originalPlaintext = "alamakotakamilapsaicos"  # Zachowaj oryginalny tekst

#alam
#akot
#akam
#ilap
#saic
#os

# Encrypt
def encrypt_column_cipher(plaintext, key):

    columnCipher = ""  # Zmienna przechowująca zaszyfrowany tekst

    while len(plaintext) % key != 0:
        plaintext += "_"

    #print(plaintext)  exit()

    for i in range(key):
        for j in range(i, len(plaintext), key):
            columnCipher += plaintext[j]

    return columnCipher


# Decrypt
def decrypt_column_cipher(ciphertext, key):
    rows = len(ciphertext) // key  # Obliczamy liczbę wierszy
    plaintext = ""  # Zmienna przechowująca odszyfrowany tekst
    
    for j in range(rows):  # Iterujemy po wierszach
        for i in range(key):  # Iterujemy po kolumnach
            plaintext += ciphertext[i * rows + j]
    
    #print(plaintext)
    return plaintext.rstrip("_")  # Usuwamy ewentualne dopełnienia "_"


encrypt = encrypt_column_cipher(originalPlaintext, key)
decrypt = decrypt_column_cipher(encrypt, key)

#print(encrypt)
#print(decrypt)
assert decrypt == originalPlaintext
