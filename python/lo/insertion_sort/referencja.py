a = 12
b = [1,2,3,4]

def referencja( aa, bb ):
    aa = 55
    bb[0] = 9

print(a)
print(b)
referencja( a, b )
print(a)
print(b)

