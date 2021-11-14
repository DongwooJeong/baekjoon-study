N=int(input())
def fibonacci(n):
    if n==0:
        num=0
    elif n==1:
        num=1
    else:
        num=fibonacci(n-2)+fibonacci(n-1)
    return num
print(fibonacci(N))