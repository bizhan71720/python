n = int(input())

for i in range(1,n+1):
    print(chr(32*(3-(i%2))+i)+chr(32*(3-((i-1)%2))+i))