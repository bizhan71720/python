n = int (input("adad ra vared konid:"))

def is_prime(num):
    aval = True
    for i in range(2,(num//2)+1):
       if num%i == 0:
           aval = False
           break
    return aval

prims=0
for i in range(2,n):
    # print("cheking",i)
    aval=is_prime(i)
    # print ("number is prime:",aval)
    if aval:
        # print("---------->add 1 to primes number")
        prims=prims+1
print(prims)
# aval=is_prime(2)
# print(aval)