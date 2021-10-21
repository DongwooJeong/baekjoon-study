a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())
K = [a,b,c,d,e,f,g,h,i,j]
L = []
for i in K:
    M = i%42
    L.append(M)
N = 0
for i in range(42):
    if i in L:
        N=N+1
print(N)
