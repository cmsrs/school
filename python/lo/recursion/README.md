# Rekurencja

## Ciąg rekurencyjny

Specyfikacja:
```text
rec_seq(n) = {
    1                dla n = 1
    3 * rec_seq(n-1) dla n > 1
}
```

Kod:
```python
def rec_seq(n):
    #print(f"rec_seq({n}) called")
    if n == 1:
        return 1
    return 3 * rec_seq(n-1)

rec_seq_return = rec_seq(3)
print("out=", rec_seq_return)
```

<img src="console_seq.png" />
rys. Uruchomienie programu

<img src="rec_seq.png" />
rys. Wywołania rekurencyjne dla funkcji  ```rec_seq``` dla ```n = 3```

## Ciąg Fibonacciego

Specyfikacja:
```text
fib(n) = {
    0               dla n = 0
    1               dla n = 1
    fib(n-1) + fib(n-2)  dla n > 1
}
```

Kod:
```python
def fib(n):
    #print(f"fib({n}) called")
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fib_result = fib(4)
print("out=", fib_result)
```


<img src="fib.png"  />
rys. Schemat wywołań rekurencyjnych funkcji ```fib``` dla ```n = 4```

