n = int(input())
"""
    Start Code From Here
"""
for i in range(1,n+1):
    print('1 '*abs(i-n)+(str(i)+' ')*i)