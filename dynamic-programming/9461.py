T=int(input())
def P(N):
    dp = [0] * 100000 
    dp[1] = 1 
    dp[2] = 1
    dp[3] = 1
    for k in range(4,n+1): 
        dp[k] = (dp[k-2]+ dp[k-3])
    return print(dp[N])
for i in range(T):
    n=int(input())
    P(n)
