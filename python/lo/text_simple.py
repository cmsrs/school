"""
Algorytmy na tekstach (1)

#print( ord("A") ) # 65
#print( chr(65) ) # A
#print( ord("B") ) # 66
#print( ord("Z") ) # 90


od 65 do 90 jest 26 znaków
"""

print('######1######')

for i in range(65, 91):  # Change 90 to 91 to include 90 in the range
    print(f"{i}  {chr(i)}")


"""
65  A
66  B
67  C
68  D
69  E
70  F
71  G
72  H
73  I
74  J
75  K
76  L
77  M
78  N
79  O
80  P
81  Q
82  R
83  S
84  T
85  U
86  V
87  W
88  X
89  Y
90  Z

"""

print('######2######')


for i in range(65, 91):  # Change 90 to 91 to include 90 in the range
    print( f"{chr(i)}", end=" ")


"""
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
"""


print()
print('######3######')

def show_alphabet_from( start):
    for i in range(ord(start), 91):  # Change 90 to 91 to include 90 in the range
        print( f"{chr(i)}", end=" ")

show_alphabet_from('S')

"""
S T U V W X Y Z 
"""

print()
print('######3######')
def show_alphabet_from_round( start):
    start_nu = ord(start)
    for _ in range(26):  # Change 90 to 91 to include 90 in the range
        print(chr(start_nu), end=' ')
        start_nu += 1
        if start_nu > ord('Z'):
            start_nu = ord('A')  # back to A after Z


show_alphabet_from_round('S')


