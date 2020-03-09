n = int(input('enter number:'))
for i in range (n,-1,-1):
    x=i
    y=n-i
    print((" ")*(i),end="")

    while (x < n):
        print (1,end="")
        x = x+1
    print ('0',end='')             
    while (y > 0):
        print (2,end="")
        y = y-1
        x = x-1
        
    print()
