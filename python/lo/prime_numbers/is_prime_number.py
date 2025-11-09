from math import sqrt


def is_prime_number(n: int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    square_root = int( sqrt(n) )
    for i in range(3, square_root + 1, 2):
        if n % i == 0:
            return False
    return True


test1 = is_prime_number(11)
test2 = is_prime_number(15)
test3 = is_prime_number(2)

print(test1)  # True
print(test2)  # False
print(test3)  # True