n = int(input("enter number:"))
for i in range(-n,n+1):
    for j in range(-i,i+1):
        print(n,i,j,end="   ")
    print()