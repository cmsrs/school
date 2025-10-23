def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        swapped = False
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                # Swap arr[j] and arr[j+1]
                #tmp = arr[j]
                #arr[j] = arr[j+1]
                #arr[j+1] = tmp                    
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break                
    return arr


# Example usage:
input = [8, 12, 9, 11, 3]
print("Input: ", input)
sorted_array = bubble_sort(input)
print("Sorted array is:", sorted_array)  # Output: Sorted array is: [3, 8, 9, 11, 12]
print("Sorted array is (input):", input)  # Output: Sorted array is: [3, 8, 9, 11, 12]

assert [3, 8, 9, 11, 12] == sorted_array
assert [3, 8, 9, 11, 12] == input 
