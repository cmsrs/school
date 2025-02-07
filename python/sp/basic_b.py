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
    j = j + 2

print('######3######')

j = 10
for i in range(10):
    print("index", i, " j:",  j)    
    j = j + i

print('######4######')

for i in range(10, 100, 10):
    print(i)

print('######5######')

list5 = [10, 20, 30]

for i in range(3):
    print("index: ", i, " value: ", list5[i])

print('######6######')

list6 = ['red', 'green', 'blue']

for i in range(3):
    print("index: ", i, " value: ", list6[i])

print('######7######')

list7 = ['red', 'green', 'blue']

for i in list7:
    print("index: ", i)
