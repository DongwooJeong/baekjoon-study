from math import factorial
T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    print(factorial(k+n)//(factorial(k+1)*factorial(n-1)))