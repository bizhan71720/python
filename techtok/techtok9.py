n = int(input("Enter number:"))
even_n=int(n/2)
odd_n=even_n+1
odd=(odd_n/2)*(2+((n-1)*2))
even=(even_n/2)*(4+((n-1)*2))
print("odd=",odd)
print("even=",even)