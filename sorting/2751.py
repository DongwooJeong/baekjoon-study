import sys
N=int(input())
numlist=[]
for i in range(N):
    sortnum=int(sys.stdin.readline())
    numlist.append(sortnum)
sortlist=sorted(numlist)
for i in sortlist:
    sys.stdout.write(str(i)+'\n')