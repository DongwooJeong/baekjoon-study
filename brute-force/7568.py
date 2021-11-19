N=int(input())
whlist=[]
order=[]
for i in range(N):
    w,h = map(int,input().split())
    whlist.append((w,h))

for i in range(N):
    count=0
    for j in range(N):
        if whlist[i][0]< whlist[j][0] and whlist[i][1] < whlist[j][1]:
            count+=1
    order.append(count+1)

for k in order:
    print(k,end=" ")
    