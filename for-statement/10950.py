T=int(input())
list = []
for i in range(T):
    A, B = map(int, input().split())
    list.append(A+B)
for i in list:
    print(i)
