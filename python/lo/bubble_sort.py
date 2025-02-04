def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):  # Powtarzamy n-1 razy
        for j in range(n -i):  # Iterujemy po kolejnych parach, to samo co range(0, n-i)
            if arr[j] > arr[j + 1]:  # Jeśli elementy są w złej kolejności
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamiana miejscami - metoda tuple unpacking
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

# Przykład użycia
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)

print(f"Sorted numbers: {sorted_numbers}")
assert sorted_numbers == [11, 12, 22, 25, 34, 64, 90]


# Przykład użycia wbudowanej funkcji sortującej
numbers = [64, 34, 25, 12, 22, 11, 90]
numbers.sort()
print(f"Sorted numbers using built-in sort: {numbers}")
assert numbers == [11, 12, 22, 25, 34, 64, 90]
