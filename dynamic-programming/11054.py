N=int(input())
a=list(map(int, input().split()))
dp=[0]*N
dpi=[0]*N
dpd=[0]*N
for i in range(N):
    for j in range(i):
        if a[i] > a[j] and dpi[i] < dpi[j]:
            dpi[i] = dpi[j]
    dpi[i] += 1
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if a[i] > a[j] and dpd[i] < dpd[j]:
            dpd[i] = dpd[j]
    dpd[i] += 1
for i in range(N):
    dp[i]=dpi[i]+dpd[i]-1
print(max(dp))