
n = int(input ("enter number:"))

for i in range (n,1,-1):
    print((" ")*(n-i)+(". ")*(i))
for i in range (1,n+1):
    print((" ")*(n-i)+(". ")*(i))
