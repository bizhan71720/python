n = int(input('enter number:'))
#print('n i j')
for i in range (-n,0):
    for j in range(-n+1,n):
        if (n-abs(j)>=abs(i)):
            print('*',end="")
        else:
            print(" ",end="")
    print('')
 
