A = 1
B = 1
list = []
while A or B != 0:
    A, B = map(int, input().split())
    list.append(A+B)
list.pop()
for i in list:
    print(i)

