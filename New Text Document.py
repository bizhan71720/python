
n = int(input("enter numbre :"))
for i in range(n,0,-1): 
    for j in range(-n+1,n):
        if(n-abs(j)<=i):
            print(1+abs(j),end="")
        else:
            print(" ",end="")
    print("")
    
