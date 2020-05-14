n = int (input("enter number:"))
a = 1
b = 0 
for i in range(n):
    s = a + b
    print(s,end=" , ")
    a = b
    b = s
    print()