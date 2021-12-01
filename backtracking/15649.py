N,M=map(int,input().split())
numlist=[]

def dfs():
    if len(numlist)==M:
        print(' '.join(map(str,numlist)))
        return
    for i in range(1,N+1):
        if i not in numlist:
            numlist.append(i)
            dfs()
            numlist.pop()
dfs()

