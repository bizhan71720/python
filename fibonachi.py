import os

class color : 
    GREEN = '\033[92m'
    WHITE = '\033[0m'
n = int (input("enter number:"))
a = 1
b = 0 
for i in range(1,1+n):
    s = a + b
    print(color.GREEN + str(i)+")")
    print(color.WHITE + str(s))
    a = b
    b = s
    print()