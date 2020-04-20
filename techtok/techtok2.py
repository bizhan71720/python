n = int(input('enter number :'))
for i in range (1,n+1):
    for j in range (-i+1,i):
        print (int(((i*(i+1))/2)-abs(j)),end=',')
    print()
