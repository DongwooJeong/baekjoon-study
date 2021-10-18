N = int(input())
K = N
i = 0
while True:
    A = N%10
    B = (N//10+N%10)%10
    C = 10*A+B
    N = C
    i = i+1
    if N == K:
        break
print(i)
