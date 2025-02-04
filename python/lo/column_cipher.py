columnCipher = ""

original_plaintext = "alamakotakamilapsaicos"  # Zachowaj oryginalny tekst

plaintext = original_plaintext



#alam
#akot
#akam
#ilap
#saic
#os

key = 4


while len(plaintext) % key != 0:
    plaintext += "_"

#print(plaintext)    
#exit()

# Encrypt
for i in range(key):
    for j in range(i, len(plaintext), key):
        columnCipher += plaintext[j]

#print(columnCipher)


# Decrypt

def decrypt_column_cipher(ciphertext, key):
    rows = len(ciphertext) // key  # Obliczamy liczbę wierszy
    plaintext = ""  # Zmienna przechowująca odszyfrowany tekst
    
    for j in range(rows):  # Iterujemy po wierszach
        for i in range(key):  # Iterujemy po kolumnach
            plaintext += ciphertext[i * rows + j]
    
    #print(plaintext)
    return plaintext.rstrip("_")  # Usuwamy ewentualne dopełnienia "_"


decrypt = decrypt_column_cipher(columnCipher, key)

#print(decrypt)
assert decrypt == original_plaintext
