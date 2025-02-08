"""
Szyfr Cezara (inaczej przesunięcie Cezara) to prosty szyfr przesuwający każdą literę w alfabecie o określoną liczbę miejsc.
Na przykład dla przesunięcia o 2 miejsca:

    A -> C
    B -> D
    C -> E
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


dla klucza 2:

A -> C
B -> D
C -> E
X -> Z
Y -> A
Z -> B


"""

key = 2
plaintext = "ABCXYZ"

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
assert "CDEZAB" == cipherText


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

assert "ABCXYZ" == plaintextDecrypt
assert plaintext == plaintextDecrypt
