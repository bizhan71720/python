n = int(input('enter number:'))

for i in range(-n+1,n):
    for j in range(-n+1,n):
        if(abs(i)<=abs(j)):
            print(n-abs(i),end=' ')
        elif(abs(i)>abs(j)):
            print(n-abs(j),end=' ')
    print()
