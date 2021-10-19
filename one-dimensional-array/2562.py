list = []
for i in range(9):
    X = int(input())
    list.append(X)
print(max(list))
print(int(list.index(max(list)))+1)
