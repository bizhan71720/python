n = int (input("enter number:"))
a = 1
b = 0 
for i in range(1,1+n):
    s = a + b
    print(str(i)+")")
    print(str(s))
    a = b
    b = s
    print()
