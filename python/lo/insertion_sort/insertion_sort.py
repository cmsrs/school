def  insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        item = arr[i]
        j = i - 1
        while j >= 0 and  arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item 
    return arr


# Example usage:
input = [8, 12, 9, 11, 3]
print("Input: ", input)
sorted_array = insertion_sort(input)
print("Sorted array is:", sorted_array)  # Output: Sorted array is: [3, 8, 9, 11, 12]
print("Sorted array is (input):", input)  # Output: Sorted array is: [3, 8, 9, 11, 12]

assert [3, 8, 9, 11, 12] == sorted_array
assert [3, 8, 9, 11, 12] == input

