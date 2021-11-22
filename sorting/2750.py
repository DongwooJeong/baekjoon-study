N=int(input())
numlist=[]
for i in range(N):
    sortnum=int(input())
    numlist.append(sortnum)
sortlist=sorted(numlist)
for i in sortlist:
    print(i)