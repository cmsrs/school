suma = 0
dzien = 1
dzien_maks = 1
maksimum = 0

while suma < 100:
    ile = int(input("Ile gruszek nazbierałeś dnia " + str(dzien) + ": "))

    if ile > maksimum:
        maksimum = ile
        dzien_maks = dzien

    suma = suma + ile
    dzien = dzien + 1

print("Maksymalna liczba gruszek, jaką nazbierałeś to: " + str(maksimum) +
      " w dniu: " + str(dzien_maks) +
      ", a łączna liczba gruszek to: " + str(suma))
