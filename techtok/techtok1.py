n = int(input('enter number:'))
for i in range (n,-1,-1):
    x=i
    y=n-i
    print((" ")*(i),end="")

    while (x < n):
        x =x+1
        print (x,end="")
    print ('0',end='')             
    while (y > 0):
        print (x,end="")
        y = y-1
        x = x-1
        
    print()
input()
