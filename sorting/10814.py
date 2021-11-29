N=int(input())
info=[]
for i in range(N):
    info.append(input().split())
for i in range(len(info)):
    info[i][0]=int(info[i][0])
info.sort(key=lambda x:x[0])
for [i,j] in info:
    print(i,j)