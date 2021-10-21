N = int(input())
L = list(map(int, input().split()))
M = max(L)
for i in range(N):
    L[i] = L[i]/M*100
A = sum(L)/len(L)
print(A)

