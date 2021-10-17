T = int(input())
dictionary = {}
for i in range(T):
    A, B = map(int, input().split())
    dictionary[i]=A+B

for key in dictionary:
    print("Case #"+str(int(key)+1)+":",dictionary[key])