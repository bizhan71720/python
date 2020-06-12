n = int(input())
"""
    Start Code From Here
"""
for i in range(n):
    print(('0 '*i)+chr(65+i),('1 '*(n-1-i)))