"""
Algorytmy na tekstach (2)

Funkcja weryfikuje, czy podany ciąg znaków spełnia format polskiego kodu pocztowego (NN-NNN), gdzie N oznacza cyfrę. 
Sprawdza długość ciągu, obecność myślnika na trzeciej pozycji oraz to, czy pozostałe znaki są cyframi.

"""
def validate_polish_postal_code(postal_code):
    # Sprawdzenie długości
    if len(postal_code) != 6:
        return False
    
    # Sprawdzenie formatu XX-XXX
    if not (postal_code[0].isdigit() and postal_code[1].isdigit()):
        return False
    if postal_code[2] != "-":
        return False
    if not (postal_code[3].isdigit() and postal_code[4].isdigit() and postal_code[5].isdigit()):
        return False

    return True


assert True == validate_polish_postal_code("01-234")
assert False == validate_polish_postal_code("123-45")
assert False == validate_polish_postal_code("AB-123")
assert True == validate_polish_postal_code("12-345")
