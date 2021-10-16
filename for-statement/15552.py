import sys
T=int(sys.stdin.readline())
list = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    list.append(A+B)
for i in list:
    print(i)