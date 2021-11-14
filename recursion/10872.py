def factorial(n):
    if n==0:
        return 1
    else:
        num = n*factorial(n-1)
    return num

k=int(input())
print(factorial(k))