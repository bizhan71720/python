n = int(input("enter number :"))
j=0
for i in range(1,n+1):
    if (n <= 52):
        if (i <= 26):
            print(" 0"*(i-1),chr(i+64),"1 "*(n-i))
        else:
            print(" 0"*(i-1),chr(i+70),"1 "*(n-i))
if (n > 52):
        print("your number is out of range:(")
        j=1
