import sys
N = int(sys.stdin.readline())
sortnum = []
for i in range(N):
    sortnum.append(list(map(int, sys.stdin.readline().split())))
sortnum.sort(key=lambda x: (x[0], x[1]))
for i in sortnum:
    print(i[0], i[1])