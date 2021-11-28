import sys
listc=[]
N=int(sys.stdin.readline())
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    listc.append((x,y))

listc.sort(key=lambda x: (x[1], x[0]))
for x, y in listc:
    print(x,y)