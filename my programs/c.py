n = int(input())
"""
    Start Code From Here
"""
for i in range(1,n+1):
    print((' '*(n-i+1)),end='')
    for j in range(1,i+1):
        print(str(j)+' ',end='')
    print()