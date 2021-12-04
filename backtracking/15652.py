N,M=map(int,input().split())
numlist=[]

def dfs(start):
    if len(numlist)==M:
        print(' '.join(map(str,numlist)))
        return
    for i in range(start,N+1):
            numlist.append(i)
            dfs(i)
            numlist.pop()
dfs(1)

