import math
A, B, V = map(int, input().split())
K=(V-B)/(A-B)
print(math.ceil(K))

