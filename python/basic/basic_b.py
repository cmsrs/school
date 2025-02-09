print('######0######')

for i in range(10):
    print(i)

"""

0
1
2
3
4
5
6
7
8
9

"""


print('######1######')

for i in range(10):
    if( i % 2 == 0):
        print(i)

"""

0
2
4
6
8

"""



print('######2######')

j = 10
for _ in range(10):
    print(j)    
    j = j + 2


"""

10
12
14
16
18
20
22
24
26
28


"""



print('######3######')

j = 10
for i in range(10):
    print("index", i, " j:",  j)    
    j = j + i


"""

index 0  j: 10
index 1  j: 10
index 2  j: 11
index 3  j: 13
index 4  j: 16
index 5  j: 20
index 6  j: 25
index 7  j: 31
index 8  j: 38
index 9  j: 46


"""



print('######4######')

for i in range(10, 111, 25):
    print(i)


"""

10
35
60
85
110


"""


print('######5######')

list5 = [10, 20, 30]

for i in range(3):
    print("index: ", i, " value: ", list5[i])

"""

index:  0  value:  10
index:  1  value:  20
index:  2  value:  30


"""



print('######6######')

list6 = ['red', 'green', 'blue']

for i in range(3):
    print("index: ", i, " value: ", list6[i])


"""

index:  0  value:  red
index:  1  value:  green
index:  2  value:  blue


"""


print('######7######')

list7 = ['red', 'green', 'blue']

for i in list7:
    print("index: ", i)


"""

index:  red
index:  green
index:  blue


"""



print('######8######')

list8 = [1, 2, 3, 4, 5, 6, 7]
print(list8)

print( list8[:3] )
print( list8[3:] )
print( list8[1] )


[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3]
[4, 5, 6, 7]
2


print('######9######')

for i in range(10):
    if( i == 5):
        print("________")
    else:
        print(i)
        

"""

0
1
2
3
4
________
6
7
8
9



"""


