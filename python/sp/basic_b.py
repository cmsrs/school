print('######0######')

for i in range(10):  # range(10) generuje liczby od 0 do 9
    print(i)

print('######1######')

for i in range(10):
    if( i % 2 == 0):
        print(i)

print('######2######')

j = 10
for _ in range(10):
    print(j)    
    j = j + 1

print('######3######')

j = 10
for i in range(10):
    print(j)    
    j = j + i

print('######4######')

for i in range(10, 100, 10):
    print(i)
