#get n
a = int(input("enter number:"))
a=a-1
b=1
k=0
#calculat n!
for c in range (1,a+1):
    b = c*b
#amout to k
for d in range (a+1):
    f=1
    i=1
    #calculate k!
    for e in range(1,d+1):
        f = e*f
    h = a-d
    #calculate (n-k)!
    for g in range(1,h+1):
        i = g*i
    j=(b)/(f*i)
    k=k+1
    print(int(j))
