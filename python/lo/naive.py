
       #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
text = 'sdcostsdfdsasfsdfdasdfdsafdsafcostreytetr'
pattern = 'cost'

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i

        # match = True
        # for j in range(m):
        #     if text[i + j] != pattern[j]:
        #         match = False
        #         break
        # if match:
        #     return i
    return -1

result = naive_search(text, pattern)
print(f"Pattern found at index: {result}")





