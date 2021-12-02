N,M=map(int,input().split())
numlist=[]

def dfs(start):
    if len(numlist)==M:
        print(' '.join(map(str,numlist)))
        return
    for i in range(start,N+1):
        if i not in numlist:
            numlist.append(i)
            dfs(i+1)
            numlist.pop()
dfs(1)

