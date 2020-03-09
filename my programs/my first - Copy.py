l=0
n = int(input('enter number :'))
for i in range (-n+1,n):
        for j in range(-n,n+1):
                if(n-abs(i)>=abs(j)):
                    if (j==0):
                        print("",end="")
                    else:
                        if(j==-1):
                            print("",end="")
                        else:
                            print(abs(j),end='')
                else:
                    print(" ",end="")
        print('')
input()
