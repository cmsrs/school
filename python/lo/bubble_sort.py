
"""
Sortowanie bąbelkowe to prosty algorytm sortowania, który działa poprzez wielokrotne przechodzenie przez listę, porównywanie sąsiadujących ze sobą elementów i zamienianie ich miejscami, jeśli są w złej kolejności. Proces ten jest powtarzany, aż lista będzie posortowana.

Poniżej znajduje się kod z dodanymi komentarzami w języku polskim:

W skrócie, algorytm sortowania bąbelkowego działa poprzez "przepychanie" większych elementów na koniec listy w każdej iteracji, stąd nazwa "bąbelkowe".

"""

def bubble_sort(arr):
    n = len(arr)  # Pobieramy długość listy
    for i in range(1, n):  # Powtarzamy n-1 razy
        for j in range(n - i):  # Iterujemy po kolejnych parach, to samo co range(0, n-i)
            if arr[j] > arr[j + 1]:  # Jeśli elementy są w złej kolejności
                # Zamiana miejscami - metoda tuple unpacking (zakomentowana)
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Zamiana miejscami - uzycie zmiennej tymczasowej (temp)
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr  # Zwracamy posortowaną listę

# Przykład użycia
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)

#print(f"Sorted numbers: {sorted_numbers}")
assert sorted_numbers == [11, 12, 22, 25, 34, 64, 90]


# Przykład użycia wbudowanej funkcji sortującej
numbers2 = [64, 34, 25, 12, 22, 11, 90]
numbers2.sort()
#print(f"Sorted numbers using built-in sort: {numbers2}")
assert numbers2 == [11, 12, 22, 25, 34, 64, 90]
assert numbers2 == sorted_numbers

