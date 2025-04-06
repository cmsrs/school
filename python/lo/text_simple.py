"""
Algorytmy na tekstach (1)

#print( ord("A") ) # 65
#print( chr(65) ) # A
#print( ord("B") ) # 66
#print( ord("Z") ) # 90

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


print('######3######')





