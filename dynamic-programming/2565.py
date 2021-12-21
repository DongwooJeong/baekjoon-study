N = int(input())
A = []
B = []
dp = [0 for i in range(N)]
for i in range(N):
    A.append(list(map(int, input().split())))
A.sort(key = lambda x:x[0])
for i in range(N):
    B.append(A[i][1])
for i in range(N):
    for j in range(i):
        if B[i] > B[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(N - max(dp))