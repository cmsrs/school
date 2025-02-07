"""
Szyfr Cezara (inaczej przesunięcie Cezara) to prosty szyfr przesuwający każdą literę w alfabecie o określoną liczbę miejsc.
Na przykład dla przesunięcia o 3 miejsca:

    A → D
    B → E
    C → F
    itd.

W programie zakladamy ze szyfrujemy tylko duze litery alfabetu angielskiego.    

kody ASCII:

65  ->	A
66  -> 	B
67  -> 	C
68  -> 	D
...
90  -> 	Z

od 90 do 65 jest 26 znaków


dla klucza 3:

A -> D
B -> E
...
X -> A
Y -> B
Z -> C


"""

#plaintext = "ALA MA KOTA A KAMILA PSA XYZ"
key = 3
plaintext = "ABXYZ"
#encrypt = "DEABC" # klucz 3


#print( ord("A") ) # 65
#print( chr(65) ) # A
#print( ord("B") ) # 66
#print( ord("Z") ) # 90


# Encrypt
def encrypt_caesar_cipher(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        code = ord(plaintext[i]) + key
        if code > 90: #ord("Z") = 90
            code -= 26

        ciphertext += chr(code)
    return ciphertext


cipherText = encrypt_caesar_cipher(plaintext, key)
assert "DEABC" == cipherText


# Decrypt
def decrypt_caesar_cipher(cipherText, key):
    plaintext = ""
    for i in range(len(cipherText)):
        code = ord(cipherText[i]) - key
        if code < 65: #ord("A") = 65
            code += 26

        plaintext += chr(code)
    return plaintext



plaintextDecrypt = decrypt_caesar_cipher(cipherText, key)

assert "ABXYZ" == plaintextDecrypt
assert plaintext == plaintextDecrypt
