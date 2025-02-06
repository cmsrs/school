
a = 123456789
#out = []

if( a == 0):
    print('0')
    exit()

while a > 0:
    b = a % 10
    #out.append(b)
    a = (a - b) // 10
    print('b=', b)    

#print(out)
#out.reverse()
#print(out)
