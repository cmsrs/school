def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        minimum_index  = i
        for j in range(i+1, n):
            print(i,j)
            if arr[j] < arr[minimum_index]:
                minimum_index = j 
        #improve 
        if i != minimum_index:
            arr[i], arr[minimum_index] = arr[minimum_index], arr[i] 
    return arr


# Example usage:
input = [8, 12, 9, 11, 3]
print("Input: ", input)
sorted_array = selection_sort(input)
print("Sorted array is:", sorted_array)  # Output: Sorted array is: [3, 8, 9, 11, 12]
print("Sorted array is (input):", input)  # Output: Sorted array is: [3, 8, 9, 11, 12]

assert [3, 8, 9, 11, 12] == sorted_array
assert [3, 8, 9, 11, 12] == input
