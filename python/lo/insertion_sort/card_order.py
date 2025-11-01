arr = [8, 9, 12, 11, 3]


def card_order(arr, i):
    item = arr[i]
    j = i - 1
    while j >= 0 and  arr[j] > item:
        arr[j + 1] = arr[j]
        j -= 1
    print( 'lista po przestawieniu elementow', arr, ', gdzie wstawiamy j =' , j, ', co wstawiamy item =', item)
    arr[j + 1] = item 


#krok 6
print('wejscie1', arr, 'przestawiamy element o indeksie 3') # Input [8, 9, 12, 11, 3]
card_order(arr, 3)
print('wynik1', arr)  # Output: [8, 9, 11, 12, 3]

#krok 8
print('wejscie2', arr, 'przestawiamy element o indeksie 4') # Input [8, 9, 11, 12, 3]
card_order(arr, 4)
print('wynik2', arr)  # Output: [3, 8, 9, 11, 12]
