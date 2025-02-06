n = int( input("Ile liczb chcesz podac? ")  )

for i in range(n):
    a  = int( input(f"podaj {i+1} liczbe: ") )
    if( i == 0):
        min = a
    else:
        if ( a < min ):
            min = a

print(f"Minimum wynosi {min}")
